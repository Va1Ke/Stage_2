# Hotel Rent Room
It is web-application which allows users to record information about clients, rooms in hotel and the rental
orders.

## 1. Orders
### 1.1 Display list of orders
The mode is designed to view the list of orders, if it possible to display the number of orders for a specified
period of time.<br>

Main scenario: 
* User selects item “Orders”;
* Application displays list of Orders.

![Orders](images/orders_list.png)

The list displays the following columns:
* id - unique order id
* client_id - unique client id
* room_id - unique room id
* name - client name
* phone_nuber - client phone number
* rented - when rented
* on_days - how much time rented

### 1.2 Add order
Main scenario:
* User clicks the “Add” button in the orders list view mode
* Application displays form to enter order data
* User enters order data and presses “Save” button
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then record is adding to database
* If error occurs, then error message is displaying
* If new order record is successfully added, then list of orders with added records is displaying

Cancel operation scenario:
* User clicks the “Add” button in the order list view mode
* Application displays form to enter order data
* User enters order data and presses “Cancel” button;
* Data don’t save in data base, then list of orders records is displaying to user.
* If the user selects the menu item "Orders”, ”Clients” or "Hotel", the data will not be saved to the database and the corresponding form with updated data will be opened.

![Orders](images/order_add.png)

### 1.3 Edit order
Main scenario:
* User clicks the “Edit” button in the orders list view mode
* Application displays form to enter order data
* User enters order data and presses “Save” button
* If any data is entered incorrectly, incorrect data messages are displayed
* If entered data is valid, then edited data is added to database
* If error occurs, then error message is displaying
* If order record is successfully edited, then list of orders with added records is displaying

Cancel operation scenario:
* User clicks the “Edit” button in the orders list view mode;
* Application displays form to enter order data;
* User enters order data and presses “Cancel” button
* Data don’t save in database, then list of orders records is displaying to user.
* If the user selects the menu item "Orders”, ”Clients” or "Hotel", the data will not be saved to the database and the corresponding form with updated data will be opened

![Orders](images/order_edit.png)

### 1.4 Delete order
Main scenario:
* User clicks the “delete” button in the orders list view mode
* Application displays form to enter order id
* User enters order id and presses “delete” button
* If any data is entered incorrectly, incorrect data messages are displayed
* If error occurs, then error message is displaying

![Orders](images/order_delete.png)

## 2.Clients
### 2.1 Display list of Clients
This mode is intended for viewing and editing the clients list.<br>
Main scenario:
* User selects item “Clients”
* Application displays list of clients

![Clients](images/client_list.png)

The list displays the following columns:
* id - unique client id
* name - client name
* phone_number - client phone number

### 2.2 Add a Client
Main scenario:
* User clicks the “Add” button in the clients list view mode
* Application displays form to enter order data
* User enters order data and presses “add” button
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then record is adding to database
* If error occurs, then error message is displaying
* If new order record is successfully added, then list of orders with added records is displaying

Cancel operation scenario:
* User clicks the “Add” button in the order list view mode
* Application displays form to enter order data
* User enters order data and presses “Cancel” button;
* Data don’t save in database, then list of orders records is displaying to user.
* If the user selects the menu item "Orders”, ”Clients” or "Hotel", the data will not

![Clients](images/client_add.png)

### 2.3 Edit Client
Main scenario:
* User clicks the “Edit” button in the client list view mode
* Application displays form to enter order data
* User enters order data and presses “Save” button
* If any data is entered incorrectly, incorrect data messages are displayed
* If entered data is valid, then edited data is added to database
* If error occurs, then error message is displaying
* If order record is successfully edited, then list of orders with added records is displaying

Cancel operation scenario:
* User clicks the “Edit” button in the orders list view mode;
* Application displays form to enter order data;
* User enters order data and presses “Cancel” button
* Data don’t save in database, then list of orders records is displaying to user.
* If the user selects the menu item "Orders”, ”Clients” or "Hotel", the data will not be saved to the database and the corresponding form with updated data will be opened

![Clients](images/client_edit.png)

### 2.4 Client delete
Main scenario:
* User clicks the “delete” button in the client list view mode
* Application displays form to enter order id
* User enters order id and presses “delete” button
* If any data is entered incorrectly, incorrect data messages are displayed
* If error occurs, then error message is displaying

![Orders](images/client_delete.png)

## 3. Hotel
### 3.1 Display list of room
This mode is intended for viewing and editing the clients list.<br>
Main scenario:
* User selects item “Hotel”
* Application displays list of clients

![Orders](images/room_list.png)

The list displays the following columns:
* id - unique room id
* area - area of a room
* number_of_beds - number of beds in a room
* price_for_a_night - price for one night
* busy - indicate renting


### 3.2 Add a room
Main scenario:
* User clicks the “Add” button in the room list view mode
* Application displays form to enter order data
* User enters order data and presses “add” button
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then record is adding to database
* If error occurs, then error message is displaying
* If new order record is successfully added, then list of orders with added records is displaying

Cancel operation scenario:
* User clicks the “Add” button in the order list view mode
* Application displays form to enter order data
* User enters order data and presses “Cancel” button;
* Data don’t save in database, then list of orders records is displaying to user.
* If the user selects the menu item "Orders”, ”Clients” or "Hotel", the data will not

![Clients](images/room_add.png)

### 3.3 Edit Room
Main scenario:
* User clicks the “Edit” button in the room list view mode
* Application displays form to enter order data
* User enters order data and presses “Save” button
* If any data is entered incorrectly, incorrect data messages are displayed
* If entered data is valid, then edited data is added to database
* If error occurs, then error message is displaying
* If order record is successfully edited, then list of orders with added records is displaying

Cancel operation scenario:
* User clicks the “Edit” button in the orders list view mode;
* Application displays form to enter order data;
* User enters order data and presses “Cancel” button
* Data don’t save in database, then list of orders records is displaying to user.
* If the user selects the menu item "Orders”, ”Clients” or "Hotel", the data will not be saved to the database and the corresponding form with updated data will be opened

![Orders](images/room_edit.png)

### 3.4 Room delete
Main scenario:
* User clicks the “delete” button in the room list view mode
* Application displays form to enter order id
* User enters order id and presses “delete” button
* If any data is entered incorrectly, incorrect data messages are displayed
* If error occurs, then error message is displaying

![Orders](images/room_delete.png)