# Hotel Rent Room
It is web-application which allows clients to rent room in hotel.

## Entity:
This application include two entity with relationships as one to many. (Clients and Rooms)<br>
Each room has different number of place to live there. That's mean that in a room can live different numbers of clients.

## How to start a project

* First you have to configure config file and create .env file for docker-compose db and local db in repository folder.
  * If you want to run project local with your local db you should uncomment SQLALCHEMY_DATABASE_URL for local and comment other two urls.<br>
  <br>
    Than you should run:<br>
    flask --app hotel run -h 0.0.0.0 -p 5000<br>
    flask db upgrade --directory hotel/migrations
  <br>
  <br>
* If you want to run a project first time using docker-compose you should uncomment SQLALCHEMY_DATABASE_URL for docker and comment other two urls.<br>
<br> 
  Than you should run:<br>
  docker-compose up --build <br>
  <br>
  And when docker-compose started to make migrations use:<br>
  docker exec <your_container_app_name> flask --app hotel db upgrade

## API URLs
### Clients
* 127.0.0.1:5000/clients/ - get all client and add new client 
* 127.0.0.1:5000/clients/change/38/ - edit client info and delete client
* 127.0.0.1:5000/clients/<phone_number>/ - find client by phone_number 
### Hotel
* 127.0.0.1:5000/rooms/ - get all rooms and add new room 
* 127.0.0.1:5000/rooms/<search_by_free_amount>/ - find a room with free numbers of place
* 127.0.0.1:5000/rooms/change/<room_id>/ - edit room info and delete room

