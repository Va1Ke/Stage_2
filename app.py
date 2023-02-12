from flask import Flask,  render_template, url_for

app = Flask(__name__)


@app.route('/')
def Main():
    return render_template("main.html")
@app.route('/order_list/')
def Orders():
    return render_template("orders.html")
@app.route('/client_list/')
def Clients():
    return render_template("clients.html")
@app.route('/room_list/')
def Hotel():
    return render_template("hotel.html")


if __name__ == '__main__':
    app.run()
