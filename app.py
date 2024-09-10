from flask import Flask, request

app = Flask(__name__)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    #codiog de autorizacion
    return f"Código de autorización recibido: {code}"

if __name__ == '__main__':
    app.run(port=5000)