from PIL import Image
import glob, os

in_path = os.path.join(os.getcwd(),'images_jpeg')
out_path = os.path.join(os.getcwd(),'compressed_images_jpeg')
# dir_sat = 'sat_tiff'
#
D = 500
#
# img = Image.open(os.path.join("/mnt/c/Code/Python/insight",'images_jpeg','tile_10000_2000.jpeg')).convert("RGB")
# img.resize((500, 500), Image.BILINEAR)


os.chdir(in_path)
for file in glob.glob("*.jpeg"):
    print(file)
    img = Image.open(file).convert("RGB")
    img = img.resize((D, D), Image.BILINEAR)
    img.save(os.path.join(out_path,file))
