from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from user_profile.models import *
from notice.models import Notification
# Create your views here.
from django.contrib.auth.decorators import permission_required

from notice.models import Notification
def ShowNotifications(request):
    if Notification.sender == Notification.user:
        print('Получатель является оправителем')
    else:
        print('Получатель не является отправителем')
        user = request.user
        notifications = Notification.objects.filter(user=user).order_by('-date')
        Notification.objects.filter(user=user, is_seen=False).update(is_seen=True)
        dict = {
            'notifications': notifications
        }
    return render(request, 'notice/notifications.html', dict)


def DeleteAllAuthorNotice(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).delete()
    return redirect('show-notifications')



