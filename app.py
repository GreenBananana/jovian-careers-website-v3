from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
from sqlalchemy import text

app = Flask(__name__)



@app.route("/")
def hello_jovian():
  jobs = load_jobs_from_db()
  return render_template('home.html',
                        jobs=jobs) # first jobs is name used later, second jobs is the variable inside this method.

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host ='0.0.0.0', debug = True)