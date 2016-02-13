#!/usr/bin/env python
#########################################
# Addon.xml generator
# for Kodi addons
# By: marduk191
# Email: marduk191@gmail.com
# Github: https://github.com/marduk191
#########################################
"""
Add your information to the User input section
Then run addonxmlgen.py
Your file will be named addon.xml
"""

import os
import xml.etree.ElementTree as ET

### User input ###
ADDON_ID = "plugin.video.id2"
ADDON_NAME = "my addon"
ADDON_VERSION = "4.5.6"
ADDON_PROVIDER = "my.org"
MYIMPORT = "xbmc.python2"
MYIMPORT_VERS = "2.24.69"
EX_PROVIDES = "Video2"
SUMMARY_TEXT = "This is my summary"
DESCRIPTION_TEXT = "This is a test description"
DISCLAIMER_TEXT = "This is my disclaimer"
LANGUAGE_TEXT = "en2"
PLATFORM_TEXT = "all2"
LICENSE_TEXT = "GPLV2"
FORUM_TEXT = "http://thisismyurl.com"
WEBSITE_TEXT = "http://www.thisismysite.com"
EMAIL_TEXT = "Thisismyemail@gmail.com"
SOURCE_TEXT = "http://github.com/myuser"
#################################################

### Used for parsing, DO NOT EDIT ###
TREE = ET.parse('template.xml')
ROOT = TREE.getroot()
#####################################

### Working with the XML values ###
for addon in ROOT.iter('addon'):
    addon.set('id', ADDON_ID)
    addon.set('name', ADDON_NAME)
    addon.set('version', ADDON_VERSION)
    addon.set('provider-name', ADDON_PROVIDER)
TREE.write('output.xml')

for requires in ROOT.iter('import'):
    requires.set('addon', MYIMPORT)
    requires.set('version', MYIMPORT_VERS)
TREE.write('output.xml')

for extension in ROOT.iter('provides'):
    extension.text = str(EX_PROVIDES)
TREE.write('output.xml')

for description in ROOT.iter('description'):
    description.set('lang', "en_GB")
    description.text = str(DESCRIPTION_TEXT)
TREE.write('output.xml')

for summary in ROOT.iter('summary'):
    summary.set('lang', "en_GB")
    summary.text = str(SUMMARY_TEXT)
TREE.write('output.xml')

for disclaimer in ROOT.iter('disclaimer'):
    disclaimer.set('lang', "en_GB")
    disclaimer.text = str(DISCLAIMER_TEXT)
TREE.write('output.xml')

for language in ROOT.iter('language'):
    language.text = str(LANGUAGE_TEXT)
TREE.write('output.xml')

for platform in ROOT.iter('platform'):
    platform.text = str(PLATFORM_TEXT)
TREE.write('output.xml')

for license in ROOT.iter('license'):
    license.text = str(LICENSE_TEXT)
TREE.write('output.xml')

for forum in ROOT.iter('forum'):
    forum.text = str(FORUM_TEXT)
TREE.write('output.xml')

for website in ROOT.iter('website'):
    website.text = str(WEBSITE_TEXT)
TREE.write('output.xml')

for email in ROOT.iter('email'):
    email.text = str(EMAIL_TEXT)
TREE.write('output.xml')

for source in ROOT.iter('source'):
    source.text = str(SOURCE_TEXT)
TREE.write('output.xml')
###################################################

### adding XML header because of inherited stripping above ###
with open('output.xml', 'r') as original:
    DATA = original.read()
with open('addon.xml', 'w') as modified:
	modified.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n\n" + DATA)

### removing temp file ###
os.remove("output.xml")

print("complete!")
