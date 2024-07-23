from src.utils.DateFormar import DateFormat

class Record():
    def __init__(self,id,temperature=None,humedity=None,gas_level=None,light=None,createdAt=None) -> None:
        self.id = id
        self.temperature = temperature
        self.humedity = humedity
        self.gas_level = gas_level
        self.light  = light
        self.createdAt = createdAt
        
    def to_json(self):
        return {
            'id':self.id ,
            'temperature':self.temperature,
            'humedity':self.humedity,
            'gas_level':self.gas_level,
            'light':self.light,
            'createdAt': DateFormat.convert_date(self.createdAt)
        }