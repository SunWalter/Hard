from sys import argv
from os.path import exists
script, from_file, to_file = argv

# print ("copying from %s to %s." % (from_file, to_file))

# in_file =  # indifine read only

#
# print ("Does the output file exist? %r" % exists(to_file))
# print ("Hit ENTER to continue and CTRL-C to abort.")
# input('>')

# out_file =
open(to_file,'w').write(open(from_file).read())

# print ("Alright, All done.")

# out_file.clos/
