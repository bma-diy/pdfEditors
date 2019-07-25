'''
Be sure to have Python 2.7 and the pyPDF2 package installed.

	python --version
	sudo easy_install pip
	sudo pip install PyPDF2

Place all of your PDFs in the folder, "OriginalPDFs". 
Once you navigate to directory holding the script in Command Line, type "python pdfSplitter.py" but without the quotes.

When the program finishes:
The first two pages of each PDF will be placed in the "groupOne" folder.
The last three pages of each PDF will be placed in the "groupTwo" folder.



'''

from PyPDF2 import PdfFileWriter, PdfFileReader
import os

def append_groupOne(input,output,page_split):
    [output.addPage(input.getPage(page_num)) for page_num in range(0, page_split)] #Pages 1

def append_groupTwo(input,output,page_split):
    [output.addPage(input.getPage(page_num)) for page_num in range(page_split, input.numPages)] #Pages 3-end

def create_Directory(dirName):

	#https://thispointer.com/how-to-create-a-directory-in-python/

	#Create target Directory if don't exist
	if not os.path.exists(dirName):
		# Create directory
		os.mkdir(dirName)
		print("Directory \"{}\" Created ".format(dirName))

	else:

		print("Directory \"{}\" exists.".format(dirName))

print("\n")

if not os.path.exists("OriginalPDFs"):
	
	create_Directory("OriginalPDFs")
	print("Please place PDFs that need to be split into a folder named \"OriginalPDFs\" and rerun script.")
else:

	create_Directory("groupOne")
	create_Directory("groupTwo")

	## setting user_input to float to await integer input.
	user_input = float(2.2)
	print("\nThis script will split PDF documents located in the folder \"OriginalPDFs\" into two smaller PDFs and place the newly formed PDFs into folders \"groupOne\" and \"groupTwo\".")

	print("Example: If your doc has 5 pages, and you want to split the first two pages from the last three, enter the number \"2\"")

	while type(user_input) is not int:
		try:
			
			user_input = input ("Enter the page number where the split should be (the last page of first section): ")
		except NameError: 
			pass

		if type(user_input) is not int:
			print("Please enter an integer only.")

	print("\n")

	for filename in [f for f in os.listdir(os.getcwd()+"/OriginalPDFs")]:
		if not filename.endswith(".pdf"):
			continue
			
		print(filename)

		original = PdfFileReader(file("OriginalPDFs/" + filename,"rb"))
		togroupOne = PdfFileWriter()
		togroupTwo = PdfFileWriter()


		append_groupOne(original, togroupOne, user_input)
		append_groupTwo(original, togroupTwo, user_input)

		togroupOne.write(file("groupOne/" + filename,"wb"))
		togroupTwo.write(file("groupTwo/" + filename,"wb"))

	print("\nScript has completed running! ")
	print("Check \"groupOne\" and \"groupTwo\" folders for newly split PDFs.\n")



