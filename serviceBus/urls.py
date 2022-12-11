from django.urls import path
from .routers import UserManagementRouter, RoomManagementRouter

urlpatterns = [

    path("login/", UserManagementRouter.login),
    path("logout/", UserManagementRouter.logout),
    path("signUp/", UserManagementRouter.signUp),


    #general room paths
    path("room/", RoomManagementRouter.getRooms),
    path("user/rooms/", RoomManagementRouter.getSubscribedRooms),
    path("room/<roomId>/message/", RoomManagementRouter.sendMessage),
    path("room/<roomId>/message", RoomManagementRouter.getMessages),


    #private room paths
    path("room/private/create/", RoomManagementRouter.createPrivateRoom),
    path("room/private/<roomId>/join/", RoomManagementRouter.joinPrivateRoom),
    path("room/private/<roomId>/leave/", RoomManagementRouter.leavePrivateRoom),


    #public room paths
    path("room/public/create/", RoomManagementRouter.createPublicRoom),
    path("room/public/<roomId>/join/", RoomManagementRouter.joinPublicRoom),
    path("room/public/<roomId>/leave/", RoomManagementRouter.leavePublicRoom),



]