
# Librerias para el blockchain
import datetime
import hashlib
import json
from flask import Flask, jsonify, request

# Librerias para la criptomoneda
import requests
from uuid import uuid4
from urllib.parse import urlparse

class Blockchain:

# La funcion init lanza el programa, y crea el bloque génesis llamando 
# a la función create_block() con los parámetros de prueba y hash iniciales.
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof = 1, previous_hash = '0')
        self.nodes = set()

# Agrega un nodo a la red blockchain. Parsea la dirección proporcionada 
# y agrega el nombre de dominio del nodo a un conjunto de nodos.
    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_lenght = len(self.chain)

        for node in network:
            response  = requests.get(f'http://{node}/get_chain')
            ### AQUI A LO MEJOR HAY QUE QUITAR EL GET_
            if response.status_code == 200:
                length = response.json(['length'])
                chain = response.json(['chain'])

                if length > max_lenght and self.is_chain_valid(chain):
                    max_lenght = length
                    longest_chain = chain
            
            if longest_chain:
                self.chain = longest_chain
                return True
            return False


# Crea un nuevo bloque en la cadena con todos los datos necesarios incluidos. 
# Luego, reinicia la lista de transacciones y agrega el bloque a la cadena.
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'transactions': self.transactions}
        self.transactions = []
        self.chain.append(block)
        return block
    
# Agrega una transacción a la lista de transacciones pendientes en la blockchain.
    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({'sender': sender,
                             'receiver': receiver,
                             'amount': amount})
        previous_block = self.get_previous_block()
        return previous_block['index'] +1

# Obtenemos el bloque anterior en la cadena blockchain.
    def get_previous_block(self):
        return self.chain[-1]

# Realiza la prueba de trabajo para encontrar un número (proof) que cumpla con las condiciones dadas. 
# Incrementa el proof hasta que se encuentre un hash que comience con una cantidad 
# específica de ceros (mientras mas ceros, mas sube la dificultad de calculo)
    def proof_of_work(self, previous_proof):
        # sourcery skip: simplify-boolean-comparison, str-prefix-suffix
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()

            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
# Calcula el hash SHA-256 de un bloque utilizando la función de hash de la biblioteca hashlib.
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
# Verifica la validez de una cadena blockchain. Comprueba que cada bloque en la cadena 
# tenga el hash correcto y cumpla con las condiciones de prueba de trabajo establecidas.
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        # new_proof = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            
            previous_block = block
            block_index += 1
        return True
    
# Minar el Blockchain

# Creando la web app
app = Flask(__name__)

# Creando una direccion para el nodo en el puerto 5000
node_address = str(uuid4()).replace('-', '')

# Creando la Blockchain
blockchain = Blockchain()

# Minar un nuevo bloque
@app.route('/mine', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.add_transaction(sender = node_address, receiver = 'Jp', amount = 1)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': "Enhorabuena, has minado un bloque.", 
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions': block['transactions']}
    return jsonify(response), 200

# Obteniendo la cadena completa
@app.route('/chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

# Comprobando la validez de la cadena de bloques
@app.route('/verify', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': "La cadena es valida"}
    else:
        response = {'message': "El blockchain es invalido"}
    return jsonify(response), 200



# Agregando una nueva transaccion al blockchain
@app.route('/add', methods=['POST'])
def add_transaction():
    json = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']
    # if not all (key in json for key in transaction_keys):
    if any (key not in json for key in transaction_keys):
        return "Algun elemento de la transaccion esta faltando", 400

    index = blockchain.add_transaction(json['sender'], json['receiver'], json['amount'])
    response = {'message': f"La transaccion sera agregada al bloque {index}"}
    return jsonify(response), 201


# Paso 3 / Descentralizando el blockchain

# Conectando nuevos nodos
@app.route('/connect_node', methods=['POST'])
def connect_node():
    json = request.get_json()
    nodes = json.get('nodes')
    if nodes is None:
        return "No mode", 401
    for node in nodes:
        blockchain.add_node(node)
    response = {'message': "Todos los nodos estan conectados. La MoneDrag Blockchain contiene los siguientes nodos: ",
                'total_nodes': list(blockchain.nodes)}
    return jsonify(response), 201

# Reemplazando la cadena por la mas larga
@app.route('/replace_chain', methods=['GET'])
def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': "La cadena fue reemplazada por la mas larga",
                    'new_chain': blockchain.chain}
    else:
        response = {'message': "La cadena es la mas larga.",
                    'actual_chain': blockchain.chain}
    return jsonify(response), 200

# Lanzando la app
app.run(host = '0.0.0.0', port = 5000)

# Direccion para empezar a trabajar en Postman
# http://127.0.0.1:5000/chain

# Comandos para utilizar en Postman
# /mine - Minar un bloque
# /chain - Te muestra la cadena actualizada
# /verify - Verifica si la cadena esta correcta
# /add - Agrega una transaccion
# /connect_node - Conecta un nuevo nodo
# /replace_chain - Reemplaza la cadena por la mas larga

# Matar el proceso del puerto 5000 (flask) si se queda pillado:
# lsof -i:5000
# kill <PID>

# PRUEBAS CHATGPT CORRECCION
# Video minuto 1:58
# No funcionan los nodos, revisar


