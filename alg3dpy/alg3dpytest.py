import os
os.system('cls')
os.system('echo Hey... this is a test!')
import alg3dpy as ag
import numpy as np
print 'ckpt1'
pt1  =  ag.Vec( np.array([10,45*np.pi/180.,0],dtype=ag.FLOAT) )
pt2  =  ag.Vec( np.array([10,45*np.pi/180.,100],dtype=ag.FLOAT) )

print 'ckpt2'
z     = np.array([0,0,-1] , dtype=ag.FLOAT)
vecxz = np.array([1,0,-1] , dtype=ag.FLOAT)
c1    = ag.CoordC(1, ag.O, ag.CSYSGLOBAL ,z, vecxz) 
c1.rebuild()
print 'ckpt3'

newO  = np.array([14.1421356,0,0], dtype=ag.FLOAT)
z     = np.array([0,0,1]  , dtype=ag.FLOAT)
vecxz = np.array([-1,0,1]  , dtype=ag.FLOAT)
print 'ckpt4'
c2    = ag.CoordC(2, newO, ag.CSYSGLOBAL, ag.Z, vecxz) 
print 'ckpt5'
c2.rebuild()
print 'ckpt6'

print c1
print c2
print pt2
pt_new = c1.transform( pt2, c2 )
print pt_new
