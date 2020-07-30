from django.urls import path
from  dashboard.views import BugListView
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', BugListView.as_view()),


]