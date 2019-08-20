
import os, shutil 

#### EDIT SPOT ########################
#######################################
#	Modify this line to set the root folder for the transformation.
# 	Bumblebee will walk all the way down the directory tree from
#	this folder.
basedir = "Some_folder"
#######################################


def process_file(filename, dirname):
	print "[Processing file %s]" % filename
	with open(os.path.join(dirname, filename), "r") as source:
		with open(os.path.join("new", dirname, filename), "w") as target:
			target_content = source.read()
			if __filter__(filename):
			
				#### EDIT SPOT ########################
				#######################################
				#	Add here yout transfomations by copying and pasting this line:
				#
				#		target_content = target_content.replace("<replace-this>", "<with-this>")
				#
				#	and replacing:
				#		<replace-this> with the string you want to replace
				#		<with-this> with the string you want to place
				#
				# this is an example:
				target_content = target_content.replace("bumblebee sucks", "bumblebee rules!")		
				#######################################
			
			# do not touch this line
			target.write(target_content)
				
def __filter__(fname):
	
	#### EDIT SPOT ########################
	#######################################
	#	Modify this function to filter undesired file formats
	# 	to transform.
	#
	#	'fname' is the complete name of the file (including extension)
	#	
	#	Example: to proces only .log files use:
	#		return (fname[-3:] != "LOG") and (fname[-3] != "log")
	#
	return True
	#######################################

def process_dir(args, dirname, filenames):
	print "[Processing dir %s]" % dirname
	os.makedirs(os.path.join("new", dirname))
	for fname in filenames:
		if "." in fname: # avoid folders
			process_file(fname, dirname)
		
def init():
	if os.path.exists("new"):
		print "Cleaning dest dir: new"
		shutil.rmtree("new")
	print "Creating dest dir: new"
	os.mkdir("new")

init()
os.path.walk(basedir, process_dir, None)
