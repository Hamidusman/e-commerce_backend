from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'ratings', views.RatingViewSet, basename='rating')
router.register(r'cart', views.CartViewSet, basename='cart')

urlpatterns = router.urls