from django.urls import path
from .import views
urlpatterns = [
   path('',views.index,name='index'),
   path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('chekout/',views.chekout,name='chekout'),
    path('appointment/',views.appointment,name='appointment'),
    path('packages/',views.packages,name='packages'),
    path('packaeges/',views.packaeges,name='packaeges'),
    path('packagesb/',views.packagesb,name='packagesb'),
    path('product/',views.product,name='product'),
    path('chekoutform/',views.chekoutform,name='chekoutform'),
    path('services/',views.services,name='services'),
    path('blog/',views.blog,name='blog'),
    path('contectus/',views.contectus,name='contectus'),
    path('about/',views.about,name='about'),
    path('pay/',views.pay,name='pay'),
    path('appo/',views.appo,name='appo'),
]