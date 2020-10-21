from flask import Flask, render_template, flash, url_for, redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index_daftar():
    return render_template('daftar.html')

@app.route('/jadwal')
def index_jadwal():
    return render_template('jadwal.html')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')