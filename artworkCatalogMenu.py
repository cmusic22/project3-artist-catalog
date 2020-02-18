from artFunctions import * 	
from sys import exit
# menu
def showMenu():
	print('1. Add New Artist')
	print('2. Search All Artwork by Artist')
	print('3. Display All For Sale by Artist')
	print('4. Add New Artwork')
	print('5. Delete Artwork')
	print('6. Change Availability')
	print('7. Quit')

	choice = int(input('Enter Choice: '))

	if choice == 1:
		addNewArtist()
	elif choice == 2:
		searchByArtist()
	elif choice == 3:
		forSaleByArtist()
	elif choice == 4:
		addNewArtwork()
	elif choice == 5:
		deleteArtwork()
	elif choice == 6:
		changeAvailability()
	elif choice == 7:
		raise SystemExit()
	else:
		print('Invalid Selection')
		showMenu()