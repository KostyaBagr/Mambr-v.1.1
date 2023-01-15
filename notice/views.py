from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from notice.models import Notification
# Create your views here.
def ShowNotifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')


    dict = {
        'notifications':notifications
    }
    return render(request, 'notice/notifications.html', dict)


def DeleteNotifications(request, notice_id):
    user =request.user
    notifications = Notification.objects.filter(id=notice_id,user=user).delete()
    return redirect('show-notifications')

def DeleteAllAuthorNotice(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).delete()
    return redirect('show-notifications')