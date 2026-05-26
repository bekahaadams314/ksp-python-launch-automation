import krpc

# connection to the server 
conn = krpc.connect(
    name='Recovery',
    address='192.168.1.138',
    rpc_port=50000, stream_port=50001)
print(conn.krpc.get_status().version)

# Get the active vessel
vessel = conn.space_center.active_vessel

# vehicle recovery
vessel.recover()