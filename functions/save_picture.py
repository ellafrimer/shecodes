from urllib import request
import random

def save_picture(url):
    file_name = './images/' + str(random.randint(1, 1000)) + ".jpg"
    request.urlretrieve(url, file_name)
    print("File saved as ", file_name)


save_picture("http://www.she-codes.org/sc/wp-content/uploads/2014/11/logo-copy200.png")
