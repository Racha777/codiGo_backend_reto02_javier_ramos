from flask import Flask, redirect,render_template,request,session, url_for

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

@portafolio.route('/contacto',methods=['GET','POST'])
def contacto():
    contacto_form=ContactoForm()
    listaMensajes=fb.getCollection('mensajes')
    context={
        'mensajes':listaMensajes,
        'contacto_form':contacto_form
    }
    if contacto_form.validate_on_submit():
        dataNuevoMensaje={
            'nombre':contacto_form.nombre.data,
            'email':contacto_form.email.data,
            'mensaje':contacto_form.mensaje.data,
        }
        nuevoMensaje=fb.insertDocument('mensajes',dataNuevoMensaje)
        return redirect(url_for('portafolio.contacto'))
    return render_template('portafolio/contacto.html',**context)