from flask import Flask,  render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from .config import settings
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+settings.MYSQL_USER+':'+settings.MYSQL_PASSWORD+'@localhost:'+settings.MYSQL_PORT+'/'+settings.MYSQL_DATABASE
db = SQLAlchemy(app)

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/order_list/')
def orders():
    return render_template("/Orders/orders.html")

@app.route('/order_list/add/')
def add_order():
    return render_template("/Orders/add_order.html")

@app.route('/order_list/edit/')
def edit_order():
    return render_template("/Orders/edit_order.html")

@app.route('/order_list/delete/')
def delete_order():
    return render_template("/Orders/delete_order.html")

@app.route('/client_list/')
def clients():
    return render_template("/Clients/clients.html")

@app.route('/client_list/add/')
def add_client():
    return render_template("/Clients/add_client.html")

@app.route('/client_list/edit/')
def edit_client():
    return render_template("/Clients/edit_client.html")

@app.route('/client_list/delete/')
def delete_client():
    return render_template("/Clients/delete_client.html")

@app.route('/room_list/')
def hotel():
    return render_template("/Hotel/hotel.html")

@app.route('/room_list/add/')
def add_room():
    return render_template("/Hotel/add_room.html")

@app.route('/room_list/edit/')
def edit_room():
    return render_template("/Hotel/edit_room.html")

@app.route('/room_list/delete/')
def delete_room():
    return render_template("/Hotel/delete_room.html")

if __name__ == '__main__':
    app.run()
