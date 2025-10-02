

from django.shortcuts import render

def bmi_calculator(request):
    bmi = None
    if request.method == "POST":
        try:
            height = float(request.POST.get("height")) / 100  # cm → meters
            weight = float(request.POST.get("weight"))
            bmi = round(weight / (height * height), 2)

            # Print result in terminal
            print("Height:", height * 100, "cm")
            print("Weight:", weight, "kg")
            print("BMI:", bmi)

        except (ValueError, ZeroDivisionError):
            bmi = None  # in case of invalid input

    return render(request, "myapp/math.html", {"bmi": bmi})