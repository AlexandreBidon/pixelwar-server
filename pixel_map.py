import logging


class PixelMap():

    def __init__(self):
        self.__matrix = [["#ffffff"] * 37] * 57

    def modify_pixel(self, data):
        logging.info("Pixel at {},{} was changed".format(data["x"], data["y"]))
        self.__matrix[data["y"]][data["x"]] = data["color"]

    def return_matrix(self):
        return self.__matrix
