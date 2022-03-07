import namespace as _syms
from datetime import date

def get_starting_date(month, year=None): 
  if year: cyear = year
  else:
    today = date.today()
    cyear = today.year()

  sdate = '%s-%s-01' % (cyear, month)
  sdate = date.fromisoformat(sdate)
  return sdate



def parse_dates(today): 
  month = today.month
  year  = today.year

  next_month = month + 1
  next_year  = year

  if month == _syms.DECEMBER: 
    next_month  = _syms.JANUARY
    next_year = year + 1

  dfrom = '%s-%s-01' % (year, month)
  dto   = '%s-%s-01' % (next_year, next_month)

  d = {
      'dfrom': dfrom,
      'dto'  : dto,
    }

  return d


