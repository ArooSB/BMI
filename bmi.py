def calculate_bmi():
    message = "Hello, let's check your BMI!"
    print(message)
    print("-" * len(message))
    print("")

    weight = float(input("Please enter your weight in kilograms: "))
    height = float(input("Please enter your height in meters: "))

    # formula to calculate BMI
    bmi = weight / (height * height)

    # Rounding BMI to 2 decimal
    bmi = round(bmi, 2)

 # BMI result classified in one of the following categories and give heathcare tip

    if bmi < 18.5:
        category = "Underweight"
        tip = "Try adding more calorie-dense, nutritious foods to your diet and consider strength training exercises."
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        tip = "Maintain your healthy weight by continuing a balanced diet and regular exercise."
    elif 25 <= bmi < 30:
        category = "Overweight"
        tip = "Focus on a balanced diet and regular physical activity to help manage your weight."
    else:
        category = "Obesity"
        tip = "Consult with a healthcare provider to develop a personalized weight management plan."

    print("\nThank you for the Info!")
    print("")
    print(f"Your BMI is: {bmi}")
    print(f"You fall under '{category}' category.")
    print(f"Here's a tip for you: {tip}")


calculate_bmi()