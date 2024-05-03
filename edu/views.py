from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView , DetailView
from django.shortcuts import render , redirect
from .models import Lectures
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView , UpdateView ,DeleteView , FormView 
from django.contrib.auth import logout as AuthLogout , login as AuthLogin , authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt , csrf_protect
from django.utils.decorators import method_decorator
# Create your views here.

class ScheduleView(LoginRequiredMixin , ListView):
    model = Lectures
    template_name = 'base/parts/schedule.html'
    context_object_name = 'lec'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        """ 
        this commented line for filtering the data according to 
        the user  who is logged in and showing only his lectures
        """
      #  context['lec'] = context['lec'].filter(author=self.request.user)
        context['count'] = context['lec'].filter(status=False).count()
        return context
    

class LecDetails(DetailView):
    model = Lectures
    template_name = 'base/parts/LecDetail.html'
    context_object_name = 'lecs'
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
class CustomerLoginView(LoginView):
    template_name = "base/parts/login.html"
    fields = "__all__"
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy("Edu:schedule")

class CustomerRegisterView(FormView):
    template_name = 'base/parts/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("Edu:login")
    
    def form_valid(self, form) :
        user = form.save()
        if user is not None:
            AuthLogin(self.request,user)
        return super(CustomerRegisterView , self).form_valid(form)
    def get(self,*args,**kwargs ):
        if self.request.user.is_authenticated :
            return redirect('Edu:login')
        return super(CustomerRegisterView , self ).get(*args,**kwargs)


def logout(request):
    AuthLogout(request)
    return redirect('Edu:login')
def home(request):
    return render(request , 'base/parts/home.html')