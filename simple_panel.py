import numpy as np
from bempy import *

# x = [1,0]
# y = [0,0]
# x = [0,0,0]
# y = [0,1,2]
x = [2,1,0]
y = [0,0,0]
points = np.vstack([x, y])
body = Body(points)
body_panels = BoundVortexPanels(body)
body_panels.update_strengths()
xvort, gam = body_panels.vortices
xc = body_panels.collocation_pts
Uinfty = np.array((1,0))
vel = np.zeros((2,xc.shape[1])) + Uinfty[:,np.newaxis]
for xv, g in zip(xvort.T, gam):
    vel += body_panels.induced_velocity(xc, xv, g)
vel_dot_n = np.sum(vel * body_panels.normals, 0)
print("gam:" + str(gam))
print("vel: " + str(vel))
print("vel . n:" + str(vel_dot_n))