from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def __init__(self, request):
        print('3')

        self.name = request.GET['name']
        self.status = request.GET['status']
        self.password1 = request.GET['password']
        self.password2 = request.GET['password']
        self.phone = request.GET['phone']
        print('4')

    def create_user(self):

        print("2")



