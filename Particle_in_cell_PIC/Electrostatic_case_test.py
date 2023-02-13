import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt

#basic parameters
n0=10.**12
phi0=0
Te=1
v_drift=7000 #7km/s
phi_p=-7  #7V plate potention 

EPS0 = 8.854e-12		#permittivity of free space
QE = 1.602e-19			#elementary charge
K = 1.381e-23			#boltzmann constant
AMU = 1.661e-27			#atomic mass unit
M = 32*AMU            	#ion mass (molecular oxygen)

lD = sqrt(EPS0*Te/(n0*QE))    	#Debye length
vth = sqrt(2*QE*Ti/M)			#thermal velocity with Ti in eV

#total n node
nx=16
ny=10
ts=200
dh = lD
np_insert = (ny-1)*15	#insert 15 particles per cell 

#compute some other values
nn = nx*ny             	#total number of nodes
dt = 0.1*dh/v_drift		#time step, at vdrift move 0.10dx
Lx = (nx-1)*dh         	#domain length in x direction
Ly = (ny-1)*dh         	#domain length in y direction

#compute some other values
nn = nx*ny             	#total number of nodes
dt = 0.1*dh/v_drift		#time step, at vdrift move 0.10dx
Lx = (nx-1)*dh        	#domain length in x direction
Ly = (ny-1)*dh         	#domain length in y direction



#specify plate dimensions
box=np.zeros((2,2))
box[1,:] = [floor(nx/3),floor(nx/3)+2]; #x range
box[2,:] = [1,floor(ny/2)];             #y range

#create an object domain for visualization
data = zeros(nx,ny);
for j in range(box[2,1],box[2,2]+1):
    data[box[1,1]:box[1,2],j]=ones(box(1,2)-box(1,1)+1,1);

#calculate specific weight
flux = n0*v_drift*Ly       #flux of entering particles
npt = flux*dt              #number of real particles created per timestep
spwt = npt/np_insert       #specific weight, real particles per macroparticle
mp_q = 1                   #macroparticle charge
max_part=20000             #buffer size

#allocate particle array
part_x = np.zeros((max_part,2)) #particle positions
part_v = np.zeros((max_part,2)) #particle velocities

A = np.zeros((nx,ny))

for i in range(2,nx):
    for j in range(2,ny):
        u=(j-1)*nx+i
        A[u,u] = -4/(dh*dh);    #phi(i,j)
        A[u,u-1]=1/(dh*dh);     #phi(i-1,j)
        A[u,u+1]=1/(dh*dh);     #phi(i+1,j)
        A[u,u-nx]=1/(dh*dh);    #phi(i,j-1)
        A[u,u+nx]=1/(dh*dh);    #phi(i,j+1)

#initialize
phi = np.ones(nx,ny)*phi0         #set initial potential to phi0
np = 0                         #clear number of particles

for it in range(ts):
    den=np.zeros((nx,ny))
    efx=np.zeros((nx,ny))
    efy=np.zeros((nx,ny))

    #deposite particle 
    for p in range(np):
    	

#notation
#x100=x_{k+2}
#x150=x_{k+0.5}
#x000=x_{k}
#x050=x_{k-0.5}

#resources:

#Good video: https://youtu.be/I09QeVDoEZY
#from wiki: https://en.wikipedia.org/wiki/Particle-in-cell


#based on this example Figure 3: 
# https://www.particleincell.com/2010/es-pic-method/

#code explain
#https://www.particleincell.com/2011/particle-in-cell-example/

#MatLab code from source:
# PIC code: https://www.particleincell.com/wp-content/uploads/2011/11/flow_around_plate.m
# field solver: https://www.particleincell.com/wp-content/uploads/2011/11/eval_2dpot_GS.m