from src.database.db import get_connection
from .entities.Record import Record
import numpy as np

class recordModel():
    @classmethod
    def get_records(cls):
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
    
    @classmethod
    def get_temperature_statistics(cls):
        try:
            connection = get_connection()
            temperatures = []
            
            with connection.cursor() as cursor:
                cursor.execute('''
                    SELECT temperature 
                    FROM record 
                    WHERE createdAt >= NOW() - INTERVAL '7 days'
                ''')
                resultset = cursor.fetchall()
                
                for row in resultset:
                    temperatures.append(row[0])
                    
            connection.close()
            
            if not temperatures:
                return {
                    'message': 'No data available for the past week'
                }
            
            temperatures_array = np.array(temperatures, dtype=float)  # Convert to float
            
            # Calculate mode
            counts = np.bincount(temperatures_array.astype(int))  # Cast to int for bincount
            mode = np.argmax(counts)
            
            statistics = {
                'mean': float(np.mean(temperatures_array)),
                'median': float(np.median(temperatures_array)),
                'std_dev': float(np.std(temperatures_array)),
                'min': float(np.min(temperatures_array)),
                'max': float(np.max(temperatures_array)),
                'mode': float(mode)  # Convert mode to float
            }
            
            return statistics
        except Exception as ex:
            raise Exception(f"Error calculating statistics: {ex}")
        
