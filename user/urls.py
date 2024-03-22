from django.urls import path
import user.views

urlpatterns =[
    path('ureg/', user.views.ureg1, name='ureg'),
    path('uhome/', user.views.userhome, name='uhome'),
    path('searchitems/', user.views.searchitems, name='searchitems'),
    path('searchitems1/<id>', user.views.searchitems1, name='searchitems1'),
    path('addcart/', user.views.addcart, name='addcart'),
    path('deletecart/<id>', user.views.deletecart, name='deletecart'),
    path('viewcart/', user.views.viewcart, name='viewcart'),
    path('payment/', user.views.payment, name='payment'),
    path('paymentcon/',user.views.paymentcon,name='paymentcon'),
    path('savepayment/', user.views.savepayment, name='savepayment'),
    path('uservieworderstatus/',user.views.uservieworderstatus, name='uservieworderstatus'),
    path('uservieworderstatus1/<id>', user.views.uservieworderstatus1, name='uservieworderstatus1'),
    path('cancelorder/', user.views.cancelorder, name='cancelorder'),
    path('cancelorder1/<id>', user.views.cancelorder1, name='cancelorder1'),
    path('cancelorder2/', user.views.cancelorder2, name='cancelorder2'),

]