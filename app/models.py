from django.db import models

# Create your models here.
class Register(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.fname

class Clogin(models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Alogin(models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Product_category(models.Model):
    product_category = models.CharField(max_length=20)  
    def __str__(self) -> str:
        return self.product_category  

class Service_category(models.Model):
     service_category = models.CharField(max_length=20)

     def __str__(self) -> str:
        return self.service_category

class Product(models.Model): 
    product_img = models.ImageField(upload_to = 'profile') 
    product_name = models.CharField(max_length=20)
    product = models.ForeignKey(Product_category, on_delete=models.CASCADE)
    product_desc = models.CharField(max_length=20)
    product_price = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.product_name    


class Service(models.Model):
    service_name = models.CharField(max_length=20)
    service = models.ForeignKey(Service_category, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.service_name

class Appointment(models.Model):
    client_name = models.CharField(max_length=20)
    client_address = models.CharField(max_length=20)
    client_mobile = models.CharField(max_length=20)
    client_email = models.CharField(max_length=20)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    def __str__(self) -> str:
        return self.client_name

class Packages(models.Model):
    packaeges_name = models.CharField(max_length=20)
    service = models.TextField()
    packaeges_price = models.PositiveIntegerField()
    packaeges_offer = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.packaeges_name

class Chekout(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone = models.IntegerField()
    society = models.CharField(max_length=20)
    landmark = models.CharField(max_length=20)
    pcode  = models.IntegerField() 
    city = models.CharField(max_length=20)
    organization = models.CharField(max_length=50)
    gst = models.CharField(max_length=20)
    def __str__(self ) -> str:
        return self.fname

class Academy(models.Model):
    course_name = models.CharField(max_length=20)
    course_duration = models.CharField(max_length=20)
    course_trainer = models.CharField(max_length=20)
    course_about = models.CharField(max_length=50)
    def __str__(self ) -> str:
        return self.course_name                       

class Blog(models.Model):
    bname = models.CharField(max_length=50)    
    btitle = models.CharField(max_length=50)
    dname = models.TextField()
    uname = models.CharField(max_length=50)
    date = models.DateField()
    image = models.ImageField(upload_to='profile')

    def __str__(self) ->str:
        return self.bname