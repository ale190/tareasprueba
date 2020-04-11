from django import template
from django.utils.safestring import mark_safe

from tareas.models import Tarea

import markdown2

register = template.Library()
#Archivo de registro donde guardarán las tags creadas.

#Forma corta de registrar un tag, mediante un decorador.


#register.simple_tag('last_course')
#Forma extensa de registrar un tag.
@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''Convierte markdown en html'''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
