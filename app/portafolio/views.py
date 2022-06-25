from flask import Flask,render_template,request,session

from . import portafolio

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
    return render_template('portafolio/contacto.html')