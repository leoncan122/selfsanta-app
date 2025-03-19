=========================== Basic Details ==================================
Application Name: SelfSanta system
Developer: Leon Cangini
Status: Prototype stage

=========================== Description ====================================

This prototype is a user platform system divided into sub-applications: 
the user, funds, messaging, product links y purchases modules. It has a one-point access 
mechanism to these sub-applications to centralize all request and response 
transactions. 

The users module creates the users, store and provides the user lists where products from internet were selected, also used to apply the control access.

The messaging module allow notify the user in real time.

Funds module record any intervention with the payment system, and retrieve the totals each user has. Is a must to delivery the purchases.

The purchase store the information related to orders and interact with the funds module to manage the total reserves.

This application uses the FastAPI framework driven by Python 3.8. For persistance we want to make use of SQL and NoSQL databases.


Update: 14/03
We decided to ensure that the funds domain must have a 5/5 availability. 
We must implement a redis database to queue the transactions for the celery worker that send the payments, manage errors and retries.
Conversely this will also ensure the transactions are as fast as possible reducing the latency of the requests.

The requirements.txt will guide you with the dependencies. Just install by running:

# Steps

- Create venv environment
- source Scripts/activate
- pip install -r requirements.txt
- uvicorn app.main:app 

## Sprints

- 1 / 3 User managment
- 2 / 5 Funds management
- 3 / 8 Product Links managment
- 9 / 11 Purchase management
- 12 / 15 Messaging management

## Domains

/user-managment
  /users
    ├── user.controller.js
    ├── user.service.js
    ├── user.model.js
  /gifts
    ├── gifts.controller.js
    ├── gifts.service.js
    ├── gifts.model.js

/messaging-managment
  /notifications
    ├── notifications.controller.js
    ├── notifications.service.js
    ├── notifications.model.js

/funds-management
  /deposits
    ├── deposits.controller.js
    ├── deposits.service.js
    ├── deposits.model.js
  /spends
    ├── spends.controller.js
    ├── spends.service.js
    ├── spends.model.js
  

/links-management
  /product-links
    ├── link.controller.js
    ├── link.service.js
    ├── link.model.js
  /scheduler-management
    ├── scheduler.controller.js
    ├── scheduler.service.js
    ├── scheduler.model.js

/purchase-management 
  /product
    ├── product.controller.js
    ├── product.service.js
    ├── product.model.js
  /

 Ruta de la API Sugerida

  Usuarios (/users):

    POST /users: Crear un nuevo usuario.
    GET /users/{id}: Obtener detalles de un usuario.
    PATCH /users/{id}: Actualizar información de un usuario.
    DELETE /users/{id}: Eliminar un usuario.


  Regalos (/gifts):

    POST /gifts: Agregar un nuevo regalo.
    GET /gifts: Obtener todos los regalos.
    PATCH /gifts/{id}: Actualizar un regalo.
    DELETE /gifts/{id}: Eliminar un regalo.


  Fondos (/funds):

    POST /funds: Añadir fondos a la cuenta del usuario.
    GET /funds: Consultar saldo actual.
    PATCH /funds/{id}: Actualizar transacciones de fondos.


  Notificaciones (/notifications):

    POST /notifications: Crear una nueva notificación.
    GET /notifications: Listar todas las notificaciones.
    PATCH /notifications/{id}: Marcar una notificación como leída.


  Enlaces de productos (/product-links):

    POST /product-links: Añadir un enlace de producto.
    GET /product-links: Listar todos los enlaces.
    PATCH /product-links/{id}: Actualizar un enlace de producto.
    DELETE /product-links/{id}: Eliminar un enlace de producto.


  Programación de compras automáticas (/scheduler-management):

    POST /scheduler: Crear una nueva programación de compra.
    GET /scheduler: Consultar programación de compras.
    DELETE /scheduler/{id}: Eliminar una programación.


  Compras automáticas (/purchase-management):

    POST /products: Realizar la compra automática de un producto.
    GET /products: Consultar historial de compras realizadas.


