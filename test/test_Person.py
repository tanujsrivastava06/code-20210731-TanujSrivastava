import json
from assignment import HealthData, OverWeightCount;

def JsonData():
	with open('data.json') as d:
		data = json.load(d);
		return data;


class Test:
	def test_PersonHealth1(self):
		i=JsonData()[0]
		height=i['HeightCm']
		weight=i['WeightKg']
		d=HealthData(height,weight)
		assert d['BMI Category']=='Moderately obese'
		assert d['Health Risk']=='Medium risk'

				
	def test_PersonHealth2(self):
		i=JsonData()[2]
		height=i['HeightCm']
		weight=i['WeightKg']
		d=HealthData(height,weight)
		assert d['BMI Category']=='Normal weight'
		assert d['Health Risk']=='Low risk'
		
		
		
	def test_overweight(self):
		c=OverWeightCount(JsonData());
		assert c==1




