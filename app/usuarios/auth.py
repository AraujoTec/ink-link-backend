from ninja.security import HttpBearer, HttpBasicAuth

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "password":
            return token

class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password, empresa):
        if username == "admin" and password == "secret" and empresa == "1":
            return username