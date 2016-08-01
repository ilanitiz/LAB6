#LAB6 Python starter code
#imports go here
#import MySQLdb
import _mysql

#code goes here

buffer = "true"

def oneQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="Aaaaaa1!",db="beer")
	db.query("""SELECT * FROM beer;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def twoQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="Aaaaaa1!",db="beer")
	db.query("""SELECT * FROM future;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def threeQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="Aaaaaa1!",db="beer")
	#db.query("""SELECT * FROM brewery WHERE breweryID NOT IN (SELECT * FROM brewery as a, funding AS b WHERE  
	#	a.breweryID = b.breweryID;)""")
	db.query("""SELECT breweryID FROM brewery WHERE breweryID not in (select breweryID from funding)""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	if nR == 0:
		print("""all breweries have at least 1 future contract""")
	db.close()
	
while buffer:
	print("""
	0.Exit
	1.See beers
	2.See futures
	3.See if a brewery has no futures contracts
	""")
	buffer=input("what would you like to do? ")
	if buffer == 1:
		oneQuery()
	if buffer == 2:
		twoQuery()
	if buffer == 3:
		threeQuery()