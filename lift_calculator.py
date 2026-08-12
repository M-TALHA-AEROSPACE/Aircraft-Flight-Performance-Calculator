import math

# VARIABLES AND CONSTANTS (ISA Model):

P0 = 101325      # Sea level pressure (Pa)
T0 = 288.15      # Sea level temperature (K)
L = 0.0065       # Temperature lapse rate (K/m)
g = 9.80665      # Gravity (m/s²)
R = 287.05       # Gas constant (J/kg·K)
STALL_AOA = 15.0 # Stall angle limit (Degrees)
cd0 = 0.02       # Parasite drag coefficient (Baseline)
oswald_e = 0.8   # Oswald wing efficiency factor

# FUNCTION (Lift Calculation):

def lift_force(air_density, velocity, wing_area, lift_coefficient):
    lift = air_density * wing_area * (velocity ** 2) * lift_coefficient * 0.5
    return lift

# USER INPUTS:

velocity = float(input("ENTER VELOCITY (m/s): "))
altitude = float(input("ENTER ALTITUDE (m): "))
wingspan = float(input("ENTER WINGSPAN b (m): "))
mean_chord = float(input("ENTER MEAN CHORD c (m): "))
aoa = float(input("ENTER ANGLE OF ATTACK (degrees): "))
aircraft_weight = float(input("ENTER AIRCRAFT WEIGHT (N): "))


# CALCULATIONS:

# Atmospheric Calculations:
H = altitude
T = T0 - (L * H)
P = P0 * ((1 - (L * H) / T0) ** (g / (R * L)))
air_density = P / (R * T)
Tc = T - 273.15

# Wing Geometry Calculations:

wing_area = wingspan * mean_chord
aspect_ratio = (wingspan ** 2) / wing_area

# Angle of Attack & Stall Logic:

if aoa > STALL_AOA:
    print("\n⚠️ WARNING: STALL DETECTED! Wing Angle exceeds limit (15°). Critical loss of lift!")
    lift_coefficient = 0.3
else:
    lift_coefficient = 0.2 + (0.1 * aoa)

# Aerodynamic Forces (Lift & Drag):

total_lift = lift_force(air_density, velocity, wing_area, lift_coefficient)

# Induced Drag Coefficient (CDi) & Total Drag:

cdi = (lift_coefficient ** 2) / (math.pi * aspect_ratio * oswald_e)
total_cd = cd0 + cdi
total_drag = 0.5 * air_density * (velocity ** 2) * wing_area * total_cd

# Minimum Stall Speed & Safety Factor:

v_stall = math.sqrt((2 * aircraft_weight) / (air_density * wing_area * 1.5))
safety_factor = total_lift / aircraft_weight

# PRINTING RESULTS:

print("\n" + "="*35)
print("         FLIGHT PERFORMANCE REPORT")
print("="*35)
print("TEMPERATURE         :", round(Tc, 2), "°C")
print("PRESSURE            :", round(P, 2), "Pa")
print("DENSITY             :", round(air_density, 4), "kg/m³")
print("-" * 35)
print("WING AREA           :", round(wing_area, 2), "m²")
print("ASPECT RATIO (AR)   :", round(aspect_ratio, 2))
print("CALCULATED CL       :", round(lift_coefficient, 2))
print("-" * 35)
print("LIFT FORCE          :", round(total_lift, 2), "N")
print("TOTAL DRAG (Thrust) :", round(total_drag, 2), "N")
print("MINIMUM STALL SPEED :", round(v_stall, 2), "m/s")
print("LIFT-TO-WEIGHT RATIO:", round(safety_factor, 2), "x")
print("="*35)

# CONDITIONS & FLIGHT EVALUATION:

if aoa <= STALL_AOA:
    if total_lift >= aircraft_weight:
        print("Takeoff Successful! Lift exceeds weight.")
    else:
        req_speed = math.sqrt((2 * aircraft_weight) / (air_density * wing_area * lift_coefficient))
        print("Insufficient Lift! Increase speed to at least", round(req_speed, 2), "m/s")
else:
    print("CRITICAL: Plane in STALL condition. Reduce pitch angle immediately!")
