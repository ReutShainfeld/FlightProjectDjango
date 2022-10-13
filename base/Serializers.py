from django.contrib.auth.models import User
from .models import * 
from rest_framework import serializers

 
 
class AirlineCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model =Airline_Company
        fields ='__all__'
        # depth=1

    def save(self, *args,**kwargs):
        #userid=self.validated_data['user_id']
        airlineCompany = Airline_Company(#user_id=userid,
        #user_id=self.instance,
        user_id=self.validated_data['user_id'],
        name=self.validated_data['name'],
        #country_id=self.instance
        country_id=self.validated_data['country_id']
        )
        airlineCompany.save()
        return airlineCompany

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model =Administrator
        fields ='__all__'
    def save(self, **kwargs):
        administrator = Administrator(first_name=self.validated_data['first_name'],
                    last_name=self.validated_data['last_name'],
                    user_id=self.instance           
        )
        administrator.save()
        return administrator


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model =Country
        fields ='__all__'
        depth=1

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields ='__all__'


class FlightSerializer(serializers.ModelSerializer):
    # airline_company=serializers.PrimaryKeyRelatedField()
    class Meta:
        model = Flight
        fields = '__all__'
        # depth=1
    # def country1(self):
    #     return Country.objects.get(id=self.validated_data['origin_country_id'])
        
    # def country2(self):
    #     return Country.objects.get(id=self.validated_data['destination_country_id'])  


    def save(self,*args, **kwargs):
        # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        # print(self.country1())
        # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        # airline_company=Airline_Company.objects.get(id=self.validated_data['airline_company_id'])
        # origin_country=Country.objects.get(id=self.validated_data['origin_country_id'])
        # destination_country=Country.objects.get(id=self.validated_data['destination_country_id'])

        flight = Flight(
        # airline_company_id=airline_company,
        # origin_country_id=origin_country,
        # destination_country_id=destination_country,
        airline_company_id=self.validated_data['airline_company_id'],
        origin_country_id=self.validated_data['origin_country_id'],
        destination_country_id=self.validated_data['destination_country_id'],
        departure_time=self.validated_data['departure_time'],
        landing_time=self.validated_data['landing_time'],
        remaining_tickets=self.validated_data['remaining_tickets'] 
        )
        flight.save()
        return flight

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model =Ticket
        fields ='__all__'

    def save(self,*args, **kwargs):
        print("6")
        #customer=Customer.objects.get(id=1)
        #customer=self.validated_data['customer_id_id'],
        #customer=Customer.objects.get(id=self.validated_data['customer_id'])
        #print(customer)
        ticket = Ticket(flight_id=self.validated_data['flight_id'],
        #flight_id=self.instance,
        customer_id=self.validated_data['customer_id']
        )
        print("8")
        ticket.save()
        print("9")
        return ticket

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model =Customer
        fields ='__all__'
        # depth=1
    
    def save(self, **kwargs):
        customer = Customer(first_name=self.validated_data['first_name'],
                    last_name=self.validated_data['last_name'],
                    address=self.validated_data['address'],
                    phone_no=self.validated_data['phone_no'],
                    credit_card_no=self.validated_data['credit_card_no'],
                    user_id=self.instance             
        )
        customer.save()
        return customer
        
    # def save(self, **kwargs):
    #     new_customer=Customer(
    #         first_Name=self.validated_data['first_Name']


    #     )
        
    #         id =models.AutoField(primary_key=True,editable=False)
    # first_Name = models.TextField(max_length=50,null=True,blank=True)
    # last_Name = models.TextField( max_length=50,null=True,blank=True)
    # address = models.TextField( max_length=50,null=True,blank=True)
    # phone_No = models.TextField( max_length=50,null=True,blank=True,unique=True)
    # credit_Card_no = models.TextField( max_length=50,null=True,blank=True,unique=True)
    # user_Id =  models.OneToOneField(User,on_delete=models.SET_NULL,null=True,unique=True)
 
   # createdTime=models.DateTimeField(auto_now_add=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields ='__all__'
        # depth=1
    
    def save(self, **kwargs):
        user = User(username=self.validated_data['username'],
                    email=self.validated_data['email'],
                    password=self.validated_data['password'],
                    # user_id=self.instance             
        )
        user.save()
        return user

