#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from zhihu.models import User
from django import forms
from django.template import RequestContext
import pdb

# Create your views here.

##登陆界面表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

##登陆
def login(request):
    if request.method=='POST':
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            #获取表单用户名和密码
            username = userForm.cleaned_data['username']
            password = userForm.cleaned_data['password']

            #将表单提交并与数据库相比较
            match = User.objects.filter(username__exact = username, password__exact = password)
            if match:
                #匹配成功，跳转到起始页index
                response = HttpResponseRedirect('/zhihu/index/')

                #将用户名写入cookie中，失效时间为3600ms
                response.set_cookie('username', username, 3600)
                return response
            else:
                #匹配失败，不跳转
                HttpResponseRedirect('/zhihu/login/')
    else:
        userForm = UserForm()
    return render_to_response('login.html', {'userForm',userForm}, context_instance = RequestContext(request))

#注册
def register(request):
    if request.method=='POST':
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            #获得表单数据
            account = userForm.cleaned_data['username']
            passwd = userForm.cleaned_data['password']

            #添加到数据库
            User.objects.create(username = account, password = passwd)
            return HttpResponseRedirect(u'注册成功!')
    else:
        userForm = UserForm()
    return render_to_response('register.html', {'userForm',userForm}, content_instance = RequestContext(request))

#退出
def logout(request):
    response = HttpResponse(u'退出成功!')

    #清理cookie
    response.delete_cookie('username')
    return response

#首页,待完善
def index(request):
    username = request.COOKIES.get('username','')
    return render_to_response('index.html', {'username',username})

