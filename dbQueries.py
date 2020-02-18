import artFunctions
from artDatabase import Artist
from artDatabase import Artwork

def addArtistQuery(name, email):
	artistEntry = Artist(name = name, email = email)
	artistEntry.save()
	print('Artist Added!')

def lookUpArtworkByArtist(artistName):

	query = Artwork.select(Artwork).join(Artist).where(Artist.name == artistName)
	return 	query

def artistArtForSale(artistName):

	query = Artwork.select(Artwork).join(Artist).where(Artwork.sold == True).where(Artist.name == artistName)
	return query

def addArtworkQuery(artist, artwork, price, sold):
	artworkEntry = Artwork(artist = artist, artwork = artwork, price = price, sold = sold)
	artworkEntry.save()
	print('Artwork Added!')

def deleteArt(artworkName):
	deleteQuery = Artwork.delete().where(Artwork.artwork == artworkName)
	deleteQuery.execute()
	print(artworkName + ' was deleted.')

def updateAvailability(artwork, sold):
	query = Artwork.update({Artwork.sold: sold}).where(Artwork.artwork == artwork)
	query.execute()
	print('Query has been updated.')
	return query
