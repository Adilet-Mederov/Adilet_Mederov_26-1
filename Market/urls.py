"""Market URL Configuration

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
from django.urls import path


from products.views import MainPageCBV,ProductsCBV, ProductsDetailCBV, ProductsCreateCBV
from Market import settings
from django.conf.urls.static import static
from users.views import RegisterCBV, LogoutCBV, LoginCBV


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageCBV.as_view()),
    path('products/', ProductsCBV.as_view()),
    path('products/<int:id>/', ProductsDetailCBV.as_view()),
    path('products/create/', ProductsCreateCBV.as_view()),

    path('users/register/', RegisterCBV.as_view()),
    path('users/login/', LoginCBV.as_view()),
    path('users/logout', LogoutCBV.as_view())


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)