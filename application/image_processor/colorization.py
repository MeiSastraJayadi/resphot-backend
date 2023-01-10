import numpy as np
from PIL import Image
import tensorflow as tf
import cv2
from .main_proc import read_image

generator = tf.keras.models.load_model("./application/result/keras_generator")

def coloring_image(path) : 
    # img = read_image(path)
    # img = cv2.resize(img, (120, 120))
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = np.array(((img,)))
    # print(img.shape)
    # result = generator(img).numpy()
    # result = Image.fromarray(result * 255).astype('uint8').resize(1024, 1024) 
    # print(image.shape)
    direc = path.split("/")
    name = direc[3]
    image = Image.open(path).resize((120, 120))
    gray_image = image.convert("L") 
    array_image = (np.asarray(gray_image).reshape((120, 120, 1)))/ 255
    image = np.array((array_image,))
    result = generator(image).numpy()
    image = Image.fromarray((result[0] * 255).astype("uint8")).resize((1024, 1024))
    image = np.asanyarray(image)
    cv2.imwrite(f"./application/images/{name}", image)
