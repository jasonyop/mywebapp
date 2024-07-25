from flask import Flask, render_template
import psutil
import platform

app = Flask(__name__)

@app.route('/')
def main():

    os_information = platform.platform()
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    return render_template('index.html', os_information=os_information, cpu=cpu, memory=memory)

app.run(host='0.0.0.0', port=5000)
