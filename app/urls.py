from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm , MyPasswordChangeForm ,MyPasswordResetForm

urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.ProdutDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm, success_url=
    '/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm),name='password_reset'),
    path('mshirts/<slug:data>', views.mshirts, name='mshirtsdata'),
    path('mshirts/', views.mshirts, name='mshirts'),
    path('mhoodjack/<slug:data>', views.mhoodjack, name='mhoodjackdata'),
    path('mhoodjack/', views.mhoodjack, name='mhoodjack'),
    path('mjeans/<slug:data>', views.mjeans, name='mjeans'),
    path('mjeans/', views.mjeans, name='mjeans'),
    path('mtrouser/<slug:data>', views.mtrouser, name='mtrouser'),
    path('mtrouser/', views.mtrouser, name='mtrouser'),
    path('mactivewear/<slug:data>', views.mactivewear, name='mactiveweardata'),
    path('mactivewear/', views.mactivewear, name='mactivewear'),
    path('wdress/<slug:data>', views.wdress, name='wdressdata'),
    path('wdress/', views.wdress, name='wdress'),
    path('wtops/<slug:data>', views.wtops, name='wtopsdata'),
    path('wtops/', views.wtops, name='wtops'),
    path('wjeans/<slug:data>', views.wjeans, name='wjeansdata'),
    path('wjeans/', views.wjeans, name='wjeans'),
    path('wskirts/<slug:data>', views.wskirts, name='wskirtsdata'),
    path('wskirts/', views.wskirts, name='wskirts'),
    path('wactivewear/<slug:data>', views.wactivewear, name='wactiveweardata'),
    path('wactivewear/', views.wactivewear, name='wactivewear'),
    path('girls/<slug:data>', views.girls, name='girlsdata'),
    path('girls/', views.girls, name='girls'),
    path('boys/<slug:data>', views.boys, name='boys'),
    path('boys/', views.boys, name='boys'),
    path('registration/',views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path('checkout/', views.checkout, name='checkout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
