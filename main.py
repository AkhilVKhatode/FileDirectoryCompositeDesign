from abc import ABC, abstractmethod

# Component class
class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass

# File class (leaf component)
class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def show_details(self):
        print(f"File: {self.name}, Size: {self.size}KB")

# Directory class (composite component)
class Directory(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
        self.components = []

    def add_component(self, component: FileSystemComponent):
        self.components.append(component)

    def remove_component(self, component: FileSystemComponent):
        self.components.remove(component)

    def show_details(self):
        print(f"Directory: {self.name}")
        for component in self.components:
            component.show_details()

# FileSystemController class - Main controller to demonstrate usage
if __name__ == "__main__":
    # Create files
    file1 = File("file1.txt", 10)
    file2 = File("file2.jpg", 25)
    file3 = File("file3.pdf", 50)

    # Create directories
    directory1 = Directory("Documents")
    directory2 = Directory("Images")
    directory3 = Directory("Work")

    # Add files to directories
    directory1.add_component(file1)
    directory1.add_component(file3)

    directory2.add_component(file2)

    # Create a main directory and add subdirectories
    main_directory = Directory("Root")
    main_directory.add_component(directory1)
    main_directory.add_component(directory2)

    # Add subdirectory to a directory
    directory1.add_component(directory3)

    # Show details of the entire file system
    print("File System Details:")
    main_directory.show_details()
