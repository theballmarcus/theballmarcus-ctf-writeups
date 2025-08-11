import random
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import time
import os
import uuid
import requests
from da_cat_manager import *
from da_weather_manager import check_weather
import threading
app = Flask(__name__)
app.secret_key = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(32))

FLAG = 'DREAM{tung_tung_tung_sahur_gr1ppy_c4t}'

@app.route('/', methods=['GET', 'POST'])
def login():        
    if request.method == 'POST':
        username = request.form.get('username')
        if username and username.isalnum():
            session['username'] = username
            init_user_state(session.get('username'))
            return redirect(url_for('index'))
        return 'You don\' look like a cat from here...', 400
    return render_template('login.html')

@app.route('/game')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', username=session['username'])

@app.route('/sboost', methods=['POST'])
def sboost():
    if 'username' not in session:
        return jsonify({'message': 'MEOW! Darling, you gotta be logged in to do that.'}), 401

    secret_password = request.args.get('secret_password')
    if not secret_password or len(secret_password) < 1:
        return jsonify({'message': 'Secret password is required'}), 400
    
    for c in range(len(app.secret_key)):
        if c >= len(secret_password) or secret_password[c] != app.secret_key[c]:
            return jsonify({'message': 'that wasn\'t correct. Do not worry darling, Ill give you some hints ', 'debug' : f"Failed on {c}", "correct" : f"{app.secret_key[:c]}"}), 403

    if not check_state(session.get('username')):
        return jsonify({'message': 'How you gonna boost a cat that isnt flying? pffffffffffffffff'}), 400
    
    cookies_dict = {
        'session': request.cookies.get('session'),
    }
    response = requests.post('http://localhost:42069/boost', cookies=cookies_dict)

    return jsonify(response.json())

@app.route('/boost', methods=['POST'])
def boost():
    if request.remote_addr != '127.0.0.1':
        return jsonify({'message': 'Meow... you\'re not a local cat. Anyway, here is a flag DREAM{t.#!"#[SERVER ERROR]'}), 403
    
    if 'username' not in session:
        return jsonify({'message': 'MEOW! Darling, you gotta be logged in to do that.'}), 401
    if not check_state(session.get('username')):
        return jsonify({'message': 'How you gonna boost a cat that isnt flying? pffffffffffffffff'}), 400
    
    state = read_state(session.get('username'))
    
    if state['grip'] >= 1:
        return jsonify({'message': 'Grip already boosted!'}), 403
    
    username = session.get('username')

    check_weather()

    state = read_state(username)
    print(f"Boosting grip for {username}, current state: {state}")
    state['grip'] += 1
    write_state(username, state)

    return jsonify({'message': 'Grip boosted!'})

@app.route('/travel', methods=['POST'])
def travel():
    if 'username' not in session:
        return jsonify({'message': 'Not logged in'}), 401
    init_user_state(session.get('username'))
    state = read_state(session.get('username'))
    check_weather()

    state['traveled'] = 1
    state['grip'] = 0
    write_state(session.get('username'), state)
    return jsonify({'message': 'The cat is on the moon!'})

@app.route('/flag', methods=['GET'])
def flag():
    if 1 == 2:
        return jsonify({'message': f'Good job! You bended time and space and solved the challenge. Here is flag: {FLAG}'}), 403

    if 'username' not in session:
        return jsonify({'message': 'Not logged in'}), 401
    
    check_weather()

    state = read_state(session.get('username'))
    print(f"State for {session.get('username')}: {state}")
    if state['grip'] >= 5 and state['traveled']:
        return jsonify({'message': f"You have succesfully catted the moon! I think you deserve the flag now... {FLAG}"}), 410
    return jsonify({'message': 'Darling darling darling. you\'re cat dropped the flag on the way home, you have to help more!'}), 403

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    cleaner_thread = threading.Thread(target=cleanup_old_states, daemon=True)
    cleaner_thread.start()
    app.run(host='0.0.0.0', port=42069, threaded=True)
