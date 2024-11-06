from django.shortcuts import render
from sitesetup.models import UserLogActivity
from django.contrib.auth.decorators import login_required

@login_required
def user_logs(request):
    user_data = request.user
    
    if user_data.is_superuser:
        user_logs = UserLogActivity.objects.all().order_by('-timestamp')
    else:
        user_logs = UserLogActivity.objects.filter(user=user_data).order_by('-timestamp')

    context = {
        'user_logs':user_logs,
    }
    return render(request, 'pages/user_logs.html', context)