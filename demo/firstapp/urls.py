# Import necessary modules
from django.contrib import admin # Django admin module
from django.urls import path	 # URL routing
from firstapp import views   # Import views from the authentication app
 
 

# Define URL patterns
urlpatterns = [
  path('admin/', admin.site.urls),
	path('', views.home ,name='homepage' ),	 # Home page
	path('add/',views.add,name='add' ),
  path('delete/<int:roll>',views.delete,name='delete'),
  path('update/<int:roll>',views.update,name='udapte'),
  path('do-update/<int:roll>/',views.do_update,name='do_update')
]

 