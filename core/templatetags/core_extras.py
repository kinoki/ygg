from django import template
from django.forms import CheckboxInput, FileInput, ClearableFileInput

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    disallow = [FileInput().__class__.__name__, CheckboxInput().__class__.__name__,
                ClearableFileInput().__class__.__name__]
    if field.field.widget.__class__.__name__ in disallow:
        css = css.replace("form-control", "")
        return field.as_widget(attrs={"class": css})
    return field.as_widget(attrs={"class": css})
