from django.urls import path
import owner.views

urlpatterns =[
    path('oreg/', owner.views.oreg1, name='oreg'),
    path('veg/', owner.views.veg1, name='veg'),
    path('ohome/', owner.views.ownerhome, name='ohome'),
    path('vieworderdetails/', owner.views.vieworders, name='vieworderdetails'),
    path('vieworders1/<id>', owner.views.vieworders1, name='vieworders1'),
    path('assignorder/', owner.views.assignorder, name='assignorder'),
    path('vieworderstatus/',owner.views.vieworderstatus, name='vieworderstatus'),
    path('vieworderstatus1/<id>', owner.views.vieworderstatus1, name='vieworderstatus1'),
    path('viewstock/', owner.views.viewstock, name='viewstock'),
    path('editveg/', owner.views.editveg, name='editveg'),
    path('editveg1/<id>', owner.views.editveg1, name='editveg1'),
    path('deleteveg/<id>', owner.views.deleteveg, name='deleteveg'),
    path('editveg2/', owner.views.editveg2, name='editveg2'),

]