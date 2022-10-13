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


@api_view(['POST','DELETE','PATCH'])
def flights(request,id=0):
    if request.method == 'POST':  #  checked-good
        with transaction.atomic():
            if int(request.data['airline_company_id']) not in Airline_Company.objects.values_list('id', flat=True):
                return JsonResponse({"error":"there is no airline company with this ID"} ) 
            airline_Company=Airline_Company.objects.get(id=request.data['airline_company_id'])  
            if int(request.data['origin_country_id']) not in Country.objects.values_list('id', flat=True):
                return JsonResponse({" origin country id error":"there is no country with this ID"} )  
            origin_country=Country.objects.get(id=request.data['origin_country_id']) 
            if int(request.data['destination_country_id']) not in Country.objects.values_list('id', flat=True):
                return JsonResponse({" destination country id error":"there is no country with this ID"} )
            destination_country=Country.objects.get(id=request.data['destination_country_id']) 
            if int(request.data['remaining_tickets'])<=0:
                return JsonResponse({" error":"remaining tickets must be up to 0"} )
            if request.data['origin_country_id'] == request.data['destination_country_id']:
                return JsonResponse({"error":" the origin country and the destination country cannot be the same country"} )   
            if request.data['landing_time'] <= request.data['departure_time']:
                return JsonResponse({"error":" the landing time cannot be before or equal to the departure time"} )   
            new_flight = FlightSerializer(  data=request.data)
            #instance=airline_Company
            if new_flight.is_valid():
                flight = new_flight.save()
            else:
                return Response(new_flight.errors, status.HTTP_400_BAD_REQUEST)
            return Response(data=FlightSerializer(flight).data, status=status.HTTP_201_CREATED)
                    
    if request.method =='DELETE':  
        flight = Flight.objects.get(id=id)
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        #return JsonResponse({'DELETE': id})
    
    if request.method =='PATCH': # checked-good
        flight = Flight.objects.get(id=id)
        # if int(request.data['origin_country_id']) == int(request.data['destination_country_id']):
        #     return JsonResponse({"error":" the origin country and the destination country cannot be the same country"} )  
        if int(request.data['airline_company_id']) not in Airline_Company.objects.values_list('id', flat=True):
            return JsonResponse({"error":"there is no airline company with this ID"} ) 
        flight.airline_company_id=Airline_Company.objects.get(id=request.data['airline_company_id'])
        if int(request.data['origin_country_id']) not in Country.objects.values_list('id', flat=True):
            return JsonResponse({" origin country id error":"there is no country with this ID"} ) 
        flight.origin_country_id=Country.objects.get(id=request.data['origin_country_id'])
        if request.data['destination_country_id'] not in Country.objects.values_list('id', flat=True):
            return JsonResponse({" destination country id error":"there is no country with this ID"} )
        flight.destination_country_id==Country.objects.get(id=request.data['destination_country_id'])
        if request.data['landing_time'] <= request.data['departure_time']:
            return JsonResponse({"error":" the landing time cannot be before or equal to the departure time"} )   
        flight.departure_time=request.data['departure_time']
        flight.landing_time=request.data['landing_time']
        if int(request.data['remaining_tickets'])<=0:
            return JsonResponse({" error":"remaining tickets must be up to 0"} )
        flight.remaining_tickets=request.data['remaining_tickets']
        flight.save()
        serializer=FlightSerializer(flight)#data=request.data,partial=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update_airline(request,id):# checked-good (can check again)
    if request.method =='PATCH':
        # if int(request.data['user_id_id']) not in User.objects.values_list('id', flat=True):
        #     return JsonResponse({"error":"there is no user with this ID"} )
        airlineCompany = Airline_Company.objects.get(id=id)
        # userid=User.objects.get(id=request.data['user_id'])
        # airlineCompany.user_id_id=userid.id
        airlineCompany.name=request.data['name']
        # if int(request.data['country_id']) not in Country.objects.values_list('id', flat=True):
        #     return JsonResponse({"error":"there is no country with this ID"} )
        countryid=Country.objects.get(id=request.data['country_id'])
        airlineCompany.country_id_id=countryid.id
        airlineCompany.save()
        serializer=AirlineCompanySerializer(airlineCompany)#data=request.data,partial=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_my_flights(request, id=0):#checked-good
    if request.method =='GET':
        airline = Airline_Company.objects.get(id=id)
        flights = airline.flight_set.all()
        serializer =FlightSerializer(flights, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)



# @api_view(['POST'])
# def addFlights(request):
# # def addFlights(request,company_id=0,country1id=0,country2id=0):
#     if request.method == 'POST':  # add a customer
#         with transaction.atomic():
#             airline_Company=Airline_Company.objects.get(id=request.data['airline_company_id'])            
#             new_flight = FlightSerializer(instance=airline_Company,  data=request.data)
#             if new_flight.is_valid():
#                 flight = new_flight.save()
#             else:
#                 return Response(new_flight.errors, status.HTTP_400_BAD_REQUEST)
#             return Response(data=FlightSerializer(flight).data, status=status.HTTP_201_CREATED)