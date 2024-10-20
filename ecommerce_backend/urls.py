from django.contrib import admin
from django.urls import path, include
'''
schema_view = get_schema_view(
   openapi.Info(
      title="Your API Title",
      default_version="v1",
      description="Your API description",
      terms_of_service="https://example.com/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
)

urlpatterns = [
   # Your existing URL patterns
   # ...
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls'))
]
