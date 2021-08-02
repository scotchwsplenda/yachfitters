from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path('', views.get_df_panda, name='index'),
    # path('choose_team', views.choose_teamy, name='index'),
    path('choose_team/', views.choose_team_view),
    path('cool_form/<acr>/', views.cool_form_view, name='cool_form_team'),
    path('', TemplateView.as_view(template_name='brokerage/base.html')),
]