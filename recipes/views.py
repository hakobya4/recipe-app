from django.shortcuts import render
# to display lists and details
from django.views.generic import ListView, DetailView
from .models import Recipes
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
from .forms import RecipesSearchForm
from .models import Recipes
from .utils import get_chart
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'recipes/recipes_home.html')


def about(request):
    return render(request, 'recipes/about.html')


@login_required
def search(request):
    form = RecipesSearchForm(request.POST or None)
    recipes_df = None
    chart = None
    if request.method == 'POST':
        # read book_title and chart_type
        difficulty_type = request.POST.get('difficulty_type')
        chart_type = request.POST.get('chart_type')
        # display in terminal - needed for debugging during development only
        print(difficulty_type, chart_type)
        if difficulty_type == '#1':
            difficulty_type = 'easy'
        elif difficulty_type == '#2':
            difficulty_type = 'medium'
        elif difficulty_type == '#3':
            difficulty_type = 'intermediate'
        else:
            difficulty_type = 'hard'

        qs = Recipes.objects.filter(difficulty=difficulty_type)
        # convert the queryset values to pandas dataframe
        if qs:
            recipes_df = pd.DataFrame(
                qs.values('id', 'name', 'description', 'totalTime', 'direction', 'ingredients'))
            nav = []
            # adds link to the column name of each row of a pandas table
            for i, name in enumerate(recipes_df['name']):
                name = '<a href="/list/' + \
                    str(recipes_df['id'][i]) + '">' + str(name) + '</a>'
                nav.append(name)

            chart = get_chart(chart_type, recipes_df,
                              labels=recipes_df['name'].values)

            recipes_df['name'] = nav

            # convert the dataframe to HTML
            recipes_df = recipes_df.to_html(index=False, escape=False)

    # pack up data to be sent to template in the context dictionary
    context = {
        'form': form,
        'recipes_df': recipes_df,
        'chart': chart
    }

    # do nothing, simply display page
    return render(request, 'recipes/search.html', context)


class RecipesListView(LoginRequiredMixin, ListView):  # class-based view
    model = Recipes  # specify model
    template_name = 'recipes/main.html'


class RecipesDetailView(LoginRequiredMixin, DetailView):
    model = Recipes
    template_name = 'recipes/detail.html'
