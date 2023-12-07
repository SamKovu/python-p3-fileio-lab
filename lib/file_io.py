def write_file(file_name, file_content):
    with open(str(file_name)+".txt", mode="w", encoding="utf-8") as file:
        file.write(file_content)


def append_file(file_name, append_content):
    with open(str(file_name)+".txt", mode="a", encoding="utf-8") as file:
        file.write(append_content)

def read_file(file_name):
    with open(str(file_name)+".txt", encoding="utf-8") as file:
        return file.read()
    
    
write_file(file_name="test", file_content="Log 1: Samuel\n" )
append_file(file_name="test", append_content="Log 2: Kovu")

print(read_file(file_name="test"))