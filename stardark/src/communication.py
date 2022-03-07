
def notify_user_half(usr, date, budget, percent, spent):
  budget = str(budget)
  spent = str(spent)
  print("""
            Dear %s, 
            We want to commuincate that on %s you have already spent  %s
            of your monthly budget (%s) [roughly %s of your total budget].
            We also wanted to let you know that if your monthly spending 
            reaches the limit set by your budget, your account will be suspended. 
            To prevent this from happening, we invite you to renew your monthly budget.
            

            Kindly, 
            Stardark team. 

            """ % (usr, date, spent, budget, percent))
  return

def notify_user_offline(usr, budget, date):
  print ("""
            Dear %s, 
            This email is used to notify you that your account has been suspended 
            on %s for having reached the maximum spending set by your budget.
            We wanted to remind you that you can set a new budget for this month 
            or wait for the next automatic renewal next month. 

            Kindly, 
            Stardark team. 

          """ % (usr, date))
  return
