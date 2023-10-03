from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("home", views.home, name="pothome"),
    path("index<int:order>", views.index, name="potindex"),
    # path("sites", views.site_index, name="site-index"),
    # path("search", views.search, name="search"),
    # path("<int:tpr>", views.fabric_by_number),
    # path("glossary", views.glossary, name="glossary"),
    # path("no-match", views.no_match, name="no-match"),
    # path("site_<slug:slug>", views.site, name="site-type"),
    # path("report_<slug:slug>", views.report, name="report-type"),
    path("<slug:slug>", views.industry, name="industry-type"),
    
]
