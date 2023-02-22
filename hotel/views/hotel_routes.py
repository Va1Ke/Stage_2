from flask import Blueprint, render_template, request, redirect, url_for
from jinja2 import TemplateNotFound
from hotel.models.models import db
from hotel.service.hotel_crud import Hotel_crud
from hotel.service.schemas.hotel_schemas import AddRoom, EditRoomInfo

hotel_rout = Blueprint('hotel_rout', __name__)

@hotel_rout.route('/room_list/')
def hotel():
    """Hotel page"""
    return render_template("Hotel/hotel.html")


@hotel_rout.route('/room_list/add/', methods = ['GET','POST'])
async def add_room_html():
    """Page for adding rooms"""
    if request.method == 'GET':
        return render_template("/Hotel/add_room.html")
    if request.method == "POST":
        area = request.form['area']
        number_of_beds = request.form['number_of_beds']
        price_for_a_night = request.form['price_for_a_night']
        room = AddRoom(area=area, number_of_beds=number_of_beds, price_for_a_night=price_for_a_night)
        record = Hotel_crud(db=db).add_room(room=room)
        if record == "Success":
            return redirect('/room_list/')
        else:
            return redirect('/bad_request/')


@hotel_rout.route('/room_list/edit/', methods = ['GET','POST'])
async def edit_room():
    """Page for editing rooms"""
    if request.method == 'GET':
        return render_template("/Hotel/edit_room.html")
    if request.method == "POST":

        id = request.form['id']
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
        new_room = EditRoomInfo(id=id, area=area, number_of_beds=number_of_beds,
                                price_for_a_night=price_for_a_night, busy=busy)
        record = Hotel_crud(db=db).edit_room(room=new_room)
        if record == "Success":
            return redirect('/room_list/')
        else:
            return redirect('/bad_request/')

@hotel_rout.route('/room_list/delete/', methods = ['GET','POST'])
async def delete_room():
    """Page for deleting rooms"""
    if request.method == 'GET':
        return render_template("/Hotel/delete_room.html")
    if request.method == "POST":
        id = request.form['id']
        record = Hotel_crud(db=db).delete_room(id=id)
        if record == "Success":
            return redirect('/room_list/')
        else:
            return redirect('/bad_request/')

@hotel_rout.route('/bad_request/')
def error():
    """Page for bad request message"""
    return render_template("bad_request.html")