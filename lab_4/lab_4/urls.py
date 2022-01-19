from django.contrib import admin
from django.urls import path

from computers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/', views.master),
    path('master/detail-<str:name>/', views.get_inf, name='detail_url'),

]
