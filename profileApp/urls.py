from django.urls import path
from .api.views import ProfileList, SingleProfile


urlpatterns = [
    path('', ProfileList.as_view(),),
    path('<int:pk>/', SingleProfile.as_view(),)
]
