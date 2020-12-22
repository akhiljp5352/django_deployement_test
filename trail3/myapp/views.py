from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from myapp import models
import json
from django.core.serializers.json import DjangoJSONEncoder
from json import dumps
from django.core import serializers
from django.http import HttpResponse
import pandas as pd

def loginpage(request):
    return render(request,'userlogin.html')

def log_in(request):
    username=request.POST['username']
    password=request.POST['password']
    user= authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return render(request,'userhome.html',{'username':username})
    else:
        return render(request,'userlogin.html')

def log_out(request):
    logout(request)
    return redirect('login')

def voterslist(request):
    constituency_value = request.user.profile.constituency
    voters = list(models.Voters.objects.filter(constituency=constituency_value))
    voters = serializers.serialize("json", voters)
    json_voters=json.dumps(voters,cls=DjangoJSONEncoder)
    test='hi'
    return render(request,'voterslistview_list.html',{'data': json_voters,'user':constituency_value,'test':test})




def viewchart(request):
    constituency_value = request.user.profile.constituency
    voters = list(models.Voters.objects.filter(constituency=constituency_value).values())
    voters_df=pd.DataFrame(voters)
    gender_count=dict(voters_df['gender'].value_counts())
    gender_count_keys=list(gender_count.keys())
    gender_count_values = list(gender_count.values())
    gender_dict={'keys':gender_count_keys,'values':gender_count_values}
    print(gender_dict)
    return render(request,'graph.html',{'gender':gender_dict})
