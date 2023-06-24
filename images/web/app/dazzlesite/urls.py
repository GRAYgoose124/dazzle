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

from dazzlesite.views import dizzy
from dict_builder.views import dict_builder, second_page, DynamicArgsView

urlpatterns = [
    path("admin/", admin.site.urls),
    # simple call to dizzy-request.py
    path("dizzy/", dizzy.request, name="dizzy"),
    # dictbuilder app
    path("", dict_builder, name="dict_builder"),
    path(
        "dynamic/<str:function_namespace>/",
        DynamicArgsView.as_view(),
        name="dynamic_args",
    ),
    path("dict-builder/second/", second_page, name="second_page"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
