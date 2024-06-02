# Forked from Zachac/Tweego-File-Splitter
This is a fork of https://github.com/Zachac/Tweego-File-Splitter with some significant rework done with the help of Copilot.

Notable changes :
- use utf8 as decoding for the script to just work.
- sanitize filenames because sometime passages titles introduce an error with incorrect character in filename / path.
- include subdirectories for special files / sections (SpecialPassages, StoryData, StoryScripts, StyleSheet, Widgets). Please note that it's not an option (yet?) so it writes files under subfolders even if you don't want to.
- include a -help or -? command line option. Well it's not that helpful but should be included, maybe if it will include more options 😅

<p>Please note that I'm not a python dev (or whatever a dev), so Copilot was really helpful for me here and to be honest it did almost all the work.<br>
Only tested in commandline mode under windows10 for now and it works. Should also work wherever python could be installed if you can launch a python script.<br>
Not tested : usage from within another python file like described below in the original Readme.md.</p>
<p>Uses re, sys, os, Path from pathlib, Optional from typing.</p>
<br>
<br>

Original Readme :<br>
# Tweego-File-Splitter
Splits a .twee file up into separate files. By default, a new folder is created to house the split files.

## Purpose
As of the current version (1.3.0) of [Tweego](https://www.motoslave.net/tweego/), decompiling will result in a single large file. However, a large benefit of using Tweego is to be able to organize a Twee game into a folder structure. To convert the single decompiled file into this folder structure requires spending large amounts of times simply creating new files. So having the ability to automatically split large .twee files can help automate this process.

## Usage
From within another python file
```python
import tweego_file_splitter
tweego_file_splitter.splitFile("fileToSplit.twee")
```

From the command line
```
python tweego_file_splitter tweefile [outputDirectory]
```

## Dependencies
* Python 3
