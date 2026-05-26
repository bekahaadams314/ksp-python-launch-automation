import krpc
import math

# connection to the server 
conn = krpc.connect(
    name='Launch Sequence',
    address='192.168.1.138',
    rpc_port=50000, stream_port=50001)
print(conn.krpc.get_status().version)

# Get the active vessel
vessel = conn.space_center.active_vessel

# Turn on SAS 
vessel.control.sas = True

# Set throttle to 100%
vessel.control.throttle = 1.0

# Activate the first stage (LAUNCH!)
vessel.control.activate_next_stage()

# get telemetry of vessel
height_curr = vessel.flight().surface_altitude 
height_previous = 0; 
parachute = vessel.parts.parachutes

while height_curr > height_previous:
    height_previous = height_curr
    height_curr = vessel.flight().surface_altitude
    fuel_amount = vessel.resources.amount('SolidFuel')
    print(fuel_amount)
    if (height_curr < height_previous):
        vessel.control.activate_next_stage()


# -----
# Get all parts on the vessel
# all_parts = print(vessel.parts.all)