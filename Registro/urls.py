from django.urls import path
from . import views

urlpatterns=[
    path('usuario/<int:pk>', views.UsuarioDetailView.as_view(),name='usuario-detail'),
]

urlpatterns +=[
    path('usuario/create/',views.UsuarioCreate.as_view(),name='usuario_create'),
    path('usuario/<int:pk>/update/',views.UsuarioUpdate.as_view(),name='usuario_update'),
    path('usuario/<int:pk>/delete/',views.UsuarioDelete.as_view(),name='usuario_delete'),
]
