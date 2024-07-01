from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Test_Home.html')

@app.route('/Test_Explore.html')
def explore():
    return render_template('Test_Explore.html')

@app.route('/Test_Support.html')
def support():
    return render_template('Test_Support.html')

@app.route('/Test_About.html')
def about():
    return render_template('Test_About.html')

@app.route('/Burger.html')
def burger():
    return render_template('Burger.html')

@app.route('/Spaghetti.html')
def spaghetti():
    return render_template('Spaghetti.html')

@app.route('/Fried_Chicken.html')
def fried_chicken():
    return render_template('Fried_Chicken.html')

@app.route('/Beef_Wellington.html')
def beef_wellington():
    return render_template('Beef_Wellington.html')

@app.route('/Salmon.html')
def salmon():
    return render_template('Salmon.html')

@app.route('/Mac_and_Cheese.html')
def mac_and_cheese():
    return render_template('Mac_and_Cheese.html')

if __name__ == '__main__':
    app.run(debug=True)
