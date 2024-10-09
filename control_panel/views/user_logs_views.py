from django.shortcuts import render
from sitesetup.models import UserLogActivity

def user_logs(request):
    user_data = request.user
    user_logs = UserLogActivity.objects.filter(user=user_data)
    context = {
        'user_logs':user_logs,
    }
    return render(request, 'pages/user_logs.html', context)