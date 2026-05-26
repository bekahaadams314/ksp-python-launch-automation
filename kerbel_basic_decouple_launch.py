import krpc

# connection to the server 
conn = krpc.connect(
    name='Kerbel Basic Staged Launch',
    address='192.168.1.138',
    rpc_port=50000, stream_port=50001)
print(conn.krpc.get_status().version)

# Get the active vessel
vessel = conn.space_center.active_vessel

# Turn on SAS 
vessel.control.sas = True

# Set throttle to 100%
vessel.control.throttle = 1.0

# gather parts for active vessel
parts = vessel.parts

# Activate the first stage (LAUNCH!)
#vessel.control.activate_next_stage()

# max stage number 
max_stage = 0; 

#Get initial max stage snapshot
for part in parts.all:
    if (part.stage > max_stage):
        max_stage = part.stage

#Stop loopin when at final stage!!!
while max_stage > 0:

    #Get max fuel snapshot
    fuel_amount = 0
    for part in parts.all: 
        if (part.stage == max_stage):
            fuel_amount = fuel_amount + part.resources.amount('SolidFuel')

    #Edge case for zero fuel stages (Such as a decoupler only stage)
    if(fuel_amount == 0):
        print("I am thirsty :(")

    #Stage
    vessel.control.activate_next_stage()

    #Live monitoring of fuel
    while fuel_amount > 0:
        fuel_amount = 0 
        #Loop through to get updated fuel count
        for part in parts.all: 
            if (part.stage == max_stage):
                fuel_amount = fuel_amount + part.resources.amount('SolidFuel')
                print(max_stage, fuel_amount)

    #Lower stage value to remain updated
    max_stage = max_stage - 1

