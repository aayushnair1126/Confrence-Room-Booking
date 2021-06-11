from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics,permissions
from django.contrib.auth import login ,logout
from rest_framework.authentication import SessionAuthentication,BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

for user in User.objects.all():
    Token.objects.get_or_create(user=user)


class RegisterAPI(generics.GenericAPIView):

	serializer_class = RegisterSerializer

	def post(self,request,*args,**kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception = True)
		user = serializer.save()
		token = Token.objects.get(user = user).key
		data={}
		data['token']=token
		return Response({
			'status': status.HTTP_201_CREATED,
			'msg':"You are Registered Successfully",
			"user" :{'username':user.username,'email':user.email},
			"token": data,
			})


class LoginView(generics.GenericAPIView):

	serializer_class = LoginSerializer

	def post(self,request,*args,**kwargs):

		serializer = LoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data["user"]
		login(request, user)
		token, created = Token.objects.get_or_create(user=user)

		return Response({
			'status': status.HTTP_201_CREATED,
			'msg':"welcome %s, you have logged in" % user.username,
			"token": token.key,
			}, status=200)

class LogoutView(generics.GenericAPIView):
	serializer_class = LogoutSerializer
	def post(self,request,*args,**kwargs):
		Token.objects.get(user=request.user).delete()
		logout(request)

		return Response({
			'status':status.HTTP_204_NO_CONTENT,
			'msg':'you have logged out'}, status=204)