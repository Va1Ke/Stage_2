from flask import Blueprint, render_template, request, redirect, url_for
from jinja2 import TemplateNotFound
import requests
import json

hotel_rout = Blueprint('hotel_rout', __name__)

@hotel_rout.route('/room_list/', methods=['GET','POST'])
def hotel():
    """Hotel page"""
    if request.method == 'GET':
        rooms = requests.get("http://127.0.0.1:5000/rooms/")
        return render_template("Hotel/hotel.html", rooms=rooms.json())
    if request.method == "POST":
        busy = int(request.form['busy'])
        free_rooms = requests.post(f"http://127.0.0.1:5000/rooms/{busy}/")
        return render_template("Hotel/hotel.html", rooms=free_rooms.json())


@hotel_rout.route('/room_list/add/', methods=['GET','POST'])
async def add_room_html():
    """Page for adding rooms"""
    if request.method == 'GET':
        return render_template("/Hotel/add_room.html")
    if request.method == "POST":
        area = request.form['area']
        number_of_beds = request.form['number_of_beds']
        price_for_a_night = request.form['price_for_a_night']
        room_attrs = {
            "area": area,
            "number_of_beds": number_of_beds,
            "price_for_a_night": price_for_a_night
        }
        response = requests.post("http://127.0.0.1:5000/rooms/", json=room_attrs)
        if response.status_code == 200:
            return redirect('/room_list/')
        else:
            return redirect('/bad_request/')


@hotel_rout.route('/room_list/edit/', methods=['GET','POST'])
async def edit_room():
    """Page for editing rooms"""
    if request.method == 'GET':
        return render_template("/Hotel/edit_room.html")
    if request.method == "POST":
        room_id = request.form['id']
        area = request.form['area']
        number_of_beds = request.form['number_of_beds']
        price_for_a_night = request.form['price_for_a_night']
        busy = int(request.form['busy'])
        if busy == 1:
            busy = True
        elif busy == 0:
            busy = False
        else:
            print(busy)
            return redirect('/bad_request/busy/')

        room_attrs = {
            "area": area,
            "number_of_beds": number_of_beds,
            "price_for_a_night": price_for_a_night,
            "busy": busy
        }
        response = requests.put(f"http://127.0.0.1:5000/rooms/change/{room_id}", json=room_attrs)
        if response.status_code == 200:
            return redirect('/room_list/')
        else:
            return redirect('/bad_request/')

@hotel_rout.route('/room_list/delete/', methods=['GET','POST'])
async def delete_room():
    """Page for deleting rooms"""
    if request.method == 'GET':
        return render_template("/Hotel/delete_room.html")
    if request.method == "POST":
        room_id = request.form['id']
        response = requests.delete(f"http://127.0.0.1:5000/rooms/change/{room_id}/")
        if response.status_code == 200:
            return redirect('/room_list/')
        else:
            return redirect('/bad_request/')

@hotel_rout.route('/room_list/delete/error/')
async def delete_error():
    """Page for deleting rooms"""
    return render_template("/Hotel/delete_error.html")


@hotel_rout.route('/bad_request/')
def error():
    """Page for bad request message"""
    return render_template("bad_request.html")