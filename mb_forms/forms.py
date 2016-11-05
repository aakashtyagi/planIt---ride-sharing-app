from django import forms, template
from django.utils.encoding import python_2_unicode_compatible

from mb_forms.templatetags.formtags import FormNode
from django.forms import models
from mb_forms.fields import Field
from mb_forms.widgets import Select, SelectMultiple, MultipleHiddenInput

__all__ = ('BaseForm', 'Form',)


@python_2_unicode_compatible
class LayoutRenderer(object):
    _template_node = FormNode(
        'form',
        [template.Variable('form')],
        {
            'using': template.Variable('layout'),
            'only': False,
            'with': None,
        })

    def _render_as(self, layout):
        context = template.Context({
            'form': self,
            'layout': layout,
        })
        return self._template_node.render(context)

    def __str__(self):
        return self._render_as('forms/layouts/default.html')

    def as_p(self):
        return self._render_as('forms/layouts/p.html')

    def as_ul(self):
        return self._render_as('forms/layouts/ul.html')

    def as_table(self):
        return self._render_as('forms/layouts/table.html')


class BaseForm(LayoutRenderer, forms.BaseForm):
    pass


class Form(LayoutRenderer, forms.Form):
    pass

__all__ = ('ModelForm', 'ModelChoiceField', 'ModelMultipleChoiceField')


class ModelForm(LayoutRenderer, models.ModelForm):
    def __new__(cls, *args, **kwargs):
        return super(ModelForm, cls).__new__(cls, *args, **kwargs)

class ModelChoiceField(Field, models.ModelChoiceField):
    widget = Select


class ModelMultipleChoiceField(Field, models.ModelMultipleChoiceField):
    widget = SelectMultiple
    hidden_widget = MultipleHiddenInput
