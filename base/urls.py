from django.contrib import admin
from django.urls import path
from base import FacadeBase
from rest_framework_simplejwt.views import TokenObtainPairView
from base import AdministratorFacade,  AirlineFacade, CustomerFacade, AnonymousFacade
from . import views
from .AnonymousFacade import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView
 
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login',TokenObtainPairView.as_view() ),
    path('', views.index),
    path('get_flights_by_parameters', views.get_flights_by_parameters),
    path('get_airline_by_parameters', views.get_airline_by_parameters),
    path('get_airline_by_username/', views.get_airline_by_username),
    path('get_user_role_by_user/', views.get_user_role_by_user),
    path('get_customer_by_user', views.get_customer_by_user),
    path('get_airline_by_user', views.get_airline_by_user),
    path('get_admin_by_user', views.get_admin_by_user),
    path('get_my_tickets/<id>', CustomerFacade.get_my_tickets),
    path('get_user_by_username/', views.get_user_by_username),
    path('get_flights_by_airline_id/', views.get_flights_by_airline_id),
    path('customers/<id>', AdministratorFacade.customers),
    path('customers', AdministratorFacade.customers),
    path('get_all_countries/<id>', FacadeBase.get_all_countries),
    path('get_all_countries', FacadeBase.get_all_countries),
    path('get_all_airlines/<id>', FacadeBase.get_all_airlines),
    path('get_all_airlines', FacadeBase.get_all_airlines),
    path('get_all_flights/<id>', FacadeBase.get_all_flights),
    path('get_all_flights', FacadeBase.get_all_flights),
    path('create_new_user', FacadeBase.create_new_user),
    path('flights', AirlineFacade.flights),
    path('flights/<id>', AirlineFacade.flights),
    #path('addFlights', AirlineFacade.addFlights),
    path('get_my_flights/<id>', AirlineFacade.get_my_flights),
    path('update_airline/<id>', AirlineFacade.update_airline),
    path('airline', AdministratorFacade.airline),
    path('airline/<id>', AdministratorFacade.airline),
    path('administrators', AdministratorFacade.administrators),
    path('administrators/<id>', AdministratorFacade.administrators),
    path('tickets', CustomerFacade.tickets),
    path('update_customer/<id>', CustomerFacade.update_customer),
    path('tickets/<id>', CustomerFacade.tickets),
    # path('addUser', AnonymousFacade.addUser),
]

# urlpatterns = [
#     path('', views.index),
#     #path('customers/<username>', customersView.customers),
#     path('customers/<id>', customersView.customers),
#     path('customers', customersView.customers),
#     path('users', customersView.myUsers),
#     path('users/<id>', customersView.myUsers),
# ]