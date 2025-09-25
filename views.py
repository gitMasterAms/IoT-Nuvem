# views.py - Arquivo que gerencia as rotas e a lógica de comunicação com o Arduino.

from flask import Blueprint, render_template, request, jsonify
import serial
import time

# --- CONFIGURAÇÕES DA PORTA SERIAL ---
# Altere para sua porta, ex: 'COM3' no Windows ou '/dev/ttyUSB0' no Linux
PORTA_SERIAL = 'COM5'
BAUD_RATE = 9600
arduino = None  # Variável global para a conexão serial

# Tenta estabelecer a conexão com a porta serial
try:
    arduino = serial.Serial(PORTA_SERIAL, BAUD_RATE, timeout=1)
    time.sleep(2)  # Tempo para a conexão serial ser estabelecida
    print(f"Sucesso: Conectado à porta serial {PORTA_SERIAL}.")
except serial.SerialException as e:
    print(f"Erro Crítico: Não foi possível conectar à porta serial {PORTA_SERIAL}. {e}")
    print("Verifique se a porta está correta, se o Arduino está conectado e se nenhum outro programa está usando a porta.")
    arduino = None
except Exception as e:
    print(f"Um erro inesperado ocorreu: {e}")
    arduino = None

# Cria um "Blueprint" para organizar as rotas
main_blueprint = Blueprint('main', __name__)

def close_serial_on_exit():
    """Função para fechar a porta serial de forma segura ao sair."""
    if arduino and arduino.is_open:
        arduino.close()
        print("Conexão serial fechada.")

@main_blueprint.route('/')
def index():
    """Renderiza a página HTML principal."""
    return render_template('index.html')

@main_blueprint.route('/send_command', methods=['POST'])
def send_command():
    """Recebe comandos do frontend e os envia para o Arduino."""
    if not arduino or not arduino.is_open:
        return jsonify({'status': 'error', 'message': 'Erro: Porta serial não conectada.'}), 500

    data = request.json
    h = data.get('h')
    v = data.get('v')

    try:
        # Converte para float e valida os valores
        h_float = float(h)
        v_float = float(v)

        if not (-20 <= h_float <= 20 and -12 <= v_float <= 12):
            return jsonify({'status': 'error', 'message': 'Distâncias fora do intervalo permitido (H: -20 a 20, V: -12 a 12).'}), 400

        # Formata e envia o comando para o Arduino
        comando = f"{h_float} {v_float}\n"
        arduino.write(comando.encode())
        return jsonify({'status': 'success', 'message': f'Enviado: {comando.strip()}'})

    except (ValueError, TypeError):
        return jsonify({'status': 'error', 'message': 'Erro: Insira valores numéricos válidos.'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Erro ao enviar dados: {e}'}), 500

@main_blueprint.route('/send_return', methods=['POST'])
def send_return():
    """Envia o comando de retorno (21) para o Arduino."""
    if not arduino or not arduino.is_open:
        return jsonify({'status': 'error', 'message': 'Erro: Porta serial não conectada.'}), 500

    try:
        comando = "21\n"
        arduino.write(comando.encode())
        return jsonify({'status': 'success', 'message': f'Enviado: {comando.strip()}'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Erro ao enviar comando de retorno: {e}'}), 500

@main_blueprint.route('/read_serial', methods=['GET'])
def read_serial():
    """Lê dados da porta serial e os retorna para o frontend."""
    if arduino and arduino.in_waiting > 0:
        try:
            linha = arduino.readline().decode().strip()
            if linha:
                return jsonify({'data': linha})
        except Exception as e:
            print(f"Erro ao ler da serial: {e}")
            return jsonify({'data': ''})
    return jsonify({'data': ''})
