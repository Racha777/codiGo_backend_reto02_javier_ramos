from flask import Flask,render_template,request,session

from . import portafolio
from .forms import ContactoForm

from app import fb

@portafolio.route('/')
def index():
    dictBiografia=fb.getCollection('biografia')[0]
    session['biografia']=dictBiografia
    return render_template('portafolio/index.html',**dictBiografia)

@portafolio.route('/proyectos')
def proyectos():
    listaProyectos=fb.getCollection('proyectos')

    context={
        'proyectos':listaProyectos
    }

    return render_template('portafolio/portafolio.html',**context)

@portafolio.route('/acercade')
def acercade():
    return render_template('portafolio/acercade.html')

@portafolio.route('/contacto')
def contacto():
    contacto_form=ContactoForm()
    context={
        'contacto_form':contacto_form
    }
    return render_template('portafolio/contacto.html',**context)