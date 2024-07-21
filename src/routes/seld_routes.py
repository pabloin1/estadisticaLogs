from flask import Blueprint, jsonify
from models.RecordModel import recordModel

main = Blueprint('record_blueprint', __name__)

@main.route('/')
def get_records():
    try:
        records = recordModel.get_records()
        return jsonify(records)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/temperature-statistics')
def get_temperature_statistics():
    try:
        statistics = recordModel.get_temperature_statistics()
        return jsonify(statistics)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
