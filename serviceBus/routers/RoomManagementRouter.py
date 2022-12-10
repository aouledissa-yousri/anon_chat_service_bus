from rest_framework.decorators import api_view
from django.http import JsonResponse
from ..helpers import RequestHelper
from ..adapters import restClientAdapter


class RoomManagementRouter:

    @api_view(["GET"])
    @staticmethod
    def getRooms(request):
        return JsonResponse(restClientAdapter.getRooms(request.headers["Token"]), safe=False)
    

    @api_view(["POST"])
    @staticmethod
    def createPrivateRoom(request):
        return JsonResponse(restClientAdapter.createPrivateRoom(request.headers["Token"], RequestHelper.getRequestBody(request)))

    
    @api_view(["PATCH"])
    @staticmethod
    def joinPrivateRoom(request, roomId):
        return JsonResponse(restClientAdapter.joinPrivateRoom(request.headers["Token"], roomId))
    

    @api_view(["PATCH"])
    @staticmethod
    def leavePrivateRoom(request, roomId):
        return JsonResponse(restClientAdapter.leavePrivateRoom(request.headers["Token"], roomId))


    

    @api_view(["POST"])
    @staticmethod
    def createPublicRoom(request):
        return JsonResponse(restClientAdapter.createPublicRoom(request.headers["Token"], RequestHelper.getRequestBody(request)))
    

    @api_view(["PATCH"])
    @staticmethod
    def joinPublicRoom(request, roomId):
        return JsonResponse(restClientAdapter.joinPublicRoom(request.headers["Token"], roomId))
    

    @api_view(["PATCH"])
    @staticmethod
    def leavePublicRoom(request, roomId):
        return JsonResponse(restClientAdapter.leavePublicRoom(request.headers["Token"], roomId,))
    



    @api_view(["POST"])
    @staticmethod
    def sendMessage(request, roomId):
        return JsonResponse(restClientAdapter.sendMessage(request.headers["Token"], roomId, RequestHelper.getRequestBody(request)))
    

    @api_view(["GET"])
    @staticmethod
    def getMessages(request, roomId):
        return JsonResponse(restClientAdapter.getMessages(request.headers["Token"], roomId), safe=False)
    
