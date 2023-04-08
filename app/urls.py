from django.urls import path
from .import views
urlpatterns = [
   path('',views.index,name='index'),
   path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('appointment/',views.appointment,name='appointment'),
    path('packages/',views.packages,name='packages'),
    path('packaeges/',views.packaeges,name='packaeges'),
    path('cart/',views.cart,name='cart'),
    path('chekout/',views.chekout,name='chekout'),
    path('product/',views.product,name='product'),
    path('chekoutform/',views.chekoutform,name='chekoutform'),
    path('academy/',views.academy,name='academy'),
    path('certificate/',views.certificate,name='certificate'),
]