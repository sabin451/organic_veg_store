from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Admin.models import oreg, category,login,ureg,staff
from .models import vegdet,stocks,assign
from user.models import order_master,order_child

# Create your views here.
def ownerhome(request):
    context = {}
    template = loader.get_template("ownerhome.html")
    return HttpResponse(template.render(context, request))
def oreg1(request):
    if request.method=="POST":
        name=request.POST.get("name")
        shname=request.POST.get("shname")
        loc=request.POST.get("loc")
        rno=request.POST.get("rno")
        lmark=request.POST.get("lmark")
        cno=request.POST.get("cno")
        uname=request.POST.get("uname")
        pwd=request.POST.get("password")
        s=oreg()
        s.name=name
        s.shname=shname
        s.location=loc
        s.rno=rno
        s.lmark=lmark
        s.cno=cno
        s.uname=uname
        s.pwd=pwd
        s.status='pending'
        s.save()
        l=login()
        l.uname=uname
        l.pwd=pwd
        l.utype='owner'
        l.save()
        return HttpResponse("<script>alert('Register successfully');window.location='/oreg';</script>")

    else:
        context = {}
        template = loader.get_template("ownerreg.html")
        return HttpResponse(template.render(context, request))
def veg1(request):
    if request.method=="POST":
        vegname=request.POST.get("vegname")
        cat = request.POST.get("category")
        rate=request.POST.get("rate")
        image=request.FILES["image"]
        des=request.POST.get("description")
        stock=request.POST.get("stock")
        s=vegdet()
        s.vegname=vegname
        s.category=cat
        s.rate=rate
        s.image=image
        s.des=des
        s.stock=stock
        s.status='pending'
        uname=request.session["uname"]
        o=oreg.objects.get(uname=uname)
        s.oid=o.id
        s.save()
        v=vegdet.objects.raw("select max(id) as id from owner_vegdet")
        for i in v:
            vid=i.id
        vs=stocks()
        vs.vid=vid
        vs.st=stock
        vs.save()
        return HttpResponse("<script>alert('vegetable added successfully');window.location='/veg';</script>")
    else:
        s=category.objects.all()
        context = {'key':s}
        template = loader.get_template("addvegdetails.html")
        return HttpResponse(template.render(context, request))
def vieworders(request):
    uname=request.session["uname"]
    oid=oreg.objects.get(uname=uname)
    o=order_master.objects.raw("select distinct(admin_ureg.id),admin_ureg.name,admin_ureg.location,admin_ureg.lmark,admin_ureg.phone,user_order_master.* from admin_ureg,user_order_master,user_order_child,owner_vegdet,admin_oreg where admin_ureg.id=user_order_master.uid and user_order_master.id=user_order_child.oid and user_order_child.vid=owner_vegdet.id and owner_vegdet.oid=admin_oreg.id and user_order_master.status='pending' and admin_oreg.id=%s",[oid.id])
    context = {'key': o}
    template = loader.get_template("vieworderdetails.html")
    return HttpResponse(template.render(context, request))
def vieworders1(request,id):
    uname=request.session["uname"]
    request.session["orderid"]=id
    oid=oreg.objects.get(uname=uname)
    s=staff.objects.filter(oid=oid.id)
    o=order_child.objects.raw("select user_order_child.*,admin_category.cname,owner_vegdet.vegname,owner_vegdet.rate from user_order_master,user_order_child,owner_vegdet,admin_category where user_order_master.id=user_order_child.oid and user_order_child.vid=owner_vegdet.id and owner_vegdet.category=admin_category.id and user_order_master.id=%s",[id])
    context = {'key': o,'k':s}
    template = loader.get_template("vieworderdetails1.html")
    return HttpResponse(template.render(context, request))
def assignorder(request):
    a=assign()
    uname=request.session["uname"]
    oid=oreg.objects.get(uname=uname)
    a.orderid=request.session["orderid"]
    orderid=request.session["orderid"]
    a.sid=request.POST.get("sname")
    a.oid=oid.id
    a.status='pending'
    a.save()
    o=order_master.objects.get(id=orderid)
    o1=order_child.objects.filter(oid=orderid)
    for i in o1:
        o2=order_child.objects.get(id=i.id)
        o2.status='assign'
        o2.save()
    o.status='assign'
    o.save()
    return HttpResponse("<script>alert('order assigned successfully');window.location='/vieworderdetails';</script>")
def vieworderstatus(request):
    uname=request.session["uname"]
    oid=oreg.objects.get(uname=uname)
    o=order_master.objects.raw("select distinct(admin_ureg.name),admin_ureg.location,admin_ureg.lmark,admin_ureg.phone,user_order_master.* from admin_ureg,user_order_master,user_order_child,owner_vegdet,admin_oreg where admin_ureg.id=user_order_master.uid and user_order_master.id=user_order_child.oid and user_order_child.vid=owner_vegdet.id and owner_vegdet.oid=admin_oreg.id  and admin_oreg.id=%s",[oid.id])
    context = {'key': o}
    template = loader.get_template("ownervieworderstatus.html")
    return HttpResponse(template.render(context, request))
def vieworderstatus1(request,id):
    uname=request.session["uname"]
    request.session["orderid"]=id
    oid=oreg.objects.get(uname=uname)

    o=order_child.objects.raw("select user_order_child.*,admin_category.cname,owner_vegdet.vegname,owner_vegdet.rate from user_order_master,user_order_child,owner_vegdet,admin_category where user_order_master.id=user_order_child.oid and user_order_child.vid=owner_vegdet.id and owner_vegdet.category=admin_category.id and user_order_master.id=%s",[id])
    context = {'key': o}
    template = loader.get_template("ownervieworderstatus1.html")
    return HttpResponse(template.render(context, request))
def viewstock(request):
    uname=request.session["uname"]
    uid=oreg.objects.get(uname=uname)
    s=stocks.objects.raw("select owner_vegdet.*,owner_stocks.st from owner_vegdet,owner_stocks,admin_oreg where admin_oreg.id=owner_vegdet.oid and owner_vegdet.id=owner_stocks.vid and admin_oreg.id=%s",[uid.id])
    context = {'k': s}
    template = loader.get_template("viewstock.html")
    return HttpResponse(template.render(context, request))
def editveg(request):
    uname=request.session["uname"]
    uid=oreg.objects.get(uname=uname)
    s=stocks.objects.raw("select owner_vegdet.*,owner_stocks.st from owner_vegdet,owner_stocks,admin_oreg where admin_oreg.id=owner_vegdet.oid and owner_vegdet.id=owner_stocks.vid and admin_oreg.id=%s",[uid.id])
    context = {'k': s}
    template = loader.get_template("editveg.html")
    return HttpResponse(template.render(context, request))
def deleteveg(request,id):
    vid=vegdet.objects.get(id=id)
    vid.delete()
    st=stocks.objects.get(id=id)
    st.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/editveg';</script>")
def editveg1(request,id):
    v=vegdet.objects.get(id=id)
    request.session["vid"]=id
    context = {'k':v}
    template = loader.get_template("editveg1.html")
    return HttpResponse(template.render(context, request))
def editveg2(request):
    vid=request.session["vid"]
    v=vegdet.objects.get(id=vid)
    v.rate=request.POST.get("rate")
    v.save()
    return HttpResponse("<script>alert('rate updated successfully');window.location='/editveg';</script>")












