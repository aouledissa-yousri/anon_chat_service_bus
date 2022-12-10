from rest_framework.decorators import api_view
from django.http import JsonResponse
from ..helpers import RequestHelper
from ..adapters import soapClientAdapter


class UserManagementRouter:

    @api_view(["POST"])
    @staticmethod
    def signUp(request):
        data = RequestHelper.getRequestBody(request)

        try:
            return JsonResponse(soapClientAdapter.signUp(data["username"], data["password"]))
        
        except KeyError:
            return JsonResponse({"message": "invalid payload"})
    

    @api_view(["DELETE"])
    @staticmethod
    def logout(request):

        try:
            return JsonResponse(soapClientAdapter.logout(request.headers["Token"]))
        
        except KeyError:
            return JsonResponse({"message": "invalid payload"})

    
    @api_view(["POST"])
    @staticmethod
    def login(request):
        data = RequestHelper.getRequestBody(request)

        try:
            return JsonResponse(soapClientAdapter.login(data["username"], data["password"]))
        
        except KeyError:
            return JsonResponse({"message": "invalid payload"})
    

