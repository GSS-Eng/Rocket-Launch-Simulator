# Importing tools I've built to simplify calcs:
import MyTools as mt

#____________________________________________________________________________________________

# Constants being used:
pi = 3.14159265358979323846264
g = -9.81

print(f"Constants: Pi = {pi:.4f}, g = {g:.4f} m/s²")

#____________________________________________________________________________________________

# Insert the variables below:
# Initial positions on XYZ-Space;
# Target Altitude;
# Precise time of tracking;
# Initial velocity module;
# The angle of launch V x XZ-Plane.
# The angle between the XZ-Plane projection of V and the X-Axis.
# Each Dimension Acceleration;

# Feel free to use your prefered units: 
Distance = "Meters" # Replace options: Kilometers.
Time = "Seconds" # Replace options: Hours.
Angle = "Rad" # Replace options: Degrees.
Velocity = "Meters/Second" # Replace options: Kilometers/Hour.
Acceleration = "Meters/Square_Second" # Replace options: Kilometers/Square_Hour"

SYO = 0.0
SXO = 0.0
SZO = 0.0
TAR_A = 0.0
t = 2.0
z = pi/4
o = pi/4
VO = 30.0
AX = 0.0
AY = -9.81
AZ = 0.0

#____________________________________________________________________________________________

# # Making sure the accelerations are fixed.
if AX is not float or AY is not float or AZ is not float:
    raise ValueError("If the acceleration relies on an expression, \
type it down below where the code indicates.")

#____________________________________________________________________________________________

# Converting values to Internation System (IS):
if Distance == "Kilometers":
    Sxo = SXO*1000
    Syo = SYO*1000
    Szo = SZO*1000
    Target_Height = TAR_A*1000
else: 
      Sxo = SXO
      Syo = SYO
      Szo = SZO
      Target_Height = TAR_A
      

if Time == "Hours":
    tt = 3600*t
else:
    tt = t
    
if Angle == "Degrees":
    Z = (z*pi)/180
    O = (o*pi)/180
else:
    Z = z
    O = o

if Velocity == "Kilometers/Hour":
    Vo = VO/3.6
else:
    Vo = VO

if Acceleration == "Kilometers/Square_Hour":
    Ax = (7.71604938*(10**-5))*AX
    Ay = (7.71604938*(10**-5))*AY
    Az = (7.71604938*(10**-5))*AZ
else: 
    Ax = AX
    Ay = AY 
    Az = AZ

#____________________________________________________________________________________________

# Printing the Input Parameters:
print("\n--- Input Parameters ---")
print(f"Point of Time: {t:.4f} s")
print(f"Initial Position: ({Sxo:.4f}, {Syo:.4f}, {Szo:.4f}) m")
print(f"Target Altitude: {TAR_A: .4f} m")
print(f"Angle of Launch (Elevation): {Z:.4f} rad")
print(f"Horizontal Angle (Azimuth): {O:.4f} rad")
print(f"Initial Velocity: {Vo:.4f} m/s")
print(f"Accelaration on Axis X, Y, Z: ({Ax:.4f}, {Ay:.4f}, {Az:.4f}) m/s^2")

# Verifying the Sin and Cos values:
print("\n--- Trigonometric Verification ---")
print(f"Sin(Z): {mt.sin(Z):.4f}")
print(f"Cos(Z): {mt.cos(Z):.4f}")
print(f"Sin(O): {mt.sin(O):.4f}")
print(f"Cos(O): {mt.cos(O):.4f}")

#____________________________________________________________________________________________

# Isolating variables that doesn't rely on time:
A_Ground = mt.RVector(Ax, Az)
A = mt.RVector3(Ax, Ay, Az)
Vyo = Vo*mt.sin(Z)
Vxo = Vo*mt.cos(Z)*mt.cos(O)
Vzo = Vo*mt.cos(Z)*mt.sin(O)

#____________________________________________________________________________________________

# Preventing wrong prompts and defining main physics variables:
if Vo < 0:
    raise ValueError("Velocity has to be in module")
    
if t < 0:
    raise ValueError("Time can't be negative")
 
if Ay >= 0:
    raise ValueError("Impossible to track full movment with no or inverted gravity action, total time is infinite")

#____________________________________________________________________________________________

# Defining Highest Altitude:
if Vyo <= 0:
    Height = Syo
else: Height = Syo - (Vyo**2)/(2*Ay)
    
