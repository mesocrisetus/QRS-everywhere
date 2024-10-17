from flask import Flask,redirect,render_template,request,url_for
import qrcode
import os
import re



app = Flask(__name__)

@app.route('/')
def index():
    #elimnar archivos constantemente
    for filename in os.listdir("./static/img/"):
        file_path = os.path.join("./static/img/", filename)
        try:
            
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
                print(f"Archivo eliminado: {file_path}")
        
        except Exception as e:
            print(f"No se pudo eliminar {file_path}. Error: {e}")

    return render_template('index.html')

@app.route('/generarqr', methods=['POST'])
def generarqr():
    url = request.form['url']
    img = qrcode.make(url)

    image_name = re.sub(r'[\\/*?:"<>|]', "", url)
    if len(image_name) > 50:
        image_name = image_name[:50]
    type(img)
    
        
    image_name = 'picture.png'
    #img.save(f"./static/img/{image_name}.png")
    #path = f"./static/img/{image_name}.png"
    path = os.path.join("./static/img/", image_name + ".png")
    img.save(path)


    print(path)
    return render_template('index.html', path=path)

if __name__ == '__main__':
    app.run() 