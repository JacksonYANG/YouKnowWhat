from django.shortcuts import render
from django.http import HttpResponseRedirect
from zhihu.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
