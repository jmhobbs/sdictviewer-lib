import sys, os
import sdictviewer.formats.dct.sdict as sdict
import sdictviewer.dictutil

if 3 > len( sys.argv ):
	print
	print "usage: %s [dictionary] [word]" % sys.argv[0]
	print
	print "dictionary - An SDict format dictionary"
	print "             (Example: http://sdict.com/en/view.php?file=webster_1913.dct)"
	print "word       - The word to look up"
	print
	exit()

if not os.path.exists( sys.argv[1] ):
	print
	print "Dictionary file", sys.argv[1], "does not exist."
	print
	exit()

dictionary = sdict.SDictionary( sys.argv[1] )
dictionary.load()

start_word = sys.argv[2]

found = False

for item in dictionary.get_word_list_iter( start_word ):
    try:
        if start_word == str( item ):
            instance, definition = item.read_articles()[0]
            print "%s: %s" % ( item, definition )
            found = True
            break
    except:
        continue

if not found:
    print "No definition for '%s'." % start_word

dictionary.close()
