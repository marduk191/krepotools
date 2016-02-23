Kodi Repository template
=========================

* Author:	marduk191 (<marduk191@gmail.com>)
* Created:	February 6, 2016
* Github:	<https://github.com/marduk191/krepotools>
* Zip Download:	[Releases](https://github.com/marduk191/krepotools/releases)





Table of Contents
=================
  * [Description](#description)
  * [Usage](#usage)
    * [Notes](#notes)
    * [Naming Conventions](#naming-conventions)
  
  * [Report issues](#questions-comments-concerns-issues)

<br>
<br>
#Description
-------------
This is a template for setting up a Kodi repository. It includes exmple repositories and tools for automating your workflow.

#Usage
------------
* Make a subfolder with a proper naming convention.
* Modify your addon.xml file in any subfolder (version increase triggers a zip build).
* Add your icon.png  (512x512px png).
* Add your fanart.jpg (1280x720px jpg).
* Write your changelog file (changes in this release).
* Run release.py (Builds addons.xml, addons.md5, and zips any plugin/repo folders that have a version change in the addon.xml file )
* Push to github

#Questions, Comments, Concerns, Issues
-------------------------------------
If you have any of these, go ahead and [submit an issue](https://github.com/marduk191/krepotools/issues),

#Notes
------------------------
Make sure you are keeping track of your commits. Have the individual commits done before running the release.py script. This makes it easier to follow because each "release" can get a version in the commit logs.

Please keep a changelog!

#Naming conventions:
* Repository folders are usually "repository.yourname"
* Video plugins are "plugin.video.yourname"
* etc etc, check the Kodi wiki for more information on naming conventions.
