from core.yolo_config import cfg
from core.functions import *

class train_network():
    def __init__(self):
        classes = read_clases(cfg.classes)
        print(classes)

if __name__ == "__main__":
    train_network()