from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import AutorViewSet, LibroViewSet

router = SimpleRouter()
router.register('autores', AutorViewSet, basename='autores')
router.register('libros', LibroViewSet, basename='libros')


urlpatterns = router.urls


