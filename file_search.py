import os


def search_proc(dir_path, word_to_track):
    for item in os.scandir(dir_path):
        if os.path.isfile(item)==True:
            def search_text(word_to_track):
                with open(item, 'r') as file_stream: #open file to search word from
                    for paragraph in file_stream.readlines():
                        if (word_to_track in paragraph):
                            return True
                        else:
                            return False
            if search_text(word_to_track):
                print(item.path)
            else:
                print("File not found!")
        else:
            print("Not a File!")

search_proc("C:/Users/moses/Desktop/abc", "the")

