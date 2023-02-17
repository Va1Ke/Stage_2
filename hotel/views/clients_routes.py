from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from main import app, db



@app.route('/client_list/')
def clients():
    """Clients page"""
    return render_template("/Clients/clients.html")


@app.route('/client_list/add/')
def add_client():
    """Page for adding clients"""
    return render_template("/Clients/add_client.html")


@app.route('/client_list/edit/')
def edit_client():
    """Page for editing clients"""
    return render_template("/Clients/edit_client.html")


@app.route('/client_list/delete/')
def delete_client():
    """Page for deleting clients"""
    return render_template("/Clients/delete_client.html")