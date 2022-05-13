import logging
import json


class PixelMap():

    def __init__(self):
        self.reset()

    def reset(self):
        line = ["#6a5cff"] * 37
        self.__matrix = []
        for i in range(57):
            self.__matrix.append(line.copy())

    def modify_pixel(self, data):
        logging.info("Pixel at {},{} was changed".format(data["x"], data["y"]))
        self.__matrix[data["y"]][data["x"]] = data["color"]

    def return_matrix(self):
        return json.dumps(self.__matrix)
