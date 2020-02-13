from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
_version = '1.0'
_wifi = 'wifi'
_money = 'money'
_uri = '/tracker/{module}/api/v{version}'


def __get_route(module, destination):
    return '{uri}/{destination}'.format(uri=_uri.format(module=module, version=_version), destination=destination)


def __get_wifi_route(destination):
    return __get_route(module=_wifi, destination=destination)


def __get_money_route(destination):
    return __get_route(module=_money, destination=destination)


@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'


@app.route(__get_wifi_route('connections'), methods=['GET'])
def get_connections():
    return 'List of wifi connections'


@app.route(__get_money_route('payments'), methods=['GET'])
def get_payments():
    return 'List of payments'


@app.route(__get_money_route('outcomes'), methods=['GET'])
def get_outcomes():
    return 'List of outcomes'


@app.route(__get_money_route('incomes'), methods=['GET'])
def get_incomes():
    return 'List of incomes'


if __name__ == '__main__':
    app.run()
