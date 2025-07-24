#Creamos una aplicacion con Flask 
#y usamos

# request: sirve para acceder a datos 
#formularios y archivos subidos tipo pdf, documentos, etc

# redirect, url_for: sirven para redirigir entre rutas o direcciones

# send_from_directory: para poder enviar o servir un
#archivo especifico sea documentos, imagenes o pdfs, esto evita que
#nadie pueda ingresar a rutas sin permisos

# session: guarda los datos del usuario en sesion.
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, session
import os

#Definimos un "app.secret_key" es necesario para usar "session"
#y colocaremos una clave que debe ser secreta y segura
app = Flask(__name__)
app.secret_key = 'RAZA_2000'


#Aqui modificaremos las credenciales del administrador para que pueda
#ingresar al panel de administrador
USERNAME = 'admin'
PASSWORD = '1234'

# Carpeta donde se guardan los pdfs
UPLOAD_FOLDER = os.path.join('uploads', 'pdfs')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#En este apartado se mostrar el inicio de sesion asiendo el uso
#de GET pra mostrar un formulario hecho en HTML 
#y un POST para verificar y validad el usuario y contraseña 
#del administrador
#si la respuesta es correcta guardara la sesion y se redirigira 
#al panel de administrador
#sino, mostrara un mensaje de credenciales incorrectas.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return 'Credenciales incorrectas'
    return '''
        <h2>Iniciar sesión</h2>
        <form method="post">
            Usuario: <input type="text" name="username"><br>
            Contraseña: <input type="password" name="password"><br>
            <input type="submit" value="Entrar">
        </form>
    '''


#Panel de administrador desde el cual podremos subir,
#eliminar y ver una lista de los pdfs subidos al servidor
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    mensaje = ''

    #Una vez subido un archivo
    #se encarga de verificar que el nombre del arhivo no este vacio
    #sea el caso enviara un mensaje avisando
    #Tambien verifica que sea un archivo pdf sino enviara 
    #un mensaje que solo se permite archivos pdfs
    #si todo se cumple se guarda en la carpeta "uploads/pdfs/"
    #y se envia un mensaje Archivo subido.
    if 'file' in request.files:
        file = request.files['file']
        if file.filename == '':
            mensaje = 'Nombre de archivo vacío'
        elif not file.filename.lower().endswith('.pdf'):
            mensaje = 'Solo se permiten archivos PDF'
        else:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            mensaje = f'Archivo subido: {file.filename}'

    #Tambien tenemos la opcion de eliminar un PDF, previamente guardado 
    #en "uploads/pdfs/" si el archivo existe se eliminara, sea el caso
    #que no enviara un mensaje de que el archivo no existe.
    elif 'delete' in request.form:
        filename = request.form.get('delete')
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            mensaje = f'Archivo eliminado: {filename}'
        else:
            mensaje = 'El archivo no existe'

    #En este apartado enlistara todos los PDFS,
    #previamente guardados en "uploads/pdfs/"
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    archivos = os.listdir(app.config['UPLOAD_FOLDER'])
    archivos = [f for f in archivos if f.lower().endswith('.pdf')]

    return render_template('admin.html', archivos=archivos, mensaje=mensaje)


#Aqui nos permite ver o descargar un PDF con una URL,
#ejemplo http://127.0.0.1:5001/uploads/pdfs/ejemplo.pdf
@app.route('/uploads/pdfs/<filename>')
def download_pdf(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

#Esto sirve para eliminar la sesion y redirigir nuevamente al login
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

#Aqui ejecutamos el servidor directamenta,
#como tambien aceptamos conexiones desde cualquier dispositivo.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)