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

@api_view(['POST','DELETE'])
def tickets(request,id=0): #checked-good
    if request.method == 'POST':  
        with transaction.atomic():
            # flightID=Flight.objects.get(id=request.data['flight_id'])
            #customerID=Customer.objects.get(id=request.data['customer_id'])
            if int(request.data['customer_id']) not in Customer.objects.values_list('id', flat=True):
                return JsonResponse({"error":"there is no customer with this ID"} )
            customer=Customer.objects.get(id=request.data['customer_id'])
            if int(request.data['flight_id']) not in Flight.objects.values_list('id', flat=True):
                return JsonResponse({"error":"there is no flight with this ID"} )
            flight=Flight.objects.get(id=request.data['flight_id'])
            new_ticket = TicketSerializer( data=request.data )
            print(new_ticket)
            print(request.data)
            if new_ticket.is_valid():
                ticket = new_ticket.save()
            else:
                return Response(new_ticket.errors, status.HTTP_400_BAD_REQUEST)
            return Response(data=TicketSerializer(ticket).data, status=status.HTTP_201_CREATED)


    if request.method =='DELETE': # delete a ticket #checked-good
        ticket = Ticket.objects.get(id=id)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        #return JsonResponse({'DELETE': id})

@api_view(['GET'])
def get_my_tickets(request,id=0): #checked-good
    if request.method =='GET':
        # customer_Id = Customer.objects.get(id=request.data['customer_Id'])
        customer_Id = Customer.objects.get(id=id)
        # if customer_Id not in Ticket.objects.values_list('customer_id', flat=True):
        #     return JsonResponse({'error': "no tickets found"})
        tickets = customer_Id.ticket_set.all()
        serializer = TicketSerializer(tickets,many=True)
        return Response( status=status.HTTP_200_OK, data=serializer.data)

@api_view(['PATCH'])  #checked-good
def update_customer(request,id):
    if request.method =='PATCH': # update a customer
        #user=User.objects.get(id=request.data['user_id'])
        customer = Customer.objects.get(id=id)
        print(11111)
        print(customer)
        print(222222)
        customer.first_name=request.data['first_name']
        customer.last_name=request.data['last_name']
        customer.address=request.data['address']
        customer.phone_no=request.data['phone_no']
        customer.credit_card_no=request.data['credit_card_no']
        customer.save()
        #serializer=CustomerSerializer(customer,data=request.data,partial=True)
        serializer=CustomerSerializer(customer)#data=request.data,partial=True)
        #if serializer.is_valid():
            #serializer.save()
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    


