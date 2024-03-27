from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from game_products.views import home_page, MyLoginView, logout_view, edit, delete, create

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_page, name="home"),
    path("login/", MyLoginView.as_view()),
    path("logout/", logout_view),
    path('edit/<int:pk>/', edit, name='edit'),
    path("delete/<int:pk>/", delete),
    path('create/<int:pk>/', create),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
