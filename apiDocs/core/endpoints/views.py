from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from .schemes import *
from .response import *

# Create your views here.

class RegisterView(APIView):
    """Creates new users.
       Requires [Phone number, password]
    """

    summary = "Create User"

    tags = ["Account"]
    post_tag = ['Registration']
    request_schema = CreateRequestSchema
    response_schema = {
        "200":CreateUserResponse,
        "400":CreateUserBadResponse,
    }

    def post(self, request):
        return Response({}, status=status.HTTP_200_OK)


class PersonalView(APIView):
    """Adds Personal info to user.
    """

    summary = "Create User [Personal Information]"
    header_params = PersonalRequestHeaderSchema

    tags = ["Account"]
    post_tag = ['Registration']
    request_schema = PersonalRequestSchema
    response_schema = {
        "200":PersonalUserResponse,
        "404":PersonalUserNotFoundResponse,
        "500":PersonalUserInternalResponse,
    }

    def post(self, request):
        return Response({}, status=status.HTTP_200_OK)


class ContactView(APIView):
    """Adds Contact info to user.
    """

    summary = "Create User [Contact Information]"
    header_params = PersonalRequestHeaderSchema

    tags = ["Account"]
    post_tag = ['Registration']
    request_schema = ContactRequestSchema
    response_schema = {
        "200":ContactUserResponse,
        "404":ContactUserNotFoundResponse,
        "500":ContactUserInternalResponse,
    }

    def post(self, request):
        return Response({}, status=status.HTTP_200_OK)


class LoginView(APIView):

    """Authenticating a user"""

    summary = "Login"

    tags = ["Account"]
    post_tag = ['Registration']
    request_schema = LoginRequestSchema
    response_schema = {
        "200":LoginResponse,
        "401":UnauthorizedLoginResponse,
        "403":ForbiddenLoginResponse,
        "404":NotFoundLoginResponse,
        "406":NotAcceptedLoginResponse,
        "500":InternalLoginResponse,
    }


    def post(self, request):
        return Response({}, status=status.HTTP_200_OK)
