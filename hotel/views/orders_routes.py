from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from main import app, db


@app.route('/')
def main():
    """Main page"""
    return render_template("main.html")


@app.route('/order_list/')
def orders():
    """Orders page"""
    return render_template("/Orders/orders.html")


@app.route('/order_list/add/')
def add_order():
    """Page for adding orders"""
    return render_template("/Orders/add_order.html")


@app.route('/order_list/edit/')
def edit_order():
    """Page for editing orders"""
    return render_template("/Orders/edit_order.html")


@app.route('/order_list/delete/')
def delete_order():
    """Page for deleting orders"""
    return render_template("/Orders/delete_order.html")