from artDatabase import Artist
from artDatabase import Artwork
from dbQueries import *
#from artworkCatalogMenu import showMenu as Menu #Circular issue? but then how do you call the menu back?


#----Functions

def addNewArtist():
	name = input('Enter artist name: ').lower()
	email = input('Enter artist email: ').lower()

	addArtistQuery(name, email)
	#pass true to main to run menu again
	start = True
	return start

def searchByArtist():
	artistName = input('Enter artist name: ').lower()
	artistLookup = lookUpArtworkByArtist(artistName)

	for artist in artistLookup.tuples():
		print(artist)

	start = True
	return start

def forSaleByArtist():
	artistName = input('Enter artist name: ').lower()
	artByArtist = artistArtForSale(artistName)
	for artist in artByArtist.tuples():
		print(artist)

	start = True
	return start

def addNewArtwork():
	artist = input('Enter Artist ID: ')
	#verify artist is in DB
	artwork = input('Enter Artwork Title: ')
	price = float(input('Enter Price: $'))
	#popout into seperate function?
	sold = getSoldInput()
	#put in query module
	artworkAddSuccsess = addArtworkQuery(artist, artwork, price, sold)
	
	start = True
	return start

def deleteArtwork():
	artworkName = input("Which piece of art \nwould you like to delete?")
	deleteArt(artworkName)
	#run query to find and remove artwork
	start = True
	return start
	
def changeAvailability():
	artwork = input("What peice of art would you like to updae? ")
	sold = getSoldInput()
	if sold == 't':
		sold = True
	elif sold == 'f':
		sold = False
	updateAvailability(artwork, sold)
	#update artwork
	start = True
	return start

def getSoldInput():
	ask = True;
	while ask == True:
		soldInput = input('Artwork is for sale? T or F').lower()
		if soldInput == 't':
			sold = bool(soldInput)
			ask = False
		elif soldInput == 'f':
			sold = bool('')
			ask = False
		else:
			print('Please input T or F')
			ask = True
	return sold