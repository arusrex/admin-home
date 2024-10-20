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

    path('backups/', views.backups, name='backups'),
    path('db_backups/', views.db_backup, name="db_backup"),
    path('db_restore/', views.db_backup_restore, name="db_restore"),

    path('login/', views.logar, name='login'),
    path('logout/', views.deslogar, name='logout'),

    path('register/', views.register, name='register'),

    path('password/', views.enviar_email_password, name='password'),

    # USER DATA
    path('user_data/', views.user_data, name="user_data"),
    path('user_logs/', views.user_logs, name="user_logs"),
    path('site_setup/', views.site_setup, name="site_setup"),

    # USERS
    path('users/', views.users, name="users"),
    path('edit_user/<int:id>/', views.edit_user, name="edit_user"),
    path('delete_user/<int:id>/', views.delete_user, name="delete_user"),

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