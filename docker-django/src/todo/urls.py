from django.urls import path
from .views import IndexView
from .views import notLoginView

urlpatterns = [
    path('', IndexView.as_view(), name='Index'),
    path('notlogin/', notLoginView.as_view(),name='notLogin'),
    path('notloginmail/', notLoginView.as_view(),name='notLoginMail'),
]