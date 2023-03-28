import os
import re

folder = r"wiki"

REGEX = r' \S*(\S*([a-zA-Z]\S*[0-9])|([0-9]\S*[a-zA-Z]))\S*'

pathsDict = {}
absPathsArr = []


def rename(folder, folderNew):
    for file in os.listdir(folder):
        # Checking if the file is present in the list
        oldName = os.path.join(folder, file)
        if "." not in file:
            newName = re.sub(REGEX, "", file)
            newName = os.path.join(folder, newName)
            rename(oldName, newName)
            os.rename(oldName, newName)
            oldName = addSpaceCharacter(oldName)
            pathArray = pathPossibilities(oldName)
            for path in pathArray:
                pathsDict[path] = "/"+addSpaceCharacter(newName)
        else:
            if re.search(REGEX, file):
                fileExtension = file.split(".")
                newName1 = re.sub(
                    REGEX, ".", fileExtension[0])+fileExtension[1]
                newName = os.path.join(folder, newName1)
                os.rename(oldName, newName)
                newName = os.path.join(folderNew, newName1)
                absPathsArr.append(fr"{newName}")
                oldName = addSpaceCharacter(oldName)
                pathArray = pathPossibilities(oldName)
                for path in pathArray:
                    pathsDict[path] = "/"+addSpaceCharacter(newName)


def addSpaceCharacter(path, spacing="%20"):
    newPath = ""
    for i in path:
        if i == " ":
            newPath += "%20"
        else:
            newPath += i
    return newPath


def pathPossibilities(path):
    pathArray = [path]
    for i in range(len(path)):
        if path[i] == "/":
            pathArray.append(path[i+1:])
    return pathArray


def renamePaths():
    for file in absPathsArr:
        for key in pathsDict:
            try:
                inplace_change(file, key, pathsDict[key])
            except:
                continue


def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)


def buildIndex(folder, filename="readme.md"):
    indexPaths = {}
    count = 0
    for file in os.listdir(folder):
        # Checking if the file is present in the list
        name = os.path.join(folder, file)
        if ".md" not in file:
            continue
        else:
            title = name[name.find("/")+1:name.find(".md")]
            name = addSpaceCharacter(name)
            indexPath = f"- [{title}]({name})"
            indexPaths[name] = indexPath

    for indexPath in indexPaths:
        with open(filename) as f:
            s = f.read()
            if indexPath.lower() in s.lower():
                # File already in index
                continue

        # Safely write the new file to index
        with open(filename, 'a') as f:
            if count > 0:
                f.write(f"\n{indexPaths[indexPath]}")
            else:
                if endsWithWhitespace(filename):
                    f.write(f"{indexPaths[indexPath]}")
                else:
                    f.write(f"\n{indexPaths[indexPath]}")
            count += 1


def endsWithWhitespace(filename):
    with open(filename, "rb") as file:
        try:
            file.seek(-2, os.SEEK_END)
            while file.read(1) != b'\n':
                file.seek(-2, os.SEEK_CUR)
        except OSError:
            file.seek(0)
        last_line = file.readline().decode()
    return "\n" in last_line


def main():
    rename(folder, folder)
    renamePaths()
    buildIndex(folder)


if __name__ == "__main__":
    main()
