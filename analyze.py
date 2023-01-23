import numpy
import matplotlib.pyplot


#backLegSensorValues = numpy.load('data/info.npy', mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII',  max_header_size=10000)
#FrontLegSensorValues = numpy.load('data/frontInfo.npy', mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII',  max_header_size=10000)
#matplotlib.pyplot.plot(backLegSensorValues,linewidth=4, label = "back")

#matplotlib.pyplot.plot(FrontLegSensorValues, label = "front")
#matplotlib.pyplot.legend()
sins = numpy.load('data/back_sins.npy', mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII',  max_header_size=10000)
fsins = numpy.load('data/front_sins.npy', mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII',  max_header_size=10000)
matplotlib.pyplot.plot(sins, linewidth=4, label = "sins")
matplotlib.pyplot.plot(fsins, label = "fsins")
matplotlib.pyplot.show()
