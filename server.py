from flask import Flask, render_template
app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template("index.html", rows = int(4))

# @app.route('/<x>')
# def rows(x):
#     return render_template("index.html", rows = int(x))

# @app.route('/<x>/<y>/<color1>/<color2>')
# def rowcolumncolors(x, y, color1, color2):
#     return render_template("index.html", rows = int(x), columns = int(y), redsq = color1, blacksq = color2)


@app.route('/')
def checkerboard():
    return render_template('index.html', num_rows = 8, num_cols = 8, color1 = 'red', color2 = 'black')

@app.route('/<num_rows>')
def checkerboard_x(num_rows):
    return render_template('index.html', num_rows = int(num_rows), num_cols = 8, color1 = 'red', color2 = 'black')

@app.route('/<num_rows>/<num_cols>')
def checkerboard_x_y(num_rows, num_cols):
    return render_template('index.html', num_rows = int(num_rows), num_cols = int(num_cols), color1 = 'red', color2 = 'black')

@app.route('/<num_rows>/<num_cols>/<color1>/<color2>')
def checkerboard_x_y_c1_c2(num_rows, num_cols, color1, color2):
    return render_template('index.html', num_rows = int(num_rows), num_cols = int(num_cols), color1 = color1, color2 = color2)


if __name__=="__main__":
    app.run(debug=True)