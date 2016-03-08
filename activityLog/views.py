from django.shortcuts import render
from .models import Activity


# Create your views here.
def default(request):
    activities = Activity.objects.all
    return render(request, 'activityLog/table.html',
                  {'activities': activities})


def add_entry(request, sn):
    if request.method == "GET":
        index = int(sn)-1
        new = Activity.objects.order_by('name')[index]
        return render(request, 'activityLog/edit.html', {'activity': new})
    else:
        new = Activity()
        new.name = request.POST['name']
        new.description = request.POST['description']
        new.done = request.POST.get('done', False)
        new.remarks = request.POST.get('remarks', "moving on")
        new.save()
        return default(request)
