from flask import Flask, request, render_template
import otst_salary_calculator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    estimated_credits = None
    estimated_salary = None
    salary = 9690
    if request.method == "POST":
        try:
            credits = float(request.form["credits"])
            days = float(request.form["days"])
            tax_input = request.form["tax_input"]
            estimated_credits = otst_salary_calculator.est_credits(credits, days)  # Call your script's function
            
            if tax_input == "no":
                estimated_salary = otst_salary_calculator.est_salary_nontax(credits, days, salary)
            elif tax_input == "yes":
                estimated_salary = otst_salary_calculator.est_salary_tax(credits, days, salary)
            else:
                estimated_salary = "Invalid tax input"
        except ValueError:
            credits = "Invalid input"
            days = "Invalid Input"
    return render_template("index.html", estimated_credits=estimated_credits, estimated_salary=estimated_salary)

'''
    result = None
    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            result = calculator.add(a, b)  # Call your script's function
        except ValueError:
            result = "Invalid input"
    return render_template("index.html", result=result)
'''
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)