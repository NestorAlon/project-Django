from django.urls import path, include
from . import views  # --- (1)

urlpatterns = [
    path('', views.ArticleList.as_view(), name='index'),  # --- (2)
    path('create', views.ArticleCreate.as_view(), name='create'),
    path('detail/<int:article_id>/', views.ArticleDetail.as_view(), name='detail'), # Ruta para la vista de detalles con un parámetro dinámico 'article_id'
    path('edit/<int:article_id>/', views.ArticleUpdate.as_view(), name='edit'),
    path('delete/<int:article_id>/', views.ArticleDelete.as_view(), name='delete'), 
]
