from django.views.generic import FormView

from .forms import ExampleForm


class ExampleFormView(FormView):
    form_class = ExampleForm
    template_name = 'form_example.html'
