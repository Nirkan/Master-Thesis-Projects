import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
 
w1 = [8.6,5.2,6.1,10,3.9,3.3,6.1,4.2,4.2,3.2,7.1,3.8,4.0,9.8,5.2,6.7,4.1,4.7,5.4,5.3,3.5]

w2 = [6.7,4.6,14.5,7.8,4.5,4.5,4.9,4.7,3.6,5.3,7.0,4.8,4.2,5.5,6.6,5.5,5.8,4.4,4.7,6.0,5.3]

vw1 = [68,25,21,27,39,43,27,31,30,19,76,37,20,51,16,19,36,76,39,78,74]

vw2 = [67,76,68,51,23,44,20,55,45,44,68,36,44,54,21,22,35,82,86,65,90]

Theta1d = [0,68.4,72,51.1,40.1,0,58,45.2,47,69.8,0,60.9,47,47.9,77.8,73.7,64.9,26.6,62.7,23.4,29.8]

Theta2d = [28.2,0,26.5,0,57.6,30.4,62.3,0,35.1,0,0,58,49.7,37.4,72,73.2,67.1,24.3,17.1,43.8,0]



#w1 = [8.6,5.2,6.1,10,3.9,3.3,6.1,4.2,4.2,3.2,7.1,3.8,4.0,9.8,5.2,6.7,4.1,4.7,5.4,5.3,3.5,5.9,4.5,4.3,4.9,4.0,5.0,5.6,4.2,6.2,4.3,3.9]

#w2 = [6.7,4.6,14.5,7.8,4.5,4.5,4.9,4.7,3.6,5.3,7.0,4.8,4.2,5.5,6.6,5.5,5.8,4.4,4.7,6.0,5.3,5.9,4.5,4.3,4.9,4.0,5.0,5.6,4.2,6.2,4.3,3.9]

#vw1 = [68,25,21,27,39,43,27,31,30,19,76,37,20,51,16,19,36,76,39,78,74,39,86,41,39,52,38,36,30,44,85,73]

#vw2 = [67,76,68,51,23,44,20,55,45,44,68,36,44,54,21,22,35,82,86,65,90,39,86,41,39,52,38,36,30,44,85,73]

#Theta1d = [0,68.4,72,51.1,40.1,0,58,45.2,47,69.8,0,60.9,47,47.9,77.8,73.7,64.9,26.6,62.7,23.4,29.8,62.7,17.1,61.2,62.7,54.7,65,66.4,70.5,60.7,0,30.8]

#Theta2d = [28.2,0,26.5,0,57.6,30.4,62.3,0,35.1,0,0,58,49.7,37.4,72,73.2,67.1,24.3,17.1,43.8,0,62.7,17.1,61.2,62.7,54.7,65,66.4,70.5,60.7,0,30.8]



# convert degrees to radians

Theta1 = [Theta1d*(np.pi/180) for Theta1d in Theta1d]

Theta2 = [Theta2d*(np.pi/180) for Theta2d in Theta2d]



w1T = [w1*(np.cos(Theta1)) for w1,Theta1 in zip(w1,Theta1)]

w2T = [w2*(np.cos(Theta2)) for w2,Theta2 in zip(w2,Theta2)]

vw1T = [vw1/(np.cos(Theta1)) for vw1,Theta1 in zip(vw1,Theta1)]

vw2T = [vw2/(np.cos(Theta2)) for vw2,Theta2 in zip(vw2,Theta2)] 


w = [(w1T+w2T)/2 for w1T,w2T in zip(w1T,w2T)]

vw = [(vw1T+vw2T)/2 for vw1T,vw2T in zip(vw1T,vw2T)]

print('Theta1 = ', [round(Theta1,2) for Theta1 in Theta1])
print('Theta2 = ', [round(Theta2,2) for Theta2 in Theta2])
print('w1 = ', [round(w1, 2) for w1 in w1])
print('w2 = ', [round(w2, 2) for w2 in w2])
print('w1T = ',[round(w1T, 2) for w1T in w1T])
print('w2T = ',[round(w2T, 2) for w2T in w2T])
print('vw1T = ',[round(vw1T, 2) for vw1T in vw1T])
print('vw2T = ',[round(vw2T, 2) for vw2T in vw2T])


print(len(w1),len(w2),len(vw1),len(vw2),len(w1T),len(w2T),len(vw1T),len(vw2T),len(w),len(vw))

Age = []

for w,vw in zip(w,vw) : 
	d    = (w/206265)*(3.3*1.018e17)
	age  = d/vw
	agey = age/(3600*24*365)
	
	Age.append(agey)
	

print('Age = ', [round(Age,2) for Age in Age])

dAge = [Age*0.2 for Age in Age]

#plt.plot(Age[0:3], 'Dy', label = 'Region 1')
#plt.plot(Age[3:7], 'xy', label = 'Region 2')
#plt.plot(Age[7:10], 'og', label = 'Region 3')
#plt.plot(Age[10:16], 'vm', label = 'Region 4')
#plt.plot(Age[16:20], '*c', label = 'Region 5')

x1 = [1,2,3]
x2 = [4,5,6,7]
x3 = [8,9,10]
x4 = [11,12,13,14,15,16]
x5 = [17,18,19,20,21]
#x5 = [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]

plt.errorbar(x1,Age[0:3], yerr= dAge[0:3], fmt ='Dy', label = 'Region 1',capsize = 4)
plt.errorbar(x2,Age[3:7], yerr= dAge[3:7], fmt='xy', label = 'Region 2', capsize = 4)
plt.errorbar(x3,Age[7:10], yerr= dAge[7:10],fmt='og', label = 'Region 3', capsize = 4)
plt.errorbar(x4,Age[10:16],yerr= dAge[10:16], fmt='vm', label = 'Region 4', capsize = 4)
plt.errorbar(x5,Age[16:21],yerr = dAge[16:21], fmt = '*c', label = 'Region 5', capsize = 4)


plt.xlabel('Outflow ID', fontsize = 16)
plt.ylabel('Age (years)', fontsize = 16)

#plt.xlim([0, 20.5])
plt.xticks([1,5,10,15,20])  

plt.legend(loc = 'upper right')

plt.show()
 


