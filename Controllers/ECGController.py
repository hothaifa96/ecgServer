import json

from flask import Flask, request
from Service.ECGService import *

app = Flask(__name__)


@app.route('/<int:id>', methods=['POST'])
def wav_receiver(id):
    wav = request.files['wav']
    print(wav)
    print(id)
    if save_wav(id, wav):
        return {"ok": True}
    else:
        return {'Error': False}


app.run(host='0.0.0.0', port=3002)
