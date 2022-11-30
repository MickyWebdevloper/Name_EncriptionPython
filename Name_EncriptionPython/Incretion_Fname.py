import os
import sys
import secrets
from PIL import Image


# Let's increpte the filename using secrets.
# def Incrept_Extensition(fname):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(fname)
#     print(f'{_} : printing filename')
#     print(f'{f_ext} : printing file extensition')

#     # JOining file extensition with random_hex.
#     path_file = random_hex + f_ext
#     # print(path_file)

#     # Saving with anothername here.
#     # path_file.save('Newdon.jpg')
#     img = Image.open(fname)
#     img.save(path_file)

#     # Result returning path_file.
#     return path_file


# if __name__ == '__main__':
#     fname = input('Type file name with Extensition want to Incrept : ')
#     Incrept_Extensition(fname)


class NameChanging:
    def __init__(self, fname) -> None:
        self.fname = fname

    def changing_file_extensition(self):
        # fname = input('Type here filename with extensition.')
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(self.fname)
        # print(f'{_} : printing filename')
        # print(f'{f_ext} : printing file extensition')

        # JOining file extensition with random_hex.
        path_file = random_hex + f_ext
        # print(path_file)

        # Saving with anothername here.
        # path_file.save('Newdon.jpg')
        img = Image.open(fname)
        img.save(path_file)

        # Result returning path_file.
        return path_file

    def folder_encription(self):
        print(self.fname)


if __name__ == '__main__':
    # while True:
    # print('Choose Folder_Excription or File_Excription, just Type Folder without extensition or File with extensition:')
    # file_folder = input()
    fname = input('Type File or Folder Name want to Incrept :')
    object = NameChanging(fname)
    # if fname == 'fname':
    #     object.folder_encription()
    # elif fname == 'fname':
    #     object.changing_file_extensition()

    object.changing_file_extensition()

    # print('If you want to continue "C" or exit() "N"')
    # chose = input()
    # if chose == 'C' or 'c':
    #     try:
    #         continue
    #     except:
    #         print('Type C or c')

    # elif chose == 'N' or 'n':
    #     sys.exit()
