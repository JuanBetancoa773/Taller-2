from flask import Blueprint, jsonify, render_template
import random, socket
from .data import pokeneas

main = Blueprint('main', __name__)

@main.route('/pokenea-json')
def pokenea_json():
    p = random.choice(pokeneas)
    p_info = {
        "id": p["id"],
        "nombre": p["nombre"],
        "altura": p["altura"],
        "habilidad": p["habilidad"],
        "container_id": socket.gethostname()
    }
    return jsonify(p_info)

@main.route('/pokenea-img')
def pokenea_img():
    p = random.choice(pokeneas)
    p["container_id"] = socket.gethostname()
    return render_template('index.html', p=p)
