from database.db import get_connection
from .entities.Record import Record

class recordModel():
    
    @classmethod
    def get_sales(cls):
        try:
            connection = get_connection()
            records = []
            
            with connection.cursor() as cursor:
                cursor.execute('SELECT id, temperature, humedity, gas_level, light, createdAt FROM record')
                resultset = cursor.fetchall()
                
                for row in resultset:
                    record = Record(row[0], row[1], row[2], row[3], row[4], row[5])
                    records.append(record.to_json())
            
            connection.close()
            return records
        except Exception as ex:
            raise Exception(f"Error getting records: {ex}")
    