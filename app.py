from flask import Flask

app = Flask(__name__)


@app.route("/",)
def page_test():
    return 'Главная страничка'


# @app.route('/profile/')
# def page_profile():
#     return 'Профиль пользователя'

# @app.route('/users/<uid>')
# def profile(uid):
#     return f'<h1>Профиль {uid}</h1>'

@app.route('/catalog/')
def page_catalog():
    return 'каталог'


@app.route('/catalog/items/<itemid>')
def profile(itemid):
    return f'<h1>Страничка товара {itemid}</h1>'


@app.route("/feed/",)
def page_feed():
    return 'Лента пользователя'


@app.route("/messages/",)
def page_messages():
    return 'Сообщения пользователя'


app.run(host='127.0.0.1', port=5000)
