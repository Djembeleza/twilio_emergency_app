def read_file(file_path: str):
    """This function returns the content of a .txt file

    Args:
        file_path (str): The path of the document to open
    """
    try:
        with open(file_path, 'r') as text_file:
            return text_file.read()
    except FileNotFoundError:
        return f"Error: The file {file_path} was not found."
    except IOError:
        return f"Error: Could not read the file '{file_path}'"
