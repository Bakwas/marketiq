from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import enchant
import json

class SuggestionList(APIView):
    """
    List all suggestions.
    """
    def get(self, request, format=None):
        d = enchant.Dict("en_US")
        return Response(json.dumps(d.suggest("Helo")))

