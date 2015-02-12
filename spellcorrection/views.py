# Create your views here.
from django.http import HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework.response import Response
import enchant


class SuggestView(APIView):

    """
    This is a view class for the suggest endpoint. It only supports a GET method with a single
    query parameter named 'q'
    """

    def __init__(self):
        """
        Only the English dictionary is required for the exercise.
        """
        self.dictionary = enchant.Dict('en_US')

    """
    Returns a list of suggestions for the word supplied as parameter.
    Also returns a misspelt flag that shows whether the original word was actually misspelt.
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

    """
    This is a view class for the root endpoint /. It only supports a GET method.
    """

    def __init__(self):
        self.endpoints = {'suggest': '/suggest?q={query}'}

    """
    Returns a dictionary of all available URLs/endpoints.
    """

    def get(self, request, format=None):
        return Response({'endpoints': self.endpoints})
