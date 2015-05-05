import unittest
from pysces.timestepper import *
from pysces.body import flat_plate
from pysces.panel import BoundVortices
import numpy as np
from numpy.testing import assert_array_equal, assert_array_almost_equal

class TestTimestepper(unittest.TestCase):
    def test_euler(self):
        body = flat_plate(20)
        Uinfty = (1,0)
        dt = 0.1
        flow = ExplicitEuler(body, Uinfty, dt, BoundVortices)
        self.assertEqual(flow.time, 0)
        self.assertEqual(len(flow.wake), 1)
        vort = flow.bound.vortices
        self.assertEqual(vort.circulation, -flow.wake.circulation)
        flow.advance()
        self.assertEqual(flow.time, dt)
        self.assertEqual(len(flow.wake), 2)

    def test_rk4(self):
        body = flat_plate(20)
        Uinfty = (1,0)
        dt = 0.1
        flow = RungeKutta4(body, Uinfty, dt, BoundVortices)
        self.assertEqual(flow.time, 0)
        self.assertEqual(len(flow.wake), 1)
        vort = flow.bound.vortices
        self.assertEqual(vort.circulation, -flow.wake.circulation)
        flow.advance()
        self.assertEqual(flow.time, dt)
        self.assertEqual(len(flow.wake), 2)

if __name__ == "__main__":
    unittest.main()