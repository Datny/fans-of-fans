from groups.views import *
from django.urls import path, re_path

app_name="groups"

urlpatterns = [
    path('groups/',views.ListGroups.as_view(), name="all"),
    path('new/', views.CreateGroupView.as_view(), name="create"),
    re_path(r'posts/in/(?{<slug>[-]\w+)/$', views.SingleGroup.as_view(),name="single")
]