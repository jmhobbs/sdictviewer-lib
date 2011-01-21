# About

This is a trimmed down version of sdictviewer to be used as a library.  I've made no modifications to it beyond ripping out files that weren't needed.

<http://sdictviewer.sourceforge.net/>

# Installation

    git clone git://github.com/jmhobbs/sdictviewer-lib.git
    python setup.py install

# Usage

	import sys
	import sdictviewer.formats.dct.sdict as sdict
	import sdictviewer.dictutil

	dictionary = sdict.SDictionary( 'webster_1913.dct' )
	dictionary.load()

	start_word = sys.argv[1]

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

# License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Copyright (C) 2006-2008 Igor Tkach
