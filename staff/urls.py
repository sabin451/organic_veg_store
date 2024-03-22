from django.urls import path
import staff.views

urlpatterns =[
    path('shome/',staff.views.staffhome),
    path('staffvieworderdetails/', staff.views.staffvieworders, name='staffvieworderdetails'),
    path('staffvieworders1/<id>', staff.views.staffvieworders1, name='staffvieworders1'),
    path('updatestatus/',staff.views.updatestatus,name='updatestatus'),
    path('updatestock/', staff.views.updatestock, name='updatestock'),
    path('us/', staff.views.us, name='us')

]