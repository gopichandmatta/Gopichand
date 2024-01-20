from django.shortcuts import render
from .models import Reg
from django.views import View
from django.http import HttpResponse


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class Reginput(View):
    def get(self, request):
        return render(request, 'reginput.html')


class Loginput(View):
    def get(self, request):
        return render(request, 'loginput.html')


class Register(View):
    def post(self, request):
        fn = request.POST['t1']
        ln = request.POST['t2']
        un = request.POST['t3']
        pd = request.POST['t4']
        r1 = Reg(firstname=fn, lastname=ln, username=un, password=pd)
        r1.save()
        res = HttpResponse('<html><body bgcolor="pink"><h1><center><br><br><br>Registered Successfully🥳🥳</center></h1></body></html>')
        return res


class Login(View):
    def post(self,request):
        un=request.POST['t1']
        pd=request.POST['t2']
        qs=Reg.objects.filter(username=un,password=pd)
        if qs:
            res=HttpResponse('<html><body bgcolor="pink"><h1><center><br><br><br>Login SuccessFully🥳🥳</center></h1></body></html>')
            return res
        else:
            res=HttpResponse('<html><body bgcolor="pink"><h1><center><br><br><br>Login Failed😔😔</center></h1></body></html>')
            return res