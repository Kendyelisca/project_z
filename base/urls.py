from django.urls import path
from . import views


urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocates_list, name="advocates"),
    # path('advocates/<str:username>/', views.advocates_details )
        path('advocates/<str:username>/', views.AdvocateDetail.as_view() )
]