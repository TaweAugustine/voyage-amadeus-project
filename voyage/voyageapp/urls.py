from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ( 
    TravelInspiration, 
    FavoritesViewSet,
    TravelInspirationDetail,
    TravelInspirationSearch,
)

router = DefaultRouter()
router.register("favorites", FavoritesViewSet)

urlpatterns = [

    path('travel-inspiration/', TravelInspiration.as_view(),name="travel-inspiration"),
    path('travel-inspiration/<str:pk>/', TravelInspirationDetail.as_view(),name="travel-inspiration-detail"),
    path('travel-inspiration/search/<str:keyword>/', TravelInspirationSearch.as_view(),name="travel-inspiration-search"),


    path('', include(router.urls)),


]

