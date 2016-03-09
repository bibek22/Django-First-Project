from django.shortcuts import render
from .models import Activity


# Create your views here.
def default(request, id=None):
    activities = Activity.objects.all
    if id:
        Activity.objects.filter(id=id)[0].delete()
    return render(request, 'activityLog/table.html',
                  {'activities': activities})


def add_entry(request, sn):
    if request.method == "GET":
        index = int(sn)
        new = Activity.objects.filter(id=index)[0]
        return render(request, 'activityLog/edit.html', {'activity': new})
    else:
        new = Activity()
        new.name = request.POST['name']
        new.description = request.POST['description']
        new.done = request.POST.get('done', "")
        new.remarks = request.POST.get('remarks', "moving on")
        new.save()
        return default(request)


def add(request):
    new = Activity()
    if request.method == 'POST':
        new.name = request.POST['name']
        new.description = request.POST['description']
        new.remarks = request.POST.get('remarks', "")
        new.save()
        return default(request) 
    return render(request, 'activityLog/edit.html', {'activities': new})
