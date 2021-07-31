import json
from assignment import DataColumn, OverWeightCount;

def JsonData():
	with open('data.json') as d:
		data = json.load(d);
		return data;


class Test:
	def test_1(self):
		i=JsonData()[0]
		height=i['HeightCm']
		weight=i['WeightKg']
		d=DataColumn(height,weight)
		assert d['BMI Category']=='Moderately obese'
		assert d['Health Risk']=='Medium risk'

		

	def test_2(self):
		i=JsonData()[1]
		height=i['HeightCm']
		weight=i['WeightKg']
		d=DataColumn(height,weight)
		assert d['BMI Category']=='Moderately obese'
		assert d['Health Risk']=='Medium risk'
		
	def test_3(self):
		i=JsonData()[2]
		height=i['HeightCm']
		weight=i['WeightKg']
		d=DataColumn(height,weight)
		assert d['BMI Category']=='Normal weight'
		assert d['Health Risk']=='Low risk'
		
	def test_4(self):
		i=JsonData()[3]
		height=i['HeightCm']
		weight=i['WeightKg']
		d=DataColumn(height,weight)
		assert d['BMI Category']=='Normal weight'
		assert d['Health Risk']=='Low risk'
		
	def test_5(self):
		i=JsonData()[4]
		height=i['HeightCm']
		weight=i['WeightKg']
		d=DataColumn(height,weight)
		assert d['BMI Category']=='Moderately obese'
		assert d['Health Risk']=='Medium risk'
		
	def test_6(self):
		i=JsonData()[5]
		height=i['HeightCm']
		weight=i['WeightKg']
		d=DataColumn(height,weight)
		assert d['BMI Category']=='Overweight'
		assert d['Health Risk']=='Enhanced risk'
		
	def test_overweight(self):
		c=OverWeightCount(JsonData());
		assert c==1




