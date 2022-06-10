import math

wheelbase = 0.446365                            # radstand in [m]
max_steering = 28                               # maximaler Lenkeinschlag in [°]
dodge = 0.500                                   # wie weit soll ausgewichen werden in [m]

max_steering_rad = max_steering/180*math.pi     # Umrechnung [°] in [rad]
kr = wheelbase/math.tan(max_steering_rad)       # Berechnung Kurvenradius bei max_steering in [m]
angle = math.acos((kr-dodge/2)/kr)              # Berechnung erforderliche Winkel 
b = kr * angle                                  # Berechnung Bogenlänge für einen Lenkeinschlag

print(b)
