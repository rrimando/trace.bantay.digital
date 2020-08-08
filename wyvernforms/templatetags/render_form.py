from django import template

register = template.Library()


@register.filter(name="render_form")
def render_form(form: str):

    return "Test"
