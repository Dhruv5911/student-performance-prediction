from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    status = None

    if request.method == "POST":
        study = float(request.form["study"])
        attendance = float(request.form["attendance"])
        sleep = float(request.form["sleep"])

        # Create DataFrame from user input
        input_df = pd.DataFrame(
            [[study, attendance, sleep]],
            columns=["StudyHours", "Attendance", "Sleep"]
        )

        marks = model.predict(input_df)[0]
        prediction = round(marks, 2)
        status = "PASS" if marks >= 40 else "FAIL"

    return render_template(
        "index.html",
        prediction=prediction,
        status=status
    )

if __name__ == "__main__":
    app.run(debug=True)
