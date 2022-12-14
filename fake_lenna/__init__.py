import cv2

from fake_lenna.views import LennaController
from src.cmm.service.common import Common

if __name__ == '__main__':
    while True:
        menu = Common.menu(["close", "show original", "Edge with Canny"])
        if menu == "0":
            print(" ### close ### ")
            break
        elif menu == "1":
            print(" ### show original ### ")
            c = LennaController()
            this = c.modeling('Lenna.png')
            print(f'Shape is {this.shape}')
            cv2.imshow('Gray', this)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif menu == "2":
            print(" ### Edge with Canny ### ")

        else:
            print(" ### error ### ")

'''
a = cv2.imread('./data/Lenna.png', cv2.IMREAD_COLOR)
print(f'Shape is {a.shape}')
cv2.imshow('Gray', a)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''