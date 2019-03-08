from django.conf.urls import url,include
from user import views

urlpatterns = [
    url(r'^login/', views.login, name="login"),
    url(r'^register/', views.register, name='register'),
    url(r'^register_action/', views.register_action, name='register_action'),
    url(r'^login_action/', views.login_action, name='login_action'),

]

app_name = 'user'