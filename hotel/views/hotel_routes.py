from flask import Blueprint, render_template, request, redirect, url_for
from hotel.service.hotel_crud import Hotel_crud
from hotel.service.schemas import hotel_schemas
from main import app, db


@app.route('/room_list/')
def hotel():
    """Hotel page"""
    return render_template("/Hotel/hotel.html")


@app.route('/room_list/add/', methods = ['GET','POST'])
async def add_room_html():
    """Page for adding rooms"""
    if request.method == 'GET':
        return render_template("/Hotel/add_room.html")
    if request.method == 'POST':
        area = request.form['area']
        number_of_beds = request.form['number_of_beds']
        price_for_a_night = request.form['price_for_a_night']
        #record = await Hotel_crud(db=db).add_room(hotel_schemas(area=area,number_of_beds=number_of_beds,price_for_a_night=price_for_a_night))
        #if record == hotel_schemas.RoomInfoReturn:
        #    return HTTPException(status_code=200, detail=" Success")
        #else:
        #    rise HTTPException(status_code=400, detail="Error")
        return redirect(url_for('add_room_html'))

@app.route('/room_list/edit/')
def edit_room():
    """Page for editing rooms"""
    return render_template("/Hotel/edit_room.html")


@app.route('/room_list/delete/')
def delete_room():
    """Page for deleting rooms"""
    return render_template("/Hotel/delete_room.html")