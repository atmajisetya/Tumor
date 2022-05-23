from cProfile import run
from detect import *
from PIL import Image


img_path = "C:\Capstone\Tumor\yolov5\multi"
weight_path = "C:\Capstone\Tumor\yolov5\model_epoch300_yolov5s_augmented.pt"

# list_img = ["C:\Capstone\Tumor\yolov5\multi\y94.jpg", "C:\Capstone\Tumor\yolov5\multi\y95.jpg",
#             "C:\Capstone\Tumor\yolov5\multi\y97.jpg", "C:\Capstone\Tumor\yolov5\multi\y98.jpg", "C:\Capstone\Tumor\yolov5\multi\y99.jpg"]


result_folder_path = run(weights=weight_path, source=img_path)
#print("folder hasil neng kene dab: ", result_folder_path)
list_img = os.listdir("runs\detect\exp6")
list_img_path = []
for x in list_img:
    list_img_path.append("runs\detect\exp6" + "\\" + x)
print(list_img_path)

im = Image.open(r"runs\\detect\\exp6\\y99.jpg")
im.show()
