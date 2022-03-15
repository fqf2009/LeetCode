# Design a data structure that simulates an in-memory file system.
# Implement the FileSystem class:
# - FileSystem() Initializes the object of the system.
# - List<String> ls(String path)
#   - If path is a file path, returns a list that only contains this file's name.
#   - If path is a directory path, returns the list of file and directory names
#     in this directory.
# The answer should in lexicographic order.
# - void mkdir(String path) Makes a new directory according to the given path.
#   The given directory path does not exist. If the middle directories in the
#   path do not exist, you should create them as well.
# - void addContentToFile(String filePath, String content)
#   - If filePath does not exist, creates that file containing given content.
#   - If filePath already exists, appends the given content to original content.
# - String readContentFromFile(String filePath) Returns the content in the
#   file at filePath.
#
# Constraints:
# -  1 <= path.length, filePath.length <= 100
# -  path and filePath are absolute paths which begin with '/' and do not
#    end with '/' except that the path is just "/".
# -  You can assume that all directory names and file names only contain
#    lowercase letters, and the same names will not exist in the same directory.
# -  You can assume that all operations will be passed valid parameters, and
#    users will not attempt to retrieve file content or list a directory or
#    file that does not exist.
# -  1 <= content.length <= 50
# -  At most 300 calls will be made to ls, mkdir, addContentToFile, and
#    readContentFromFile.
from typing import List


class FNode:
    def __init__(self, name: str, isFile: bool, content: str = '') -> None:
        self.name = name
        self.children = {}
        self.isFile = isFile
        self.content = content
    
    def ls(self) -> List[str]:
        if self.isFile:
            return [self.name]
        else:
            return sorted(self.children.keys())
    
    def mkdir(self, name: str) -> 'FNode':
        if name not in self.children:
            self.children[name] = FNode(name, isFile=False)
        return self.children[name]

class FileSystem:
    def __init__(self):
        self.root = FNode(name = '', isFile=False)

    def ls(self, path: str) -> List[str]:
        if path == '/':
            return self.root.ls()
        stems = path.split('/')
        node = self.root
        for stem in stems[1:]:
            node = node.children[stem]
        return node.ls()

    def mkdir(self, path: str) -> None:
        stems = path.split('/')
        node = self.root
        for stem in stems[1:]:
            if stem not in node.children:
                node = node.mkdir(stem)
            else:
                node = node.children[stem]

    def addContentToFile(self, filePath: str, content: str) -> None:
        stems = filePath.split('/')
        node = self.root
        for stem in stems[1:-1]:
            node = node.children[stem]
        filename = stems[-1]
        if filename in node.children:
            node.children[filename].content += content
        else:
            node.children[filename] = FNode(filename, isFile=True, content=content)

    def readContentFromFile(self, filePath: str) -> str:
        stems = filePath.split('/')
        node = self.root
        for stem in stems[1:]:
            node = node.children[stem]
        return node.content


if __name__ == '__main__':
    def unitTest():
        inputs = [["FileSystem", "ls", "mkdir", "addContentToFile", "ls", 
                   "readContentFromFile"],
                  [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]]
        expected = [None, [], None, None, ["a"], "hello"]
        outputs = [None]
        obj = globals()[inputs[0][0]](*inputs[1][0])        # obj = FileSystem()
        for i in range(1, len(inputs[0])):
            r = getattr(obj, inputs[0][i])(*inputs[1][i])   # obj.ls(path),...,etc.
            outputs.append(r)
        print(outputs)
        assert outputs == expected

    unitTest()
