from django.urls import path, include
from . import views
from django.conf.urls import url 
from .views import update_view, detail_view, GeeksDeleteView

urlpatterns = [path("", views.home, name="home"),
                path('', include('django.contrib.auth.urls')),
                path("addnew/", views.add_project, name="add_project"),
                path('manage/',views.manage, name='manage'),
                path('table/',views.table, name='table'),
                path('<id>/', detail_view ),
                path('<id>/update/', update_view ),
                path('<pk>/delete/', GeeksDeleteView.as_view()),
]

