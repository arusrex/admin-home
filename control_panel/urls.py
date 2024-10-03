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

    path('login/', views.login, name='login'),

    path('register/', views.register, name='register'),

    path('password/', views.password, name='password'),

]