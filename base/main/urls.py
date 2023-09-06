from django.contrib import admin
from django.urls import path, include

from .views import index, run_bot # , bots_list, bot_switcher

urlpatterns = [
    path('', index, name='index'),
    # path('bots_list', bots_list, name='bots_list'),
    path('run_bot/<int:pk>', run_bot, name='run_bot'),
]
