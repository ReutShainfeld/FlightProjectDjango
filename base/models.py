from django.db import models
from email.policy import EmailPolicy
from tokenize import Name
from django.db import models
from django.contrib.auth.models import User


class User_Role(models.Model):
    #Id =models.AutoField(primary_key=True,editable=False)
    Role_Name = models.TextField(max_length=15,null=True,blank=True,unique=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.Role_Name

# class Userr(models.Model):
#     #Id =models.AutoField(primary_key=True,editable=False)
#     Username = models.TextField(max_length=50,null=True,blank=True,unique=True)
#     Password = models.TextField( max_length=50,null=True,blank=True)
#     Email = models.TextField(max_length=50,null=True,blank=True,unique=True)
#     User_Role = models.ForeignKey(User_Role,on_delete=models.SET_NULL,null=True,)
#     createdTime=models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #    return self.Username

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField( max_length=50,)
    address = models.CharField( max_length=50)
    phone_no = models.CharField( max_length=50,unique=True)
    credit_card_no = models.CharField(max_length=64,unique=True)
    user_id =  models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.first_name

class Country(models.Model):
    #Id =models.AutoField(primary_key=True,editable=False)
    name = models.TextField(max_length=50,null=True,blank=True, unique=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    
    def __str__(self):
       return self.name
       
    class Meta:
        db_table ='countries'

class Airline_Company(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=52,unique=True)
    country_id = models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table ='airline_companies'

    def __str__(self):
       return self.name

class Flight(models.Model):
    airline_company_id = models.ForeignKey(Airline_Company,on_delete=models.SET_NULL,null=True)# related_name='Airline_Company_Id',)
    origin_country_id=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True,related_name='origin_country_id')
    destination_country_id =models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    departure_time=models.DateTimeField()
    landing_time=models.DateTimeField()
    remaining_tickets=models.IntegerField()
    #Remaining_Tickets=models.TextField(null=True,blank=True,)
    

class Ticket(models.Model):
    #Id =models.AutoField(primary_key=True,editable=False)
    flight_id = models.ForeignKey(Flight,max_length=50,null=True,on_delete=models.SET_NULL)
    customer_id = models.ForeignKey(Customer,max_length=50,null=True,on_delete=models.SET_NULL)
    
    class Meta:
        unique_together=('flight_id','customer_id',)

    def __str__(self):
       return '{}/{}'.format(self.flight_id,self.customer_id)




class Administrator(models.Model):
    #Id =models.AutoField(primary_key=True,editable=False)
    first_name = models.TextField(max_length=50,null=True,blank=True)
    last_name = models.TextField( max_length=50,null=True,blank=True)
    user_id =  models.OneToOneField(User,on_delete=models.SET_NULL,null=True,unique=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return self.first_name

# class Account(models.Model):
#     #Id =models.AutoField(primary_key=True,editable=False)
#     user=models.OneToOneField(User, on_delete=models.CASCADE)
#     user_role=models.ForeignKey(User_Role,on_delete=models.SET_NULL,null=True)






