def process_file():
    try:
        file = open("data.txt")
        print(file.read())

    except FileNotFoundError:
        print("Logging: File not found")
        raise

try:
    process_file()

except FileNotFoundError:
    print("Please check the file path")