from django.urls import path
from django.contrib import admin                                                                                                    
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login_register', views.login_register, name='login_register'),
    path('logout', views.logoutUser, name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)