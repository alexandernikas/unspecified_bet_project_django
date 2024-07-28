from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import BetSlip
from .serializers import BetSlipSerializer

class LatestBetSlips(APIView):
    def get(self, request, format=None):
        bet_slips = BetSlip.objects.all()[0:11]
        serializer = BetSlipSerializer(bet_slips, many=True)
        return Response(serializer.data)