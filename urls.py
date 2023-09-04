from django.urls import path
from . import views
from .views import PasswordForm

urlpatterns =[
    path('', views.log_in, name="log_in"),
    path('main', views.main, name="main"),
    path('log_out', views.log_out, name="log_out"),
    path('signup', views.signup, name="signup"),
    path('depts', views.depts, name="depts"),
    path('<int:dept_id>', views.employees, name="employees"),
    path('password', PasswordForm.as_view(template_name = "firm/password_change.html"), name="password"),
    path('password_success', views.password_success, name="password_success"),
]