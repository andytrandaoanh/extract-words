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

def formatBookInfo(record, description):
#((1, 'The First-Time Manager', 'Loren B. Belke', 2012), [('book_id', 3, None, None, None, None, 0, 53251), ('book_title', 253, None, None, None, None, 1, 0), ('book_author', 253, None, None, None, None, 1, 0), ('book_year', 2, None, None, None, None, 1, 32768)])
		#expression for item in list
	field_names  = [item[0] for item in description]

	book_info = {}

	index = 0

	for field in field_names:
		book_info[field] = record[index]
		index += 1

	return book_info

def getBookData(book_id):
	DB_NAME = "lexicon"
	db = get_connection(DB_NAME)
	cursor = db.cursor()
	select_sql= ("select * from books where book_id = " + str(book_id) +";")
	try:
		cursor.execute(select_sql)
		record = cursor.fetchone()
		return formatBookInfo(record, cursor.description)
	except Exception as e:
		print("Error encountered:", e)
	finally:
		cursor.close
		db.close

def formatWordList(records):
	wordList = []
	for word in records:
		wordList.append(word[0])	
	return wordList

def getWordList():
	DB_NAME = "lexicon"
	db = get_connection(DB_NAME)
	cursor = db.cursor()
	select_sql= ("select word_form from pure_words order by 1;")
	try:
		cursor.execute(select_sql)
		records = cursor.fetchall()
		return formatWordList(records)
	except Exception as e:
		print("Error encountered:", e)
	finally:
		cursor.close
		db.close

def formatSentences(records, description):
	field_names  = [item[0] for item in description]
	sentences = []
	for record in records:
		sentences.append((record[0],record[1]))
	return sentences

def getSentences(book_id):
	DB_NAME = "lexicon"
	db = get_connection(DB_NAME)
	cursor = db.cursor()
	select_sql= ("select  sent_content, sent_num from sentences where book_id  = " + str(book_id) +";")
	try:
		cursor.execute(select_sql)
		records = cursor.fetchall()
		return formatSentences(records, cursor.description)
	except Exception as e:
		print("Error encountered:", e)
	finally:
		cursor.close
		db.close

