import wave
import matplotlib.pyplot as plt
import numpy as np

#Reference: https://blog.csdn.net/xsc_c/article/details/8941338
def read_wave_data(file_path):
	#open a wave file, and return a Wave_read object
	f = wave.open(file_path,"rb")
	#read the wave's format infomation,and return a tuple
	params = f.getparams()
	#get the info
	nchannels, sampwidth, framerate, nframes = params[:4]
	#Reads and returns nframes of audio, as a string of bytes. 
	str_data = f.readframes(nframes)
	#close the stream
	f.close()
	#turn the wave's data to array
	wave_data = np.frombuffer(str_data, dtype = np.short)
	#for the data is stereo,and format is LRLRLR...
	#shape the array to n*2(-1 means fit the y coordinate)
	wave_data.shape = -1, 2
	#transpose the data
	wave_data = wave_data.T
	#calculate the time bar
	time = np.arange(0, nframes) * (1.0/framerate)
	return wave_data, time
 
def main():
	wave_data, time = read_wave_data(input('Enter the path of first wav file:').replace('"',''))	
	wave_data2, time2 = read_wave_data(input('Enter the path of second wav file:').replace('"',''))
	#draw the wave
	plt.subplot(321)
	plt.plot(time, wave_data[0])
	plt.title('First File(Left Channel)')
	plt.subplot(322)
	plt.plot(time, wave_data[1])
	plt.title('First File(Right Channel)')
	plt.subplot(323)
	plt.plot(time, wave_data2[0], c = "g")
	plt.title('Second File(Left Channel)')
	plt.subplot(324)
	plt.plot(time, wave_data2[1], c = "g")
	plt.title('Second File(Right Channel)')
	plt.subplot(325)
	plt.plot(time, wave_data[0]-wave_data2[0], c = "r")
	plt.title('Difference between Left Channel')
	plt.subplot(326)
	plt.plot(time, wave_data[1]-wave_data2[1], c = "r")
	plt.title('Difference between Right Channel')
	plt.show()
	
if __name__ == "__main__":
	main()