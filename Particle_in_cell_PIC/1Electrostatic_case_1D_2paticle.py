import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import copy

Lx=1
nx=300
nt=10
E0=100

m=1.
q=-0.1
dt=0.01

x0=np.array([0.0,0.1,0.2]) #3 particles
v0=np.array([1.]*len(x0))
t0=np.array([0.]*len(x0))

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
	#print(t)
	return x,v,a,t

def field_calc(x,v,x_grid,Ex):
	
	#count the particle
	dx=abs(x_grid[1]-x_grid[0])
	particle_count=np.zeros(np.shape(Ex))
	for i in range(len(x)):
		for j in range(len(x_grid)):
			if x_grid[j]-0.5*dx<x[i] and x[i]<x_grid[j]+0.5*dx:
				particle_count[j]=particle_count[j]+q 
	#print(particle_count)
	#calculate the electric field
	Ex_t=np.zeros(np.shape(Ex))
	for i in range(len(x_grid)):
		for j in range(len(x_grid)):
			if j==i:
				pass
			else:
				Ex_t[i]=Ex_t[i]+q*particle_count[j]/(abs(x_grid[i]-x_grid[j]))**2.

	Ex_t=Ex+Ex_t

	return Ex_t

def particle_calc(Ex,x_grid,dt,x0,v0,t0,nt):
	keep_going=True
	x=x0
	v=v0
	a=np.zeros(np.shape(x))
	t=t0
	x_list=[]
	a_list=[]
	t_list=[]
	#for j in range(nt):
	while keep_going:
		Ex_t=field_calc(x,v,x_grid,Ex)

		for i in range(len(x)):
			x[i],v[i],a[i],t[i]=particle_mover(x[i],v[i],t[i],x_grid,Ex_t,dt)
		x=copy.deepcopy(x)
		v=copy.deepcopy(v)
		a=copy.deepcopy(a)
		t=copy.deepcopy(t)

		print(t)
		x_list.append(x)
		a_list.append(a)
		t_list.append(t)
		#print(t_list)

		if np.min(x)>Lx or np.max(x)<0:
			keep_going=False
	print(t_list)	
	return x_list,a_list,t_list

Ex,x_grid=init(E0=E0,nx=nx)

x_list,a_list,t_list=particle_calc(Ex,x_grid,dt,x0,v0,t0,nt)

x_list=np.array(x_list)
t_list=np.array(t_list)

print(t_list)
print(np.shape(x_list))

plt.clf()
for i in range(len(x0)):
	plt.scatter(x_list[:,i],t_list[:,i],s=5,label='particle')
plt.plot(x_grid,Ex/np.max(Ex),alpha=0.5,color='red',label='E field')
plt.xlabel('x')
plt.ylabel('time')
#plt.legend()
plt.show()



