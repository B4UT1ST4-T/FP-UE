# BMI Checker

# BMI Constants
UNDER = 18.5
NORMAL = 24.9
OVER = 29.9

# Pangwewelcome sa user
print("Mabuhay ito ang iyong BMI Checker!")

# Tatanggap ng input mula sa user
name = input("Ilagay ang iyong pangalan: ")
weight = float(input("Ilagay ang iyong timbang sa kg: "))
height = float(input("Ilagay ang iyong taas sa metro: "))
height = height / 100 # Convert cm to m if needed
bmi = weight / (height ** 2)  
# Pagkalkula ng BMI at kategorya

if weight > 0 or height > 0: 
    if bmi < UNDER:
        category = "Underweight"
    elif bmi <= NORMAL:
        category = "Normal weight"
    elif bmi <= OVER:
        category = "Overweight"
    else:
        category = "Obesity"   
        
    print(f"hello {name}, ang iyong BMI ay: {bmi:.2f} at ikaw ay nasa kategoryang {category}.")  # noqa: E501
else:
    print("Ang timbang at taas ay dapat positibo.")