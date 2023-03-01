from flask import Blueprint, render_template, request, redirect
import requests

orders_rout = Blueprint('orders_rout', __name__)

@orders_rout.route('/')
def main():
    """Main page"""
    return render_template("main.html")


@orders_rout.route('/order_list/', methods=['GET', 'POST'])
def orders():
    """Orders page"""
    if request.method == 'GET':
        response = requests.get("http://127.0.0.1:5000/orders/")
        return render_template("/Orders/orders.html", orders=response.json())
    if request.method == "POST":
        client_id = request.form['client_id']
        response = requests.post(f"http://127.0.0.1:5000/orders/{client_id}/")
        return render_template("/Orders/orders.html", orders=response.json())



@orders_rout.route('/order_list/add/', methods=['GET', 'POST'])
def add_order():
    """Page for adding orders"""
    if request.method == 'GET':
        return render_template("/Orders/add_order.html")
    if request.method == "POST":
        client_id = request.form['client_id']
        room_id = request.form['room_id']
        rented = request.form['rented']
        renting_ends = request.form['renting_ends']
        order_attrs = {
            "client_id": client_id,
            "room_id": room_id,
            "rented": rented,
            "renting_ends": renting_ends
        }
        check = requests.get("http://127.0.0.1:5000/orders/")
        for room in check.json():
            if int(room.get("client_id")) == int(client_id) and int(room.get("room_id")) == int(room_id):
                raise redirect('/bad_request/')
        response = requests.post("http://127.0.0.1:5000/orders/", json=order_attrs)
        if response.status_code == 200:
            return redirect('/order_list/')
        return redirect('/bad_request/')


@orders_rout.route('/order_list/edit/', methods=['GET', 'POST'])
def edit_order():
    """Page for editing orders"""
    if request.method == 'GET':
        return render_template("/Orders/edit_order.html")
    if request.method == "POST":
        order_id = request.form['id']
        client_id = request.form['client_id']
        room_id = request.form['room_id']
        rented = request.form['rented']
        renting_ends = request.form['renting_ends']
        order_attrs = {
            "client_id": client_id,
            "room_id": room_id,
            "rented": rented,
            "renting_ends": renting_ends
        }
        response = requests.put(f"http://127.0.0.1:5000/orders/change/{order_id}", json=order_attrs)
        if response.status_code == 200:
            return redirect('/order_list/')
        return redirect('/bad_request/')


@orders_rout.route('/order_list/delete/', methods=['GET', 'POST'])
def delete_order():
    """Page for deleting orders"""
    if request.method == 'GET':
        return render_template("/Orders/delete_order.html")
    if request.method == "POST":
        room_id = request.form['id']
        response = requests.delete(f"http://127.0.0.1:5000/orders/change/{room_id}/")
        if response.status_code == 200:
            return redirect('/order_list/')
        return redirect('/bad_request/')
