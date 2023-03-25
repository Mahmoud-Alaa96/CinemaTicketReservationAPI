"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tickets import views
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import  DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register("guest", views.viewsets_guest)
router.register("movie", views.viewsets_movie)
router.register("reservation", views.viewsets_reservation)


urlpatterns = [
    path('admin/', admin.site.urls),
    #1
    path('django/jsonresponsenomode/', views.noRestNoModel),
    #2
    path('django/jsonresponsefrommode/', views.noRestFromModel),
    #3
    
    path('rest/fbv/', views.FBV_list), 
    path('rest/fbv/<int:pk>', views.FBV_pk),
    #4

    path('rest/cbv/', views.CBV_List.as_view()), 
    path('rest/cbv/<int:pk>', views.CBV_pk.as_view()),

    #5
    path('rest/mixins/', views.mixins_list.as_view()),

    #5.2 GET PUT DELETE from rest framework class based view mixins
    path('rest/mixins/<int:pk>', views.mixins_pk.as_view()),

    #6
    path('rest/generics/', views.generics_list.as_view()),
            #5

    #6.2
    path('rest/generics/<int:pk>', views.generics_pk.as_view()),

    #7 viewsets 
    path('rest/viewsets/', include(router.urls)),
 
    #8
     
    path('fbv/findmovie', views.find_movie), 
  
    path('fbv/new_reservations', views.new_reservations), 

    path('api-auth',include("rest_framework.urls") ), 

    path('api-token-auth/', obtain_auth_token),
    
    path('rest/Post/<int:pk>', views.Post_pk.as_view()),



]
