from functools import partial
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import re
from urllib import response
from django.http import HttpResponse

from base.Serializers import CustomerSerializer
#from .users import users
#from .models import Users
from .models import *
from .Serializers import *
from rest_framework import status
from django.db import transaction,IntegrityError
from rest_framework.parsers import JSONParser 

@api_view(['GET','POST','DELETE']) #checked-good
def customers(request,id=0):
    if request.method =='GET':
        try:
            if int(id) > 0: #get single customer
                customer = Customer.objects.get(id=id)
                serializer = CustomerSerializer(customer)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            else: #get all customers
                customers =Customer.objects.all()
                serializer =CustomerSerializer(data=customers, many = True)
                serializer.is_valid()
                return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Exception as ex:
            print (ex)
            return Response(status=status.HTTP_400_BAD_REQUEST)# data=ex)

    if request.method == 'POST':  # add a customer
        with transaction.atomic():
            # if request.data['user_id'] not in User.objects.values_list('id', flat=True):
            #     return JsonResponse({"error":"there is no user with this ID"} )
            user=User.objects.get(id=request.data['user_id'])
            print(user)
            new_customer = CustomerSerializer(instance=user, data=request.data)
            if new_customer.is_valid():
                customer = new_customer.save()
            else:
                return Response(new_customer.errors, status.HTTP_400_BAD_REQUEST)
            return Response(data=CustomerSerializer(customer).data, status=status.HTTP_201_CREATED)
                    
    if request.method =='DELETE': # delete a customer
        customer = Customer.objects.get(id=id)
        #serializer = CustomerSerializer(data=customer)
        #serializer.is_valid()
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        #return JsonResponse({'DELETE': id})



@api_view(['POST','DELETE'])  #checked-good
def airline(request,id=0):
    if request.method == 'POST':  # add a customer
        with transaction.atomic():
            if int(request.data['country_id']) not in Country.objects.values_list('id', flat=True):
                return JsonResponse({"error":"there is no country with this ID"} )
            countryid=Country.objects.get(id=request.data['country_id'])
            if int(request.data['user_id']) not in User.objects.values_list('id', flat=True):
                return JsonResponse({"error":"there is no user with this ID"} )
            userID=User.objects.get(id=request.data['user_id'])
            new_airlineCompany = AirlineCompanySerializer( data=request.data)
            if new_airlineCompany.is_valid():
                airlineCompany = new_airlineCompany.save()
            else:
                return Response(new_airlineCompany.errors, status.HTTP_400_BAD_REQUEST)
            return Response(data=AirlineCompanySerializer(airlineCompany).data, status=status.HTTP_201_CREATED)
                    
    if request.method =='DELETE': #checked-good
        airlineCompany = Airline_Company.objects.get(id=id)
        airlineCompany.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, )
        #return JsonResponse({'DELETE': id})

@api_view(['POST','DELETE'])
def administrators(request,id=0):
    if request.method == 'POST':  # add a customer
        with transaction.atomic():
            # if int(request.data['user_id']) not in User.objects.values_list('id', flat=True):
            #     return JsonResponse({"error":"there is no user with this ID"} )
            userid=User.objects.get(id=request.data['user_id'])
            new_administrator = AdministratorSerializer(instance=userid, data=request.data)
            if new_administrator.is_valid():
                administrator = new_administrator.save()
            else:
                return Response(new_administrator.errors, status.HTTP_400_BAD_REQUEST)
            return Response(data=AdministratorSerializer(administrator).data, status=status.HTTP_201_CREATED)
                    
    if request.method =='DELETE': # delete a customer
        administrator =Administrator.objects.get(id=id)
        #serializer = CustomerSerializer(data=customer)
        #serializer.is_valid()
        administrator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        #return JsonResponse({'DELETE': id})