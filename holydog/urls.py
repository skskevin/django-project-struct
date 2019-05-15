#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from apps.accounts import views as accounts_views
from django.views.generic import TemplateView

urlpatterns = [
    # demo url conf, include must have single quote(')
    # url(r'^path/$', include('apps.app.urls'))
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/logout', accounts_views.user_logout),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('example/', include('apps.example.urls')),
]

# 关闭调试模式，如果未部署Nginx,则添加此URL，让Django提供静态文件
# if settings.DEBUG is False:
#     urlpatterns += [
#         path(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#     ]

# UPLOAD MEDIA IN DEBUG
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
