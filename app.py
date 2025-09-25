# app.py - Arquivo principal para iniciar o servidor Flask.

from flask import Flask
from views import main_blueprint, close_serial_on_exit

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Registra o blueprint que contém todas as rotas da aplicação
app.register_blueprint(main_blueprint)

# Garante que a porta serial seja fechada ao encerrar o app
import atexit
atexit.register(close_serial_on_exit)

if __name__ == '__main__':
    # Inicia o servidor Flask
    # O uso de use_reloader=False é importante para não tentar abrir a porta serial duas vezes
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
