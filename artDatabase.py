from peewee import *

#create database
db = SqliteDatabase('artist.sqlite', pragmas={'foreign_keys': 1});


class Artist(Model):
	name = CharField()
	email = CharField()

	class Meta:
		database = db

	def __str__(self):
		return f'{self.name} emal address is {self.email}'

class Artwork(Model):
	artist = ForeignKeyField(Artist)#need to pass id from
	artwork = CharField(unique = True) #needs to be unique
	price = DecimalField() #found on docs.peewee-orm.com
	sold = BooleanField(default = True) #presume the peice of artwork is for sale until sold

	class Meta:
		database = db

	def __str__(self):
		return f'{self.artist} created {self.artwork} and is {self.sold} for {self.price}'

#connect to databases & create databases
db.connect()
#db.pragma('foreign_keys', 1, permanent=True)#run param to allow foreign keys
db.create_tables([Artist, Artwork])
