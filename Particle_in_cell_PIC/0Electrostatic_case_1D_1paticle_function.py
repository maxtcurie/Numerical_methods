import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt

Lx=1
nx=1000
E0=10


m=1.
q=-1.
dt=0.001

x0=0.
v0=1.
t0=0.

def init(E0=1,nx=100):
	Ex=np.concatenate((np.zeros(nx),E0*np.ones(nx),np.zeros(nx)))
	x_grid=np.linspace(0,Lx,len(Ex))
	return Ex,x_grid

def particle_mover(x,v,t,x_grid,Ex,dt):
	i=np.argmin(abs(x-x_grid))
	#F=q*E(x)
	F=q*Ex[i] 
	a=F/m 
	dv=a*dt
	v=v+dv
	x=x+v*dt
	t=t+dt

	return x,v,a,t


def particle_calc(Ex,x_grid,dt,x0,v0,t0):
	keep_going=True
	x=x0
	v=v0
	t=t0
	x_list=[]
	a_list=[]
	t_list=[]
	while keep_going:
		x,v,a,t=particle_mover(x,v,t,x_grid,Ex,dt)

		x_list.append(x)
		a_list.append(a)
		t_list.append(t)

		if x>Lx or x<0:
			keep_going=False

	return x_list,a_list,t_list

Ex,x_grid=init(E0=E0,nx=nx)

x_list,a_list,t_list=particle_calc(Ex,x_grid,dt,x0,v0,t0)

plt.clf()
plt.scatter(x_list,t_list,s=5,label='particle')
plt.plot(x_grid,Ex/np.max(Ex),alpha=0.5,color='red',label='E field')
plt.xlabel('x')
plt.ylabel('time')
plt.legend()
plt.show()

l=Lx/3.
v_min=np.sqrt(2*q*E0*l/m)
print('v_min='+str(v_min))

#one particle does not have effect the field 

#v_min to go through the electric field barrer 
#1/2*m*v_min^2=q*E*l 
#v_min=np.sqrt(2*q*E*l/m)

