from django.contrib import admin
from computers import views as computers_views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'computers', computers_views.PCViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
]