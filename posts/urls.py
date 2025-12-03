from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.story_selection, name = "select"),
    path('story_1', views.fill_in_blanks_1, name= "list_1"),
    path('story_2', views.fill_in_blanks_2, name= "list_2"),
    path('story_3', views.fill_in_blanks_3, name= "list_3"),
    path('story_4', views.fill_in_blanks_4, name= "list_4"),
    path('story_5', views.fill_in_blanks_5, name= "list_5"),
    path('story_6', views.fill_in_blanks_6, name= "list_6"),
    path('story_8', views.fill_in_blanks_8, name= "list_8"),
    path('page', views.post_page, name= "page"),
    path('send-email/', views.send_email_url, name='send_email_url'),
    path('story_1/<str:idname>/', views.fillin_detail_view, name='fillin_detail'),
    path('generated-story', views.fill_in_blanks_1_generated, name='generated_story')
]