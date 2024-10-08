from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
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

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form #if in url then use request.args
  job = load_job_from_db(id)

  add_application_to_db(id, data)
  #store this in db
  #send an email
  #display an acknowledgement
  return render_template('application_submitted.html',
                         application=data,
                         job=job)
  
  
    
if __name__ == "__main__":
  app.run(host ='0.0.0.0', debug = True)