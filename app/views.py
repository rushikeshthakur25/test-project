from django.shortcuts import render
from django.http import HttpResponse
from .models import Clogin, Register, Packages, Product, Chekout,Academy,Certificate
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def appointment(request):
    return render(request, 'appointment.html')


def packaeges(request):
    return render(request, 'packaeges.html')

def chekoutform(request):
    return render(request, 'chekout.html')


def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})


def cart(request):
    c = Packages.objects.all()
    return render(request, 'cart.html', {'c': c})

def academy(request):
    a = Academy.objects.all()
    return render(request, 'academy.html',{'a':a})    


def certificate(request):
    c = Certificate.objects.all()
    a = Academy.objects.all()
    return render(request, 'certificate.html',{'c':c,'a':a})    


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = Register.objects.filter(email=email)
        if user:
            msg = 'User Already Exist'
            return render(request, 'index.html', {'msg': msg})
        else:
             if password == cpassword:
                 newuser = Register.objects.create(
                     fname=fname, lname=lname, email=email, mobile=mobile, password=password)
                 msg = 'User Created Successfully'
                 return render(request, 'index.html', {'msg': msg})
             else:
                msg = 'pass not match'
                return render(request, 'login.html', {'msg': msg})


def packages(request):
    if request.method == 'POST':
        packaeges_name = request.POST['packaeges_name']
        service = request.POST['service']
        packaeges_price = request.POST['packaeges_price']
        packaeges_offer = request.POST['packaeges_offer']

        user = Packages.objects.filter(packaeges_name=packaeges_name)
        if user:
            msg = 'packages Already Exist'
            return render(request, 'packages.html', {'msg': msg})
        else:
             if packaeges_offer == packaeges_offer:
                 newuser = Packages.objects.create(
                     packaeges_name=packaeges_name, packaeges_offer=packaeges_offer, packaeges_price=packaeges_price, service=service)
                 msg = 'Packages Created Successfully'
                 return render(request, 'cart.html', {'msg': msg, })
             else:
                msg = 'not match'
                return render(request, 'packaeges.html', {'msg': msg})


def chekout(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        society = request.POST['society']
        landmark = request.POST['landmark']
        pcode = request.POST['pcode']
        city = request.POST['city']
        organization = request.POST['organization']
        phone = request.POST['phone']
        gst = request.POST['gst']

        user = Chekout.objects.filter(fname=fname)
        if user:
           msg = 'packages Already Exist'
        else:
            if lname == lname:
              newuser = Chekout.objects.create(fname=fname, lname=lname, society=society,
                                               landmark=landmark, pcode=pcode, city=city, organization=organization, phone=phone,gst=gst)
              msg = 'User Created Successfully'
              return render(request, 'chekout.html', {'msg': msg})
            else:
             msg = 'not match'
            #  return render (request,'chekout.html',{'msg':msg})
