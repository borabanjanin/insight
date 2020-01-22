import os, gdal

in_path = os.path.join(os.getcwd())
input_filename = 'test.tif'
# input_filename = '\\test.tif'

out_path = os.path.join(os.getcwd(),'images_tiff')
# out_path = 'C:\\Code\\Python\\insight\\images'
output_filename = 'tile_'

tile_size_x = 500
tile_size_y = 500

ds = gdal.Open(input_filename)
band = ds.GetRasterBand(1)
xsize = band.XSize
ysize = band.YSize

for i in range(0, xsize, tile_size_x):
    for j in range(0, ysize, tile_size_y):
        com_string = "gdal_translate -of GTIFF -srcwin " + str(i)+ ", " + \
        str(j) + ", " + str(tile_size_x) + ", " + str(tile_size_y) + " " + \
        os.path.join(in_path,input_filename) + " " + \
        os.path.join(out_path,output_filename) + str(i) + "_" + str(j) + ".tif"
        os.system(com_string)

for filename in os.listdir(os.path.join(os.getcwd(),'images_tiff')):
    input_file = os.path.join(os.getcwd(),'images_tiff',filename)
    save_file = os.path.join(os.getcwd(),'images_png',filename.replace('.tif','.png'))
    com_string = 'gdal_translate -of PNG '+input_file+' '+ save_file
    os.system(com_string)
