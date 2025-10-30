def simple_poet(filename):
    """Read a file and return a list of lines as strings."""
    with open(filename, 'r') as f:
        lines = f.readlines()
    # Strip trailing newlines
    lines = [line.rstrip('\n') for line in lines]
    return lines

