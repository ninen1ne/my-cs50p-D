def read_file(filename, file_format):
    content = []
    with open(f'{filename}.{file_format}', 'r') as file:
        for line in file:
            content.append(line.rstrip())

    return content

def write_file(filename, file_format, content):
    with open(f'{filename}.{file_format}', 'a') as file:
        if isinstance(content, list):
            for line in content:
                file.write(f'{line}\n')
        else:
            file.write(f'{content}\n')