from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from quotes.models import Author, Quote
from quotes.forms import QuoteForm, AuthorForm, UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required

class UserDetailView(DetailView):
    context_object_name = 'user_detail'
    model = User
    template_name = "quotes/user_detail.html"

class AuthorDetailView(DetailView):
    context_object_name = 'author_detail'
    model = Author
    template_name = "quotes/author_detail.html"

class AuthorListView(ListView):
    context_object_name = 'authors'
    model = Author

class QuoteDetailView(DetailView):
    context_object_name = 'quote_detail'
    model = Quote
    template_name = "quotes/quote_detail.html"

class QuoteListView(ListView):
    context_object_name = 'quotes'
    model = Quote
    template_name = "quotes/quote_list.html"



class RandomView(ListView):
    context_object_name = 'random_quote'
    model = Quote
    template_name = "quotes/random_list.html"

    def get_queryset(self):
        return Quote.objects.order_by('?').first()

class QuoteCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = ''
    model = Quote
    form_class = QuoteForm

    def form_valid(self,form):
        return super().form_valid(form)

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm

    def form_valid(self,form):
        return super().form_valid(form)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('quotes:random'))



def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('quotes:user'))

            else:
                return HttpResponse("Account not active")
        else:
            print('Someone tried to login and failed')
            print('Username: {} and Password: {}'.format(username,password))
            return HttpResponse("Invalid credentials")
    else:

        return render(request, 'quotes/login_form.html',{})











def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.username = user.email
            user.save()
            registered = True

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()


    return render(request, 'quotes/user_form.html',
                                {'user_form':user_form,
                                'registered': registered})
