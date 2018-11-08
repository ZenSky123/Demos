from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
