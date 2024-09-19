from sqlalchemy import create_engine, text
import os #needed for secrets

db_connection_string = os.environ['DB_CONNECTION_STRING'] # don't share this!!!! Make a secret or env variable

engine = create_engine(db_connection_string,pool_use_lifo=True, pool_pre_ping=True) #ssl certificate may be required with different db providers.

with engine.connect() as connection:
  result = connection.execute(text("select * from jobs"))

  result_dicts = []
  for row in result.all():
    result_dicts.append(row._asdict())

def load_jobs_from_db():
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

def load_job_from_db(id):
  with engine.connect() as connection:
  
    result = connection.execute(text(f"select * from jobs where id = {id}"))
    row = result.fetchone()
    if row:
      return row._asdict()
    else:
      return None

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
      query = text(
          "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
      )
      try:
          conn.execute(
              query,
              {
                  "job_id": job_id,
                  "full_name": data["full_name"],
                  "email": data["email"],
                  "linkedin_url": data["linkedin_url"],
                  "education": data["education"],
                  "work_experience": data["work_experience"],
                  "resume_url": data["resume_url"],
              },
          )
          conn.commit()
      except Exception as e:
          print(f"Error adding application: {e}")
          return "Failed to submit application", 500

