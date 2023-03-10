from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Toronto, Ontario',
  'salary': '$90,000'
}, {
  'id': 2,
  'title': 'Data Engineer',
  'location': 'Toronto, Ontario'
}, {
  'id': 3,
  'title': 'Business Analyst',
  'location': 'Calgary, Alberta',
  'salary': '$75,000'
}]


@app.route("/")
def hello_otto():
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
