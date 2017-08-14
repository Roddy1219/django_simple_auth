from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate

class IndexView(View):
    def get(self,reqeust):
        return render(reqeust,'users/index.html')





class LoginView(View):
    '''
        User login view
    '''

    def get(self, request):
        return render(request,'users/users_login.html')

    def post(self, reqeust):
        pass


class RegisterView(View):
    '''
        User register view
    '''

    def get(self, request):
        return render(request,'users/users_register.html')

    def post(self, request):
        pass


class ForgotPassView(View):

    """
        User forgot password view ,user not login
    """

    def get(self, request):
        return render(request,'users/users_forgotpasswd.html')

    def post(self, request):
        pass


class RestPassView(View):
    """
        User rest password view , user is logined
    """

    def get(self, reqeust):
        return render(reqeust,'users/users_resetpasswd.html')

    def post(self, request):
        pass


class UserInfoView(View):
    """
        Display user base information
    """

    def get(self, request):
        return render(request,'users/users_baseinfo.html')

class UserLogout(View):
    """
        User logout

    """
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/')



