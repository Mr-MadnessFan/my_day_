
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView

from plan.models import Plan, TimeUntilDone


def detail_page(request, slug):
    plan = get_object_or_404(Plan, slug=slug)
    context = {
        'plan':plan
    }
    return render(request, 'details.html', context)

def not_done_page(request):
    plan = Plan.objects.all().filter(status=Plan.Status.NotDone)
    time_until_done = TimeUntilDone.objects.all()
    context = {
        'plan':plan,
        "time_until_done":time_until_done
    }
    return render(request, 'index.html', context)

def done_page(request):
    plan = Plan.objects.all().filter(status=Plan.Status.Done)
    time_until_done = TimeUntilDone.objects.all()
    context = {
        'plan':plan,
        "time_until_done": time_until_done
    }
    return render(request, 'done.html', context)

class UpdatePlanView(UpdateView):
    model = Plan
    fields = ('title', 'slug','body', 'time_until_done', 'status')
    template_name = 'crud/update.html'

class DeletePlanView(DeleteView):
    model = Plan
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('home_page')

class CreatePlanView(CreateView):
    model = Plan
    fields = ('title', 'slug','body', 'time_until_done', 'status')
    template_name = 'crud/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

