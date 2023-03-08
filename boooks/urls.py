from django.urls import path
from . import views
urlpatterns = [
    path('list', views.listviewApi.as_view()),
    path('detail/<int:pk>', views.detailviewApi.as_view()),
    path('add', views.addbookApi.as_view())

]
