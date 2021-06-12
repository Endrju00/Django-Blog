from django.shortcuts import render
# from django.http import HttpResponse
from first_app.models import Topic, WebPage, AccessRecord, User
from first_app.forms import NewUserForm
# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'accessrecords': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)

def users(request):
    # user_list = User.objects.order_by('first_name')
    # user_dict = {'users': user_list}                                      lvl2
    # return render(request, 'first_app/users.html', context=user_dict)
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR form invalid')
    return render(request, 'first_app/users.html', {'form': form})
