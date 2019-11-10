from django.contrib import admin
from django.urls import include, path
# import polls.views as views
from . import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    # path('',views.IndexView.as_view()),
    path('', views.index),
]
