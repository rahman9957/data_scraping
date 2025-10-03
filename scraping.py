import os
print(os.getcwd())

def ucapan(text):
    print(text)

ucapan("hi selamat datang!")


def create_directory(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

create_directory("Scraping")

def create_new_file(path):
    f=open(path,'w')
    f.write("ibnu pemburu bawox")
    f.close()

create_new_file("Scraping/test.txt")

def write_to_file(path,data):
    with open(path,'a') as file:
        file.write(data + '\n')

#def clear_file(path):
 #   f=open(path,'w')
 #   f.close()

#clear_file("Scraping/test.txt")

def read_data(path):
    with open(path,'rt') as file:
        for line in file:
            print(line)

read_data("scraping/test.txt")
