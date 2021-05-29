from django.shortcuts import render
from rest_framework_jwt.settings import api_settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app_auth.models import User
from app_auth.serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.

class VerifyJWTAPIVIEW(APIView):
    permission_classes = (AllowAny, IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    
    def post(self, request):
        try:
            print(request)
            print("AAAAAAAAAA")
            token = request.data['jwt_token']
            jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
            print(token)

            user_data = jwt_decode_handler(token)
            try:
                user = User.objects.get(username=user_data['username'])
                serializer = UserSerializer(user)
                user_data.update(serializer.data)
                user_data.update({'jwt_token': token})
                return Response(
                    {'user': user_data},
                    status=status.HTTP_200_OK
                )
            except User.DoesNotExist:
                print("AAAAAAAAAA")
                return Response(
                    {'message': 'verified user not found'},
                    status=status.HTTP_403_FORBIDDEN
                )

        except KeyError:
            return Response(
                {'message': 'bad request'},
                status=status.HTTP_400_BAD_REQUEST
            )
