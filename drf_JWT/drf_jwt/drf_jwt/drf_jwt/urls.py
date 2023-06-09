from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns = [
    # for admin site
    path(f"{settings.ADMIN_URL}/", admin.site.urls),
    # from user app (Django)
    path("user/", include("user.urls", namespace="user")),
    # from user api (DRF)
    path("user-api/", include("user.api.urls", namespace="user_api")),
    # main(auth) app
    path("auth/", include("main.urls", namespace="main")),

]

if settings.DEBUG:
    urlpatterns += [
        # Testing 404 and 500 error pages
        path("404/", TemplateView.as_view(template_name="404.html"), name="404"),
        path("500/", TemplateView.as_view(template_name="500.html"), name="500"),
    ]

    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]


def bad(request):
    """ Simulates a server error """
    1 / 0


if not settings.DEBUG:
    urlpatterns += [
        path("bad/", bad),
        # path('', include('djvue.urls')),
    ]
