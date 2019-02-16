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
