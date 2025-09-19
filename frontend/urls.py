from django.urls import path

from .import views
app_name = "frontend"

urlpatterns = [
    path('', views.home, name="home"),

    # ogolo own
    path('account/sign-in/', views.ogolo_redirect),
    path('api/process-ogolo/', views.process_ogolo),
    
]
