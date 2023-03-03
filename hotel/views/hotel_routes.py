from flask import Blueprint, render_template, request, redirect
import requests


hotel_rout = Blueprint('hotel_rout', __name__)

@hotel_rout.route('/room_list/', methods=['GET', 'POST'])
def hotel():
    """Hotel page"""
    if request.method == 'GET':
        rooms = requests.get("http://127.0.0.1:5000/rooms/", timeout=100)
        return render_template("Hotel/hotel.html", rooms=rooms.json())
    if request.method == "POST":
        search_by_free_amount = int(request.form['search'])
        free_rooms = requests.post(f"http://127.0.0.1:5000/rooms/{search_by_free_amount}/", timeout=100)
        return render_template("Hotel/hotel.html", rooms=free_rooms.json())


@hotel_rout.route('/room_list/add/', methods=['GET', 'POST'])
async def add_room_html():
    """Page for adding rooms"""
    if request.method == 'GET':
        return render_template("/Hotel/add_room.html")
    if request.method == "POST":
        area = int(request.form['area'])
        price_for_a_night = int(request.form['price_for_a_night'])
        max_amount_clients = int(request.form['max_amount_clients'])
        room_attrs = {
            "area": area,
            "price_for_a_night": price_for_a_night,
            "max_amount_clients": max_amount_clients
        }
        response = requests.post("http://127.0.0.1:5000/rooms/", json=room_attrs, timeout=100)
        if response.status_code == 200:
            return redirect('/room_list/')
        return redirect('/bad_request/')


@hotel_rout.route('/room_list/edit/', methods=['GET', 'POST'])
async def edit_room():
    """Page for editing rooms"""
    if request.method == 'GET':
        return render_template("/Hotel/edit_room.html")
    if request.method == "POST":
        room_id = request.form['id']
        area = request.form['area']
        price_for_a_night = request.form['price_for_a_night']
        max_amount_clients = request.form['max_amount_clients']
        room_attrs = {
            "area": area,
            "price_for_a_night": price_for_a_night,
            "max_amount_clients": max_amount_clients
        }
        response = requests.put(f"http://127.0.0.1:5000/rooms/change/{room_id}", json=room_attrs, timeout=100)
        if response.status_code == 200:
            return redirect('/room_list/')
        return redirect('/bad_request/')

@hotel_rout.route('/room_list/delete/', methods=['GET', 'POST'])
async def delete_room():
    """Page for deleting rooms"""
    if request.method == 'GET':
        return render_template("/Hotel/delete_room.html")
    if request.method == "POST":
        room_id = request.form['id']
        response = requests.delete(f"http://127.0.0.1:5000/rooms/change/{room_id}/", timeout=100)
        if response.status_code == 200:
            return redirect('/room_list/')
        return redirect('/bad_request/')

@hotel_rout.route('/bad_request/')
def error():
    """Page for bad request message"""
    return render_template("bad_request.html")
