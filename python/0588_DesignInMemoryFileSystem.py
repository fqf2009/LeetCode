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
from typing import List, Optional
from abc import ABC, abstractmethod


class FSNode(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def isFile(self) -> bool:
        pass

    @abstractmethod
    def ls(self) -> List[str]:
        pass


class FileNode(FSNode):
    def __init__(self, name, content: str = ''):
        super().__init__(name)
        self._content = content

    def isFile(self) -> bool:
        return True

    def ls(self) -> List[str]:
        return [self._name]

    def appendContent(self, content: str = ''):
        self._content += content

    @property
    def content(self):
        return self._content


class DirNode(FSNode):
    def __init__(self, name):
        super().__init__(name)
        self._children = {}

    def isFile(self) -> bool:
        return False

    def ls(self) -> List[str]:
        return sorted(self._children.keys())

    def mkDir(self, name: str) -> 'DirNode':
        if name not in self._children:
            self._children[name] = DirNode(name)
        return self.getDir(name)

    def getDir(self, name: str) -> 'DirNode':
        node = self._children[name]
        assert isinstance(node, DirNode)
        return node

    def getFile(self, name: str) -> 'FileNode':
        node = self._children[name]
        assert isinstance(node, FileNode)
        return node

    def getFSNode(self, name: str) -> 'FSNode':
        node = self._children[name]
        return node

    def fileExists(self, name: str) -> bool:
        return name in self._children and isinstance(self._children[name], FileNode)

    def dirExists(self, name: str) -> bool:
        return name in self._children and isinstance(self._children[name], DirNode)

    def addFile(self, name: str, node: 'FileNode'):
        self._children[name] = node


class FileSystem:
    def __init__(self):
        self.root = DirNode(name = '/')

    def _getFSNode(self, path: str) -> Optional[FSNode]:
        if path == '/': return self.root
        names = str.split(path.lstrip('/'), '/')
        dir = self.root
        for name in names[:-1]:
            if dir.dirExists(name):
                dir = dir.getDir(name)
            else:
                return None
        if dir.fileExists(names[-1]) or dir.dirExists(names[-1]):
            return dir.getFSNode(names[-1])
        else:
            return None

    def ls(self, path: str) -> List[str]:
        node = self._getFSNode(path)
        return node.ls() if node else []

    def _mkdir(self, path: str) -> DirNode:
        dir = self.root
        for folderName in path.split('/')[1:]:
            dir = dir.mkDir(folderName)
        return dir

    def mkdir(self, path: str) -> None:
        self._mkdir(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        names = filePath.split('/')
        dirPath = '/'.join(names[:-1])
        dir = self._mkdir(dirPath)
        filename = names[-1]
        if not dir.fileExists(filename):
            dir.addFile(filename, FileNode(filename, content=content))
        else:
            dir.getFile(filename).appendContent(content)

    def readContentFromFile(self, filePath: str) -> str:
        node = self._getFSNode(filePath)
        assert isinstance(node, FileNode)
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
