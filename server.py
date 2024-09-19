from flask import Flask, render_template, session, redirect
import random

app = Flask(__name__)

app.secret_key = "password"

@app.route('/')
def index():
    if 'gold_earned' not in session:
        session['gold_earned'] = 0 
    return render_template('index.html')

@app.route('/farm_gold', methods=['POST'])
def farm_gold():
    gold = random.randint(10, 20)
    session['gold_earned'] = session['gold_earned'] + gold
    print(f"{gold} gold earned from the farm!")
    return redirect('/')

@app.route('/cave_gold')
def cave_gold():
    gold = random.randint(5, 10)
    session['gold_earned'] = session['gold_earned'] + gold
    print(f"{gold} gold earned from the cave!")
    return redirect('/')

@app.route('/house_gold')
def house_gold():
    gold = random.randint(2, 5)
    session['gold_earned'] = session['gold_earned'] + gold
    print(f"{gold} gold earned from the house!")
    return redirect('/')

@app.route('/casino_gold')
def casino_gold():
    gold = random.randint(-50, 50)
    session['gold_earned'] = session['gold_earned'] + gold
    print(f"{gold} gold earned/lost from the casino!")
    return redirect('/')

@app.route('/clear')
def donate():
    session.clear()
    return redirect('/')

if __name__ == ('__main__'):
    app.run(debug=True, port=5000)