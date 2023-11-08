from django.test import TestCase

from .models import Recipes
from .forms import RecipesSearchForm


class RecipeModelTest(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Recipes.objects.create(name='Pizza', difficulty='Hard',
                               adapted='BBC', adapted_link='BBC.com', description='Mom\'s pizza pie',
                               prepTime=20, cookTime=30, totalTime=50, serving=3,
                               ingredients='dough, cheese, sauce, pepperoni')

    def test_recipes_name(self):
        # Get a users object to test
        users = Recipes.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its data
        field_label = users._meta.get_field('name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_recepies_name_max_length(self):
        # Get a users object to test
        users = Recipes.objects.get(id=1)

        # Get the metadata for the 'author_name' field and use it to query its max_length
        max_length = users._meta.get_field('name').max_length

        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 120)

    def test_get_absolute_url(self):
        recipe = Recipes.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')

    def test_form_renders_chart_type_input(self):
        form = RecipesSearchForm(data={'difficulty': ''})
        self.assertIn('chart_type', form.as_p())

    def test_form_invalid_data(self):
        form = RecipesSearchForm(data={'difficulty': 'easy', 'chart_type': ''})
        self.assertFalse(form.is_valid())
