# Design a text editor with a cursor that can do the following:
#  - Add text to where the cursor is.
#  - Delete text from where the cursor is (simulating the backspace key).
#  - Move the cursor either left or right.
# When deleting text, only characters to the left of the cursor will
# be deleted. The cursor will also remain within the actual text and
# cannot be moved beyond it. More formally, we have that
# 0 <= cursor.position <= currentText.length always holds.
# Implement the TextEditor class:
#  - TextEditor() Initializes the object with empty text.
#  - void addText(string text) Appends text to where the cursor is.
#    The cursor ends to the right of text.
#  - int deleteText(int k) Deletes k characters to the left of the
#    cursor. Returns the number of characters actually deleted.
#  - string cursorLeft(int k) Moves the cursor to the left k times.
#    Returns the last min(10, len) characters to the left of the cursor,
#    where len is the number of characters to the left of the cursor.
#  - string cursorRight(int k) Moves the cursor to the right k times.
#    Returns the last min(10, len) characters to the left of the cursor,
#    where len is the number of characters to the left of the cursor.
# Constraints:
#   1 <= text.length, k <= 40
#   text consists of lowercase English letters.
#   At most 2 * 104 calls in total will be made to addText, deleteText,
#   cursorLeft and cursorRight.


# String slicing
class TextEditor:
    def __init__(self):
        self.buffer = ""
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.buffer = self.buffer[: self.cursor] + text + self.buffer[self.cursor :]
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        cnt = min(k, self.cursor)
        self.cursor -= cnt
        self.buffer = self.buffer[: self.cursor] + self.buffer[self.cursor + cnt :]
        return cnt

    def leftText(self):
        return self.buffer[max(0, self.cursor - 10) : self.cursor]

    def cursorLeft(self, k: int) -> str:
        self.cursor -= min(k, self.cursor)
        return self.leftText()

    def cursorRight(self, k: int) -> str:
        self.cursor += min(k, len(self.buffer) - self.cursor)
        return self.leftText()


# Two stacks
# - 10 times faster the other two solutions
# - Because str is immutable, the price of manipulating long text is high
class TextEditor1:
    def __init__(self):
        self.lstack = []
        self.rstack = []

    def addText(self, text: str) -> None:
        self.lstack.append(text)

    def deleteText(self, k: int) -> int:
        cnt = 0
        while self.lstack and k > 0:
            s = self.lstack.pop()
            if len(s) <= k:
                cnt += len(s)
                k -= len(s)
            else:
                self.lstack.append(s[:-k])
                cnt += k
                k = 0
        return cnt

    def leftText(self, k):
        res = ""
        for s in reversed(self.lstack):
            cnt = min(len(s), k)
            res = s[-cnt:] + res
            k -= cnt
            if k == 0: break
        return res

    def cursorLeft(self, k: int) -> str:
        cnt = 0
        while self.lstack and k > 0:
            s = self.lstack.pop()
            if len(s) <= k:
                self.rstack.append(s)
                cnt += len(s)
                k -= len(s)
            else:
                self.lstack.append(s[:-k])
                self.rstack.append(s[-k:])
                cnt += k
                k = 0
        return self.leftText(10)

    def cursorRight(self, k: int) -> str:
        cnt = 0
        while self.rstack and k > 0:
            s = self.rstack.pop()
            if len(s) <= k:
                self.lstack.append(s)
                cnt += len(s)
                k -= len(s)
            else:
                self.lstack.append(s[:k])
                self.rstack.append(s[k:])
                cnt += k
                k = 0
        return self.leftText(10)


# Two strings
class TextEditor2:

    def __init__(self):
        self.lbuf = ""
        self.rbuf = ""

    def addText(self, text: str) -> None:
        self.lbuf += text

    def deleteText(self, k: int) -> int:
        cnt = min(len(self.lbuf), k)
        self.lbuf = self.lbuf[:-cnt]
        return cnt

    def cursorLeft(self, k: int) -> str:
        cnt = min(len(self.lbuf), k)
        self.rbuf = self.lbuf[-cnt:] + self.rbuf
        self.lbuf = self.lbuf[:-cnt]
        return self.lbuf[-10:]
        
    def cursorRight(self, k: int) -> str:
        cnt = min(len(self.rbuf), k)
        self.lbuf = self.lbuf + self.rbuf[:cnt]
        self.rbuf = self.rbuf[cnt:]
        return self.lbuf[-10:]


if __name__ == "__main__":

    def unitTest(Editor):
        print(Editor.__name__)
        editor = Editor()

        inputs = [
            [
                "addText",
                "deleteText",
                "addText",
                "cursorRight",
                "cursorLeft",
                "deleteText",
                "cursorLeft",
                "cursorRight",
            ],
            [["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]],
        ]
        expected = [None, 4, None, "etpractice", "leet", 4, "", "practi"]
        outputs = []
        for i in range(len(inputs[0])):
            outputs.append(getattr(editor, inputs[0][i])(*inputs[1][i]))
        print(outputs)
        assert outputs == expected

    unitTest(TextEditor)
    unitTest(TextEditor1)
    unitTest(TextEditor2)
