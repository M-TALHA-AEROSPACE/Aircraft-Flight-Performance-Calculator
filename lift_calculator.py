#variables and constant:

P0 = 101325      
T0 = 288.15      
L = 0.0065       
g = 9.80665    
R = 287.05
H=altitude

#function

def lift_force(air_density,velocity,wing_area,lift_coefficient):
  lift_force=air_density*wing_area*velocity**2*lift_coefficient*0.5
  return lift_force

#user input

velocity=float(input("ENTER VELOCITY:"))
altitude=float(input("ENTER ALTITUDE:"))
lenght=float(input("ENTER LENGHT:"))
lift_coefficient=float(input("ENTER LIFT COEFFICIENT:"))
aircraft_weight=float(input("ENTER AIRCRAFT WEIGHT:"))

total_lift= lift_force(air_density,velocity,wing_area,lift_coefficient)
#calculations:

T=T0-(L.H)
P=P0*1-((L*H)/T0)
p=P/R*T
Tc=T-273.15

#printing

print("LIFT:",round(total_lift,2),"N")
print("TEMPRATURE:",round(Tc,2),"°C")
print("PRESSURE:",round(P,2),"Pa")
print("DENSITY:",round(p,2),"KGM³")

#conditions

if total_lift>= aircraft_weight:
     print("Takeoff Successful! Lift exceeds weight.")
else:
     print("Insufficient Lift! Speed boost required.")
