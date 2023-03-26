from flask import Flask
from flask import request

from db import DataBase

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Application server'


@app.route('/questions')
def get_questions():
    """Получение всех вопросов"""
    return dataBase.get_all_questions()


@app.route('/questionsByLevel')
def get_questions_by_level():
    """Получение вопросов по уровню"""
    level = int(request.args.get('level', default=1, type=int))
    return dataBase.get_questions_by_level(level)


if __name__ == '__main__':
    dataBase = DataBase(r'./db/questions.json')
    app.run(debug=True, host="0.0.0.0")
