import numpy as np
data = np.genfromtxt("sensor_data.csv",delimiter=",",skip_header=1,usecols=(1,2,3,4))
strdt = np.genfromtxt("sensor_data.csv",delimiter=",",skip_header=1,usecols=(0),dtype=str)
#temperature
d1 = data[:,0]
mx1 = d1.max()
mn1 = d1.min()
avg1 = d1.mean()
print(f"Temperature -> Maximun : {mx1}, Minimum : {mn1}, Average : {avg1}")
#distance
d2 = data[:,1]
mx2 = d2.max()
mn2 = d2.min()
avg2 = d2.mean()
print(f"Distance -> Maximun : {mx2}, Minimum : {mn2}, Average : {avg2}")
#battery
d3 = data[:,2]
mx3 = d3.max()
mn3 = d3.min()
avg3 = d3.mean()
print(f"Battery -> Maximun : {mx3}, Minimum : {mn3}, Average : {avg3}")
#humidity
d4 = data[:,3]
mx4 = d4.max()
mn4 = d4.min()
avg4 = d4.mean()
print(f"Humidity -> Maximun : {mx4}, Minimum : {mn4}, Average : {avg4}")
#index for highest temperature
ind = np.argmax(d1)

with open("sensor_data!.csv",'w') as ft:
    ft.write(f"Temperature -> Maximun : {mx1}, Minimum : {mn1}, Average : {avg1}\n")
    ft.write(f"Distance -> Maximun : {mx2}, Minimum : {mn2}, Average : {avg2}\n")
    ft.write(f"Battery -> Maximun : {mx3}, Minimum : {mn3}, Average : {avg3}\n")
    ft.write(f"Humidity -> Maximun : {mx4}, Minimum : {mn4}, Average : {avg4}\n")
    ft.write(f"Maximum Temperature at : {strdt[ind]}")
