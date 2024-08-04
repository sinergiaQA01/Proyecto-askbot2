"""
main url configuration file for the askbot site
"""
from django.conf import settings
from django.conf.urls import handler404
from django.urls import include, path, re_path

import askbot.urls
from askbot import is_multilingual
from askbot.views.error import internal_error as handler500
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
import followit.urls

admin.autodiscover()

if is_multilingual():
    from django.conf.urls.i18n import i18n_patterns
    urlpatterns = i18n_patterns(
        path(r'%s' % settings.ASKBOT_URL, include(askbot.urls))
    )
else:
    urlpatterns = [
        path(r'%s' % settings.ASKBOT_URL, include(askbot.urls))
    ]

urlpatterns += [
    re_path(r'^admin/', admin.site.urls),
    #(r'^settings/', include(askbot.deps.livesettings.urls)),
    re_path(r'^followit/', include(followit.urls)),
    re_path(r'^robots.txt', include('robots.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = 'askbot.views.error.internal_error'