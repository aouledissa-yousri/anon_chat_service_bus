from Global.settings import SECRET_KEY
from django.http import JsonResponse
import jwt


#check if access token is valid or not when making a post request to the server
def checkAccessToken(func, algorithm="HS256"):

    def wrapper(request, *args, **kwargs):
        try: 
            _token = request.headers["Token"]

            try:
                jwt.decode(_token, SECRET_KEY, algorithms = [algorithm])
                return func(request, *args, **kwargs)

            except jwt.exceptions.DecodeError:
                return JsonResponse({"response": "invalid token"})

        except KeyError: 
            return JsonResponse({"response": "invalid token"})

    return wrapper