from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bengluru",
        "Salary": 100000
    },
{
        "id": 2,
        "title": "Data Scientist",
        "location": "Delhi",
        "Salary": 150000
    },
{
        "id": 3,
        "title": "Frontend Engineer",
        "location": "Remote",
    },
{
        "id": 4,
        "title": "Backend Engineer",
        "location": "San Fransisco",
        "Salary": 120000
    }
]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
