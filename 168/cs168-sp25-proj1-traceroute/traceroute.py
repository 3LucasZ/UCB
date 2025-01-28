import random
import util

# Your program should send TTLs in the range [1, TRACEROUTE_MAX_TTL] inclusive.
# Technically IPv4 supports TTLs up to 255, but in practice this is excessive.
# Most traceroute implementations cap at approximately 30.  The unit tests
# assume you don't change this number.
TRACEROUTE_MAX_TTL = 30

# Cisco seems to have standardized on UDP ports [33434, 33464] for traceroute.
# While not a formal standard, it appears that some routers on the internet
# will only respond with time exceeeded ICMP messages to UDP packets send to
# those ports.  Ultimately, you can choose whatever port you like, but that
# range seems to give more interesting results.
TRACEROUTE_PORT_NUMBER = 33434  # Cisco traceroute port number.

# Sometimes packets on the internet get dropped.  PROBE_ATTEMPT_COUNT is the
# maximum number of times your traceroute function should attempt to probe a
# single router before giving up and moving on.
PROBE_ATTEMPT_COUNT = 3

def cvtip(bs: str):
    w, len = 8, 32
    ret = ""
    while len>0:
        bs, l = cvt(bs, w)
        ret += str(l) + ("." if len != w else "")
        len -= w
    return bs, ret
def cvt(bs: str, sz: int):
    pre = bs[:sz]
    return bs[sz:], int(pre, 2)

class IPv4:
    # Each member below is a field from the IPv4 packet header.  They are
    # listed below in the order they appear in the packet.  All fields should
    # be stored in host byte order.
    #
    # You should only modify the __init__() method of this class.
    version: int
    header_len: int  # Note length in bytes, not the value in the packet.
    tos: int         # Also called DSCP and ECN bits (i.e. on wikipedia).
    length: int      # Total length of the packet.
    id: int
    flags: int
    frag_offset: int
    ttl: int
    proto: int
    cksum: int
    src: str
    dst: str

    def __init__(self, buffer: bytes):
        bitstr = ''.join(format(byte, '08b') for byte in [*buffer])
        bitstr, self.version = cvt(bitstr, 4)
        bitstr, self.header_len = cvt(bitstr, 4)
        self.header_len *= 4
        bitstr, self.tos = cvt(bitstr, 8)
        bitstr, self.length = cvt(bitstr, 16)
        bitstr, self.id = cvt(bitstr, 16)
        bitstr, self.flags = cvt(bitstr, 3)
        bitstr, self.frag_offset = cvt(bitstr, 13)
        bitstr, self.ttl = cvt(bitstr, 8)
        bitstr, self.proto = cvt(bitstr, 8)
        bitstr, self.cksum = cvt(bitstr, 16)
        bitstr, self.src = cvtip(bitstr)
        bitstr, self.dst = cvtip(bitstr)
    
    # def bin2str(self, i: int):
    #     barr = n.to_bytes((n.bit_length() + 7) // 8, 'big')
    #     s = barr.decode()

    def __str__(self) -> str:
        return f"IPv{self.version} (tos 0x{self.tos:x}, ttl {self.ttl}, " + \
            f"id {self.id}, flags 0x{self.flags:x}, " + \
            f"ofsset {self.frag_offset}, " + \
            f"proto {self.proto}, header_len {self.header_len}, " + \
            f"len {self.length}, cksum 0x{self.cksum:x}) " + \
            f"{self.src} > {self.dst}"


class ICMP:
    # Each member below is a field from the ICMP header.  They are listed below
    # in the order they appear in the packet.  All fields should be stored in
    # host byte order.
    #
    # You should only modify the __init__() function of this class.
    type: int
    code: int
    cksum: int

    def __init__(self, buffer: bytes):
        bitstr = ''.join(format(byte, '08b') for byte in [*buffer])
        bitstr, self.type = cvt(bitstr, 8)
        bitstr, self.code = cvt(bitstr, 8)
        bitstr, self.cksum = cvt(bitstr, 16)

    def __str__(self) -> str:
        return f"ICMP (type {self.type}, code {self.code}, " + \
            f"cksum 0x{self.cksum:x})"


class UDP:
    # Each member below is a field from the UDP header.  They are listed below
    # in the order they appear in the packet.  All fields should be stored in
    # host byte order.
    #
    # You should only modify the __init__() function of this class.
    src_port: int
    dst_port: int
    len: int
    cksum: int

    def __init__(self, buffer: bytes):
        bitstr = ''.join(format(byte, '08b') for byte in [*buffer])
        bitstr, self.src_port = cvt(bitstr, 16)
        bitstr, self.dst_port = cvt(bitstr, 16)
        bitstr, self.len = cvt(bitstr, 16)
        bitstr, self.cksum = cvt(bitstr, 16)

    def __str__(self) -> str:
        return f"UDP (src_port {self.src_port}, dst_port {self.dst_port}, " + \
            f"len {self.len}, cksum 0x{self.cksum:x})"

# TODO feel free to add helper functions if you'd like

def traceroute(sendsock: util.Socket, recvsock: util.Socket, ip: str) \
        -> list[list[str]]:
    """ Run traceroute and returns the discovered path.

    Calls util.print_result() on the result of each TTL's probes to show
    progress.

    Arguments:
    sendsock -- This is a UDP socket you will use to send traceroute probes.
    recvsock -- This is the socket on which you will receive ICMP responses.
    ip -- This is the IP address of the end host you will be tracerouting.

    Returns:
    A list of lists representing the routers discovered for each ttl that was
    probed.  The ith list contains all of the routers found with TTL probe of
    i+1.   The routers discovered in the ith list can be in any order.  If no
    routers were found, the ith list can be empty.  If `ip` is discovered, it
    should be included as the final element in the list.
    """

    ret = []
    for ttl in range(1, TRACEROUTE_MAX_TTL+1):
        s = set()
        done = False
        secrets = []
        for att in range(PROBE_ATTEMPT_COUNT):
            sendsock.set_ttl(ttl)
            secret = random.randint(1,60000)
            secrets.append(secret)
            sendsock.sendto(("A"*secret).encode(), (ip, TRACEROUTE_PORT_NUMBER))
        while recvsock.recv_select():
            buf, address = recvsock.recvfrom()
            try:
                ipv4 = IPv4(buf)
                buf = buf[ipv4.header_len:]
                icmp = ICMP(buf)
                buf = buf[8:]
                ipv4_2 = IPv4(buf)
                buf = buf[20:]
                udp = UDP(buf)
                buf = buf[8:]
                print(ipv4)
                print(icmp)
                print(ipv4_2)
                print(udp)
                print(buf)
            except:
                continue

            # check for legit packets
            if (not (icmp.type == 3 or 
                    (icmp.type == 11 and icmp.code == 0))): 
                continue
            if (not (ipv4.proto == 1)):
                continue
            if (not (udp.len - 8 in secrets)):
                continue
            secrets.remove(udp.len - 8)
        
            s.add(ipv4.src)
            if (address[0] == ip):
                done = True
            if (len(secrets) == 0):
                break
        util.print_result(list(s), ttl)
        ret.append(list(s))
        if done:
            break
    return ret

if __name__ == '__main__':
    args = util.parse_args()
    ip_addr = util.gethostbyname(args.host)
    print(f"traceroute to {args.host} ({ip_addr})")
    traceroute(util.Socket.make_udp(), util.Socket.make_icmp(), ip_addr)
