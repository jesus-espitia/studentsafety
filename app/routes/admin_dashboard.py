from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
from db import get_connection
from datetime import datetime

def admin_dashboard():
    nombre_admin = session.get('nombre_admin', 'Administrador')
    return render_template('admin_dashboard.html', nombre_admin=nombre_admin)