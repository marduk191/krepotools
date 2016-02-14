#!/usr/bin/env python
#########################################
# Addon.xml generator
# for Kodi addons
# By: marduk191
# Email: marduk191@gmail.com
# Github: https://github.com/marduk191
# generate an xml in Python
#########################################
"""
Run addonxml.py
Your file will be named addon.xml
"""

import os
from lxml import etree
#import pconfig
### User input ###
def getVarFromFile(filename):
    import imp
    kvars = open(filename)
    global data
    data = imp.load_source('data', '', kvars)
    kvars.close()
getVarFromFile('./pconfig')
#### Hacky bugfix, FIX LATER###
os.remove("c")
#################################################

### Used for parsing, DO NOT EDIT ###
PARSER = etree.XMLParser(remove_blank_text=True)
TREE = etree.parse('template.xml', PARSER)
ROOT = TREE.getroot()
#####################################

### Working with the XML values ###
for addon in ROOT.iter('addon'):
    addon.set('id', data.ADDON_ID)
    addon.set('name', data.ADDON_NAME)
    addon.set('version', data.ADDON_VERSION)
    addon.set('provider-name', data.ADDON_PROVIDER)
TREE.write('output.xml', pretty_print=True)

for requires in ROOT.iter('import'):
    requires.set('addon', data.MYIMPORT)
    requires.set('version', data.MYIMPORT_VERS)
TREE.write('output.xml', pretty_print=True)

for extension in ROOT.iter('provides'):
    extension.text = str(data.EX_PROVIDES)
TREE.write('output.xml', pretty_print=True)

for description in ROOT.iter('description'):
    description.set('lang', "en_GB")
    description.text = str(data.DESCRIPTION_TEXT)
TREE.write('output.xml', pretty_print=True)

for summary in ROOT.iter('summary'):
    summary.set('lang', "en_GB")
    summary.text = str(data.SUMMARY_TEXT)
TREE.write('output.xml', pretty_print=True)

for disclaimer in ROOT.iter('disclaimer'):
    disclaimer.set('lang', "en_GB")
    disclaimer.text = str(data.DISCLAIMER_TEXT)
TREE.write('output.xml', pretty_print=True)

for language in ROOT.iter('language'):
    language.text = str(data.LANGUAGE_TEXT)
TREE.write('output.xml', pretty_print=True)

for platform in ROOT.iter('platform'):
    platform.text = str(data.PLATFORM_TEXT)
TREE.write('output.xml', pretty_print=True)

for license in ROOT.iter('license'):
    license.text = str(data.LICENSE_TEXT)
TREE.write('output.xml', pretty_print=True)

for forum in ROOT.iter('forum'):
    forum.text = str(data.FORUM_TEXT)
TREE.write('output.xml', pretty_print=True)

for website in ROOT.iter('website'):
    website.text = str(data.WEBSITE_TEXT)
TREE.write('output.xml', pretty_print=True)

for email in ROOT.iter('email'):
    email.text = str(data.EMAIL_TEXT)
TREE.write('output.xml', pretty_print=True)

for source in ROOT.iter('source'):
    source.text = str(data.SOURCE_TEXT)
TREE.write('output.xml', pretty_print=True)
###################################################

### adding XML header because of inherited stripping above ###
with open('output.xml', 'r') as original:
    DATA = original.read()
with open('addon.xml', 'w') as modified:
	modified.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n" + DATA)

### removing temp file ###
os.remove("output.xml")

print("complete!")