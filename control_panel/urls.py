# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from control_panel import views
from django.urls import path

app_name = 'control_panel'

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.logar, name='login'),
    path('logout/', views.deslogar, name='logout'),

    path('register/', views.register, name='register'),

    path('password/', views.enviar_email_password, name='password'),

    path('site_setup/', views.site_setup, name="site_setup"),

    path('main_menus/', views.main_menus, name='main_menus'),
    path('edit_main_menu/<int:id>/', views.edit_main_menu, name='edit_main_menus'),
    path('delete_main_menu/<int:id>/', views.delete_main_menu, name='delete_main_menus'),

    path('sub_menus/', views.sub_menus, name='sub_menus'),
    path('edit_sub_menu/<int:id>/', views.edit_sub_menu, name='edit_sub_menu'),
    path('delete_sub_menu/<int:id>/', views.delete_sub_menu, name='delete_sub_menu'),

    path('ss_menus/', views.sub_sub_menus, name='sub_sub_menus'),
    path('edit_ss_menu/<int:id>/', views.edit_ss_menus, name='edit_ss_menu'),
    path('delete_ss_menu/<int:id>/', views.delete_ss_menus, name='delete_ss_menu'),

]