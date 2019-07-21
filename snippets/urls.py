from django.conf.urls import re_path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    re_path(r'^$',views.index),
    re_path(r'^snippets/$', views.SnippetList.as_view()),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetailAndDestroy.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)