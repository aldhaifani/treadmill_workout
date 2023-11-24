from flask import Flask, render_template
import openpyxl


app = Flask(__name__)
app.secret_key = "HdraYnfHEiTKsR3kFJbfnMdLAfUYGiew"

wb = openpyxl.load_workbook("./static/data_sheets/treadmill_workout.xlsx")
ws = wb.active

data_obj = [
    {
        "label": ws.cell(row=row, column=1).value,
        "time": ws.cell(row=row, column=2).value,
        "incline": ws.cell(row=row, column=3).value,
        "speed": ws.cell(row=row, column=4).value,
    }
    for row in range(2, ws.max_row + 1)
]


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
