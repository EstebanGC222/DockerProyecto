from flask import Flask, request, jsonify
import MySQLdb

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a la aplicación."

# Configuración de conexión a la base de datos MariaDB
db = MySQLdb.connect(
    host="mariadb",
    user="user",
    passwd="password",
    db="flaskdb"
)

# Crear tablas si no existen
with db.cursor() as cursor:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(50) NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT
        );
    """)
    db.commit()

# Ruta para registrar un usuario
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Se requieren username y password"}), 400

    try:
        with db.cursor() as cursor:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            db.commit()
        return jsonify({"message": "Usuario registrado exitosamente"}), 201
    except MySQLdb.IntegrityError:
        return jsonify({"message": "El usuario ya existe"}), 400

# Ruta para iniciar sesión
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

    if user:
        return jsonify({"message": "Login exitoso"}), 200
    else:
        return jsonify({"message": "Credenciales incorrectas"}), 401

# CRUD de ítems

# Crear ítem
@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({"message": "El nombre del ítem es obligatorio"}), 400

    with db.cursor() as cursor:
        cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (name, description))
        db.commit()

    return jsonify({"message": "Ítem creado exitosamente"}), 201

# Leer usuarios
@app.route('/users', methods=['GET'])
def get_users():
    with db.cursor() as cursor:
        cursor.execute("SELECT id, username FROM users")
        users = cursor.fetchall()

    # Convertir los datos en un formato JSON
    users_list = [{"id": user[0], "username": user[1]} for user in users]
    return jsonify(users_list), 200


# Leer ítems
@app.route('/items', methods=['GET'])
def read_items():
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM items")
        items = cursor.fetchall()

    return jsonify(items), 200

# Actualizar ítem
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    name = data.get('name')
    description = data.get('description')

    with db.cursor() as cursor:
        cursor.execute(
            "UPDATE items SET name = %s, description = %s WHERE id = %s",
            (name, description, item_id)
        )
        db.commit()

    return jsonify({"message": "Ítem actualizado exitosamente"}), 200

# Eliminar ítem
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    with db.cursor() as cursor:
        cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
        db.commit()

    return jsonify({"message": "Ítem eliminado exitosamente"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
