import plotly.graph_objects as pgo
import numpy as np
import streamlit as st
import MyTools as mt
import time as t

# Defining tab title, page layout and the initial sidebar state:
st.set_page_config(
    page_title="🚀 3D Ballistic Simulator",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Creating a start page:
if 'started' not in st.session_state:
    
    st.session_state.started = False

if not st.session_state.started:

# Background image:
    backimg = mt.base64_image("astro.jpg")

# CSS to hide the sidebar and the "top bar" on start page:
    st.markdown(f"""
        <style>
            /* Hide the Streamlit interface */
            [data-testid="stSidebar"] {{display: none;}}
            [data-testid="stHeader"], header {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            #MainMenu {{visibility: hidden;}}

            /* Bottom Left Project Info */
            .project-info {{
                position: fixed;
                bottom: 20px;
                left: 20px;
                color: white;
                font-family: 'Courier New', Courier, monospace;
                z-index: 100;
            }}

            /* Blinking "ACTIVE" effect */
            .blink {{
                color: #00f2ff; /* Cyan to match the astronaut */
                animation: blink-animation 1s steps(2, start) infinite;
            }}

            @keyframes blink-animation {{
                to {{ visibility: hidden; }}
            }}

            /* Make the background full-screen */
            .stApp {{
                background-image: url("data:image/jpg;base64,{backimg}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}


            /* Styling the Middle Button */
            div.stButton > button {{
                position: fixed; /* Fixed relative to the screen */
                top: 50%; /* Move down 50% */
                left: 50%; /* Move right 50% */
                transform: translate(-50%, -50%); /* Pull back by half its own size */
                background-color: rgba(0, 0, 0, 0.4);
                color: #ff3c23; /* NASA Red / Nebula Orange */
                border: 2px solid #ff3c23;
                padding: 10px 25px;
                font-weight: bold;
                letter-spacing: 2px; /* This makes it look more technical/minimalist */
                text-transform: uppercase;
                transition: 0.3s;
                border-radius: 5px;
                z-index: 1000;
            }}

            div.stButton > button:hover {{
                background-color: #ff3c23;
                color: white;
                box-shadow: 0 0 15px #ff3c23;
            }}

            /* Center text replacement */
            .init-text {{
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                text-align: center;
                color: white;
                font-family: 'Courier New', monospace;
                font-size: 1.2rem;
            }}
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="project-info">
            Project: BALLISTICS_SIM_V1.0<br>
            Status: <span class="blink">ACTIVE</span>
        </div>
        """, unsafe_allow_html=True)
        
    
    if st.button("START"):
        st.session_state.started = True
        st.rerun()

else:
    # This shows after clicking
    st.markdown('<p class="init-text">Initializing Systems...</p>', unsafe_allow_html=True)
    # Simulate a loading process
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        t.sleep(0.02)
        progress_bar.progress(percent_complete + 1)
    st.success("Core Systems Engaged.")
    
#____________________________________________________________________________________________

# Defining tab title, page layout and the initial sidebar state:
st.set_page_config(
    page_title="🚀 3D Ballistic Simulator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Defining page title:
st.title("🚀 3D Ballistic Simulator")

#____________________________________________________________________________________________

# Defining what functions will be on the side bar:
with st.sidebar:
    
    # Defining informative mechanism for better user experience:
    with st.expander("How it works"):
        
        st.info("""
                *Steps*
                1. Choose the interface mode;
                2. Set your launch parameters;
                3. Click 'LAUNCH';
                4. Hover over the path for physics data.
                """)
                
    I_mode = st.selectbox(
        "Interface Mode",
        ("Experience", "Objective"),
        help="""Experience: focus on the user experience.
        Objective: focus on calculations agility."""
        )
    
    
    # Defining sidebar title:
    st.title("Parameters")
    
    
    # Defining select boxes for units change:
    st.subheader("Preferred Units", divider='gray')
    
    d_unit = st.selectbox(
        "Distance Unit",
        ("m", "km", "mi", "ft"),
        help="Meters, Kilometers, Miles, Feet"
        )
    
    an_unit = st.selectbox(
        "Angle Unit",
        ("degree", "rad"),
        help="Degrees, Radians"
        )
    
    v_unit = st.selectbox(
        "Velocity Unit", 
        ("m/s", "km/h", "mi/h"), 
        help="Meters per Second, Kilometers per Hour, Miles per Hour"
        )
    
    a_unit = st.selectbox(
        "Acceleration Unit", 
        ("m/s2", "km/h2", "mi/h2"),
        help="Meters per Square Second, Kilometers per Square Hour, Miles per Square Hour"
        )
    
    
    # Defining input boxes for the parameters values:
    st.subheader("Positions", divider='blue')
    
    Sxo_input = st.number_input(
        "X-Axis Initial Position",
        min_value=-500, 
        max_value=500, 
        value=0,
        help="Range: -500m to 500m"
        )
    
    Syo_input = st.number_input(
        "Y-Axis Initial Position",
        min_value=-500, 
        max_value=500, 
        value=0,
        help="Range: -500m to 500m"
        )
    
    Szo_input = st.number_input(
        "Z-Axis Initial Position",
        min_value=-500, 
        max_value=500, 
        value=0,
        help="Range: -500m to 500m"
        )
    
    Target_Height_input = st.number_input(
        "Target Height",
        min_value=-500, 
        max_value=500, 
        value=0,
        help="""Altitude of the impact point
                Range: -500 to 500m"""
        )
    
    
    st.subheader("Angles", divider='red')
    
    Z_input = st.number_input(
        "Elevation Angle",
        min_value=-90, 
        max_value=90, 
        value=45,
        help="""Angle between Vo vector and the xy-plane/ground
                Range: -90 to 90 Deg"""
        )
    
    O_input = st.number_input(
        "Azimuth Angle",
        min_value=0, 
        max_value=360, 
        value=45,
        help="""Angle between Vo vector horizontal projection and the X-Axis
                Range: 0 to 360 Deg"""
        )
    
    
    st.subheader("Velocity & Acceleration", divider='violet')
    
    Vo_input = st.number_input(
        "Initial Velocity",
        min_value=0.001, 
        max_value=150, 
        value=15,
        help="""Instant velocity in module of the object on launch
                Range: 0.001 to 150 m/s"""
        )
    
    Ax_input = st.number_input(
        "X-Axis Acceleration",
        min_value=-20, 
        max_value=20, 
        value=0,
        help="""Object's acceleration on X-Axis
                Range: -20 to 20 m/s2"""
        )
    
    Ay_input = st.number_input(
        "Y-Axis Acceleration (g = -9.81)",
        min_value=-20, 
        max_value=-0.1, 
        value=-9.81,
        help="""Object's acceleration on Y-Axis (Gravity)
                Earth Gravity (g) = -9.81
                Range: -20 to -0.1 m/s2"""
        )
    
    Az_input = st.number_input(
        "Z-Axis Acceleration",
        min_value=-20, 
        max_value=20, 
        value=0,
        help="""Object's acceleration on Z-Axis
                Range: -20 to 20 m/s2"""
        )

#____________________________________________________________________________________________

# Constants being used:
pi = np.pi

# Converting parameters to IS:
Sxo = mt.I_distance(Sxo_input, d_unit)
Syo = mt.I_distance(Syo_input, d_unit)
Szo = mt.I_distance(Szo_input, d_unit)
Target_Height = mt.I_distance(Target_Height_input, d_unit)
Z = mt.I_angle(Z_input, an_unit)
O = mt.I_angle(O_input, an_unit)
Vo = mt.I_velocity(Vo_input, v_unit)
Ax = mt.I_acceleration(Ax_input, a_unit)
Ay = mt.I_acceleration(Ay_input, a_unit)
Az = mt.I_acceleration(Az_input, a_unit)

# Creating parameters list:
parameters = [Sxo, Syo, Szo, Target_Height, Z, O, Vo, Ax, Ay, Az]
    
#____________________________________________________________________________________________

# Verifying the Input Parameters:
print("\n--- Input Parameters ---")
print(f"Initial Position: ({Sxo:.4f}, {Syo:.4f}, {Szo:.4f}) m")
print(f"Target Altitude: {Target_Height: .4f} m")
print(f"Angle of Launch (Elevation): {Z:.4f} rad")
print(f"Horizontal Angle (Azimuth): {O:.4f} rad")
print(f"Initial Velocity: {Vo:.4f} m/s")
print(f"Initial Accelaration on Axis X, Y, Z: ({Ax:.4f}, {Ay:.4f}, {Az:.4f}) m/s^2")

# Verifying the Sin and Cos values:
print("\n--- Trigonometric Verification ---")
print(f"Sin(Z): {np.sin(Z):.4f}")
print(f"Cos(Z): {np.cos(Z):.4f}")
print(f"Sin(O): {np.sin(O):.4f}")
print(f"Cos(O): {np.cos(O):.4f}")

#____________________________________________________________________________________________

# Isolating variables that doesn't rely on time:
A_Ground = mt.RVector(Ax, Az)
A = mt.RVector3(Ax, Ay, Az)
Vyo = Vo*np.sin(Z)
Vxo = Vo*np.cos(Z)*np.cos(O)
Vzo = Vo*np.cos(Z)*np.sin(O)

#____________________________________________________________________________________________

# Defining Highest Altitude:
if Vyo <= 0:
    Height = Syo
else: Height = Syo - (Vyo**2)/(2*Ay)
              
#____________________________________________________________________________________________

# Creating logs lists:
warnings = []
errors = []

# Defining the warnings and errors: 
if Syo < 0:
    warnings.append("⚠️ * Underground level launch *")

if Target_Height < 0:
    warnings.append("⚠️ * Underground level target *")

if Height <= 0:
    warnings.append("⚠️ *** Underground Level Trajectory! *** ⚠️")

if len(parameters)<10:
    errors.append("###🚨  Missing Parameters  🚨")

if Height < Target_Height:
    errors.append("""###🚨  Impossible Trajectory  🚨
                  *** Target Height not reached *""")

#____________________________________________________________________________________________

# Defining functions to relate the log with it's images and help infos:
def related_img(y):
    
    if y == "⚠️ * Underground level launch *":
        return "L.jpeg"
    
    elif y == "⚠️ * Underground level target *":
        return "T.jpeg"
    
    elif y == "⚠️ *** Underground Level Trajectory! *** ⚠️":
        return "H.png"
    
    elif y == "###🚨  Missing Parameters  🚨":
        return "p.jpeg"
    
    elif y == """###🚨  Impossible Trajectory  🚨
                  *** Target Height not reached *""":
        return "m.jpg"
    

def related_md(y):
    
    if y == "⚠️ * Underground level launch *":
        return "** Check the Y-Axis Initial Position! **"
    
    elif y == "⚠️ * Underground level target *":
        return "** Check the Target Height! **"
    
    elif y == "⚠️ *** Underground Level Trajectory! *** ⚠️":
        return "** Check Launch and Target Height, Initial Velocity and Elevation! **"
    
    elif y == "###🚨  Missing Parameters  🚨":
        return "** Make sure to fill all Parameters! **"
    
    elif y == """###🚨  Impossible Trajectory  🚨
                  ** * Target Height not reached * **""":
        return """** Try Increasing Launch Height, Initial Velocity, and/or Elevation! **
                ** Try Decreasing Target Height! **"""

#____________________________________________________________________________________________    

# Creating 2s "checking" display for better user experience.
left, center, right = st.columns([1,2,1], vertical_alignment="center", gap="small")

with center:
    
    with st.spinner("Checking Parameters", width="stretch"):
        t.sleep(2)
    

# Creating logs displays:
# Ready to Launch:
if not errors:
    R_Launch = True
    
if R_Launch:
    
    co_text, co_img = st.columns([3, 1], vertical_alignment="center")    
    
    co_text.success("###✅ Ready to Launch ✅", icon=None)
    co_img.image("suc.png", width= 200)
    
    
    
# Warnings:
if warnings:
    
    with st.expander(f"⚠️ * {len(warnings)} Current Warnings * ⚠️"):
        
        col_txt, col_img = st.columns([4,1], vertical_alignment="top")
        
        for w in warnings:
            col_txt.warning(w, icon=None)
            col_txt.markdown(related_md(w))
            col_img.image(related_img(w), width = 180)
            st.divider()
            
        
# Errors:
if errors:
    
    colu_txt, colu_img = st.columns([3, 1], vertical_alignment="top")
    
    for e in errors:
        colu_txt.error(e, icon=None)
        colu_txt.markdown(related_md(e))
        colu_img.image(related_img(e), width = 200)
        st.divider()
        st.stop()
        
    raise
    
# Defining the Launch Button:
elif st.sidebar.button("**LAUNCH**", icon="🚀", icon_position="right", shortcut="L"):
    st.sidebar.markdown("or Press L to Launch")
    run_calcs = True
    
    
#____________________________________________________________________________________________

# Running the calculations:
if run_calcs:

    # Defining Total Trajectory Time:
    Total_Time = (-Vyo - ((Vyo)**2 - 2*Ay*(Syo - Target_Height))**0.5)/Ay
    
    # Defining the time range for calculations:
    T = np.arange(0, Total_Time, 0.01)
    
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
    
    # Continuing formulas:
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