from todoapp import views
from django.urls import path



urlpatterns = [
    path('',views.home, name = 'home'),
    path('update_Task/<str:pk>', views.updateTask, name = 'update_Task'),
    path('delete_Task/<str:pk>', views.deleteTask, name = 'delete_Task')

]
