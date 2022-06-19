import os
def fileReadWrite():
    with open("/Users/i346327/pythonds/pythonds/03-FileHandling/file1.txt") as old_file, open("/Users/i346327/pythonds/pythonds/03-FileHandling/file_new.txt",'w') as new_file:
        for line in old_file:
            if len(line.split()) == len(list(set(line.split()))):
                    new_file.write(line)
    
    os.system("cat /Users/i346327/pythonds/pythonds/03-FileHandling/file_new.txt")
fileReadWrite()