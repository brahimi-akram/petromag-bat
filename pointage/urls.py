from django.urls import path
from . import views

urlpatterns = [ 
    path('pointage/<int:ID>/',views.pointage2,name='pointage'),
    path('menu/', views.menu_view, name='menu_view'),


    # path('add_chef_station/', views.add_chef_station, name='add_chef_station'),
    path('add_employe/<int:ID>/', views.add_employe, name='add_employe'),
    path('main/<int:ID>/<int:year>', views.main_view, name='main_view'),
    path('main_all/<int:ID>/<int:year>', views.main_view_all, name='main_view_all'),
    
    
    path('remboursement/<int:ID>',views.remboursement_formule,name='remboursement'),
    path('table_employe/<int:ID>/', views.table_employe, name='table_employe'),
    path('update_employe/<int:ID>/', views.update_employe, name='update_employe'),
    path('affichage_mois/<int:ID>/', views.affichage_mois, name='affichage_mois'),
    path('pointage_mois/<int:ID>/', views.pointage_mois, name='pointage_mois'),
    path('pointage_mois_all/<int:ID>/', views.pointage_mois_all, name='pointage_mois_all'),
    path('affichage_mois_all/<int:ID>/', views.affichage_mois_all, name='affichage_mois_all'),
    path('synthese/<int:ID>/', views.synthese, name='synthese'),
    path('mission/<int:ID>/',views.mission,name='mission'),

    path('',views.login_view,name='login'),
    path("logout/",views.logout_view,name="logout"),
    
    path('fichep/',views.fiche_de_paie,name="ficheP"),
    path('err/',views.corriger_erreur , name="err"),
    path('fdp/',views.validation_fdp ,name="fdp"),
    
    path('download/<str:p>/',views.download_excel,name="download_excel"),
    path('desactiver/<int:ID>/',views.desactiver,name='desactiver'),
    path('activer/<int:ID>/',views.activer,name='activer'),
    path('add_profile',views.add_profile,name='add-profile'),
]