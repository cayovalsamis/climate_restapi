from sqlalchemy import Column, Integer, String
from database import Base
from collections import OrderedDict

class DictSerializable(object):
    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result
        
        
# class Climate_data(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.String(64), index=True, unique=True)
#     temperature = db.relationship('Temperature_data', backref='author', lazy='dynamic')
#     rainfall = db.relationship('Rainfall_data', backref='author', lazy='dynamic')
#    
#     def __repr__(self):
#         return '<Climate_data {}>'.format(self.date) 
#     
# class Temperature_data(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	temperature = db.Column(db.String(120), default='No data')
# 	climate_id = db.Column(db.Integer, db.ForeignKey('climate_data.id'))
# 
# 	def __repr__(self):
# 		return '<Temperature {}>'.format(self.temperature) 
# 
# class Rainfall_data(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	rainfall = db.Column(db.String(128), default='No data')
# 	climate_id = db.Column(db.Integer, db.ForeignKey('climate_data.id'))
# 
# 	def __repr__(self):
# 		return '<Rainfall {}>'.format(self.rainfall)

class Climate_data(DictSerializable,Base):
	__tablename__='climates'
	id = Column(Integer, primary_key=True)
	date = Column(String(64), index=True, unique=True)
	temperature = Column(String(120), default='No data')
	rainfall = Column(String(128), default='No data')
   
	def __init__(self, date=None, temperature=None, rainfall=None):
		self.date= date
		self.temperature = temperature
		self.rainfall = rainfall
   
	def __repr__(self):
		return '<Climate_data: date=%r, temperature=%r, rainfall=%r>' % (self.date, self.temperature, self.rainfall)
#		return '<Climate_data {}>'.format(self.date, self.temperature, self.rainfall) 







