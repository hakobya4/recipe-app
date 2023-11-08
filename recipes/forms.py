from django import forms

CHART__CHOICES = (  # specify choices as a tuple
    ('#1', 'Bar chart'),    # when user selects "Bar chart", it is stored as "#1"
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)
DIFF__CHOICES = (
    ('#1', 'easy'),
    ('#2', 'medium'),
    ('#3', 'intermediate'),
    ('#4', 'hard')
)
# define class-based Form imported from Django forms


class RecipesSearchForm(forms.Form):
    difficulty_type = forms.ChoiceField(choices=DIFF__CHOICES)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)
