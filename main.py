from Mess_agregator.blueprint import mess_agregator
from app import app

app.register_blueprint(mess_agregator, url_prefix='/api/')


if __name__ == '__main__':
    app.run()