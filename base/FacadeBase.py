from functools import partial
from django.shortcuts import render
from django.http import JsonResponse
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

@api_view(['GET'])
def get_all_flights(request,id=0): #checked-good
    if request.method =='GET':
        try:
            if int(id) > 0: 
                flight = Flight.objects.get(id=id)
                serializer = FlightSerializer(flight)
                print(flight.airline_company_id.name)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            else: #get all flight
                flights =Flight.objects.all()
                serializer =FlightSerializer(data=flights, many = True)
                serializer.is_valid()
                print(serializer.data)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Exception as ex:
            print (ex)
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_flights_by_parameters(request):
    if request.method =='GET':
        flights = Flight.objects.filter(origin_country_id=request.data['origin_country_id']).filter(Destination_Country_Id =request.data['Destination_Country_Id ']).filter(departure_time=request.data['date'])
        serializer = FlightSerializer(data=flights,many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

        
@api_view(['GET']) #checked-good
def get_all_airlines(request,id=0):
    if request.method =='GET':
        try:
            if int(id) > 0: #get single customer
                airlineCompany = Airline_Company.objects.get(id=id)
                serializer = AirlineCompanySerializer(airlineCompany)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            else: #get all customers
                airlineCompany =Airline_Company.objects.all()
                serializer =AirlineCompanySerializer(data=airlineCompany, many = True)
                serializer.is_valid()
                return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Exception as ex:
            print (ex)
            return Response(status=status.HTTP_400_BAD_REQUEST)# data=ex)

@api_view(['GET']) #checked-good
def get_all_countries(request,id=0):
    if request.method =='GET':
        try:
            if int(id) > 0: #get single customer
                country = Country.objects.get(id=id)
                serializer = CountrySerializer(country)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            else: #get all customers
                country =Country.objects.all()
                serializer =CountrySerializer(data=country, many = True)
                serializer.is_valid()
                return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Exception as ex:
            print (ex)
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_new_user(request):
    if request.data['username'] in User.objects.values_list('username', flat=True):
        return JsonResponse({"error":"Username is already taken"} )
    user_role=request.data['user_role']
    if user_role=="Customer" :
        newuser=User.objects.create_user(
    username=request.data['username'],
    email=request.data['email'],
    password=request.data['password'],
    is_superuser=0,
    is_staff=0
    )
    if user_role=="Administrator":
        newuser=User.objects.create_user(
    username=request.data['username'],
    email=request.data['email'],
    password=request.data['password'],
    is_superuser=1,
    is_staff=0)
    if user_role=="Airline":
        newuser=User.objects.create_user(
    username=request.data['username'],
    email=request.data['email'],
    password=request.data['password'],
    is_superuser=0,
    is_staff=1)
    if user_role=="Anonymous":
        newuser=User.objects.create_user(
    username=request.data['username'],
    email=request.data['email'],
    password=request.data['password'],
    is_superuser=0,
    is_staff=0,
    is_active=0)
    
    return Response(data=UserSerializer(newuser).data, status=status.HTTP_201_CREATED)


