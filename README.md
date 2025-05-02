# File System with Composite Pattern

This project demonstrates the use of the **Composite Design Pattern** in a file system. In this system, files and directories are modeled as components, where directories can contain both files and other directories, forming a tree-like structure.

## Structure

- **FileSystemComponent**: Abstract class representing a component (file or directory).
- **File**: Represents a file in the file system.
- **Directory**: Represents a directory that can contain files and other directories.
- **FileSystemController**: Main controller to demonstrate the functionality of the file system.

## Usage

1. **Create Files**: Instantiate `File` objects with name and size.
2. **Create Directories**: Instantiate `Directory` objects and add files or subdirectories to them.
3. **Display File System**: Use the `show_details()` method to print the structure of the entire file system.

### Example Usage

```python
from file import File
from directory import Directory

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
```
