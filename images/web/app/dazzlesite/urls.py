"""dazzlesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from dazzlesite.views import dizzy
from dictbuilder.views import (
    dictbuilder,
    webcli,
    json_api,
    DynamicArgsView,
    schedule,
    canvasapp,
)

urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url="static/favicon.ico")),
    path("admin/", admin.site.urls),
    # simple call to dizzy-request.py
    path("dizzy/", dizzy.request, name="dizzy"),
    # dictbuilder app
    path("", dictbuilder, name="dictbuilder"),
    path("webcli/", webcli, name="webcli"),
    path("schedule/", schedule, name="schedule"),
    path("json_api/", json_api, name="json_api"),
    path("canvasapp/", canvasapp, name="canvasapp"),
    path(
        "dynamic/<str:function_namespace>/",
        DynamicArgsView.as_view(),
        name="dynamic_args",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
