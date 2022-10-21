from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/localhost:5000')
def localhost():
    return render_template('localhost.html')

# @app.route('/<name>')
# def pankis_kartus(name):
#     return f'{name} '*5

@app.route('/tikrinimas')
def tikrinimas():
    return render_template('tikrinimas.html')

@app.route('/rezultatas')
def rezultatas():
    metai = int(request.args["metai"])
    if metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0):
        atsakymas = 'keliamieji'
    else:
        atsakymas = 'nekeliamieji'
    return render_template('rezultatas.html', **request.args, atsakymas = atsakymas)




if __name__ == "__main__":
    app.run(debug=True)