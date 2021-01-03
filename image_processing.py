import cv2 as cv


def process(image):
    read_image = cv.imread(cv.samples.findFile(image))
    image_rgb = cv.cvtColor(read_image, cv.COLOR_BGR2RGB)
    image_gray = cv.cvtColor(image_rgb, cv.COLOR_RGB2GRAY)
    return image_gray


def image_read(image):
    return cv.imread(cv.samples.findFile(image))

