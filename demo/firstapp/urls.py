# Import necessary modules
from django.contrib import admin  # Django admin module
from django.urls import path  # URL routing
from firstapp import views  # Import views from the authentication app


# Define URL patterns
urlpatterns = [
    path("admin/", admin.site.urls),
    path("home", views.home, name="homepage"),  # Home page
    # path('add/',views.add,name='add' ),
    path("delete/<int:roll>", views.delete, name="delete"),
    path("update/<int:roll>", views.update, name="udapte"),
    path("do-update/<int:roll>/", views.do_update, name="do_update"),
    path("add/", views.add_user, name="add_user"),
    path("", views.login_view, name="login_view"),
    path("logout/", views.logout_view, name="logout"),
    path("cl/", views.MyView.as_view(name="Known"), name="cl"),  # Class Based view usrl
    path("pageRender/", views.PageRender.as_view(), name="pageRender"),
    path("ContextPage/", views.ContextPage.as_view(), name="ContextPage"),
    path("LoginView/", views.LoginView.as_view(), name="LoginView"),
]
