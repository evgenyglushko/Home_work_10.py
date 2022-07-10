from flask import Flask
from utils import load_candidates, get_all, get_by_pk, get_by_skill
from constants import FILENAME

app = Flask(__name__)

dict = load_candidates(FILENAME)

# главная страница - показывает всех кандидатов
@app.route("/",)
def main():
    return f'<pre>Наши кандидаты:\n<pre>' \
           f'<pre>{get_all(dict)}\n<pre>'

# выводит кандидатов по pk(int)
@app.route('/candidates/<int:x>',)
def candidates(x):
    return f"<pre>{get_by_pk(x, dict)}<pre>"

# выводит кандидатов по навыку skills
@app.route('/skills/<x>',)
def skills(x):
    return f"<pre>{get_by_skill(x, dict)}<pre>"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)



