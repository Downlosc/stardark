Python version: Python 3.9.7
Db Version: postgres (PostgreSQL) 13.4

Modules: 
 - psycopg2 : 2.9.2

Running instructions: python3 main.py

----------------------------------------+

Assumptions:
 - the system performs automatically expenditures updating. 
   Even though this was taken as an assumption, a small aggregating algorithm has been 
   written so that if two records of the same shop are present in the database 
   expenditures would be the sum of all the expenditures and the budget would be the 
   sum of budgets.
   
   Although API's have been written to switch between "online" and "offline" and "notified" 
   and "unnotified" just some of them are actually used in the app: mark as offline (where necessary) 
   and mark as notified (where necessary).

   I also assumed that the system is virgin so as a starting point all the shops where marked 
   as online and not notified.

   To avoid that the systems both notifies the threshold limit and the account suspention 
   a copy of the data has been kept in RAM and the necessary updates are made both in 
   the db and the ram data structures. 

1. The solution provided avoids sending duplicate notifications by the usage of a "a_notified" boolean column
   in the t_shops table. 
2. An api has been developed in the "api.py" module that allows the system to set ad not notified a shop 
   everytime the system updates the budget. 


Extra thoughts: 

Database was populated with data related to november. Another feature has been developed.

main.py it's also runnable using some additional arguments: 
  1. -m to specify months (01 - 12 format)
  2. -y to specify a year

DOING SO WILL INVALIDATE FUTURE RESULTS (see assumptions and point 2) 

