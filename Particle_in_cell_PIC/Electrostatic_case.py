#Good video: https://youtu.be/I09QeVDoEZY
#from wiki: https://en.wikipedia.org/wiki/Particle-in-cell
#example: https://www.particleincell.com/2010/es-pic-method/

import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt


#notation
#x100=x_{k+2}
#x150=x_{k+0.5}
#x000=x_{k}
#x050=x_{k-0.5}

(x200-x100)/dt=v150
(v150-v050)/dt=q/m*(E100+0.5*(v150+v050)*B100)

