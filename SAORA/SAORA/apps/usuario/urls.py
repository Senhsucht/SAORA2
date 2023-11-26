from django.urls import path
from .views import login_view, UsuarioAPIView, AfiliadoAPIView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('api/usuario/', UsuarioAPIView.as_view(), name='usuario-list-create'),
    path('api/afiliado/', AfiliadoAPIView.as_view(), name='afiliado-list-create'),
]
