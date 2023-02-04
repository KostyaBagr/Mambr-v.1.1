from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from user_profile.models import *
from notice.models import Notification
# Create your views here.
from django.contrib.auth.decorators import permission_required


def ShowNotifications(request):
    user = request.user


    notifications = Notification.objects.filter(user=user).order_by('-date')
    Notification.objects.filter(user=user, is_seen=False).update(is_seen=True)

    dict = {
        'notifications': notifications
    }
    return render(request, 'notice/notifications.html', dict)

def get_author_email(request):
    get_author = MyUserProfile.objects.filter(author=request.user)
    get_email = get_author.email

    return get_email
def DeleteNotifications(request, notice_id):
    user = request.user
    notifications = Notification.objects.filter(id=notice_id, user=user).delete()
    return redirect('show-notifications')


def DeleteAllAuthorNotice(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).delete()

    return redirect('show-notifications')


# def get_user_id(request):
#     n = MyUserProfile.objects.filter(request.author.id)
#     get_email = n.email
#     a = print('Вот его почта',  get_email)
#     return HttpResponse(a)
