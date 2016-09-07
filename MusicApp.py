##################################
#    Marcus Daniel McFarlane     #
#    Student ID: 200912969       #
#    BSc Information Technology  #
#    University of Leeds         #
#                                #
##################################


#------------------- Imports 

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QTextEdit
from PyQt5.QtWidgets import QLineEdit, QSpinBox, QLineEdit, QSpinBox, QPushButton, QComboBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QMessageBox

import csv
import sqlite3


"""A GUI for a simple application that records details of the user's music
collection, storing the album details into a database.

@author Marcus McFarlane
"""
class MusicApp(QWidget):

    #--------------- Constructor/Initialiser
	#- Initializing an instance of a class or an object.
	#- The constructor contains classes or methods that will be run immediately when teh fiel is executed.
    def __init__(self):
        super().__init__()
        self.createWidgets()
        self.arrangeWidgets()
        self.makeConnections()
                
    #--------------- Methods
    
    
    """Creates the widgets and objects used for the GUI.
	
	"""
    def createWidgets(self):

		#_ Database
		# Creating a 'Connection' object that represents the database, which stores the data in
		# the music_app.db file.
        self.conn = sqlite3.connect('music_app.db')

        # Cursor object for the database, used to fetch the rsults. 
        self.curs = self.conn.cursor()     
        
        # Calling the execute method on the cursor object to perform sql commands.
		# I have already created the required table in the database!
        #self.curs.execute('''CREATE TABLE AlbumDetails(AlbumTitle TEXT, Artist TEXT)''')         
			
			
        #- Labels
        self.labelAlbumTitle = QLabel("Album Title:")
        self.labelAlbumTitle.setAlignment(Qt.AlignRight)

        self.labelArtist = QLabel("Artist:")
        self.labelArtist.setAlignment(Qt.AlignRight)

        self.labelSpinYear = QLabel("Year:")
        self.labelSpinYear.setAlignment(Qt.AlignRight)

        self.labelGenre = QLabel("Genre:")
        self.labelGenre.setAlignment(Qt.AlignRight)

        self.labelFormat = QLabel("Format:")
        self.labelFormat.setAlignment(Qt.AlignRight)
        self.labelNotes = QLabel("Notes")

		
        #- Single line input box
        self.sInputAlbumTitle = QLineEdit()
        self.sInputAlbumTitle.setText("Love, Fear And The Time Machine")
		
        self.sInputArtist = QLineEdit()
        self.sInputArtist.setText("Riverside")

		
        #- Multiple line input box
        self.mInputNotes = QTextEdit()
        self.mInputNotes.setText("Two-Disc special edition")


        #- Spin box
        self.dSpinYear = QSpinBox()
        self.dSpinYear.setRange(1950, 2015)
        self.dSpinYear.setSingleStep(1)
        self.dSpinYear.setValue(2015)
                

        #- Radio buttons
        self.radBtnLP = QRadioButton("LP")
        self.radBtnCD = QRadioButton("CD")
        self.radBtnMP3 = QRadioButton("MP3")
        self.radBtnFLAC = QRadioButton("FLAC")
   
        self.radBtnCD.setChecked(True)

		
        #- Combo box
        self.comBoxGenre = QComboBox() 
        self.comBoxGenre.addItem("Prog Rock")
        self.comBoxGenre.addItem("Indie")
        self.comBoxGenre.addItem("R&B")
        self.comBoxGenre.addItem("Dance")
        self.comBoxGenre.addItem("House")
        self.comBoxGenre.addItem("Hip Hop")
        self.comBoxGenre.addItem("Reggie")
        self.comBoxGenre.addItem("Club Hits")
        self.comBoxGenre.addItem("Club Classics")
   
   
        #---------- Buttons

        #- Add Album button
        self.btnAddAlbum = QPushButton("Add Album")
        
        #- Cancel button
        self.btnCancel = QPushButton("Cancel")
    
    """Creates the layouts, adding the widgets to the appropriate layouts.
	
	"""
    def arrangeWidgets(self):
        
        #------------ Layouts
		
        #- Grid Layout

        # Positioning of the widgets is set according to (row, col, rowspan, colspan).

        gridLayout = QGridLayout()

        gridLayout.addWidget(self.labelAlbumTitle, 0, 0)
        gridLayout.addWidget(self.sInputAlbumTitle, 0, 1, 1, 4)
        gridLayout.addWidget(self.labelArtist, 1, 0)
        gridLayout.addWidget(self.sInputArtist, 1, 1, 1, 4)
        gridLayout.addWidget(self.labelSpinYear, 2, 0)
        gridLayout.addWidget(self.dSpinYear, 2, 1)
        gridLayout.addWidget(self.labelGenre, 2, 2.5)
        gridLayout.addWidget(self.comBoxGenre, 2, 3, 1, 2)
        gridLayout.addWidget(self.labelFormat, 3, 0)
        gridLayout.addWidget(self.radBtnLP, 3, 1)
        gridLayout.addWidget(self.radBtnCD, 3, 2)
        gridLayout.addWidget(self.radBtnMP3, 3, 3)
        gridLayout.addWidget(self.radBtnFLAC, 3, 4)
        gridLayout.addWidget(self.labelNotes, 4, 0)
        gridLayout.addWidget(self.mInputNotes, 5, 0, 1, 5)


        #- Button layout 1
        btnLayout1 = QVBoxLayout()
        btnLayout1.addWidget(self.btnAddAlbum)
        btnLayout1.setAlignment(Qt.AlignRight)

		
        #- Button layout 2
        btnLayout2 = QVBoxLayout()
        btnLayout2.addWidget(self.btnCancel)
        btnLayout2.setAlignment(Qt.AlignLeft)


        #- Button 1 and 2 container
        btnsContainer = QHBoxLayout()
        btnsContainer.addLayout(btnLayout1)
        btnsContainer.addLayout(btnLayout2)


        #- Main Layout		
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(gridLayout)
        mainLayout.addLayout(btnsContainer)
        
		
        # Required to use self.setLayout(mainLayout) to set the layout to be 
        # used for the class.
        self.setLayout(mainLayout)

        
        
    #- Method used to make the connections and perform the behaviours for the widgets.
	# 
	# Uses the custom slot method named 'btnInt' which executes multiple behaviours:
	# 'self.btnAddAlbum.clicked.connect(self.btnInt)'
	#
	
    """Making a connnection Signal and Slot for the 'Add Album' button and the 'Cancel' button.
		
	"""
    def makeConnections(self):
        
        self.btnAddAlbum.clicked.connect(self.btnInt)
            
        self.btnCancel.clicked.connect(app.quit)

    """Makinng a custom slot for the 'Add Album' button connection that performs multiple 
	behaviours in one slot.
	
	"""    
    @pyqtSlot()
    def btnInt(self):
        
		# Using an if statement to execute code depending on the condition if
		# the 'sInputAlbumTitle' widget is empty or containing text.		
        if self.sInputAlbumTitle.text()=="":    
            
			# Displays QMesageBox			
            messageBoxValid = QMessageBox()
            messageBoxValid.setIcon(QMessageBox.Information)
            messageBoxValid.setText("Error: Album Title and/or Artist has been left blank.")
            messageBoxValid.setStandardButtons(QMessageBox.Ok)
            messageBoxValid.exec_()
			
            self.dSpinYear.setValue(2012)
			            
			# Clears the relevant input boxes.
            self.sInputAlbumTitle.clear()
            self.sInputArtist.clear()
            self.mInputNotes.clear()
        
        else:
            messageBoxInvalid = QMessageBox()
            messageBoxInvalid.setIcon(QMessageBox.Information)
            messageBoxInvalid.setText("Thank You")
            messageBoxInvalid.setStandardButtons(QMessageBox.Ok)
            messageBoxInvalid.exec_()
			
            self.dSpinYear.setValue(2012)

