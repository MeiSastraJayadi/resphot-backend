import cv2
import numpy as np

def read_image(directory) : 
    img = cv2.imread(directory)
    greater = max(list(img.shape[0:2]))
    size = (greater, greater)
    
    img = cv2.resize(img, size)
    return img


def function_to_restore(directory : str) : 
    img = cv2.imread(directory)
    greater = max(list(img.shape[0:2]))
    size = (greater, greater)
    
    img = cv2.resize(img, size)
    ycrcb_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    kernel = np.ones((5, 5), np.uint32)/25

    ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])
    equalize = cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR) 
    equalize = cv2.filter2D(equalize, -1, kernel)
    path = directory.split("/")
    name = path[3]
    cv2.imwrite(f"./application/images/{name}", equalize)
    # return equalize
