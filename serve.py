from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def serve():
    if request.method == 'POST':
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return str('running stress')

    elif request.method == 'GET':
        return str(socket.gethostbyname(hostname))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
