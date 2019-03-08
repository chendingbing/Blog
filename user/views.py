from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from user.models import User
import time,hashlib
# Create your views here.


def index(request):
    user = request.session.get('user')
    if user == None:
        return HttpResponseRedirect('/user/login/')
    return render(request,'index.html',{'user':user})

def login(request):
    #return HttpResponse('hahah')
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def register_action(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            nickname = request.POST.get('nickname')
            password = request.POST.get('password')
            confirmpassword = request.POST.get('confirmpassword')
            user = User.objects.filter(email=email).exists()
            if user == True:
                error = '该账户已经注册啦！'
                return render(request, 'register.html', {'error': error})

            if email == '' or nickname == '' or password == '':
                error = '请填写所有数据'
                return render(request, 'register.html', {'error': error})
            elif password==confirmpassword:
                if len(password) < 6:
                    error = '密码至少为6位'
                    return render(request, 'register.html', {'error': error})
                md5 = hashlib.md5()
                md5.update(password.encode('utf-8'))
                password = md5.hexdigest()
                user = User(email=email,nickname=nickname,password=password)
                user.save()
            else:
                error = '请输入一样的密码'
                return render(request, 'register.html',{'error': error})

        except Exception as e:
            return e
        return render(request,'login.html')

def login_action(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email)
        if user.exists() == True:
            user = User.objects.get(email=email)
            user_password = user.password
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            password = md5.hexdigest()
            if password == user_password:
                response = HttpResponseRedirect('/index')
                aa = user.nickname
                request.session['user'] = aa
                #request.session.set_expiry(10)
                return response
            else:
                error_password = '密码错误'
                return render(request, 'login.html', {'error_password': error_password})
        else:
            error_email = '该用户未注册'
            return render(request, 'login.html', {'error_email': error_email})