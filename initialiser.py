# main smokeager module
import os
import sys
import sqlite3

class SmokeagerFreshInit():
	"""
	Fresh Initialisation of smokeager system 
	"""

	def __init__(self):		
		self.__home_dir = self.get_home_dir()
		self.__smokeager_home_dir = self.get_smokeager_home_dir()
		#print(self.__home_dir, self.__smokeager_home_dir)

	def __create_smokeager_home_dir(self):
		""" create smokeager home directory """
		
		__smokeager_home_dir = self.__smokeager_home_dir
		if not os.path.exists(__smokeager_home_dir):
			print("Creating smokeager home directory!")
			os.makedirs(__smokeager_home_dir)
		else:
			#print("Seems like smokeager is already present!")
			pass

	@classmethod
	def get_home_dir(self):
		""" returns user's home directory path """
		try:
			home_dir = os.path.expanduser("~")
		except Exception as e:
			print("Couldn't get home directory! :(")
			print(e)
			sys.exit(1)
		else:
			return home_dir

	@classmethod
	def get_smokeager_home_dir(self):
		return os.path.join(self.get_home_dir(), ".smokeager")

	def __create_db_file(self):
		__smokeager_home_dir = self.__smokeager_home_dir
		__db_file_path = os.path.join(__smokeager_home_dir,"smokeagerDB.db")
		if not os.path.exists(__db_file_path):
			__db_file = open(__db_file_path, "wb")
			print("Created db file: %s" %__db_file)
			__db_file.close()
		else:
			__db_file = open(__db_file_path, "rb")
			#print("DB file already exists: %s" %__db_file)
			__db_file.close()

	@classmethod
	def get_db_file(self):
		""" returns db file path """

		__db_file_path = os.path.join(self.get_smokeager_home_dir(),"smokeagerDB.db")
		if os.path.exists(__db_file_path):
			return __db_file_path
		else:
			print("DB file does not exist! Please re-initialise smokeager!")
			sys.exit(1)	

	def fresh_init(self):
		""" fresh initialisation of smokeager """
		self.__create_smokeager_home_dir()
		self.__create_db_file()
		smokeagerDB = SmokeagerDB()
		smokeagerDB.test_db_conn()


class SmokeagerDB():
	""" handles all connection related activities to smokeager db """

	def __init__(self):
		self.__db_file_path = SmokeagerFreshInit.get_db_file()
		self.__conn = None

	def __connect_db(self):
		""" connects to db and sets self.__conn to conn object """

		__db = SqliteDatabase(self.__db_file_path)
		try:
			conn = __db.connect()
			self.__conn = conn
			print("Smokeager DB connected: %s" %conn)
		except Exception as e:
			print(e)
			sys.exit(1)

	def __close_db_connection(self):
		""" closes db connection using __conn obj set in class """

		if self.__conn:
			self.__conn.close()
			print("DB connection closed")
			self.__conn = None

	def get_db_conn(self):
		""" public method for getting db conn obj """
		if self.__conn:
			return self.__conn
		else:
			print("DB not connected!")	

	def close_db_conn(self):
		""" public method for closing db conn """
		self.__close_db_connection()

	def test_db_conn(self):
		self.__connect_db()
		self.__close_db_connection()

def init():
	s = SmokeagerFreshInit()
	s.fresh_init()

if __name__ == "__main__":
	init()




