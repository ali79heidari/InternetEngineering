from django.urls import path

from .views import FoodItemCreateView, select_food_create_view, profile_view, EditCalorielimitView, DeleteFood

urlpatterns = [
    path('', profile_view, name='profile'),
    path('fooditem_create/', FoodItemCreateView.as_view(), name='fooditem_create'),
    path('selectFood/', select_food_create_view, name='selectFood'),
    path('profile/', profile_view, name='profile'),
    path('calorielimit_edit/<int:pk>', EditCalorielimitView.as_view(), name='calorielimit_edit'),
    path('deleteFood/<int:pk>', DeleteFood.as_view(), name='deleteFood'),
]
