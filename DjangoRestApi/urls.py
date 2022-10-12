from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from djangoapi import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

#to view data
router.register('something',views.ViewSet_something, basename="something")

#to create user and view existing users
router.register('user',views.ViewSet_user, basename="user")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),
]
