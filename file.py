employees=["Eugene","Squidwaard","Spongeebob"]

file_path="C:/Users/vidul/OneDrive/Documents/GitHub/Fullstack/new.dir/test.txt"
try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + "\n")
    print("txt file '{file_path}' was created")
except OSError:
    print("the file already exists")
    