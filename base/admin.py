from django.contrib import admin
from .models import Administrator, Airline_Company, Airline_Company, Country, Country, Customer, Flight, Ticket, User_Role
 
admin.site.register(Airline_Company)
admin.site.register(Customer)
admin.site.register(User_Role)
admin.site.register(Flight)
admin.site.register(Country)
admin.site.register(Ticket)
admin.site.register(Administrator)


# Register your models here.

# from django.contrib import admin 
# # from .models import Account 
# from django.contrib.auth.models import User 
# from django.contrib.auth.admin import UserAdmin 
# class AccountInline ( admin.StackedInline ) : 
#     model = Account 
#     can_delete = False 
#     verbose_name_plural=' Accounts '
    
# class CustomizedUserAdmin ( UserAdmin ) : 
#     inlines = ( AccountInline , ) 

# admin.site.unregister ( User ) 
# admin.site.register( User , CustomizedUserAdmin )
