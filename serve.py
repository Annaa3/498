from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_seed():
    global curr_seed

    if request.method == 'POST':
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return str('running stress')

    elif request.method == 'GET':
        return str(socket.gethostname())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
