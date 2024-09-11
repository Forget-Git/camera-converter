import os
from common import convert

extension = "dng"

if __name__ == "__main__":
    camera = input("Select Camera (fuji,sony,ricoh): ")
    dir = input("Please input the dir: ")
    convert(dir, camera, extension)
