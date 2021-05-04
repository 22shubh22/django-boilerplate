from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views

schema_view = get_schema_view(
    openapi.Info(title="Toyoko Backend API DOCS", default_version="v1"),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "apidocs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/v1/", include("core.urls")),
    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
