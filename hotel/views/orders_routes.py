from flask import Blueprint, render_template, abort, request, redirect
from jinja2 import TemplateNotFound
from hotel.models.models import db
from hotel.service.orders_crud import Orders_crud
from hotel.service.schemas.orders_schemas import CreateOrder, EditOrder


orders_rout = Blueprint('orders_rout', __name__)

@orders_rout.route('/')
def main():
    """Main page"""
    return render_template("main.html")


@orders_rout.route('/order_list/')
def orders():
    """Orders page"""
    return render_template("/Orders/orders.html")


@orders_rout.route('/order_list/add/', methods=['GET', 'POST'])
def add_order():
    """Page for adding orders"""
    if request.method == 'GET':
        return render_template("/Orders/add_order.html")
    if request.method == "POST":
        client_id = request.form['client_id']
        room_id = request.form['room_id']
        rented = request.form['rented']
        on_days = request.form['on_days']

        new_order = CreateOrder(client_id=client_id, room_id=room_id, rented=rented, on_days=on_days)
        record = Orders_crud(db=db).create_order(new_order)
        if record == "Success":
            return redirect('/order_list/')
        else:
            return redirect('/bad_request/')


@orders_rout.route('/order_list/edit/', methods=['GET', 'POST'])
def edit_order():
    """Page for editing orders"""
    if request.method == 'GET':
        return render_template("/Orders/edit_order.html")
    if request.method == "POST":
        id = request.form['id']
        client_id = request.form['client_id']
        room_id = request.form['room_id']
        rented = request.form['rented']
        on_days = request.form['on_days']
        new_order_info = EditOrder(id=id, client_id=client_id, room_id=room_id,
                                    rented=rented, on_days=on_days)
        record = Orders_crud(db=db).edit_order(order=new_order_info)
        if record == "Success":
            return redirect('/client_list/')
        else:
            return redirect('/bad_request/')


@orders_rout.route('/order_list/delete/', methods=['GET', 'POST'])
def delete_order():
    """Page for deleting orders"""
    if request.method == 'GET':
        return render_template("/Orders/delete_order.html")
    if request.method == "POST":
        id = request.form['id']
        record = Orders_crud(db=db).delete_order(id=id)
        if record == "Success":
            return redirect('/client_list/')
        else:
            return redirect('/bad_request/')

