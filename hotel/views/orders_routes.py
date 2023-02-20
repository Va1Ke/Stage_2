from aioflask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


orders_rout = Blueprint('orders_rout', __name__)

@orders_rout.route('/')
async def main():
    """Main page"""
    return await render_template("main.html")


@orders_rout.route('/order_list/')
async def orders():
    """Orders page"""
    return await render_template("/Orders/orders.html")


@orders_rout.route('/order_list/add/')
async def add_order():
    """Page for adding orders"""
    return await render_template("/Orders/add_order.html")


@orders_rout.route('/order_list/edit/')
async def edit_order():
    """Page for editing orders"""
    return await render_template("/Orders/edit_order.html")


@orders_rout.route('/order_list/delete/')
async def delete_order():
    """Page for deleting orders"""
    return await render_template("/Orders/delete_order.html")