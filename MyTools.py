import numpy as np
import sympy as sp
import base64

# Defining a Factorial Function:
def fac(n):
    result = 1
    for x in range(1, n+1):
        result *= x
    return result

# ____________________________________________________________________________________________

# Defining Taylor Expansions relating Sin(alpha) and Cos(alpha) to alpha:
def sin(alpha):
    result_1 = 0
    for i in range(50):
        result_1 += ((((-1)**i)/fac(2*i + 1))*(alpha**((2*i) + 1)))
    return result_1


def cos(alpha):
    result_2 = 0
    for i in range(50):
        result_2 += ((((-1)**i)/fac(2*i))*(alpha**(2*i)))
    return result_2

# ____________________________________________________________________________________________

# Defining an non running file variables swap for "eval":
def Old_Variables_Swap(F):
    variables_library = globals()
    F_spaced = F.replace("*", " * ").replace("+", " + ").replace("-", " - ")\
    .replace("/", " / ").replace("(", " ( ").replace(")", " ) ")
    F_parts = F_spaced.split()
    for variable in F_parts:
        if variable in variables_library:
            Variable_value = str(variables_library[variable])
            F = F.replace(variable, Variable_value)
    return F


def varswap(F):
    F_Swapped = sp.sympify(F, locals=globals())
    return F_Swapped

#____________________________________________________________________________________________

# Defining a Pythagorean Theorem function for the Resultant Vector of 2 others:
def RVector(a,b):
    return (a**2 + b**2)**0.5

#____________________________________________________________________________________________

# Defining a faster resultant vector function for 3D:
def RVector3(a,b,c):
    return (a**2 + b**2 + c**2)**0.5

#____________________________________________________________________________________________

# Defining function to extract 
def quadratic_coefficients(F):
    expression = sp.simplify(sp.sympify(F))
    variable = list(expression.free_symbols)[0]
    Coef_a = expression.coeff(variable**2)
    Coef_b = expression.coeff(variable)
    Coef_c = expression.as_coeff_Add()[0]
    Ordered_Coefficients = np.array([float(Coef_a), float(Coef_b), float(Coef_c)])
    return Ordered_Coefficients

#____________________________________________________________________________________________

# Defining a quadratic expression solver for real roots:
def quadratic_solve_real(F):
    Roots = np.roots(quadratic_coefficients(F))
    Real_Roots = np.isreal(Roots)
    if not any(Real_Roots):
        raise ValueError("Roots are imaginary, can't proceed-.")
    return Roots[Real_Roots].real

#____________________________________________________________________________________________

# Defining an automatic pull of a quadratic expression biggest root:
def biggest_root(F):
    roots = quadratic_solve_real(F)
    return np.max(roots)

#____________________________________________________________________________________________

# Defining the ordered pair of the function's peak:
def peak_xy(F):
    a = quadratic_coefficients(F)[0]
    b = quadratic_coefficients(F)[1]
    c = quadratic_coefficients(F)[2]
    peak_x = (-b)/(2*a)
    peak_y = (-((b**2) - (4*a*c)))/(4*a)
    peak_x_y = np.array([float(peak_x), float(peak_y)])
    return peak_x_y

#____________________________________________________________________________________________

# Difining an derivating mech for quadratic equations:
# (just kept it because I did it myself and was proud of it lol)
def derivate_quadratic(F):
    Raw_Expression = sp.sympify(F)
    Simp_Expression = sp.simplify(Raw_Expression)
    Expression_Terms = Simp_Expression.as_ordered_terms()
    Coef_a = Expression_Terms[0].as_coeff_Mul()[0]
    Coef_b = Expression_Terms[1].as_coeff_Mul()[0]
    variable = list(Simp_Expression.free_symbols)[0]
    new_a = Coef_a*2
    new_b = Coef_b
    derivate_form = new_a*variable + new_b
    return derivate_form

#____________________________________________________________________________________________

# Defining an derivating mech:
# (This goes for any expressions and it's cleaner than mine unfortunatelly)
def derivate(F, x):
    Expression = sp.simplify(sp.sympify(F))
    return sp.diff(Expression, x)

