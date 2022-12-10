import requests

class RestClientAdapter:


    def __init__(self, uri):
        self.uri = uri
    

    def getRooms(self, token):
        return requests.get(self.uri+"/room", headers={"token": token}).json()


    
    def createPrivateRoom(self, token, payload):
        return requests.post(self.uri+"/room/private/create", headers={"token": token}, json=payload).json()
    
    def joinPrivateRoom(self, token, roomId):
        return requests.patch(self.uri+"/room/private/"+roomId+"/join", headers={"token": token}).json()
    
    def leavePrivateRoom(self, token, roomId):
        return requests.patch(self.uri+"/room/private/"+roomId+"/leave", headers={"token": token}).json()



    
    def createPublicRoom(self, token, payload):
        return requests.post(self.uri+"/room/public/create", headers={"token": token}, json=payload).json()

    def joinPublicRoom(self, token, roomId):
        return requests.patch(self.uri+"/room/public/"+roomId+"/join", headers={"token": token}).json()
    
    def leavePublicRoom(self, token, roomId):
        return requests.patch(self.uri+"/room/public/"+roomId+"/leave", headers={"token": token}).json()
    


    def sendMessage(self, token, roomId, payload):
        return requests.post(self.uri+"/room/"+roomId+"/message", headers={"token": token}, json=payload).json()
    
    def getMessages(self, token, roomId):
        return requests.get(self.uri+"/room/"+roomId+"/message", headers={"token": token}).json()



restClientAdapter = RestClientAdapter("http://localhost:3000")