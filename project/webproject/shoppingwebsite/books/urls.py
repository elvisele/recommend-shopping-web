from django.conf.urls import include, url
from books import views

urlpatterns = [

	url(r'^$', views.index,name='index'),
    url(r'register/$',views.register,name='register'),
    url(r'logout/$',views.user_logout,name='logout'),
    url(r'login/$',views.user_login,name='login'),
    url(r'detail/(?P<isbn>[\d]+)/$',views.detail,name='detail'),
    url(r'listing/$',views.listing,name='listing'),
    url(r'shoppingcart/$',views.shoppingcart,name='shoppingcart'),
    url(r'shoppingbuy/$',views.shoppingbuy,name='shoppingcart'),
    url(r'deleteshopping/(?P<isbn>[\d]+)/$',views.deleteshopping,name='deleteshopping'),
    url(r'deletecart/(?P<isbn>[\d]+)/$',views.deletecart,name='deletecart'),
    url(r'cart/(?P<isbn>[\d]+)/$',views.cart,name='cart'),
    url(r'buy/(?P<isbn>[\d]+)/$',views.buy,name='buy'),

]

