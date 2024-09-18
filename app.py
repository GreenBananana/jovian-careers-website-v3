from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db
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

@app.route("/job/<id>") #dynamic route.
def show_job(id):
  job = load_job_from_db(id)
  if job:  
    return render_template('jobpage.html', job=job)
  else:
    return "Job not found", 404

@app.rote("/job/<id>/apply")
def apply_to_job(id):
  job = load_job_from_db(id)
  
    
if __name__ == "__main__":
  app.run(host ='0.0.0.0', debug = True)