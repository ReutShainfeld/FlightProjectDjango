from http.client import ResponseNotReady
import statistics
from urllib import response
from django.shortcuts import render

from .AdministratorFacade import customers
from .models import Airline_Company
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .Serializers import *
from rest_framework import status
from datetime import datetime, timedelta
 
def index(req):
    return JsonResponse('hello', safe=False)

@api_view(['GET'])
def get_airline_by_username(request):#checked-good
    if request.method == 'GET':
        print("\n\n\nhey reut\n\n\n")
        company = Airline_Company.objects.get(user_id__username=request.data['username'])
        serializer = AirlineCompanySerializer(company)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
        
@api_view(['GET'])
def get_user_by_username(request):
    if request.method =='GET':
        user = User.objects.get(username=request.data['username'])
        #user = Users.objects.get(user_id.Username=="ben")
        #print(user)
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK, data=serializer.data) 
 
# @api_view(['POST'])
# def get_flights_by_parameters(request):
#     if request.method =='POST':
#         flights = Flight.objects.filter(origin_country_id=request.data['origin_country_id']).filter(destination_country_id=request.data['destination_country_id']).filter(departure_time=request.data['departure_time'])
#         serializer = FlightSerializer(data=flights,many=True)
#         if serializer.is_valid():        
#            return Response(status=status.HTTP_200_OK, data=serializer.data)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

@api_view(['POST'])  ### first checked
def get_flights_by_parameters(request):
    if request.method =='POST':
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(request.data)
        flights = Flight.objects.filter(origin_country_id=request.data['origin_country_id']).filter(destination_country_id=request.data['destination_country_id'])
        serializer = FlightSerializer(data=flights,many=True)
        serializer.is_valid()
        if len(flights) ==0:
            message ='there is no matching flight'   
            return Response(status=status.HTTP_400_BAD_REQUEST,data=message)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

@api_view(['POST'])  ### first checked
def get_airline_by_parameters(request):
    if request.method =='POST':
        print(request.data)
        airlines = Airline_Company.objects.filter(country_id=request.data['country_id']).filter(name=request.data['name'])
        serializer = AirlineCompanySerializer(data=airlines,many=True)
        serializer.is_valid()
        if len(airlines) ==0:
            message ='there is no matching airlines'   
            return Response(status=status.HTTP_400_BAD_REQUEST,data=message)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

@api_view(['GET'])
def get_flights_by_airline_id(request):
    if request.method =='GET':
        flights = Flight.objects.filter(airline_company_id=request.data['airline_company_id'])
        serializer = FlightSerializer(data=flights,many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

@api_view(['GET'])
def get_tickets_by_customer(request):
    if request.method =='GET':
        tickets = Ticket.objects.get(Customer_Id=request.data['Customer_Id'])
        print( tickets)
        serializer = TicketSerializer(data=tickets,many=True)
        print(serializer)
        return Response( status=status.HTTP_200_OK, data=serializer.data)

# @api_view(['GET'])
# def get_customer_by_user(request):#checked-good
#     if request.method =='GET':
#         user = User.objects.get(id=request.data['user_id'])
#         customer = user.customer_set.all()
#         serializer =CustomerSerializer(customer, many=True)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)
@api_view(['POST'])
def get_user_role_by_user(request):
    if request.method =='POST':
        print(1)
        print(1)
        print(1)
        if request.data['is_superuser']==True:
            admin = Administrator.objects.get(user_id=request.data['user_id'])
            serializer = AdministratorSerializer(admin)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        if request.data['is_staff']==True:
           airlines = Airline_Company.objects.get(user_id=request.data['user_id'])
           serializer = AirlineCompanySerializer(airlines)
           return Response(data=serializer.data,status=status.HTTP_200_OK)
        if request.data['is_staff']==False and request.data['is_superuser']==False :
           customers = Customer.objects.get(user_id=request.data['user_id'])
           serializer = CustomerSerializer(customers)
           return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def get_customer_by_user(request):
    if request.method =='GET':
        customers = Customer.objects.get(user_id=request.data['user_id'])
        serializer = CustomerSerializer(customers)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_airline_by_user(request):
    if request.method =='GET':
        airlines = Airline_Company.objects.get(user_id=request.data['user_id'])
        serializer = AirlineCompanySerializer(airlines)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_admin_by_user(request):
    if request.method =='GET':
        admin = Customer.objects.get(user_id=request.data['user_id'])
        serializer = CustomerSerializer(admin)
        return Response(data=serializer.data,status=status.HTTP_200_OK)





