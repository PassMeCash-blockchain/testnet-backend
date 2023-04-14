from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
# Create your views here.

from .utils import myTime

T = True
F = False

class RegisterView(APIView):

    def post(self, request):
        data = request.data
        return Response({"message": data}, status=status.HTTP_200_OK)