from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('details/<int:id>', views.details, name='details'),
    path('details/deleterecord/<int:id>', views.deleterecord, name="deleterecord"),
    path('details/editrecord/<int:id>', views.editrecord, name="editrecord"),
    path('details/editrecord/completeedit/<int:id>', views.completeedit, name="completeedit"),
]