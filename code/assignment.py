class Person:

    def __init__(self,height,weight):
        self.height = height;
        self.weight = weight;
        self.bmi=0;
        self.category='';
        self.health='';
        
    def CalculateBMI(self):
        self.bmi = self.weight/((self.height/100)**2);
        
    def HealthDetails(self):
	    if self.bmi<=18.4:
		    self.category = "Underweight"
		    self.health = "Malnutrition risk"

	    elif 18.5<=self.bmi<=24.9:
		    self.category = "Normal weight"
		    self.health = "Low risk"

	    elif 25<=self.bmi<=29.9:
		    self.category = "Overweight"
		    self.health = "Enhanced risk"

	    elif 30<=self.bmi<=34.9:
		    self.category = "Moderately obese"
		    self.health = "Medium risk"

	    elif 35<=self.bmi<=39.9:
		    self.category  = "Severely obese"
		    self.health = "High risk"

	    elif self.bmi>=40 :
		    self.category = "Very severely obese"
		    self.health = "Very high risk"
             
             
def DataColumn(height,weight):
	obj = Person(height,weight)
	obj.CalculateBMI();
	obj.HealthDetails();
	return ({'BMI':obj.bmi,'BMI Category':obj.category,'Health Risk':obj.health});
	
def OverWeightCount(data):
	count=0
	for i in data:
		height=i['HeightCm']
		weight=i['WeightKg']
		obj = Person(height,weight)
		obj.CalculateBMI();
		if 25<=obj.bmi<=29.9:
			count+=1
	return count;
	
