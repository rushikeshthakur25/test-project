from django.shortcuts import render
from django.http import HttpResponse
from .models import Clogin, Register, Packages, Product, Chekout,Academy,Blog,Appointment
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def appointment(request):
    return render(request, 'appointment.html')


def packaeges(request):
    return render(request, 'packaeges.html')

def pay(request):
    return render(request, 'pay.html')

def chekoutform(request):
    return render(request, 'chekout.html')

def contectus(request):
    return render(request, 'contectus.html')

def about(request):
    return render(request, 'About.html')


def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})


def packagesb(request):
    c = Packages.objects.all()
    return render(request, 'packagesb.html', {'c': c})

def services(request):
    a = Academy.objects.all()
    return render(request, 'services.html',{'a':a})    


def blog(request):
    mayur = Blog.objects.all()
    return render(request, 'blog.html',{'mayur':mayur})     


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
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
                     fname=fname, email=email, mobile=mobile, password=password)
                 msg = 'User Created Successfully'
                 return render(request, 'index.html', {'msg': msg})
             else:
                msg = 'pass not match'
                return render(request, 'login.html', {'msg': msg})
def log(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['cpassword'] 

        user = Clogin.objects.get(email==email)
        if user:
            if user.password==password and email==email:
                request.session['fname']=user.fname 
                msg = 'login succesfully'
                return render(request, 'index.html',{'msg':msg})
            else:
                msg = 'email and password not match'
                return render(request, 'login.html',{'msg':msg}) 
    else:
        msg = 'Account not exist'
        return render(request, 'login.html')            



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
           return render(request, 'chekout.html')
        else:
            if lname == lname:
              newuser = Chekout.objects.create(fname=fname, lname=lname, society=society,landmark=landmark, pcode=pcode, city=city, organization=organization, phone=phone,gst=gst)
              msg = ' Successfully'
              return render(request, 'pay.html', {'msg': msg})
            else:
             msg = 'not match'
            #  return render (request,'chekout.html',{'msg':msg})

def appo(request):
    if request.method =='POST':
        client_name = request.POST['name']
        client_address = request.POST['address']
        client_mobile = request.POST['number']
        client_email = request.POST['email']
        appointment_date =request.POST['date']
        appointment_time =request.POST['time']

        user = Appointment.objects.filter(client_name=client_name)
        if user:
            return render(request, 'login.html')
        else:
            if client_address == client_address:
                newuser = Appointment.objects.create(client_name=client_name,client_address=client_address,client_mobile=client_mobile,client_email=client_email,appointment_date=appointment_date,appointment_time=appointment_time)    
                return render(request, 'login.html')

import requests

headers = { 
	"Authorization": "Bearer y70kak2K0Rg7J4PAL8sdW0MutnGJEl"
}
payload = {
  'purpose': 'FIFA 16',
  'amount': '2500',
  'buyer_name': 'John Doe',
  'email': 'foo@example.com',
  'phone': '9999999999',
  'redirect_url': 'http://www.example.com/redirect/',
  'send_email': 'True',
  'webhook': 'http://www.example.com/webhook/',
  'allow_repeated_payments': 'False',
}
response = requests.post(
  "https://api.instamojo.com/v2/payment_requests/", 
  data=payload, 
  headers=headers
)              