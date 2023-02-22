from flask import Blueprint, render_template, abort, request, redirect
from jinja2 import TemplateNotFound
from hotel.models.models import db
from hotel.service.clients_crud import Clients_crud
from hotel.service.schemas.clients_schemas import EditClientInfo, AddClient

clients_rout = Blueprint('clients_rout', __name__)

@clients_rout.route('/client_list/')
def clients():
    """Clients page"""
    return render_template("/Clients/clients.html")



@clients_rout.route('/client_list/add/', methods=['GET','POST'])
def add_client():
    """Page for adding clients"""
    if request.method == 'GET':
        return render_template("/Clients/add_client.html")
    if request.method == "POST":
        name = request.form['name']
        phone_number = request.form['phone_number']
        new_client = AddClient(name=name, phone_number=phone_number)
        record = Clients_crud(db=db).add_client(client=new_client)
        if record == "Success":
            return redirect('/client_list/')
        else:
            return redirect('/bad_request/')


@clients_rout.route('/client_list/edit/', methods=['GET', 'POST'])
def edit_client():
    """Page for editing clients"""
    if request.method == 'GET':
        return render_template("/Clients/edit_client.html")
    if request.method == "POST":
        id = request.form['id']
        name = request.form['name']
        phone_number = request.form['phone_number']
        new_client_info = EditClientInfo(id=id, name=name, phone_number=phone_number)
        record = Clients_crud(db=db).edit_client(client=new_client_info)
        if record == "Success":
            return redirect('/client_list/')
        else:
            return redirect('/bad_request/')


@clients_rout.route('/client_list/delete/', methods=['GET','POST'])
def delete_client():
    """Page for deleting clients"""
    if request.method == 'GET':
        return render_template("/Clients/delete_client.html")
    if request.method == "POST":
        id = request.form['id']
        record = Clients_crud(db=db).delete_client(id=id)
        if record == "Success":
            return redirect('/client_list/')
        else:
            return redirect('/bad_request/')
