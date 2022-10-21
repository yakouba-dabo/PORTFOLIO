
from django.urls import path
from .import views
from portfoliopro.settings import DEBUG,STATIC_URL,STATICFILES_DIRS
from django.conf.urls.static import static
# from django.conf import settings


urlpatterns = [
      path('',views.index,name='index'),
      path('contact',views.contact,name='contact')
]

if DEBUG:
      # urlpatterns += static(MEDIA_URL,document_root = MEDIA_ROOT),
      urlpatterns += static(STATIC_URL,document_root = STATICFILES_DIRS)