from flask import Flask, request, render_template, jsonify
from generator import generate_diet_plan

app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/generate', methods=['POST'])
def generate():
    data = dict(request.form)

    weight = int(data["weight"])
    height = int(data["height"])
    meals = int(data["meals"])
    gender = data["gender"]
    age = int(data.get("age", 25))
    activity_level = float(data["activitylevel"])

    plan = generate_diet_plan(
        meals=meals,
        gender=gender,
        age=age,
        weight=weight,
        height=height,
        activity_level=activity_level,
    )
    return plan


if __name__ == '__main__':
    app.run(debug=True)
