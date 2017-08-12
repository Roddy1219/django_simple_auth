from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^register/$', views.RegisterView.as_view(), name="register"),
    url(r'^forgotpass/$', views.ForgotPassView.as_view(), name="forgot_pass"),
    url(r'^resetpass/$', views.RestPassView.as_view(), name="rest_pass"),
    url(r'^userinfo/$', views.UserInfoView.as_view(), name="user_info"),
    url(r'^logout/$', views.UserLogout.as_view(), name="user_logout"),
]
