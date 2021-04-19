## A cupcake-based exercise for practicing API

1. install the requirements.txt
2. start it up (flask run)
3. Away you go!

---

The landing page ('/') simply displays the flavors of all the current cupcakes, and has a form to add a cupcake.

The api has the following routes:

### GET
- '/api/cupcakes'   returns a json object of all the current cupcakes
- '/api/cupcakes/<id>' returns a json object of the cupcake with the id in the query string

### POST
- '/api/cupcakes' expects a json object with: flavor, size, rating, and image (optional), adds it to the database returns a json object of the database's version of the cupcake (including assigned id)

### PATCH
- '/api/cupcakes/<id>' updates fields supplied in the database on cupcake with id in the query string, returns json object of databases new version of the cupcake


- '/api/cupcakes/<id>' deletes cupcake with id in the query string from the database, returns a confirmation message in json object