#____________________________________________________________________________________________

# Insert in this order: Vector Magnitude, Elevation, Azimuth (xz Vector - x_axis).
def Decomp_3DVector(M, Z, O):
    import numpy as np
    My = np.sin(Z)*M
    Mx = np.cos(Z)*np.cos(O)*M
    Mz = np.cos(Z)*np.sin(O)*M
    return np.array([Mx, My, Mz])

#____________________________________________________________________________________________

# Insert in this order: Vector Magnitude, Elevation.
def Decomp_2DVector(M, Z):
    import numpy as np
    My = np.sin(Z)*M
    Mx = np.cos(Z)
    return np.array([Mx, My])

#____________________________________________________________________________________________

# C must be an np.array of the following variables (ordered):
# (Syo, Vo, Ax, Ay, Az, Target_Height)
def Angles_MaxDisp(C):

    import MyTools as mt
    import numpy as np

    Syo = C[0]
    Vo = C[1]
    Ax = C[2]
    Ay = C[3]
    Az = C[4]
    Target_Height = C[5]
    
    BestDisp = -1
    Best_Z = 0
    Best_O = 0
    
    for elevation in np.linspace(0, 90, 901):
        for azimuth in np.linspace(0, 360, 361):
            
            Z = np.radians(elevation)
            O = np.radians(azimuth)
            Vo_Components = mt.Decomp_3DVector(Vo, Z, O)
            Vxo = Vo_Components[0]
            Vyo = Vo_Components[1]
            Vzo = Vo_Components[2]
            
            discriminant = (Vyo**2 - 2*Ay*(Syo - Target_Height))
            if discriminant < 0:
                continue
            
            Total_Time = (-Vyo - ((Vyo)**2 - 2*Ay*(Syo - Target_Height))**0.5)/Ay
            MaxX_Disp = (Vxo*Total_Time) + (Ax*(Total_Time**2))/2
            MaxZ_Disp = (Vzo*Total_Time) + (Az*(Total_Time**2))/2
            Max_Disp = mt.RVector(MaxX_Disp, MaxZ_Disp)
            
            if Max_Disp > (BestDisp + 0.0001):
                BestDisp = Max_Disp
                Best_Z = Z
                Best_O = O
                
    return np.array([np.degrees(Best_Z), np.degrees(Best_O)])

#____________________________________________________________________________________________

# Units conversion:
def I_velocity(inputed, unit):
    v_conversions = {"m/s": 1, "km/h": 1/3.6, "mi/h": 0.44704}
    return (inputed * v_conversions[unit])

def I_distance(inputed, unit):
    d_conversions = {"m": 1, "km": 1000, "mi": 1600, "ft": 0.3048}
    return (inputed * d_conversions[unit])

def  I_angle(inputed, unit):
    an_conversions = {"rad": 1, "degree": np.pi/180}
    return (inputed * an_conversions[unit])

def I_acceleration(inputed, unit):
    a_conversions = {"m/s2": 1, "km/h2": 1/12.960, "mi/h2": 0.000124178}
    return (inputed * a_conversions[unit])

def Unit_velocity(inputed, unit):
    v_conversions = {"m/s": 1, "km/h": 3.6, "mi/h": 1/0.44704}
    return (inputed * v_conversions[unit])

def Unit_distance(inputed, unit):
    d_conversions = {"m": 1, "km": 1/1000, "mi": 1/1600, "ft": 1/0.3048}
    return (inputed * d_conversions[unit])

def  Unit_angle(inputed, unit):
    an_conversions = {"rad": 1, "degree": 180/np.pi}
    return (inputed * an_conversions[unit])

def Unit_acceleration(inputed, unit):
    a_conversions = {"m/s2": 1, "km/h2": 12.960, "mi/h2": 1/0.000124178}
    return (inputed * a_conversions[unit])

#____________________________________________________________________________________________

def base64_image(image_file):
    with open(image_file, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

#____________________________________________________________________________________________

# Physics formulas (laziness): 

def S2(So, Vo, A, t):
    return So + (Vo*t) + ((A*(t**2))/2)

