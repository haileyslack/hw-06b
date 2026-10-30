
import unittest
from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):

    # Original starter tests
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')

    # Additional equilateral tests
    def testEquilateralLarge(self):
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral')

    # Isosceles tests
    def testIsoscelesA(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isoceles')

    def testIsoscelesB(self):
        self.assertEqual(classifyTriangle(5, 3, 5), 'Isoceles')

    def testIsoscelesC(self):
        self.assertEqual(classifyTriangle(3, 5, 5), 'Isoceles')

    # Scalene tests
    def testScalene(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene')

    # Right triangle tests (different side orders)
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right')

    def testRightTriangleD(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right')

    # Invalid triangle tests
    def testNotTriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')

    def testNotTriangleB(self):
        self.assertEqual(classifyTriangle(1, 2, 4), 'NotATriangle')

    def testNotTriangleC(self):
        self.assertEqual(classifyTriangle(3, 1, 1), 'NotATriangle')

    # Invalid input tests
    def testZeroSide(self):
        self.assertEqual(classifyTriangle(0, 4, 5), 'InvalidInput')

    def testNegativeSide(self):
        self.assertEqual(classifyTriangle(-1, 4, 5), 'InvalidInput')

    def testAboveMaximum(self):
        self.assertEqual(classifyTriangle(201, 5, 5), 'InvalidInput')

    def testNonInteger(self):
        self.assertEqual(classifyTriangle(3.5, 4, 5), 'InvalidInput')

    # Boundary tests
    def testMaximumValid(self):
        self.assertEqual(classifyTriangle(199, 200, 200), 'Isoceles')

    def testMinimumValid(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')

    # Additional invalid input tests
    def testBooleanInput(self):
        self.assertEqual(classifyTriangle(True, 4, 5), 'InvalidInput')

    def testNegativeSecondSide(self):
        self.assertEqual(classifyTriangle(4, -1, 5), 'InvalidInput')

    def testNegativeThirdSide(self):
        self.assertEqual(classifyTriangle(4, 5, -1), 'InvalidInput')

    def testAboveMaximumSecondSide(self):
        self.assertEqual(classifyTriangle(5, 201, 5), 'InvalidInput')

    def testAboveMaximumThirdSide(self):
        self.assertEqual(classifyTriangle(5, 5, 201), 'InvalidInput')

    # Additional triangle inequality boundary tests
    def testTriangleBoundaryA(self):
        self.assertEqual(classifyTriangle(2, 3, 5), 'NotATriangle')

    def testTriangleBoundaryB(self):
        self.assertEqual(classifyTriangle(5, 2, 3), 'NotATriangle')

    def testTriangleBoundaryC(self):
        self.assertEqual(classifyTriangle(3, 5, 2), 'NotATriangle')


if __name__ == '__main__':
    unittest.main()
