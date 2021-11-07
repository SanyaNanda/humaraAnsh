from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    # path('', views.HomeView.as_view(), name="home"),
    path('add_post/',views.AddPostView.as_view(),name="add_post"),
    path('select_doctor/', views.SelectView.as_view(), name='select_doctor'),
    path('choice/<int:pk>', views.choice, name='choice'),
    # path('my_feed/',views.Feed.as_view(),name="my_feed"),
    # path('report/<int:pk>', views.ReportDetailView.as_view(), name="report_details"),


]