================
CF Pretty Form Errors
================

Quick start
-----------

1. Add "cf_pretty_form_errors" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'crispy_forms',
        'cf_pretty_form_errors',
        ...
    ]

2. If crispy forms not configured, add template pack to your settings.py::

    CRISPY_TEMPLATE_PACK = 'bootstrap3'

3. Add mixin to your form. PrettyFormPlaceholdersMixin for easy setup, PrettyFormMixin for detailed layout configuration::

4. Include {{ form.media.css }} and {{ form.media.js }} in your template, for example::

        {{ form.media.css }}
        {% crispy form %}
        {{ form.media.js }}
