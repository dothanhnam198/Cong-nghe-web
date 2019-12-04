from django.urls import path
from topics.views import (
    create_topic_view,
    detail_topic_view,
    edit_topic_view,
    edit_topic_super_user_view,
)

app_name = 'topic'

urlpatterns = [
    path('create/', create_topic_view, name='create'),
    path('<slug>/', detail_topic_view, name='detail'),
    path('<slug>/edit/', edit_topic_view, name='edit'),
    path('<slug>/edit_superuser/', edit_topic_super_user_view, name='edit_superuser'),

]