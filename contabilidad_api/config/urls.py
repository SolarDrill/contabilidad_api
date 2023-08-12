from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
from contabilidad_dev import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("contabilidad_api.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
# Your existing URL patterns
urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("users/", include("contabilidad_api.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URL patterns
urlpatterns += [
    path('api/v1/', views.main_page, name="main_page"),
    path('api/v1/departments/', views.department_list, name='department_list'),
    path('api/v1/departments/create/', views.department_create, name='department_create'),  # Add this line
    path('api/v1/departments/<uuid:pk>/update/', views.department_update, name='department_update'),  # Add this line
    path('api/v1/departments/<uuid:pk>/delete/', views.department_delete, name='department_delete'),  # Add this line
    path('api/v1/units/', views.unit_list, name='unit_list'),
    path('api/v1/units/create/', views.unit_create, name='unit_create'),
    path('api/v1/units/<uuid:pk>/update/', views.unit_update, name='unit_update'),
    path('api/v1/units/<uuid:pk>/delete/', views.unit_delete, name='unit_delete'),
    path('api/v1/suppliers/', views.supplier_list, name='supplier_list'),
    path('api/v1/suppliers/create/', views.supplier_create, name='supplier_create'),
    path('api/v1/suppliers/<uuid:pk>/update/', views.supplier_update, name='supplier_update'),
    path('api/v1/suppliers/<uuid:pk>/delete/', views.supplier_delete, name='supplier_delete'),
    path('api/v1/items/', views.item_list, name='item_list'),
    path('api/v1/items/create/', views.item_create, name='item_create'),
    path('api/v1/items/<uuid:pk>/update/', views.item_update, name='item_update'),
    path('api/v1/items/<uuid:pk>/delete/', views.item_delete, name='item_delete'),
    path('api/v1/entries/', views.send_accounting_data, name='accounting_entry_list'),
    path('api/v1/send-accounting-data/', views.send_accounting_data, name='send_accounting_data')
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
