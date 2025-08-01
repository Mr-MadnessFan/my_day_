
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import  render
from django.urls import reverse_lazy
from django.views.generic import CreateView


def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')

def dashboard_view(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request, 'dashboard.html', context)

class SingInView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
