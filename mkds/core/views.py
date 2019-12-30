from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView
from .models import Recipe, Ingredient
from .forms import RecipeForm
from django.http import HttpResponseRedirect


class HomepageView(TemplateView):
    template_name = 'core/base.html'


class RecipeListView(ListView):
    model = Recipe


class MySignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


def signup(request):
    if request.method == 'POST':
        form = MySignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('subscribe')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})


def recipeList(request):
    submitted = False
    if request.method == 'POST':
        
        
        return render(request, 'core/recipes.html', {'submitted':True})
    else: ## this is the get
        #form = RecipeForm()
        form = Recipe.objects.all()


    return render(request, 'core/recipes.html', {'form': form, 'submitted':False})


class subscriptionPaymentView(TemplateView):
    template_name = 'core/subscription_payment.html'


class subscribeView(TemplateView):
    template_name = 'core/subscribe.html'


"""
create list of recipes to show w ingredients
make em select - deal with forms
create subscription plan page - make it into profiles
add flag to ingredient for allergens
add new recipe

------------
add subscr



"""
