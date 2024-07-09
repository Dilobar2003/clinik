from django.urls import path
from .views import HomeView, CommentView, AboutView

app_name = 'main'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('about/', AboutView.as_view(), name='about')


]