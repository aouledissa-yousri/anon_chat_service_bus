import zeep

class SoapClientAdapter:

    def __init__(self, wsdlSource):
        self.wsdl = wsdlSource
        self.client = zeep.Client(wsdl = wsdlSource)
    

    def login(self, username: str, password: str):
        result = self.client.service.login(username, password)
        return zeep.helpers.serialize_object(result)
    
    def logout(self, token):
        result = self.client.service.logout(token)
        return {"message": result}
    
    def signUp(self, username: str, password: str):
        result = self.client.service.signUp(username, password)
        return {"message": result}
    


soapClientAdapter = SoapClientAdapter("http://localhost:8080/user_management_service/services/userservice?wsdl")
