from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.views.static import serve

# The folder Django loads index.html from (your React build folder)
REACT_BUILD_DIR = settings.TEMPLATES[0]['DIRS'][0]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    re_path(
        r'^(?P<path>manifest\.json|favicon\.ico|logo192\.png|logo512\.png)$',
        serve,
        {'document_root': REACT_BUILD_DIR},
    ),
    path('', TemplateView.as_view(template_name='index.html')),
]