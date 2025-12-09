from flask import Flask, request, jsonify

app = Flask(__name__)

# BANCO DE DADOS 
usuarios = {"admin@sghss.com": "senha123"} # simulaç
pacientes = []

# LOGIN (POST /login) - Atende Autenticação
@app.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    email = dados.get('email')
    senha = dados.get('senha')

    if usuarios.get(email) == senha:
        # Devolver um token falso, conforme requerido para segurança LGPD
        return jsonify({
            "mensagem": "Login bem-sucedido!",
            "token": "TOKEN-BACKEND-ADS-PYTHON-XYZ" 
        }), 200
    else:
        return jsonify({"erro": "Credenciais inválidas."}), 401

# CADASTRO DE PACIENTE (POST /pacientes)
@app.route('/pacientes', methods=['POST'])
def criar_paciente():
    dados = request.get_json()
    
    # Validação
    if 'nome' not in dados or 'cpf' not in dados:
        return jsonify({"erro": "Nome e CPF são obrigatórios."}), 400

    novo_paciente = {
        "id": len(pacientes) + 1,
        "nome": dados['nome'],
        "cpf": dados['cpf'],
        "telefone": dados.get('telefone', 'Não informado')
    }

    pacientes.append(novo_paciente)
    
    return jsonify({
        "mensagem": "Paciente cadastrado com sucesso!",
        "paciente": novo_paciente
    }), 201

# LISTAR PACIENTES
@app.route('/pacientes', methods=['GET'])
def listar_pacientes():
    return jsonify(pacientes), 200

if __name__ == '__main__':
    print("Servidor Flask iniciando...")
    app.run(debug=True, port=3000)