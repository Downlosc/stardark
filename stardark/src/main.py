import argparse 
import checker as _ch
import utils as _utils
import namespace as _syms

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--month', help='to specify a month')
parser.add_argument('-y', '--year', help='to specify a year')
args = parser.parse_args()

def main(): 
  checker = _ch.Checker()
  year  = args.year
  month = args.month
  if year and not month: 
    print('Please, specify a month')
    return 

  if month: 
    try: 
      assert month in _syms.MONTHS
    except:
      print('Month must be an integer between 1 and 12')
      return 
    if year: sdate = _utils.get_starting_date(month, year)
    else: sdate = _utils.get_starting_date(month)
    checker.set_start_date(sdate)

  checker.check()

if __name__=="__main__": 
  main()



