import os
import tempfile
from abc import ABC, abstractmethod


class FileHandler(ABC):
    """Abstract base class: every file handler MUST implement read() and write()."""

    def __init__(self, filepath):
        self.filepath = filepath

    @abstractmethod
    def read(self):
        """Read and return the file's contents."""

    @abstractmethod
    def write(self, data):
        """Write data to the file."""

    def exists(self):
        return os.path.exists(self.filepath)

class TextFileHandler(FileHandler):
    """Handles plain-text files (str data)."""

    def read(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return f.read()

    def write(self, data):
        with open(self.filepath, "w", encoding="utf-8") as f:
            f.write(data)


class BinaryFileHandler(FileHandler):
    """Handles binary files (bytes data)."""

    def read(self):
        with open(self.filepath, "rb") as f:
            return f.read()

    def write(self, data):
        with open(self.filepath, "wb") as f:
            f.write(data)


class BrokenHandler(FileHandler):
    """Implements read() but forgets write(), so it can't be instantiated."""

    def read(self):
        return "..."


def main():
    with tempfile.TemporaryDirectory() as tmp:
        # 1. Text handler
        text_handler = TextFileHandler(os.path.join(tmp, "notes.txt"))
        text_handler.write("Hello, text file!")
        print("Text read:  ", text_handler.read())

        # 2. Binary handler
        bin_handler = BinaryFileHandler(os.path.join(tmp, "data.bin"))
        bin_handler.write(bytes([72, 101, 108, 108, 111, 0, 255]))
        print("Binary read:", bin_handler.read())

        # 3. Shared behaviour inherited from the base class
        print("Exists?     ", text_handler.exists(), bin_handler.exists())

        # 4. Polymorphism: treat every handler through the same interface
        print("\nPolymorphism:")
        for handler in (text_handler, bin_handler):
            print(f"  {type(handler).__name__} -> isinstance FileHandler: "
                  f"{isinstance(handler, FileHandler)}")

    # 5. The ABC can't be instantiated directly
    print("\nEnforcement:")
    try:
        FileHandler("x.txt")
    except TypeError as e:
        print(f"  FileHandler: {e}")

    # 6. Subclasses that skip an abstract method can't be instantiated either
    try:
        BrokenHandler("x.txt")
    except TypeError as e:
        print(f"  BrokenHandler: {e}")


if __name__ == "__main__":
    main()