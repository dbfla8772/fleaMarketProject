from django.urls import path
from .views import *   

urlpatterns = [   
    path('<str:id>', detail, name="detail"),  
    path('new/', new, name="new"),
    path('edit/<str:id>', edit, name="edit"),  
    path('delete/<str:id>', delete, name="delete"), 
    path('download/<str:id>', file_download, name="download"),
]