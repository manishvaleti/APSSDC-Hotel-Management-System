from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,Rolereq,Rooms,Bookings
from .forms import BookForm, RegForm,Chgepwd,Pfupd,Rltype,Rlupd, RoomForm,BookForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from Hotel_App.functions.availability import check_availability,no_of_days
# Create your views here.
def home(request):
    return render(request,'html/home.html')

def usrreg(request):
    if request.method=="POST":
        d = RegForm(request.POST,request.FILES)
        if d.is_valid():
            d.save()
            return redirect('/login')
    d = RegForm()
    return render(request,'html/register.html',{'t':d})

@login_required
def changepwd(request):
    if request.method == "POST":
        k = Chgepwd(user=request.user,data=request.POST)
        if k.is_valid():
            k.save()
            return redirect('/login')
    k = Chgepwd(user=request)
    return render(request,'html/changepwd.html',{'t':k})

@login_required
def pfle(request):
    x = User.objects.get(id=request.user.id)
    return render(request,'html/profile.html',{'d':x})

@login_required
def pfupd(request):
    d=User.objects.get(id=request.user.id)
    if request.method=="POST":
        pf=Pfupd(request.POST,request.FILES,instance=d)
        if pf.is_valid():
            pf.save()
            return redirect('/profile')
    pf=Pfupd(instance=d)
    return render(request,'html/pfleupdate.html',{'u':pf})

@login_required
def rolereq(request):
    p = Rolereq.objects.filter(ud_id=request.user.id).count()
    if request.method == "POST":
        k =Rltype(request.POST,request.FILES)
        if k.is_valid:
            y = k.save(commit = False)
            y.ud_id = request.user.id
            y.uname = request.user.username
            y.is_checked = 0
            y.save()
            return redirect('/')
    k = Rltype()
    return render(request,'html/rolereq.html',{'d':k,'c':p})

@login_required
def gveperm(request):
    u = User.objects.all()
    r = Rolereq.objects.all()
    d = {}
    for n in u:
        for m in r:
            if n.is_superuser == 1 or n.id != m.ud_id:
                continue
            else:
                d[m.id] = n.username,m.rltype,n.role,n.id,m.id
    return render(request,'html/gvper.html',{'h':d.values()})

@login_required
def gvupd(request,t):
    y=Rolereq.objects.get(ud_id=t)
    d=User.objects.get(id=t)
    if request.method == "POST":
        n = Rlupd(request.POST,instance=d)
        if n.is_valid():
            n.save()
            #d.role = s.rltype
            y.is_checked = 1
            y.save()
            return redirect('/gvper')
    n = Rlupd(instance=d)
    return render(request,'html/gvepermissions.html',{'c':n})

@login_required
def reqdel(request,t):
    r = Rolereq.objects.get(id=t)
    u = User.objects.get(id=r.ud_id)
    if request.method == "POST":
        u.role=1
        r.delete()
        u.save()
        messages.success(request,"Request from {} Deleted Successfully".format(u.username))
        return redirect('/gvper')
    return render(request,'html/reqdel.html',{'a':u})

@login_required
def addroom(request):
    d = Rooms.objects.filter(uid_id=request.user.id)
    if request.method=="POST":
        r=RoomForm(request.POST,request.FILES)
        if r.is_valid:
            c = r.save(commit=False)
            c.uid_id = request.user.id
            c.save()
            messages.success(request,"Room Added Successfully")
            return redirect('/addroom')
    r = RoomForm()
    return render(request,'html/addroom.html',{'a':r,'x':d})

@login_required
def updtroom(request,m):
    d = Rooms.objects.get(id=m)
    if request.method == "POST":
        r = RoomForm(request.POST,request.FILES,instance=d)
        if r.is_valid():
            r.save()
            messages.info(request,"Room Updated Successfully")
            return redirect('/addroom')
    r = RoomForm(instance=d)
    return render(request,'html/updtroom.html',{'c':r})

@login_required
def delroom(request,m):
    d = Rooms.objects.get(id=m)
    if request.method=="POST":
        d.delete()
        messages.success(request,"{} Room Deleted Successfully".format(d.rno))
        return redirect('/addroom')
    return render(request,'html/delroom.html',{'x':d})

@login_required
def viewroom(request,m):
    d = Rooms.objects.get(id=m)
    return render(request,'html/view.html',{'x':d})

@login_required
def availrooms(request):
    d = Rooms.objects.all()
    return render(request,'html/showroom.html',{'x':d})
@login_required
def booking(request,m):
    d = Rooms.objects.get(id=m)
    if request.method == "POST":
        x = BookForm(request.POST)
        if x.is_valid():
            c=x.save(commit=False)
            if check_availability(m,c.sdate,c.edate):
                c.rno = request.POST['rno']
                c.uid_id = request.user.id
                c.rid_id = m
                c.save()
                messages.success(request,"Room Bookings Successfully")
                return redirect('/')
            else:
                messages.warning(request,"Room not available for mentioned dates")
                return redirect('/')
    x = BookForm()
    return render(request,'html/booking.html',{'a':d,'b':x})
@login_required
def history(request,m):
    d = Bookings.objects.filter(uid_id=m)
    r = date.today()
    return render(request,'html/history.html',{'t':d,'x':r})
@login_required
def cancelbook(request,m):
    d = Bookings.objects.get(id=m)
    if request.method == "POST":
        d.delete()
        return redirect('/profile')
    return render(request,'html/cancelbook.html',{'x':d})
@login_required
def history_man(request):
    d = Bookings.objects.all()
    return render(request,'html/history_man.html',{'t':d})
@login_required
def checkin(request,m):
    d = Bookings.objects.get(id=m)
    if request.method == 'POST':
        d.is_checkin = True
        d.ci_date = date.today()
        d.save()
        messages.success(request,"Check-In Successful")
        return redirect('/')
    return render(request,'html/checkin.html',{'t':d})
@login_required
def checkout(request,m):
    d = Bookings.objects.get(id=m)
    if request.method == 'POST':
        d.is_checkin = False
        d.co_date = date.today()
        d.save()
        messages.success(request,"Check-Out Successful")
        return redirect('/')
    return render(request,'html/checkout.html',{'t':d})

def contact(request):
    return render(request,'html/contactus.html')

def about(request):
    return render(request,'html/aboutus.html')

@login_required
def bill(request,m):
    d = Bookings.objects.get(id=m)
    a = Rooms.objects.get(id=d.rid_id)
    b = User.objects.get(id=d.uid_id)
    e = str(d.ci_date)
    f = str(d.co_date)
    g = no_of_days(e,f)
    h = a.rcost * g
    n = 0.18 * float(h)
    o = float(h) + n
    return render(request,'html/bill.html',{'x':a,'y':b,'z':g,'v':h,'t':d,'u':n,'j':o,'p':m})
