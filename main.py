from os import path
from flask import Flask,request
from pydub import AudioSegment

app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def func():
    if request.method == 'GET':
        src = "sample3.mp3"
        dst = "test11.wav"

        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")
        return "successfully converted"

if __name__ == '__main__':
    app.debug = True
    app.run()


