from flask import Flask, render_template, request, Response
from services import mrz, qr


app = Flask(__name__)


@app.route('/mrz', methods=['GET'])
def hello():
    return render_template('mrz.html')


@app.route('/qr', methods=['GET'])
def qrcode():
    return render_template('qr.html')


@app.route('/get_mrz', methods=['POST'])
def get_mrz():
    try:
        data = request.json
        print(data)
        return Response(response=mrz.generate_mrz_de_id(data),
                        status=200)
    except Exception as e:
        return Response(response=str(e), status=500)


@app.route('/get_qr', methods=['POST'])
def get_qr():
    try:
        data = request.json
        qr_data = qr.generate_qr(data)
        return qr_data
    except Exception as e:
        return Response(response=str(e), status=500)


if __name__ == '__main__':
    app.run()
