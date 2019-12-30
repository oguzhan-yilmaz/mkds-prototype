from .models import Recipe, Ingredient
from django import forms

class RecipeForm(forms.Form):
    selected_recipes = forms.ModelMultipleChoiceField(queryset=Recipe.objects.all(),  widget=forms.CheckboxSelectMultiple())