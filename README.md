# Ex.05 Design a Website for Server Side Processing
## Date:02.10.25

## AIM:
 To design a website to calculate the Body Mass Index (BMI) in the server side. 


## FORMULA:
BMI = W/H<sup>2</sup>
<br> BMI --> Body Mass Index
<br> W --> Weight
<br> H --> Height

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<!DOCTYPE html>
<html>
<head>
    <title>BMI Calculator</title>
    <style>
        body {
            background-color: cyan; /* Background color */
            font-family: Arial, sans-serif;
        }
        .container {
            width: 350px;
            margin: 100px auto;
            padding: 20px;
            background-color: red;
            border: 3px dashed purple;
            border-radius: 20px;
            text-align: center;
        }
        h2 {
            margin-bottom: 10px;
        }
        input {
            margin: 8px 0;
            padding: 8px;
            width: 90%;
        }
        button {
            margin-top: 10px;
            padding: 8px;
            width: 95%;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>BMI CALCULATOR</h2>
        <h3>JOSHUA DANIEL A - 25017654</h3>

        <form method="post">
            {% csrf_token %}
            <label>HEIGHT [cm]:</label><br>
            <input type="text" name="height"><br>
            <label>WEIGHT [kg]:</label><br>
            <input type="text" name="weight"><br>
            <button type="submit">CALCULATE BMI</button>
        </form>

        {% if bmi %}
            <h3>YOUR BMI: {{ bmi }}</h3>
        {% endif %}
    </div>
</body>
</html>

views.py



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


urls.py

from django.contrib import admin
from django.urls import path
from myapp import views   # Import views from your app

urlpatterns = [
    path("admin/", admin.site.urls),
    path("bmi/", views.bmi_calculator, name="bmi_calculator"),
]
```


## SERVER SIDE PROCESSING:
![alt text](<Screenshot (65).png>)

## HOMEPAGE:
![alt text](<Screenshot (66).png>)

## RESULT:
The program for performing server side processing is completed successfully.


