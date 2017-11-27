# encoding:utf-8
import numpy
import matplotlib.pyplot

def main():
	x = numpy.linspace(0,3,4)  # xの値域(0, 1, 2, 3)
	y = x + 1               # 直線の式
	matplotlib.pyplot.plot(x,y,"r-")      # 直線を引く
	matplotlib.pyplot.show()              # グラフ表示

if __name__ == '__main__':
	main()
