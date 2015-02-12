# Create your views here.
from django.http import HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework.response import Response
import enchant


class SuggestView(APIView):

    def __init__(self):
        self.dictionary = enchant.Dict('en_US')

    """
    List all suggestions for the word supplied as parameter.
    """

    def get(self, request, format=None):
        word = request.GET.get('q', None)
        if word:
            response = {}
            response['misspelt'] = not self.dictionary.check(word)
            response['suggestions'] = self.dictionary.suggest(word)
            return Response(response)
        else:
            return HttpResponseBadRequest(
                "Invalid query for spell correction !!")


class HomeView(APIView):

    def __init__(self):
        self.endpoints = {'suggest': '/suggest?q={query}'}

    """
    List all available URLs.
    """

    def get(self, request, format=None):
        return Response({'endpoints': self.endpoints})
