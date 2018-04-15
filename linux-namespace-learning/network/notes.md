* Aside from the loopback device, each network device (physical or virtual interfaces, bridges, etc.) can only be present in a single network namespace.

```shell
$ ip netns add netns1

$ ip netns exec netns1 ip link list
1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00

# When first created, the lo loopback device in the new namespace is down, so even a loopback ping will fail:
$ ip netns exec netns1 ping 127.0.0.1
connect: Network is unreachable

$ ip netns exec netns1 ip link set dev lo up
$ ip netns exec netns1 ping 127.0.0.1
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.051 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.043 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.045 ms

# But that still doesn't allow communication between netns1 and the root namespace.To do that, virtual ethernet devices need to be created and configured:
$ ip netns exec netns1 ifconfig veth1 10.1.1.1/24 up
$ ifconfig veth0 10.1.1.2/24 up
$ ping 10.1.1.1
PING 10.1.1.1 (10.1.1.1) 56(84) bytes of data.
64 bytes from 10.1.1.1: icmp_seq=1 ttl=64 time=0.087 ms
$ ip netns exec netns1 ping 10.1.1.2
PING 10.1.1.2 (10.1.1.2) 56(84) bytes of data.
64 bytes from 10.1.1.2: icmp_seq=1 ttl=64 time=0.054 ms
```


namespaces do not share routing tables or firewall rules, it means that packets sent from netns1 to the internet at large will get the dreaded "Network is unreachable" message.

A bridge can be created in the root namespace and the veth device from netns1. Alternatively, IP forwarding coupled with network address translation (NAT) could be configured in the root namespace.

## Network Security
By essentially turning off the network inside a namespace, administrators can ensure that processes running there will be unable to make connections outside of the namespace. 

Even processes that handle network traffic (a web server worker process or web browser rendering process for example) can be placed into a restricted namespace. Once a connection is established by or to the remote endpoint, the file descriptor for that connection could be handled by a child process that is placed in a new network namespace created by a clone() call. The child would inherit its parent's file descriptors, thus have access to the connected descriptor. Another possibility would be for the parent to send the connected file descriptor to a process in a restricted network namespace via a Unix socket.

Namespaces could also be used to test complicated or intricate networking configurations all on a single box. Running sensitive services in more locked-down, firewall-restricted namespace is another. Obviously, container implementations also use network namespaces to give each container its own view of the network


