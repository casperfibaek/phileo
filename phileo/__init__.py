try:
    from osgeo import gdal
    gdal.UseExceptions()
except:
    print("GDAL not installed. Some functions requiring image IO may not work.")

__version__ = "0.0.1"