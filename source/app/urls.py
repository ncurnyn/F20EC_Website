from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from main import views
from django.conf.urls import url

from main.views import IndexPageView, ChangeLanguageView, MovieReccomdationView, MovieRatingsView 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexPageView.as_view(), name='index'),

    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),
    path('ratings/', MovieRatingsView.as_view(), name='rate'),

    path('accounts/', include('accounts.urls')),
    path('recomendations/', MovieReccomdationView.as_view(), name='reccomend'),
    path('reccomendation_system/', views.reccomendation_system,name='script'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