# Defining highest altitude vs target altitude in advance:
if Height < Target_Height:
    raise ValueError("The projectile never reaches the Target Height.")

# Defining Total Trajectory Time:
Total_Time = (-Vyo - ((Vyo)**2 - 2*Ay*(Syo - Target_Height))**0.5)/Ay

if tt <= Total_Time:
    T = tt
else: T = Total_Time

#____________________________________________________________________________________________

# Defining the physics oblique launch formulas:
Sy = Syo + (Vyo*T) + (Ay*(T**2))/2
Sx = Sxo + (Vxo*T) + (Ax*(T**2))/2
Sz = Szo + (Vzo*T) + (Az*(T**2))/2
S_Ground = mt.RVector(Sx, Sz)
S = mt.RVector3(Sx, Sy, Sz)
Vy = Vyo + Ay*T
Vx = Vxo + Ax*T
Vz = Vzo + Az*T
V_Ground = mt.RVector(Vx, Vz)
V = mt.RVector3(Vx, Vy, Vz)
Ground_Dist = mt.RVector(Sx, Sz)

# After Total_Time/2 Sy starts to decrease, that has to be compensated:
if Vy < 0:
    Ver_Dist = (Height - Syo) + (Height - Sy)
else:
    Ver_Dist = Sy - Syo

TVer_Dist = (Height - Syo) + (Height - Target_Height)
X_TDist = Sxo + (Vxo*Total_Time) + (Ax*(Total_Time**2))/2
Z_TDist = Szo + (Vzo*Total_Time) + (Az*(Total_Time**2))/2
Ground_TDist = mt.RVector(X_TDist, Z_TDist)
X_Disp = Sx - Sxo
Y_Disp = Sy - Syo
Z_Disp = Sz - Szo
Ground_Disp = mt.RVector(X_Disp, Z_Disp)
X_TDisp = (Vxo*Total_Time) + (Ax*(Total_Time**2))/2
Z_TDisp = (Vzo*Total_Time) + (Az*(Total_Time**2))/2
Y_TDisp = (Vyo*Total_Time) + ((Ay*(Total_Time**2))/2)
TDisp = mt.RVector3(X_TDisp, Y_TDisp, Z_TDisp)
Ground_TDisp = mt.RVector(X_TDisp, Z_TDisp)

#____________________________________________________________________________________________

# Printing Results:
print("\n--- Velocity Results ---")
print(f"Initial Velocity X: {Vxo:.4f} m/s")
print(f"Initial Velocity Y: {Vyo:.4f} m/s")
print(f"Initial Velocity Z: {Vzo:.4f} m/s")
print(f"Velocity X at T: {Vx:.4f} m/s")
print(f"Velocity Y at T: {Vy:.4f} m/s")
print(f"Velocity Z at T: {Vz:.4f} m/s")
print(f"Ground Velocity at T: {V_Ground:.4f} m/s")
print(f"Resultant Velocity at T: {V:.4f} m/s")

print("\n--- Trajectory & Distance ---")
print(f"Total Flight Time: {Total_Time:.4f} s")
print(f"Peak Height: {Height:.4f} m")
print(f"Vertical Distance at T: {Ver_Dist:.4f} m")
print(f"Total Vertical Path (Flight): {TVer_Dist:.4f} m")
print(f"Ground Distance at T: {Ground_Dist:.4f} m")
print(f"Total Ground Distance: {Ground_TDist:.4f} m")

print("\n--- Position & Displacement ---")
print(f"Position at T: ({Sx:.4f}, {Sy:.4f}, {Sz:.4f}) m")
print(f"Ground Position at T: {S_Ground:.4f} m")
print(f"Displacement at T: ({X_Disp:.4f}, {Y_Disp:.4f}, {Z_Disp:.4f}) m")
print(f"Ground Displacement at T: {Ground_Disp:.4f} m")
print(f"Total Axis Displacement: ({X_TDisp:.4f}, {Y_TDisp:.4f}, {Z_TDisp:.4f}) m")
print(f"Total Displacement: {TDisp:.4f} m")
print(f"Total Ground Displacement: {Ground_TDisp:.4f} m")

print("\n--- Acceleration ---")
print(f"Acceleration Vector: ({Ax:.4f}, {Ay:.4f}, {Az:.4f}) m/s²")
print(f"Ground Acceleration: {A_Ground:.4f} m/s²")
print(f"Resultant Acceleration A: {A:.4f} m/s²")
#____________________________________________________________________________________________