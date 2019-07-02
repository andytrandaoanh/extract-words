import os, sys
import mysql.connector
from mysql.connector import errorcode

def get_connection(dbname=''):
	try:
		connection = mysql.connector.connect(
		user='andyanh', password='DGandyanh#1234',
	    host='127.0.0.1', database = dbname)
		if connection.is_connected():
			return connection 
	except Error as e:
		return e

def insert_data_to_database(myData, cursor, db):

	mySql = ("INSERT INTO lexicon.sentences "
	           "(book_id, sent_content, sent_num, date_entered)"
	           "VALUES (%s, %s, %s, NOW())")

	cursor.execute(mySql, myData)
	db.commit()


def prepare_data_for_update(dbData):

	DB_NAME = "lexicon"
	db = get_connection(DB_NAME)

	cursor = db.cursor()
	sentence_index = 0
	sentence_total = len(dbData)

	for myData in dbData:
		sentence_index += 1
		#print(row) 
		print('upload sentence no: ', sentence_index)
		insert_data_to_database(myData, cursor, db)
		#print(myData)
	print('upload completed, total sentences: ', sentence_total)
	cursor.close()
	db.close()
	sys.exit()
