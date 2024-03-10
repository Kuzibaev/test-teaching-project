from django.urls import path, include
from drf_spectacular.views import SpectacularJSONAPIView, SpectacularSwaggerView


class ApiV1View(SpectacularJSONAPIView):
    urlconf = 'api.v1.urls'
    custom_settings = {
        "SCHEMA_PATH_PREFIX_INSERT": "/v1"
    }


app_name = 'api'
urlpatterns = [
    path('v1/', include('api.v1.urls')),
    path('v1/openapi/', ApiV1View.as_view(), name='v1-openapi'),
    path('v1/swagger/', SpectacularSwaggerView.as_view(url_name='api:v1-openapi'), name='v1-swagger'),
]
