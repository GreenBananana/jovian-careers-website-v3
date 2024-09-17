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



