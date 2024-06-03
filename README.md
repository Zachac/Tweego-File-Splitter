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

## Changelog

### 1.0.1 (Update By Mellerin using Copilot)
- use utf8 as decoding for the script to just work.
- sanitize filenames because sometime passages titles introduce an error with incorrect character in filename / path.
- include subdirectories for special files / sections (SpecialPassages, StoryData, StoryScripts, StyleSheet, Widgets). Please note that it's not an option (yet?) so it writes files under subfolders even if you don't want to.
- include a -help or -? command line option. Well it's not that helpful but should be included, maybe if it will include more options 😅

<p>Please note that I'm not a python dev (or whatever a dev), so Copilot was really helpful for me here and to be honest it did almost all the work.<br>
Only tested in commandline mode under windows10 for now and it works. Should also work wherever python could be installed if you can launch a python script.<br>
Not tested : usage from within another python file like described below in the original Readme.md.</p>
<p>Uses re, sys, os, Path from pathlib, Optional from typing.</p>

#### About patterns, titles and tags
The script splits the twee file passed in argument based on patterns defined at the beginning, like this :<br>

> passage_pattern = re.compile(r":: (.+)\n((?:(?:.*\n)(?!:: ))*)")
<p>(something like :: PassageTitle [tag1 tag2 ...] )</p>
<br>
Splitting Titles and Tags are defined just below, like this :<br>

>SPECIAL_TITLES = [
>    "PassageDone", "PassageFooter", "PassageHeader", "PassageReady",
>    "StoryBanner", "StoryCaption", "StoryDisplayTitle", "StoryInit",
>    "StoryMenu"
]
>
>STORY_DATA_TITLES = ["StoryData", "StoryTitle"]
>
>TAG_SUBFOLDERS = {
>    'stylesheet': 'StyleSheet',
>    'script': 'StoryScripts',
>    'widget': 'Widgets'
>}
<br>
<p>Just to say that splitting is done with those definitions, so if your twee file is made with other patterns or you want different tags, less or more subfolders you have to modify those sections by yourself inside the code.</p>
<br>

## Tested With
- Version 1.0.0 tested with Tweego 1.3.0 and Python 3.7.3
- Version 1.0.1 tested with Tweego 2.1.1 and Python 3.7.3
