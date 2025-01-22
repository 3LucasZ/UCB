from traceroute import IPv4

def test_ipv4():
    s = "45000014bedd0000101100000102030405060708"
    b = bytes.fromhex(s)
    print(IPv4(b))

    s = "bc5e7179614c7ffc6fc43a3dd8e31e6c89595954"
    b = bytes.fromhex(s)
    print(IPv4(b))

test_ipv4()