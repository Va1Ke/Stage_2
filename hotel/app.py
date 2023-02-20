from aioflask import Flask
import asyncio
from hotel.views import clients_routes, orders_routes, hotel_routes
from hotel.db import db

app = Flask(__name__)
app.register_blueprint(clients_routes.clients_rout)
app.register_blueprint(orders_routes.orders_rout)
app.register_blueprint(hotel_routes.hotel_rout)


# @app.before_first_request
# async def startup():
#    await db.connect()
#
# @app.teardown_appcontext
# async def shutdown():
#    await db.disconnect()

if __name__ == '__main__':
    app.run()
