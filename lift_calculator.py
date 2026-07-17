#function

def lift_force(air_density,velocity,wing_area,lift_coefficient):
  lift_force=air_density*wing_area*velocity**2*lift_coefficient*0.5
  return lift_force

#user input

velocity=float(input("ENTER VELOCITY:"))
air_density=float(input("ENTER AIR DENSITY:"))
wing_area=float(input("ENTER WING AREA:"))
lift_coefficient=float(input("ENTER LIFT COEFFICIENT:"))
aircraft_weight=float(input("ENTER AIRCRAFT WEIGHT:"))

total_lift= lift_force(air_density,velocity,wing_area,lift_coefficient)

#conditions

if total_lift>= aircraft_weight:
     print("Takeoff Successful! Lift exceeds weight.")
else:
     print("Insufficient Lift! Speed boost required.")
