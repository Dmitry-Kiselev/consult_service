"""consult_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from users import views as users_views
from chat import views as chat_views

router = DefaultRouter()

router.register(r'conversations', chat_views.ConversationViewSet)
router.register(r'messages', chat_views.MessageSerializerViewSet)
router.register(r'queue', chat_views.QueueSerializerViewSet)

router.register(r'users', users_views.UserViewSet)
router.register(r'departments', users_views.DepartmentViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
