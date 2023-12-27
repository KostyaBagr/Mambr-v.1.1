
from django.shortcuts import render, redirect, get_object_or_404

from blog.models import Questions
from notice.models import Notification
def ShowNotifications(request):
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



