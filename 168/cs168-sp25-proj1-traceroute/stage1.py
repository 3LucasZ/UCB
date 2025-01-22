# # Stage 1
# sendsock.set_ttl(4)
# sendsock.sendto("Hello World From Lucas".encode(), (ip, TRACEROUTE_PORT_NUMBER))
# if recvsock.recv_select():
#     buf, address = recvsock.recvfrom()
#     print(f"Packet bytes: {buf.hex()}")
#     print(f"Packet is from IP: {address[0]}")
#     print(f"Packet is from port: {address[1]}")
# # Result: 
# # TTL=1
# # 10.42.52.3 -> 10.42.54.151 
# # ICMP Time-to-live exceeded (Time to live exceeded in transit)
# # TTL=2 
# # 128.32.255.132 → 10.42.54.151 
# # IPv4 Fragmented IP protocol 1, 
# # TTL=3
# # 128.32.255.41 → 10.42.54.151 
# # IPv4 Fragmented IP protocol 1,
# # TTL=4
# # No reply