#			 #Execute method to write Album Details to scv file.			
#            self.on_pushButtonWrite_clicked()
                               
            AlbumTitle = self.sInputAlbumTitle.text()
            Artist = self.sInputArtist.text()
				
            # Calling the execute method, inserting a row of data into the database.			
			# I used '?' to represent a parameter in SQL, and set the variable name to be
			# the same name as the attribute name.
            self.curs.execute("INSERT INTO AlbumDetails(AlbumTitle, Artist) VALUES(?, ?)", (AlbumTitle, Artist))
		
            # Saving the changes made to the database.
            self.conn.commit()
            
            self.sInputAlbumTitle.clear()
            self.sInputArtist.clear()
            self.mInputNotes.clear()
                    
        self.dSpinYear.setValue(2015)
        
        self.radBtnCD.setChecked(True)

        # I set the current index by finding the specified text, which displayed my text.
        self.comBoxGenre.setCurrentIndex(self.comBoxGenre.findText("House"))

        
    
#    """Writes the album detais to a csv file.
#	
#	"""
#    def writeCsv(self, filename):
#        
#        # opening the file with the 'a' parameter allows appending to the end of the file
#        # instead of using the 'w' parameter to write a new file.
#        with open(filename, "a") as file:
#            writer = csv.writer(file)
#            
#            listWidgets = [self.sInputAlbumTitle.text(), self.sInputArtist.text()]
#
#            writer.writerow(listWidgets)
#
#    """Create a particular named csv file.
#	
#	"""
#    def on_pushButtonWrite_clicked(self):
#        self.writeCsv("test.txt")
        
        
        
#------------------- Main Method

"""Displays a window on the screen with the included contents.

"""
if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)

    #--------- Display window (GUI)
    
    window = MusicApp()
    
    window.setWindowTitle("Album  Database")

    window.setMaximumHeight(500)
    window.setMaximumWidth(500)
    window.setMinimumHeight(350)
    window.setMinimumWidth(350)

    window.show()

    sys.exit(app.exec_())