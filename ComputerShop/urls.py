"""ComputerShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from comp_shop.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ComputerList.as_view(), name='main_page'),
    url(r'^add_computer/$', create_computer, name='create_computer'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^signin/$', signin1, name='signin'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^logout$',  logout_view, name='logout'),
    url(r'^user_page/$', user_page, name='user_page'),
    url(r'^(?P<id>\d+)$', ComputerView.as_view(), name='computer_url'),
    url(r'^order_add/$', order_add, name='order_add'),
    url(r'^order_delete/$', order_delete, name='order_delete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
