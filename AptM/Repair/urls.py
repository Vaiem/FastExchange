from django.urls import path, include

from users.views import Register
from Repair.views import CreateRepair, DetailRepair, GetViewUserRepair

urlpatterns = [
    #path('', include('django.contrib.auth.urls')),
    #заменить обработчик
    path('detail/<int:pk>/', DetailRepair.as_view(), name='detail'),
    path('create/', CreateRepair.as_view(), name='create'),
    path('getMyRepair/', GetViewUserRepair.as_view(), name='userRepair')
]