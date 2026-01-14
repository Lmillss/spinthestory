from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.story_selection, name="select"),

    path('polling_panic/', views.fill_in_blanks_1, name="list_1"),
    path('unchecked_aggression/', views.fill_in_blanks_2, name="list_2"),
    path('unnatural_disaster/', views.fill_in_blanks_3, name="list_3"),
    path('bad_influence/', views.fill_in_blanks_4, name="list_4"),
    path('gutsy_gamble/', views.fill_in_blanks_5, name="list_5"),
    path('fundraising_fiasco/', views.fill_in_blanks_6, name="list_6"),
    path('technology_termoil/', views.fill_in_blanks_8, name="list_8"),

    path(
        'stories/<slug:story_slug>/<str:idname>/',
        views.story_detail_view,
        name='story_detail'
    ),

    path('send-email/', views.send_email_url, name='send_email_url'),
    path('generated-story/', views.fill_in_blanks_generated, name='generated_story'),
]