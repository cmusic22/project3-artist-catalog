from unittest import TestCase
from unittest.mock import patch, MagicMock
from dbQueries import *


class TestStudentLists(TestCase):

	def test_add_artest_query(self):
		test_artistCatalog#initiate test db
		name = 'Test Name'
		email = 'Test'
		test_artistCatalog.addArtistQuery(name, email)
		self.assertIn(name, test_artistCatalog.artist)

	def test_add_artwork_query(self):
		test_artistCatalog#initiate test db
		#Add artist
		name = 'Test Name'
		email = 'Test'
		test_artistCatalog.addArtistQuery(name, email)
		#Add artwork
		artist = 1
		artwork = 'fun'
		price = 23.45
		sold = True
		test_artistCatalog.addArtworkQuery(artist, artwork, price, sold)
		###########
		artist2 = 1
		artwork2 = 'supa fun'
		price2 = 23.55
		sold2 = False
		test_artistCatalog.addArtworkQuery(artist2, artwork2, price2, sold2)
		self.assertIn(artist, test_artistCatalog)



	def test_look_Up_Artwork_By_Artist(self):
		test_artistCatalog#initiate test db
		#Add artist
		name = 'Test Name'
		email = 'Test'
		test_artistCatalog.addArtistQuery(name, email)
		#Add artwork
		artist = 1
		artwork = 'fun'
		price = 23.45
		sold = True
		test_artistCatalog.addArtworkQuery(artist, artwork, price, sold)
		###########
		artist2 = 1
		artwork2 = 'supa fun'
		price2 = 23.55
		sold2 = False
		test_artistCatalog.addArtworkQuery(artist2, artwork2, price2, sold2)
		#Test lookup
		test_artistCatalog.lookUpArtworkByArtist(name)
		self.assertIn(artist, test_artistCatalog)


	def test_artist_art_for_sale(self):
		test_artistCatalog#initiate test db
		#Add artist
		name = 'Test Name'
		email = 'Test'
		test_artistCatalog.addArtistQuery(name, email)
		#Add artwork
		artist = 1
		artwork = 'fun'
		price = 23.45
		sold = True
		test_artistCatalog.addArtworkQuery(artist, artwork, price, sold)
		###########
		artist2 = 1
		artwork2 = 'supa fun'
		price2 = 23.55
		sold2 = False
		test_artistCatalog.addArtworkQuery(artist2, artwork2, price2, sold2)
		test_artistCatalog.artistArtForSale(artist)
		#assertIn(artist, test_artistCatalog)
		test_artistCatalog.artistArtForSale(artist2)
		self.assertNotIn(artist2, test_artistCatalog)

	def test_delete_Art(self):
		test_artistCatalog#initiate test db
		#Add artist
		name = 'Test Name'
		email = 'Test'
		test_artistCatalog.addArtistQuery(name, email)
		###############
		#Add art
		artist = 1
		artwork = 'fun'
		price = 23.45
		sold = True
		test_artistCatalog.addArtworkQuery(artist, artwork, price, sold)
		###########
		artist2 = 1
		artwork2 = 'supa fun'
		price2 = 23.55
		sold2 = False
		test_artistCatalog.addArtworkQuery(artist2, artwork2, price2, sold2)
		test_artistCatalog.deleteArt(artwork)
		self.assertNotIn(artwork, test_arttistCatalog)

	def test_update_availablility(self):
		test_artistCatalog#initiate test db
		#Add artist
		name = 'Test Name'
		email = 'Test'
		test_artistCatalog.addArtistQuery(name, email)
		###############
		#Add art
		artist = 1
		artwork = 'fun'
		price = 23.45
		sold = True
		test_artistCatalog.addArtworkQuery(artist, artwork, price, sold)
		###########
		artist2 = 1
		artwork2 = 'supa fun'
		price2 = 23.55
		sold2 = False
		test_artistCatalog.addArtworkQuery(artist2, artwork2, price2, sold2)
		sold = True
		test_artistCatalog.updateAvailability(artist2, sold, test_artistCatalog)
		#self.assertNotIn(artwork)



	



	
