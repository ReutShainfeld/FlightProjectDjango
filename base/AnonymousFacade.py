
from django.db import transaction
from django.http import JsonResponse
from base.Serializers import CustomerSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff
        token['is_active'] = user.is_active
        # ...
 
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 
 
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
 
    return Response(routes)

@api_view(['POST'])
def addCustomers(request,id=0):
    if request.method == 'POST':  # add a customer
        with transaction.atomic():
            user=User.objects.get(id=request.data['user_id'])
            print(user)
            new_customer = CustomerSerializer(instance=user, data=request.data)
            if new_customer.is_valid():
                customer = new_customer.save()
            else:
                return Response(new_customer.errors, status.HTTP_400_BAD_REQUEST)
            return Response(data=CustomerSerializer(customer).data, status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# def addUser(request):
#     User.objects.create_user(username=request.data['username'],
#     email=request.data['email'],
#     password=request.data['password'],)
#     return JsonResponse({"done":"tes"} )


# from rest_framework.auth.models import Token
# from rest_framework.auth.views import ObtainToken
# from rest_framework.response import Response

# class MyObtainToken(ObtainToken):
#    """Return User Info along with token"""
#    def post(self, request, *arg, **kwarg):
#        serializer = self.serializer_class(request.data, context={'request':request})
#        serializer.is_valid(raise_exception=True)
#        user = serializer.valided_data['user']
#        token, _ = Token.objects.get_or_create(user)
#        return Response(
#             {
#                  'token': token.key,
#                  'username': user.username,
#                  'userid': user.pk
#             })