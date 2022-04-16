"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from Django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Django.contrib import admin
from Django.urls import path
from Django.urls import re_path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('path/2003/',views.page_2003),
    #127.0.0.1:8000
    path('',views.index_view),
    path('page/<int:pg>',views.pagen_view),
    #简易计算器
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})$',views.cal_view2),
    path('<int:n>/<str:op>/<int:m>',views.cal_view),
    re_path(r'^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})$',views.brithday_view),
    re_path(r'^birthday/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})$',views.brithday_view),
    path('test_requset',views.test_request)
]
