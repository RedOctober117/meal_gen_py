from flask import Flask, render_template, request
import meal_gen_py.db_model.model as model

app = Flask(__name__)

# For form creation https://flask.palletsprojects.com/en/3.0.x/patterns/wtforms/

@app.route('/', methods=['POST', 'GET'])
def debug_world():
    table = model.UnitAbbreviation(2, 'abc')._asdict()
    print([ i for i in request.args])
    return render_template('test_input.html.jinja', table=table)


@app.route('insert', methods=['POST', 'GET'])
def insert_route():
    insertion = 'some selection option here'
    match insertion:
        case 'a':
            return True
    return render_template('test_input.html.jinja')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

