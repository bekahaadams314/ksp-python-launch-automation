import krpc

# connection to the server 
conn = krpc.connect(
    name='Recovery',
    address='',
    rpc_port=xxx, stream_port=xxx)
print(conn.krpc.get_status().version)

# Get the active vessel
vessel = conn.space_center.active_vessel

# vehicle recovery
vessel.recover()
