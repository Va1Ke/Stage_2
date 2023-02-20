from aioflask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


clients_rout = Blueprint('clients_rout', __name__)

@clients_rout.route('/client_list/')
async def clients():
    """Clients page"""
    return await render_template("/Clients/clients.html")


@clients_rout.route('/client_list/add/')
async def add_client():
    """Page for adding clients"""
    return await render_template("/Clients/add_client.html")


@clients_rout.route('/client_list/edit/')
async def edit_client():
    """Page for editing clients"""
    return await render_template("/Clients/edit_client.html")


@clients_rout.route('/client_list/delete/')
async def delete_client():
    """Page for deleting clients"""
    return await render_template("/Clients/delete_client.html")