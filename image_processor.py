import os, gdal


in_path = os.path.join(os.getcwd())
dir_sat = 'sat_tiff'
sat_images = os.listdir(os.path.join(os.getcwd(),dir_sat))
# input_filename = '\\test.tif'

out_path = os.path.join(os.getcwd(),'images_tiff')
# output_filename = 'tile_'

tile_size_x = 2000
tile_size_y = 2000

for sat_image in sat_images:
    input_filename = os.path.join(in_path,dir_sat,sat_image)
    ds = gdal.Open(input_filename)
    band = ds.GetRasterBand(1)
    xsize = band.XSize
    ysize = band.YSize

    for i in range(0, xsize, tile_size_x):
        for j in range(0, ysize, tile_size_y):
            com_string = "gdal_translate -of GTIFF -srcwin "+ str(i)+ ", " + \
            str(j) + ", " + str(tile_size_x) + ", " + str(tile_size_y) + " " + \
            os.path.join(in_path,input_filename) + " " + \
            os.path.join(out_path,sat_image.replace(".tif","_")) + str(i) + "_" + str(j) + ".tif"
            os.system(com_string)

for filename in os.listdir(os.path.join(os.getcwd(),'images_tiff')):
    input_file = os.path.join(os.getcwd(),'images_tiff',filename)
    save_file = os.path.join(os.getcwd(),'images_jpeg',filename.replace('.tif','.jpeg'))
    com_string = 'gdal_translate -of JPEG '+input_file+' '+ save_file
    os.system(com_string)
