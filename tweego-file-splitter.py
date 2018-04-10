
import re
import sys
import distutils.dir_util

passage_pattern = re.compile(":: (.+)\n((?:(?:.*\n)(?!:: ))*)")
file_ending_pattern = re.compile("\.twee")

def nameToDirectory(filename):
    directory = filename
    match = file_ending_pattern.search(directory)

    if match:
        directory = directory[:match.start()]

    directory = directory.strip()

    return directory

def writePassage(directory, title, content):
    filename = title
    tag_start = filename.find(" [")
    
    if (tag_start > 0):
        filename = filename[:tag_start]
        
    filename = filename.strip()
    filename = directory + "/" + filename + ".twee"
    
    f = open(filename, "w")
    print(":: ", title, file=f)
    print(content.strip(), file=f)
    f.close()

def splitFile(filename, directory=None):
    f = open(filename, "r")
    content = f.read()
    f.close()

    if directory == None:
        directory = nameToDirectory(filename)

    distutils.dir_util.mkpath(directory)

    for match in passage_pattern.finditer(content):
        writePassage(directory, match.group(1), match.group(2))

if __name__ == "__main__":
    argc = len(sys.argv)
    success = True
    
    if argc <= 1 or argc > 3:
        print("Invalid number of arguments,")
        print("\tUsage: python tweego-file-splitter file [outputDirectory]")
        success = False
    elif argc == 3:
        file = sys.argv[1]
        directory = sys.argv[2]
    else:
        file = sys.argv[1]
        directory = None

    if success:
        splitFile(file, directory)
