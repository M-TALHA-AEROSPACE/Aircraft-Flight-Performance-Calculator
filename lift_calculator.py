import math

#  Variables and Constants

P0 = 101325      # Sea level pressure (Pa)
T0 = 288.15      # Sea level temperature (K)
L = 0.0065       # Temperature lapse rate (K/m)
g = 9.80665      # Gravity (m/s²)
R = 287.05       # Gas constant (J/kg·K)

#  Function

def lift_force(air_density, velocity, wing_area, lift_coefficient):
    lift = air_density * wing_area * (velocity ** 2) * lift_coefficient * 0.5
    return lift

# User Inputs 

velocity = float(input("ENTER VELOCITY (m/s): "))
altitude = float(input("ENTER ALTITUDE (m): "))
wing_area = float(input("ENTER WING AREA (m²): "))
lift_coefficient = float(input("ENTER LIFT COEFFICIENT: "))
aircraft_weight = float(input("ENTER AIRCRAFT WEIGHT (N): "))

# Calculations 

H = altitude
T = T0 - (L * H)
P = P0 * ((1 - (L * H) / T0) ** (g / (R * L)))
air_density = P / (R * T)                      
Tc = T - 273.15

#  Total Lift Call

total_lift = lift_force(air_density, velocity, wing_area, lift_coefficient)

#  Printing:

print("\n" + "="*30)
print("TEMPRATURE :", round(Tc, 2), "°C")
print("PRESSURE   :", round(P, 2), "Pa")
print("DENSITY    :", round(air_density, 4), "kg/m³")
print("LIFT       :", round(total_lift, 2), "N")
print("="*30)

# Conditions:

if total_lift >= aircraft_weight:
    print("Takeoff Successful! Lift exceeds weight.")
else:
    print("Insufficient Lift! Speed boost required.")
