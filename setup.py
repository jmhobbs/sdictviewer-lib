# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
	name='sdictviewer',
	version='1.0.0',
	description='Access SDict files',
	author='Igor Tkach (packaged by John Hobbs)',
	author_email='john@velvetcache.org',
	url='http://github.com/jmhobbs/sdictviewer-lib',
	packages=['sdictviewer', 'sdictviewer.formats', 'sdictviewer.formats.dct', 'sdictviewer.formats.pdi'],
	package_data={'sdictviewer': [ 'allkeys.txt' ] }
)
