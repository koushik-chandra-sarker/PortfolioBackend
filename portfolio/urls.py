from django.urls import path

from portfolio import views

urlpatterns = [
    path('<str:username>', views.InfoByLoggedInUserApi.as_view()),
]
