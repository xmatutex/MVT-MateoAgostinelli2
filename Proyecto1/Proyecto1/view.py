from mailbox import NoSuchMailboxError
from pipes import Template
from django.http import HttpResponse
from django.template import Context, Template


def html(request):
    mihtml=open("C:/Users/mateo/OneDrive/Desktop/ProyectoDjango/Proyecto1/Templates/template.html")
    plantilla=Template(mihtml.read())
    mihtml.close
    contexto=Context()
    documento=plantilla.render(contexto)
    return HttpResponse(documento)