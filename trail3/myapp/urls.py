from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.loginpage,name='login'),
    path('home',views.log_in,name='home'),
    path('logout',views.log_out),
    path('viewvoterlist',views.voterslist,name="voterslist"),
    path('viewchart',views.viewchart,name="viewchart"),
]