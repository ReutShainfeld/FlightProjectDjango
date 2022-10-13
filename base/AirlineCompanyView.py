# from functools import partial
# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# import re
# from urllib import response
# from django.http import HttpResponse
# from base.Serializers import CustomerSerializer
# #from .users import users
# #from .models import Users
# from .models import *
# from .Serializers import *
# from rest_framework import status
# from django.db import transaction,IntegrityError
# from rest_framework.parsers import JSONParser 

# @api_view(['GET','POST','DELETE','PATCH'])
# def airlineCompanies(request,id=0):
#     if request.method =='GET':
#         try:
#             if int(id) > 0: #get single customer
#                 airlineCompany = Airline_Company.objects.get(id=id)
#                 serializer = AirlineCompanySerializer(airlineCompany)
#                 return Response(status=status.HTTP_200_OK, data=serializer.data)
#             else: #get all customers
#                 airlineCompany =Customer.objects.all()
#                 serializer =AirlineCompanySerializer(data=airlineCompany, many = True)
#                 serializer.is_valid()
#                 return Response(status=status.HTTP_200_OK, data=serializer.data)
#         except Exception as ex:
#             print (ex)
#             return Response(status=status.HTTP_400_BAD_REQUEST)# data=ex)

#     if request.method == 'POST':  # add a customer
#         with transaction.atomic():
#             airlineCompany=Airline_Company.objects.get(id=request.data['user_ID'])
#             print(airlineCompany)
#             new_airlineCompany = AirlineCompanySerializer(instance=airlineCompany, data=request.data)
#             if new_airlineCompany.is_valid():
#                 airlineCompany = new_airlineCompany.save()
#             else:
#                 return Response(new_airlineCompany.errors, status.HTTP_400_BAD_REQUEST)
#             return Response(data=AirlineCompanySerializer(airlineCompany).data, status=status.HTTP_201_CREATED)
                    
#     if request.method =='DELETE': # delete a customer
#         airlineCompany = Airline_Company.objects.get(id=id)
#         #serializer = CustomerSerializer(data=customer)
#         #serializer.is_valid()
#         airlineCompany.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#         #return JsonResponse({'DELETE': id})
    
#     if request.method =='PATCH': # update a customer
#         #user=User.objects.get(id=request.data['user_id'])
#         airlineCompany = Airline_Company.objects.get(id=id)
#         print(11111)
#         print(airlineCompany)
#         print(222222)
#         airlineCompany.user_ID=request.data['user_ID']
#         airlineCompany.name=request.data['name']
#         airlineCompany.country_Id=request.data['country_Id']
#         airlineCompany.save()
#         #serializer=CustomerSerializer(customer,data=request.data,partial=True)
#         serializer=AirlineCompanySerializer(airlineCompany)#data=request.data,partial=True)
#         #if serializer.is_valid():
#             #serializer.save()
#         return Response(data=serializer.data,status=status.HTTP_200_OK)