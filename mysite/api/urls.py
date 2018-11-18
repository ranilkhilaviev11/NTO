from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    url(r'^get', views.GetPersonInfo, name='get'),

    path('', views.person_list, name='person_list'),
    path('view/<int:pk>', views.person_view, name='person_view'),
    path('new', views.person_create, name='person_new'),
    path('edit/<int:pk>', views.person_edit, name='person_edit'),
    path('delete/<int:pk>', views.person_delete, name='person_delete'),
]