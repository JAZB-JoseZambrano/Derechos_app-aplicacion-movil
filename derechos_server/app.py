
#Flask sirve para crear aplicaciones web en python
#Tambien usamos "send_from_directory" para poder enviar o servir un
#archivo especifico sea documentos, imagenes o pdfs, esto evita que
#nadie pueda ingresar a rutas sin permisos
from flask import Flask, send_from_directory
#Cors nos permite que aplicaciones como flutter 
#pueda hacer peticiones a nuestro servidor 
from flask_cors import CORS
#OS nos ayuda a crear rutas o direcciones compatibles
#con cualquier sistema operativo
import os

#aqui habilitamos cors para que podamos ingresar a este servidor desde
#nuestra aplicacion o desde una web sin resticciones.
app = Flask(__name__)
CORS(app)

#Previamente creada la carpeta donde se guardaran los pdfs,
#definiremos la ruta "uploads/pdfs/" la cual se guardara
#como "UPLOAD_FOLDER" para poder reutilizarlo cuando se necesite
UPLOAD_FOLDER = os.path.join('uploads', 'pdfs')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Creamos una ruta HTTP publica usando GET para solicitar al servidor
#el pdf dentro de la carpeta "uploads/pdfs/", la cual quedaria 
#asi http://192.168.200.43:5000/uploads/pdfs/codigotrabajo.pdf
@app.route('/uploads/pdfs/<filename>', methods=['GET'])
def serve_pdf(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

#Aqui ejecutamos el servidor directamenta,
#como tambien aceptamos conexiones desde cualquier dispositivo.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
