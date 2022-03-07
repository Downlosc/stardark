import settings as _sets
import psycopg2
from psycopg2 import extras

def connect():
  try:
    conn = psycopg2.connect(dbname = _sets.DB_NAME, user=_sets.DB_USER, host=_sets.DB_HOST)
    return conn
  except: print('Wrong settings, unable to connect')

def get_cursor(conn): 
  if not conn: return 
  cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
  return cursor




  
