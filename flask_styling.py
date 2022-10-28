from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("styling/home.html")
    
@app.route('/tree')
def tree():
    return render_template('styling/tree.html')

@app.route('/containers')
def containers():
    return render_template('styling/containers.html')

@app.route('/grid')
def grid():
    return render_template('styling/grid.html')

@app.route('/')
def fullpage():
    return render_template('styling/fullpage.html')

@app.route('/contacts')
def contacts():
    return render_template('styling/contacts.html')

@app.route('/flex')
def flex():
    return render_template('styling/flex.html')

@app.route('/flexpage')
def flexpage():
    return render_template('styling/flexpage.html')

if __name__ == "__main__":
    app.run(debug=True)