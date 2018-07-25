from math import sqrt, acos, degrees, pi
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MESSAGE = 'Cannot normalize the zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT_MESSAGE = 'No unique parallel component'


    def __init__(self, coordinates):
        
        try:
            if not coordinates:
                raise ValueError
            
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:    
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):

        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):

        return self.coordinates == v.coordinates

    
    def __add__(self, v):

        if self.dimension != v.dimension:
            raise ValueError('Vectors must be of equal dimension')

        return Vector([x+y for x,y in zip(self.coordinates, v.coordinates)])

    
    def __sub__(self, v):

        if self.dimension != v.dimension:
            raise Exception('Vectors must be of equal dimension')

        return Vector([x-y for x,y in zip(self.coordinates, v.coordinates)])

    
    def __mul__(self, s):

        if type(s) != int and type(s) != float:
            raise TypeError('Multiplication must be by scalar')

        return Vector([coordinate * Decimal(s) for coordinate in self.coordinates])

    
    def __rmul__(self, s):
        
        if type(s) != int and type(s) != float and type(s) != Decimal:
            raise TypeError('Multiplication must be by scalar')

        return Vector([coordinate * Decimal(s) for coordinate in self.coordinates])

    
    def magnitude(self):

        coordinates_squared = [coordinate**2 for coordinate in self.coordinates]

        return sum(coordinates_squared).sqrt()

    
    def normalize(self):

        try: 
            magnitude = self.magnitude()
            return (Decimal('1.0') / magnitude) * self

        except:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MESSAGE)

    
    def scalar_product(self, v):

        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    
    def angle_with(self, v, in_degrees=False):

        try:
            u1 = self.normalize()
            u2 = v.normalize()
            angle = acos(u1.scalar_product(u2))

            if in_degrees:
                angle = degrees(angle)
            
            return angle

        except Exception as e:
            
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MESSAGE:
                raise Exception('Cannot compute angle with the zero vector')

            raise e

    
    def get_parallel_component(self, basis):
        
        try:
            unit_basis = basis.normalize()
            weight = self.scalar_product(unit_basis)

            return weight * unit_basis

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MESSAGE:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MESSAGE)

            raise e
   

    def get_orthogonal_component(self, basis):
        
        try:
            return self - self.parallel_component(basis)

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MESSAGE:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MESSAGE)

            raise e


    def cross_product_with(self, v):

        self_coords = self.coordinates
        v_coords = v.coordinates

        if self.dimension == 2:
            self_coords += tuple([0])
            v_coords += tuple([0])
        
        x = self_coords[1]*v_coords[2] - v_coords[1]*self_coords[2]
        y = -(self_coords[0]*v_coords[2] - v_coords[0]*self_coords[2])
        z = self_coords[0]*v_coords[1] - v_coords[0]*self_coords[1]

        return Vector([x, y, z])


    def is_parallel(self, v):

        return (self.is_zero() or v.is_zero() or 
            self.angle_with(v) == pi or self.angle_with(v) == 0)


    def is_zero(self, tolerance=1e-10):

        return self.magnitude() < tolerance


# print Vector([8.462, 7.893, -8.187]).cross_product_with(Vector([6.984, -5.975, 4.778]))
# print Vector([-8.987, -9.838, 5.031]).cross_product_with(Vector([-4.268, -1.861, -8.866])).get_magnitude()
# print Decimal('0.5') * Vector([1.5, 9.547, 3.691]).cross_product_with(Vector([-6.007, 0.124, 5.772])).get_magnitude()

# print Vector([1, 2]).scalar_product_with(Vector([-2, 1]))