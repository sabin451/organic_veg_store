from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Admin.models import oreg, category,login,ureg,staff
from owner.models import vegdet,stocks,assign
from user.models import order_master,order_child
# Create your views here.
from django.http import JsonResponse

def staffhome(request):
    context = {}
    template = loader.get_template("staffhome.html")
    return HttpResponse(template.render(context, request))
def staffvieworders(request):
    uname=request.session["uname"]
    oid=staff.objects.get(uname=uname)
    o=order_master.objects.raw("select distinct(admin_ureg.id),admin_ureg.name,admin_ureg.location,admin_ureg.lmark,admin_ureg.phone,user_order_master.* from admin_ureg,user_order_master,user_order_child,owner_vegdet,admin_oreg,owner_assign,admin_staff where admin_ureg.id=user_order_master.uid and user_order_master.id=user_order_child.oid and user_order_child.vid=owner_vegdet.id and owner_vegdet.oid=admin_oreg.id and user_order_master.status='assign' and user_order_master.id=owner_assign.orderid and owner_assign.sid=admin_staff.id and owner_assign.status='pending' and admin_staff.id=%s",[oid.id])
    context = {'key': o}
    template = loader.get_template("staffvieworder.html")
    return HttpResponse(template.render(context, request))
def staffvieworders1(request,id):
    uname=request.session["uname"]
    request.session["orderid"]=id
    oid=staff.objects.get(uname=uname)

    o=order_child.objects.raw("select user_order_child.*,admin_category.cname,owner_vegdet.vegname,owner_vegdet.rate from user_order_master,user_order_child,owner_vegdet,admin_category where user_order_master.id=user_order_child.oid and user_order_child.vid=owner_vegdet.id and owner_vegdet.category=admin_category.id and user_order_master.id=%s",[id])
    context = {'key': o}
    template = loader.get_template("staffvieworderdetails1.html")
    return HttpResponse(template.render(context, request))
def updatestatus(request):
    oid=request.session["orderid"]
    o=order_master.objects.get(id=oid)
    o.status='delivered'
    o.save()
    o1=order_child.objects.filter(oid=oid)
    for i in o1:
        o2=order_child.objects.get(id=i.id)
        o2.status='delivered'
        o2.save()
    a=assign.objects.get(orderid=oid)
    a.status='delivered'
    a.save()
    return HttpResponse("<script>alert('item delivered successfully');window.location='/staffvieworderdetails';</script>")
def updatestock(request):
    if request.method=="POST":
        vname=request.POST.get("vname")
        vid=stocks.objects.get(vid=vname)
        vid.st=request.POST.get("stock")
        vid.save()
        return HttpResponse("<script>alert('stock updated successfully');window.location='/updatestock';</script>")

    else:
        uname=request.session["uname"]
        sid=staff.objects.get(uname=uname)
        o=vegdet.objects.raw("select owner_vegdet.*,owner_stocks.st from owner_vegdet,admin_staff,admin_oreg,owner_stocks where admin_oreg.id=owner_vegdet.oid and owner_vegdet.oid=admin_staff.oid and owner_vegdet.id=owner_stocks.vid and admin_staff.id=%s",[sid.id])
        context = {'k': o}
        template = loader.get_template("updatestock.html")
        return HttpResponse(template.render(context, request))
def us(request):
    if (request.method == 'GET' and request.GET.get('q') != None):
        did = request.GET.get('q')
        l = stocks.objects.filter(vid=did).values()
        return JsonResponse(list(l), safe=False)