from aioflask import Blueprint, render_template, request, redirect, url_for
from hotel.service.schemas import hotel_schemas


hotel_rout = Blueprint('hotel_rout', __name__)

@hotel_rout.route('/room_list/')
async def hotel():
    """Hotel page"""
    return await render_template("Hotel/hotel.html")


@hotel_rout.route('/room_list/add/')
async def add_room_html():
    """Page for adding rooms"""
    if request.method == 'GET':
        return await render_template("/Hotel/add_room.html")

@hotel_rout.route('/room_list/edit/')
async def edit_room():
    """Page for editing rooms"""
    return await render_template("/Hotel/edit_room.html")


@hotel_rout.route('/room_list/delete/')
async def delete_room():
    """Page for deleting rooms"""
    return await render_template("/Hotel/delete_room.html")