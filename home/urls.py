from django.urls import path
from home import views

urlpatterns = [
path("",views.index,name="home"),
path("log_out",views.log_out,name="log_out"),
path("login",views.login_user,name="login_user"),
path("login_user_form",views.login_form,name="login_form"),
path("signup",views.create_user,name="create"),
path("create_user_form",views.create_user_form,name="create_form"),
path("contact_us",views.contact_us,name="contact_us"),
path("submit_contact_form",views.submit_contact_form,name="submit_contact_form"),
path("add_question",views.add_question),
path("add_question_form",views.add_question_form),
path("attempt_quiz",views.attempt_quiz),
path("submit_question",views.submit_question),
path("result",views.result),
]
