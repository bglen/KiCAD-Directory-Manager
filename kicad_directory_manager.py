import pcbnew
import glob
import shutil
import os

class kicad_directory_manager(pcbnew.ActionPlugin):
	def defaults(self):
		self.name = "Organize Local Project Directory"
		self.category = "Project Management"
		self.description = "Orangizes the project directory and created local libraries for easy exporting and sharing."
		self.show_toolbar_button = True # Optional, defaults to False
		self.icon_file_name = os.path.join(os.path.dirname(__file__), 'simple_plugin.png') # Optional, defaults to ""

	def Run(self):
		print("Hello World")
		pcb = pcbnew.GetBoard()

		# Get project directory
		projectDirectory = pcb.GetFileName()
		projectDirectory = projectDirectory[0:projectDirectory.rfind('/')]

		# Get project name
		projectName = projectDirectory[(projectDirectory.rfind('/')+1):len(projectDirectory)]

		# Create directory folders
		folderList = ["datasheets", "3d_models", "gerbers", "images", "lib_symbols", "lib_footprints.pretty", "pdfs"]
		for folder in folderList:
			path = os.path.join(projectDirectory, folder)
			try: 
				os.mkdir(path) 
				print("Directory '%s' created successfully" % folder) 
			except OSError as error: 
				print("Directory '%s' can not be created" % folder);

		# Organize any images
		for fileName in glob.glob("*.png"):
			oldPath = os.path.join(projectDirectory, fileName) + ".png"
			newPath = os.path.join(projectDirectory, "images")
			shutil.move(oldPath, newPath)

		for fileName in glob.glob("*.jpg"):
			oldPath = os.path.join(projectDirectory, fileName) + ".png"
			newPath = os.path.join(projectDirectory, "images")
			shutil.move(oldPath, newPath)

kicad_directory_manager().register() # Instantiate and register to Pcbnew