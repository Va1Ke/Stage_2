from flask import Blueprint, render_template, request, redirect, url_for
from jinja2 import TemplateNotFound
from hotel.models.models import Hotel
from hotel.service.hotel_crud import Hotel_crud

hotel_rout = Blueprint('hotel_rout', __name__)

@hotel_rout.route('/room_list/')
def hotel():
    """Hotel page"""
    return render_template("Hotel/hotel.html")


@hotel_rout.route('/room_list/add/', methods = ['GET','POST'])
def add_room_html():
    """Page for adding rooms"""
    if request.method == 'GET':
        return  render_template("/Hotel/add_room.html")
    if request.method == "POST":
        area = request.form['area']
        number_of_beds = request.form['number_of_beds']
        price_for_a_night = request.form['price_for_a_night']
        room = Hotel(area=area, number_of_beds=number_of_beds, price_for_a_night=price_for_a_night)
        record = Hotel_crud.add_room(room)
        return redirect('/data')


@hotel_rout.route('/room_list/edit/')
def edit_room():
    """Page for editing rooms"""
    return render_template("/Hotel/edit_room.html")


@hotel_rout.route('/room_list/delete/')
def delete_room():
    """Page for deleting rooms"""
    return render_template("/Hotel/delete_room.html")