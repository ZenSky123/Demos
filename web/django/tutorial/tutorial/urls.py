from django.conf.urls import url, include

# from quickstart import views


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from snippets import views

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/%', views.UserDetail.as_view())
]
