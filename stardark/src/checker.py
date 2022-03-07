from datetime import date
import api as _api
import utils as _utils
import communication as _com

def _parseResults(res): 
  l = []
  for r in  res: 
    d = {}
    ddate    = r['a_month']
    budget   = r['a_budget_amount']
    spent    = r['a_amount_spent']
    notified = r['a_notified']
    name     = r['a_name']
    aid      = r['a_id']
    online   = r['a_online']

    strdate  = ddate.strftime('%Y-%m-%d')
    budget   = float(budget)
    spent    = float(spent)

    d['month']    = strdate
    d['budget']   = budget
    d['spent']    = spent
    d['notified'] = notified
    d['id']       = aid
    d['name']     = name
    d['online']   = online

    l.append( d )

  return l

class Checker(): 

  start_date = None
  notifications = {}
  shot = None

  def set_start_date(self, sdate): 
    self.start_date = sdate

  def get_start_date(self):
    if not self.start_date: 
      today = date.today()
      self.set_start_date(today)
    return self.start_date

  def analyze_exp(self): 
    today = date.today()
    sdate = today.strftime('%Y-%m-%d')
    
    for aid in self.shot: 
      name = self.shot[aid]['name']
      budget  = self.shot[aid]['budget']
      spent   = self.shot[aid]['spent']
      percent = round((spent * 100.00) / budget, 2)
      per     = '%d' % percent
      per += '%'

      if self.shot[aid]['budget'] <= self.shot[aid]['spent'] and self.shot[aid]['online']: 
        _api.set_shop_offline(aid)
        self.shot[aid]['online'] = False
        _com.notify_user_offline(name, budget, sdate)

      if self.shot[aid]['spent'] >= (self.shot[aid]['budget'] / 2) and not self.shot[aid]['notified'] and self.shot[aid]['online']:
        _api.set_shop_notified(aid)
        self.shot[aid]['notified'] = True
        _com.notify_user_half(name, sdate, budget, per, spent)

    return


  def aggregate_exp(self, data):
    d = {}
    for elem in data: 
      c = {}
      c['month']    = elem['month']
      c['budget']   = elem['budget']
      c['spent']    = elem['spent']
      c['notified'] = elem['notified']
      c['name']     = elem['name']
      c['online']   = elem['online']
      aid = elem['id']

      if aid not in d: d[aid] = c
      else: 
        d[aid]['budget'] += c['budget']
        d[aid]['spent']  += c['spent']
        d[aid]['month']  += c['month']

    return d

  def check(self): 
    curdate = self.get_start_date()
    dates = _utils.parse_dates(curdate)
    res   = _api.get_budgets_by_month(dates)
    data  = _parseResults(res)
    data  = self.aggregate_exp(data)
    self.shot = data
    data  = self.analyze_exp()
    
    return 
