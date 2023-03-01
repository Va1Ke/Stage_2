from flask import Blueprint, render_template, abort, request, redirect
import requests


clients_rout = Blueprint('clients_rout', __name__)

@clients_rout.route('/client_list/', methods=['GET','POST'])
def clients():
    """Clients page"""
    if request.method == 'GET':
        clients_list = requests.get("http://127.0.0.1:5000/clients/")
        return render_template("/Clients/clients.html", clients=clients_list.json())
    if request.method == "POST":
        phone_number = request.form['phone_number']
        clients_list = requests.post(f"http://127.0.0.1:5000/clients/{phone_number}/")
        return render_template("/Clients/clients.html", clients=[clients_list.json()])



@clients_rout.route('/client_list/add/', methods=['GET','POST'])
def add_client():
    """Page for adding clients"""
    if request.method == 'GET':
        return render_template("/Clients/add_client.html")
    if request.method == "POST":
        name = request.form['name']
        phone_number = request.form['phone_number']
        client_attrs = {
            "name": f"{name}",
            "phone_number": f"{phone_number}"
        }
        response = requests.post("http://127.0.0.1:5000/clients/", json=client_attrs)
        if response.status_code == 200:
            return redirect('/client_list/')
        return redirect('/bad_request/')


@clients_rout.route('/client_list/edit/', methods=['GET', 'POST'])
def edit_client():
    """Page for editing clients"""
    if request.method == 'GET':
        return render_template("/Clients/edit_client.html")
    if request.method == "POST":
        client_id = request.form['id']
        name = request.form['name']
        phone_number = request.form['phone_number']
        client_attrs = {
            "name": f"{name}",
            "phone_number": f"{phone_number}"
        }
        response = requests.put(f"http://127.0.0.1:5000/clients/change/{client_id}", json=client_attrs)
        if response.status_code == 200:
            return redirect('/client_list/')
        return redirect('/bad_request/')


@clients_rout.route('/client_list/delete/', methods=['GET', 'POST'])
def delete_client():
    """Page for deleting clients"""
    if request.method == 'GET':
        return render_template("/Clients/delete_client.html")
    if request.method == "POST":
        client_id = request.form['id']
        response = requests.delete(f"http://127.0.0.1:5000/clients/change/{client_id}")
        if response.status_code == 200:
            return redirect('/client_list/')
        return redirect('/bad_request/')

@clients_rout.route('/client_list/delete/error/')
def delete_error():
    """Page for deleting clients"""
    return render_template("/Clients/delete_error.html")
