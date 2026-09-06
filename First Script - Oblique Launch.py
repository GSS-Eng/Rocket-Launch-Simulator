# Constants:
pi = 3.14159265358979323846264
g = -9.81

print("Constants:", "Pi =", pi,",", "g =", g,"m/s")

# Inform precise time of tracking (seconds);
# Inital positions on xyz space;
# Initial velocity module;
# Each Dimension Acceleration;
# The angle of launch V x XZ-Plane.
# The angle between the XZ-Plane projection of V and the X-Axis.
T = 2
Syo = 0
Sxo = 0
Szo = 0
Vo = 30
Ax = 0
Ay = g
Az = 0
Z = pi/4
O = pi/4

print("Point of Time:",T,"s")
print("Initial Position on X-Axis:", Sxo,"m")
print("Initial Position on Y-Axis:", Syo,"m")
print("Initial Position on Z-Axis:", Szo,"m")
print("Angle of Launch (I.Velocity x XZ-Plane):", Z, "rad")
print("Horizontal Angle (I.Velocity projection on XZ-Plane x X-Axis):", O)
print("Initial Velocity:", Vo,"m/s")

# Defining a Factorial Function:
def fac(n):
    result = 1
    for x in range(1, n+1):
        result *= x
    return result

# Defining Taylor Expansions relating Sin(Z) and Cos(Z) to Z:
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

# Defining a Pythagorean Theorem function for the Resultant Vector of 2 others:
def RVector(a,b):
    result_vector = (a**2 + b**2)**0.5
    return result_vector

# Defining a faster resultant vector function for 3D:
def RVector3(a,b,c):
    final_vector = (a**2 + b**2 + c**2)**0.5
    return final_vector

# Verifying the Sin and Cos values:
print("Sin(Z):", sin(Z))
print("Cos(Z):", cos(Z))
print("Sin(O):", sin(O))
print("Cos(O):", cos(O))

# Defining the physics oblique launch formulas:
A_Ground = RVector(Ax, Az)
A = RVector3(Ax, Ay, Az)
Vyo = Vo*sin(Z)
Vxo = Vo*cos(Z)*cos(O)
Vzo = Vo*cos(Z)*sin(O)
if Ay != 0: 
    Total_Time = 2*(-Vyo/Ay)
else:
    Total_Time = None
Height = Syo + (Vyo*(Total_Time/2)) + (Ay*((Total_Time/2)**2))/2
Sy = Syo + (Vyo*T) + (Ay*(T**2))/2
Sx = Sxo + (Vxo*T) + (Ax*(T**2))/2
Sz = Szo + (Vzo*T) + (Az*(T**2))/2
S_Ground = RVector(Sx, Sz)
S = RVector3(Sx, Sy, Sz)
Vy = Vyo + Ay*T
Vx = Vxo + Ax*T
Vz = Vzo + Az*T
V_Ground = RVector(Vx, Vz)
V = RVector3(Vx, Vy, Vz)
Ground_Dist = RVector(Sx, Sz)
if Vy < 0:
    Ver_Dist = Height + (Height - Sy)
if Vy >= 0:
    Ver_Dist = Sy
TVer_Dist = 2*(Syo + (Vyo*(Total_Time/2)) + (Ay*((Total_Time/2)**2))/2)
X_TDist = Sxo + (Vxo*Total_Time) + (Ax*(Total_Time**2))/2
Z_TDist = Szo + (Vzo*Total_Time) + (Az*(Total_Time**2))/2
Ground_TDist = RVector(X_TDist, Z_TDist)
X_Disp = Sx - Sxo
Y_Disp = Sy - Syo
Z_Disp = Sz - Szo
Ground_Disp = RVector(X_Disp, Z_Disp)
X_TDisp = (Vxo*Total_Time) + (Ax*(Total_Time**2))/2
Z_TDisp = (Vzo*Total_Time) + (Az*(Total_Time**2))/2
Y_TDisp = (Vyo*Total_Time) + ((Ay*(Total_Time**2))/2)
Ground_TDisp = RVector(X_TDisp, Z_TDisp)

print("Initial Velocity on X-Axis:", Vxo,"m/s")
print("Initial Velocity on Y-Axis:", Vyo,"m/s")
print("Initial Velocity on Z-Axis:", Vzo,"m/s")
print("Total Trajectory Time =", Total_Time,"s")
print("Highest Point Approached:", Height,"m")
print("Ground Distance Travelled by T:",Ground_Dist,"m")
print("Vertical Distance Travelled by T:", Ver_Dist,"m")
print("Total Distance Travelled on X-Axis:",X_TDist,"m")
print("Total Distance Travelled on Z-Axis:",Z_TDist,"m")
print("Total Ground Distance Travelled:",Ground_TDist,"m")
print("Total Vertical Distance Travelled (on Y-Axis):", TVer_Dist,"m")
print("Displacement on X-Axis by T:", X_Disp,"m")
print("Displacement on Y-Axis by T:", Y_Disp,"m")
print("Displacement on Z-Axis by T:", Z_Disp,"m")
print("Ground Displacement by T:", Ground_Disp,"m")
print("Total Displacement on X-Axis:", X_TDisp,"m")
print("Total Displacement on Y-Axis:", Y_TDisp,"m")
print("Total Displacement on Z-Axis:", Z_TDisp,"m")
print("Total Ground Displacement:", Ground_TDisp,"m")
print("Position on X-Axis at T:", Sx,"m")
print("Position on Y-Axis at T:", Sy,"m")
print("Position on Z-Axis at T:", Sz,"m")
print("Ground Position at T:", S_Ground,"m")
print("Velocity on X-Axis at T:", Vx,"m/s")
print("Velocity on Y-Axis at T:", Vy,"m/s")
print("Velocity on Z-Axis at T:", Vz,"m/s")
print("Ground Velocity at T:", V_Ground,"m/s")
print("Resultant Velocity at T:", V,"m/s")
print("Acceleration on X-Axis at T:", Ax,"m/s^2")
print("Acceleration on Y-Axis at T:", Ay,"m/s^2")
print("Acceleration on Z-Axis at T:", Az,"m/s^2")
print("Ground Acceleration at T:", A_Ground,"m/s^2")
print("Resultant Acceleration at T:", A,"m/s^2")