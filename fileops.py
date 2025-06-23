try:
    file1 = open('myfile.txt', 'r+')
    reading_line = file1.readlines()
    print(reading_line)
    file1.close()
except FileNotFoundError:
    print("Error: The file 'myfile.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


