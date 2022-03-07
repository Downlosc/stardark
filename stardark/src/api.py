import psycopg2
import connection as _c

def get_all_budgets(): 
  con = _c.connect()
  q   = 'select * from t_budgets';
  cur = _c.get_cursor(con)
  try:
    cur.execute(q)
  except: print("oops. Something went wrong when trying to ready all budgets")
  try:
    res = cur.fetchall()
  except: res = []
  con.close()
  return res


def get_all_shops(): 
  con = _c.connect()
  q   = 'select * from t_shops';
  cur = _c.get_cursor(con)
  try:
    cur.execute(q)
  except: print("oops. Something went wrong when trying to ready all shops")

  try:
    res = cur.fetchall()
  except: res = []

  con.close()
  return res


def get_budgets_by_month(dates):
  dfrom = dates.get('dfrom') or None
  dto   = dates.get('dto') or None
  assert dfrom and dto

  q =  ' select bud.a_month, bud.a_budget_amount, bud.a_amount_spent, sho.a_name, sho.a_online, sho.a_id, sho.a_notified '
  q += ' from t_budgets as bud join t_shops as sho on bud.a_shop_id = sho.a_id '
  q += ' where a_month >= %(dfrom)s::date and a_month < %(dto)s::date' 

  con = _c.connect()
  cur = _c.get_cursor(con)
  try: cur.execute(q, {'dfrom': dfrom, 'dto': dto})
  except: print("oops. Something went wrong when trying to fetch range dates")

  try: res = cur.fetchall()
  except: res = []

  con.close()
  return res

def set_shop_offline(sid): 
  q = "update t_shops set a_online = '0' where a_id = %d" % sid
  con = _c.connect()
  cur = _c.get_cursor(con)
  try: cur.execute(q)
  except: print("oops. Something went wrong when setting the shop offline")
  con.commit()
  con.close()
  return 


def set_shop_online(sid): 
  q = "update t_shops set a_online = 't' where a_id = %d" % sid
  con = _c.connect()
  cur = _c.get_cursor(con)
  try: cur.execute(q)
  except: print("oops. Something went wrong when setting the shop online")
  con.commit()
  con.close()

  return

def set_shop_notified(sid): 
  q = "update t_shops set a_notified = '1' where a_id = %d" % sid
  con = _c.connect()
  cur = _c.get_cursor(con)
  try: cur.execute(q)
  except: print("oops. Something went wrong when setting the shop notified")
  con.commit()
  con.close()

def set_shop_unnotified(sid): 
  q = "update t_shops set a_notified = '0' where a_id = %d" % sid
  con = _c.connect()
  cur = _c.get_cursor(con)
  try: cur.execute(q)
  except: print("oops. Something went wrong when setting the shop unnotified")
  con.commit()
  con.close()
