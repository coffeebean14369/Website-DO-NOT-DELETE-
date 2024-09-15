from flask import Flask, render_template, request
from config import Config
import sqlite3
import random

app=Flask(__name__)


app.config.from_object(Config)

@app.route('/')
def home():
    conn = sqlite3.connect(app.config['DATABASE'])
    cur = conn.cursor()
    cur.execute("SELECT * FROM food;")
    foods = cur.fetchall()
    conn.close() 
    return render_template('home.html',foods=foods)

@app.route('/foods')
def all_foods():
    conn = sqlite3.connect(app.config['DATABASE'])
    cur = conn.cursor()
    cur.execute("SELECT * FROM food;")
    foods = cur.fetchall()
    conn.close() 
    return render_template("foods.html" ,foods=foods)

@app.route('/food_page/<int:id>')
def food_page(id):
    conn = sqlite3.connect(app.config['DATABASE'])
    cur = conn.cursor()
    cur.execute("select * from food where Food_id= ?;" ,(id,))
    food = cur.fetchone()
    cur.execute("""select ingredients."ingredients_discription "  from food
                join recipes on recipes.food_id = food.Food_id
                join ingredients on ingredients.resipie_id = recipes.id
                where food.food_Id = ?;""",(id,))
    ingredients= cur.fetchall()
    conn.close() 
    return render_template("food_page.html",food=food,ingredients=ingredients)

@app.route('/Contact')
def Contact():
    conn = sqlite3.connect(app.config['DATABASE'])
    cur = conn.cursor()
    cur.execute("SELECT * FROM food;")
    foods = cur.fetchall()
    conn.close() 
    return render_template('Contact.html',foods=foods)

@app.route('/About')
def About():
    conn = sqlite3.connect(app.config['DATABASE'])
    cur = conn.cursor()
    cur.execute("SELECT * FROM food;")
    foods = cur.fetchall()
    conn.close() 
    return render_template("About.html" ,foods=foods)

@app.errorhandler(404)
def invalidroute(e):
  return render_template('error.html')

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    comment = request.form['comment']
    conn = sqlite3.connect(app.config['DATABASE'])
    cur = conn.cursor()
    cur.execute("INSERT INTO feedback (name, email, comment) VALUES (?, ?, ?)", (name, email, comment))
    conn.commit()
    conn.close()
    return render_template('Contact.html')


if __name__ == '__main__':
    app.run(debug=True)
