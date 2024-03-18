from django.urls import path
from .views import IndexView, PostView, ProjetoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>', PostView.as_view(), name='post'),
    path('projeto/<int:pk>', ProjetoView.as_view(), name='projeto')
]