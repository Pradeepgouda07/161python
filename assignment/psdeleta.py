#permanent delete
import os
for filename in os.listdir():
 if filename.endswith('.rxt'):
 os.unlink(filename)

#safe delete
import send2trash
baconFile = open('bacon.txt', 'a') # creates the file
baconFile.write('Bacon is not a vegetable'.)
