import os


def file_exists(file_path: str) -> None:
    """Check if a file exists."""
    assert os.path.isfile(file_path), f"The file {file_path} does not exist."


def parent_folder_exists(file_path: str) -> None:
    """Check if the parent folder of a file exists."""
    parent_folder = os.path.dirname(file_path)
    assert os.path.isdir(parent_folder), f"Parent dir of  {file_path} does not exist."


def valid_image_type(file_path: str) -> None:
    """Check if a file is a .jpg, .jpeg, or .png."""
    ext = os.path.splitext(file_path)[1]  # Get the file extension
    valid = ext.lower() in ['.jpg', '.jpeg', '.png']
    assert valid, "Please provide input with proper format ('.jpg', '.jpeg', '.png')"
