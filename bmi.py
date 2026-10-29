# • Underweight: Below 18.5
# • Healthy Weight: 18.5 to 24.9
# • Overweight: 25.0 to 29.9
# • Obesity (Class I): 30.0 to 34.9
# • Obesity (Class II): 35.0 to 39.9
# • Severe Obesity (Class III): 40.0 or higher

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height :"))
bmi = weight / height ** 2
if bmi<18.5:{
    print("Underweight")
}
elif bmi>=18.5  and bmi<=24.9:{
    print("Healthy Weight")
}
elif bmi>=25.0 and bmi<=29.9:{
    print("Overweight")
}
elif bmi>30.0 and bmi<=34.9:{
    print("Obese class 1")
}
elif bmi>=35.0 and bmi<=39.9:{
    print("Obese class2")
}
else :{
    print("Severe obesity")
}
