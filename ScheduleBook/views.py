from django.shortcuts import render,HttpResponse,redirect
from .models import Record
from django.utils import timezone
from django.views.generic import ListView
from .forms import RecordCreateForm
# Create your views here.
def home(request):
    context =  {
        'schedules' : Record.objects.all(),
        'count': Record.objects.all().count()+1,
        'date': timezone.now
    }
    return render(request, "ScheduleBook/home.html",context)

def record_create_view(request):
    form = RecordCreateForm(request.POST or None)
    
    context = {'form' : form,
                'count': Record.objects.all().count()+1,
                'date': timezone.now
            }
    if(form.is_valid()):
        form.save()
        return redirect('record-home')
    return render(request, "ScheduleBook/record_create.html",context)

class RecordListView(ListView):
    model = Record
    template_name = "ScheduleBook/home.html"
    context_object_name = 'schedules'
    ordering = ['-id']



