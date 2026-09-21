"""
CloudKart Microservice API
"""
from flask import Flask, jsonify

application = Flask(_name_)

@application.route('/')
def index_endpoint():
    payload = {
        "service_name": "CloudKart Core Engine",
        "system_status": "UP",
        "deployment_region": "Global Gateway",
        "api_version": "1.0.0"
    }
    return jsonify(payload), 200

@application.route('/health')
def check_system_health():
    return jsonify({
        "status": "healthy",
        "database_connection": "active",
        "node_state": "operational"
    }), 200

if _name_ == '_main_':
    application.run(host='0.0.0.0', port=5000)
