# QUE ES UNA API REST 
# Una API de REST, o API de RESTful, es una interfaz de programación de aplicaciones (API o API web) que se ajusta a los límites de la arquitectura REST y permite la interacción con los servicios web de RESTful. 
# ----------------------------------------------------------------------------------------------------------------------

from flask import Flask, request # entonces para hacer la solictud json para que el cliente nos ayude a crear la tienda como el quiere crearla para eso vamos usar el metodo post que es el que nos ayuda a recibir datos en general entonces aqui lo que hace es que estamos inportantando request desde flask (basicamente la solicitud)

app = Flask(__name__)



# aqui estamos almacenando unos datos en una lista de python 
stores = [
  {
    "name": "juan_Store",
    "items": [
      {
        "name": "computer",
        "price": 10.99
      }
    ]
  } 
]  
# aqui vamos hacer una ruta flask que es la que ayudara a devolver los datos (El trabajo de la función es hacer todo lo que debe y al final devolver algo.)
@app.get("/store")
def get_stores():
    return {"stores": stores}

# cuando devolvemos un dicionario utlizando una ruta de flask se comvierte automaticamente en JSON y cuando se comvierte en JSON pasan dos cosas  
# 1. Cambie las palabras clave y los valores de Python para que coincidan con el estándar JSON (por ejemplo, Truea true).
# 2. Convierta todo en una sola cadena que nuestra API pueda devolver.


# lo que hacemos aca es que utilizamos el request.get_json() que es una funcion que nos ayudara a devolver los datos de la solicitud de json 
@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []} # aqui estamos haciendo un nuevo diccionario con una lista vacia para despues agregarlo a la solicita de la tienda ya creada entonces cuando se agregue al cliente le delvolvera como una notifcacion de que confirmacionn que fue exitosa o no 
    stores.append(new_store)
    return new_store, 201 # este codigo de estado significa creado utlizando otra manera que no sea la de flaks, hay otro estado que es el 200 que significa como ok que es el que flask devuelve por defecto 


@app.post("/store/<string:name>/item") # url lo que hace esto es que es una manera mas natural o directa de encontrar una tienda especefica y sus productos por medio de json ya que pues esta la otra de el cliente envia y nosotros buscamos hasta necontra la referencia y hacer el debido proceso 
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201 
    return {"message": "tienda no encontrada"}, 404 # el codigo 404 es un estado de negacion basicamente como no encontrado 

# este es un ejmplo de bsuqueda de una tienda utilizando el metodo get 
@app.get("/store/<string:name>")# url
def get_store(name): # definiendo la tienda a enconmtrar 
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "tienda no encontrada"}, 404

# este es un ejmplo de bsuqueda de una tienda utilizando el metodo get 
@app.get("/store/<string:name>/item") #url
def get_item_in_store(name): #definiendo la tienda a enconmtrar 
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "tienda no encontrada"}, 404


#------------------------------------------------------------------------------------------------------------------------
# QUE ES JSON?
# JSON es solo una cadena (generalmente larga) cuyo contenido sigue un formato específico.

# Ejemplo
[{"llave": "valor","otra": 25,"datos_lista": [ 2, 4, 11]},{ "sub_objetos": {"nombre": "Rolf","edad": 25}}]

        # El formato especifico de json para formar una cadena es:

        # 1. Instrumentos de cuerda
        # 2. Números
        # 3. Booleanos ( trueo false)
        # 4. Liza
        # 5. Objetos (similares a los diccionarios en Python)

if __name__ == '__main__':
    app.run(debug=True, port=8080)