from flask import Flask, render_template, Blueprint
from model import file_reader, search_numbers, date_filter, text_pars
import os



directory = os.listdir(r'C:/Users/Дмитрий Игнатов/Documents/proj/test/')

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/', methods=['POST'])
def parsing():
    file_reader.file_reader(directory)
    search_numbers.search_numbers(file_reader.data)
    date_filter.date_filter(search_numbers.found_numbers)
    text_pars.text_pars(date_filter.found_dates)
    return str(text_pars.result)

myblueprint = Blueprint('myblueprint', __name__, template_folder= "..view/templates")

app.register_blueprint(myblueprint, url_prefix="/blue")



if __name__ == '__main__':
    app.run(debug=True)
