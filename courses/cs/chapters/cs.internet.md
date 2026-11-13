@chapter cs.internet
@title The internet: IP addresses, DNS and streaming
@level as
@paper CAIE 9618 Paper 1
@time 5–7 hours
@summary The difference between the internet and the World Wide Web, the hardware that connects you to the internet, bit streaming and why bit rate matters, IPv4 and IPv6 addresses, subnet masks and subnetting, public and private and static and dynamic addresses, and how a URL and the Domain Name Service find a web page.

:::why
Every time you open a web page, play a video or send a message, a chain of events happens in less than a second: a name is turned into a number, a path is found across several networks, and a stream of bits arrives faster than you can play it. Paper 1 asks you to explain this chain, to check IP addresses, to do small calculations with bit rates and subnet masks by hand, and to choose between options for a scenario. This chapter takes the networks of [Networks: models, topologies and hardware](#cs.networks) and shows how they join up into the internet.
:::

**Before you start**, you should know what a router and a MAC address are, from [Networks: models, topologies and hardware](#cs.networks), and how to convert between binary and denary, from [Number systems and binary arithmetic](#cs.data).

:::try Warm-up
Q: What type of device connects different networks and forwards packets using IP addresses? (from [Networks: models, topologies and hardware](#cs.networks))
A: A router. A switch forwards frames by MAC address inside one network.
Q: Convert the binary number 11000000 to denary. (from [Number systems and binary arithmetic](#cs.data))
A: \(128 + 64 = 192\).
Q: How many different values can 8 bits hold? (from [Number systems and binary arithmetic](#cs.data))
A: \(2^8 = 256\) values, which are the numbers 0 to 255. This is why every part of an IPv4 address lies between 0 and 255.
:::

## The internet and the World Wide Web

People use the words "internet" and "web" as if they meant the same thing. They do not, and Paper 1 asks for the difference.

:::def Internet
A worldwide network of networks. It joins millions of LANs and WANs with routers and common rules for sending data (protocols), and it carries many services, such as the World Wide Web, email, file transfer and online games.
:::

:::def World Wide Web (WWW)
A collection of web pages and other resources, each identified by a URL and linked by hyperlinks, that a web browser requests from web servers using the HTTP or HTTPS protocol. It is one service that runs on the internet.
:::

| | The internet | The World Wide Web |
|---|---|---|
| What it is | the global network of connected networks: cables, routers and protocols | the pages and other resources stored on web servers |
| What it carries | web pages, email, video calls, file transfer, games | web pages, images and videos, linked by hyperlinks |
| What you need to use it | a connection to an internet service provider | an internet connection and a web browser |
| Identified by | IP addresses | URLs |

:::analogy
The internet is like the road network of a country: the roads, junctions and rules that let vehicles get from place to place. The web is one of the things that travel on the roads, like a delivery service that fetches goods from shops (web servers) to your door. Email is another service on the same roads. Closing the shop does not remove the roads.
:::

## Hardware that connects you to the internet

You reach the internet through an **internet service provider** (ISP), a company that has a connection to the rest of the internet and sells you access to it. The syllabus asks about four kinds of hardware and connection that make this work.

### Modems and the PSTN

:::def Modem
A device that converts the digital data from a computer into a signal that a telephone or cable line can carry, and converts the incoming signals back into digital data. The name comes from modulator-demodulator.
:::

:::def Public Switched Telephone Network (PSTN)
The worldwide network of telephone lines, exchanges and switching equipment that was built to carry voice calls. Computers can use it to reach the internet through a modem, either by dialling in or by using a broadband service on the copper telephone line.
:::

A telephone line was designed to carry the human voice, which is an analogue signal. A computer produces digital data, which is bits. The modem sits between them. When sending, it modulates an analogue signal so that it carries the bits. When receiving, it demodulates the signal back into bits. Early internet users dialled in over the telephone line, which was slow and blocked the line for voice calls. Broadband services that use the same copper line (but at frequencies that do not interfere with voice) are much faster and always on.

### Dedicated lines

:::def Dedicated line
A permanent connection between two points, rented from a telecommunications company, which is used only by the organisation that leases it and has a fixed bandwidth.
:::

A **dedicated line**, also called a leased line, is not shared with other customers, so its speed is steady at all times of day, and it is reliable. It costs much more than ordinary broadband. Businesses use dedicated lines to link their offices into a WAN, to connect a large site to an ISP, and for services such as a hospital's connection to a central record system, where a slow or failed connection would be serious.

### The cell phone network

:::def Cell phone network
A wireless network in which the area covered is divided into regions called cells. Each cell has a base station with a radio transmitter and receiver, and a device connects by radio to the base station of the cell it is in.
:::

When you carry a phone, it connects to the nearest base station (a mast). If you move into the next cell, the connection is handed over to that cell's base station without a break. The base stations are joined by cables to the telephone network and to the internet. Different generations of mobile technology, such as 4G and 5G, give different speeds, and later generations carry more data per second. A cell network gives access to the internet almost anywhere with coverage, but the signal is shared by everyone in the cell, so speeds fall when many people use it at once.

| Connection | How it works | Good for | Weakness |
|---|---|---|---|
| Modem on the PSTN | digital data converted for the telephone line | homes and small offices | slower than a dedicated line, and the line is shared |
| Dedicated line | a private leased link | businesses that need steady speed and reliability | expensive |
| Cell phone network | radio to a base station in each cell | mobile devices and places with no cable | shared by users in the cell; coverage varies |

## Bit streaming

If you wanted to watch a film by downloading it first, you would wait until the last bit had arrived. **Bit streaming** removes the wait: the film starts playing while the rest is still arriving.

:::def Bit streaming
A method of sending a continuous flow of bits, such as audio or video, so that the receiver can start to play the data as it arrives, without waiting for the whole file to be sent.
:::

:::def Buffer
An area of memory that holds data that has arrived but has not yet been used. A streaming player uses a buffer to hold a few seconds of video, so that small changes in the speed of arrival do not interrupt the playback.
:::

There are two methods of bit streaming.

:::cols
:::col Real-time streaming
The data is captured and sent as it happens, such as a live football match, a lesson broadcast live or a video call. The data is not stored on a server first. The viewer cannot skip ahead, because the rest has not happened yet. The buffer is small to keep the delay short, so the stream is sensitive to a drop in speed.
:::
:::col On-demand streaming
The data is already stored on a server, such as a recorded lesson or a film. The viewer chooses when to start and can pause, skip and replay. The player can fill a larger buffer ahead of the point being watched, so it copes better with changes in speed.
:::
:::

### Bit rate and broadband speed

:::def Bit rate
The number of bits that are transmitted or processed in one second, measured in bits per second (bps), or in multiples such as kilobits per second (kbps) and megabits per second (Mbps).
:::

Two bit rates matter. The **bit rate of the stream** is how many bits per second the video or audio needs. The **bit rate of the connection** (the broadband speed) is how many bits per second the link can deliver. For smooth playback, the connection must deliver at least as many bits per second as the player uses. If it delivers fewer, the buffer slowly empties, and when it is empty the video pauses to refill ("buffering") or the player lowers the quality to reduce the bit rate. A real-time stream suffers more because it cannot download ahead.

The speed advertised for a connection may be shared with other devices in the same home, and with other users on the same line or in the same cell. The usable speed for one stream can be much lower than the speed you pay for.

:::warn Mbps is not MB/s
Internet speeds are given in **bits** per second (a small b, as in Mbps). File sizes are given in **bytes** (a capital B, as in MB). One byte is 8 bits, so a connection of 8 Mbps downloads at most 1 MB per second. In this chapter, as in [Number systems and binary arithmetic](#cs.data), mega means \(10^6\) and giga means \(10^9\), because network speeds use the decimal prefixes.
:::

:::eg Data used by a stream
A video is streamed at a bit rate of 5 Mbps. (a) How many bits are sent in 10 minutes? (b) How many megabytes is that? [3 marks]

(a) Ten minutes is 600 s, so the number of bits is \(5 \times 10^6 \times 600 = 3 \times 10^9\) bits. [M1] [A1]

(b) Divide by 8 to convert bits to bytes: \(3 \times 10^9 \div 8 = 375 \times 10^6\) bytes, which is 375 MB. [B1]
:::

You can check the arithmetic with a short program.

```python
bit_rate_mbps = 5
minutes = 10
bits = bit_rate_mbps * 1000000 * minutes * 60
megabytes = bits / 8 / 1000000
print(bits, "bits")
print(megabytes, "MB")
```

Output:

```output
3000000000 bits
375.0 MB
```

:::eg Will it play without buffering?
A school in Kigali streams a live lesson at 2.5 Mbps. The school's connection delivers 2 Mbps. State whether the lesson will play without buffering and explain your answer. [3 marks]

- The stream needs 2.5 Mbps and the connection delivers only 2 Mbps, so the connection is slower than the stream. [B1]
- Bits arrive more slowly than the player uses them, so the buffer empties. [B1]
- A live stream cannot be downloaded ahead, so the video pauses (buffers) or its quality is reduced. [B1]
:::

## IP addresses

Every device that uses the internet needs an address, so that data can be sent to it.

:::def IP address
A unique number, given to a device on a network, that identifies the device and the network it is on, so that packets can be sent to the correct destination. It is used by routers to deliver packets.
:::

An IP address is not the same as a MAC address. A MAC address is fixed to the device's network card by its manufacturer and identifies the card. An IP address identifies a device's connection to a network and is given by the network, so a laptop has one IP address at home and another at school, while its MAC address stays the same. How are they linked? The IP address belongs to the network connection of the device (its network card) at that time, and the network keeps a table that links each IP address to the MAC address of the card that currently uses it. The router uses the IP address to get a packet to the right network, and the last step on that network uses the MAC address.

### IPv4

:::def IPv4 address
An IP address 32 bits long, written as four denary numbers from 0 to 255 separated by full stops, such as `192.168.1.20`. Each number is called an octet or a byte, and stands for 8 bits.
:::

Eight bits can hold the values 0 to 255, so an IPv4 address such as 192.168.1.20 is four bytes. In binary, 192 is 11000000, 168 is 10101000, 1 is 00000001 and 20 is 00010100. A program later in this chapter does this conversion for you.

The number of IPv4 addresses is \(2^{32} = 4\,294\,967\,296\), about 4.3 billion. That is fewer than the number of people on Earth, and each person may own several devices.

### IPv6

:::def IPv6 address
An IP address 128 bits long, written as eight groups of four hexadecimal digits separated by colons.
:::

An example of an IPv6 address:

```text
2001:0db8:0000:0000:0000:ff00:0042:8329
```

IPv6 was created because IPv4 addresses were running out. With 128 bits there are \(2^{128}\) addresses, about \(3.4 \times 10^{38}\), enough for every device many times over. Hexadecimal digits in an IPv6 address can be written in capitals or in lower case; this chapter uses lower case, as network software prints them.

Long IPv6 addresses have two shortening rules:

1. In each group, **leading zeros can be left out** (`0db8` becomes `db8`, `0042` becomes `42`, and a group `0000` becomes `0`).
2. **One run of groups that are all zeros can be replaced by `::`.** This can be used **only once** in an address, because otherwise you could not tell how many zero groups each `::` stands for.

```python
import ipaddress

full = "2001:0db8:0000:0000:0000:ff00:0042:8329"
address = ipaddress.ip_address(full)
print(address.compressed)
print(address.exploded)
print(2 ** 32, 2 ** 128)
```

Output:

```output
2001:db8::ff00:42:8329
2001:0db8:0000:0000:0000:ff00:0042:8329
4294967296 340282366920938463463374607431768211456
```

The short form `2001:db8::ff00:42:8329` has 5 groups written out, so `::` must stand for \(8 - 5 = 3\) groups of zeros. Reading a short IPv6 address back into full form means counting the groups that are shown and filling the rest with `0000`.

:::eg Valid or not valid?
State whether each address is valid and give a reason. [4 marks]

(a) `172.16.254.3`  (b) `192.168.1.256`  (c) `10.0.5`  (d) `fe80::1::2`

- (a) Valid: four numbers, each from 0 to 255. [B1]
- (b) Not valid: the last number, 256, is greater than 255. [B1]
- (c) Not valid: an IPv4 address has four numbers, and this one has only three. [B1]
- (d) Not valid: `::` has been used twice, so it is not possible to tell how many zero groups each one stands for. [B1]
:::

A program can check the dotted form. It splits the text at each full stop and tests every part.

```python
def is_valid_ipv4(text):
    parts = text.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if int(part) > 255:
            return False
    return True

for address in ["192.168.1.20", "192.168.1", "192.168.1.256", "10.0.0.x", "172.16.0.1"]:
    print(address, is_valid_ipv4(address))
```

Output:

```output
192.168.1.20 True
192.168.1 False
192.168.1.256 False
10.0.0.x False
172.16.0.1 True
```

`part.isdigit()` is False for an empty part, so an address such as `1..2.3` is rejected as well. In a Paper 2 style question, the four numbers are already in an array, and the pseudocode only has to test the range:

```pseudocode
DECLARE Valid : BOOLEAN
DECLARE Index : INTEGER

Valid ← TRUE
FOR Index ← 1 TO 4
   IF Octets[Index] < 0 OR Octets[Index] > 255 THEN
      Valid ← FALSE
   ENDIF
NEXT Index
IF Valid = TRUE THEN
   OUTPUT "Valid IPv4 address"
ELSE
   OUTPUT "Not valid"
ENDIF
```

The loop never stops early, because it has to look at all four numbers, and `Valid` starts TRUE and can only change to FALSE.

## Network part, host part and subnets

An IP address has two parts. The first part is the **network part** and says which network the device is on. The rest is the **host part** and says which device on that network. All the devices on one network share the same network part. A **subnet mask** says where the split is.

:::def Subnet mask
A 32-bit number, written like an IPv4 address, in which the 1 bits mark the network part of an address and the 0 bits mark the host part. A device ANDs an address with the mask to find the network the address belongs to.
:::

The mask is a block of 1s followed by 0s. The mask `255.255.255.0` is 24 ones followed by 8 zeros, so the first three numbers are the network part and the last number is the host part. A shorter way of writing the same thing is a **prefix** after a slash: `192.168.1.20/24` means the first 24 bits are the network part. A mask of 255.255.255.192 is 26 ones (the number 192 is 11000000), so it is written `/26`.

### Finding the network address

The **network address** is found by an **AND** of the address and the mask, bit by bit. A bit of the result is 1 only if both bits are 1. The mask keeps the network bits and turns every host bit into 0.

:::key Finding the network address
1. Write the address and the mask in binary, octet by octet.
2. AND them: 1 AND 1 gives 1, anything else gives 0.
3. The result is the **network address**: the host part is all zeros.
4. The **broadcast address** is the network address with the host part all ones. Neither the network address nor the broadcast address can be given to a device.
5. The number of **usable host addresses** is \(2^h - 2\), where \(h\) is the number of host bits (32 minus the prefix length).
:::

:::eg Network address, broadcast address and hosts
A device has the IP address 172.16.37.200 and the subnet mask 255.255.240.0. Find the network address, the broadcast address and the number of usable host addresses. [5 marks]

Only the third octet is awkward, because 240 is 11110000. The first two octets of the mask are 255, which keep them unchanged, and the fourth is 0, which makes it 0.

Third octet: 37 is 00100101 and 240 is 11110000. The AND is 00100000, which is 32. [M1]

The network address is 172.16.32.0. [A1]

The mask has \(8 + 8 + 4 = 20\) ones, so the prefix is /20 and there are \(32 - 20 = 12\) host bits. [B1]

The broadcast address has all 12 host bits as 1: the last four bits of the third octet are 1111 (so 32 + 15 = 47), and the fourth octet is 255. The broadcast address is 172.16.47.255. [B1]

The number of usable host addresses is \(2^{12} - 2 = 4096 - 2 = 4094\). [B1]
:::

The same working as a program. Python's `&` operator does an AND on every pair of bits of two whole numbers, and `format(number, "08b")` writes a number as 8 binary digits.

```python
def to_binary(address):
    return ".".join(format(int(part), "08b") for part in address.split("."))

def network_address(address, mask):
    a = address.split(".")
    m = mask.split(".")
    result = []
    for i in range(4):
        result.append(str(int(a[i]) & int(m[i])))
    return ".".join(result)

print(to_binary("172.16.37.200"))
print(to_binary("255.255.240.0"))
print(network_address("172.16.37.200", "255.255.240.0"))
```

Output:

```output
10101100.00010000.00100101.11001000
11111111.11111111.11110000.00000000
172.16.32.0
```

The number of usable hosts for some common prefixes shows how few host bits change the answer quickly:

```python
for prefix in [24, 26, 28, 30]:
    host_bits = 32 - prefix
    print("/" + str(prefix), "gives", host_bits, "host bits and", 2 ** host_bits - 2, "usable hosts")
```

Output:

```output
/24 gives 8 host bits and 254 usable hosts
/26 gives 6 host bits and 62 usable hosts
/28 gives 4 host bits and 14 usable hosts
/30 gives 2 host bits and 2 usable hosts
```

Use the tool below to try your own addresses. It shows the AND in binary, with a bar `|` between the network part and the host part, the network address, the first and last host, the broadcast address and the number of usable hosts. Try the prefix 24, then 26, and watch how the host part shrinks. Try the address 10.0.0.5 and see that it is private.

:::html
<div class="widget" data-w="cs-ip" data-ip="192.168.10.77" data-prefix="26"></div>
:::

### Two devices, one network or two?

A device uses the mask to decide whether a packet's destination is on its own network. It ANDs its own address with the mask and ANDs the destination address with the mask. If the two results are the same, the destination is on the same network, and the packet is sent directly. If they are different, the packet is sent to the **default gateway**, which is the router's address on the local network, and the router forwards it.

:::eg Same subnet or different?
A school network uses the mask 255.255.255.192. A computer with address 192.168.1.130 sends data to a computer with address 192.168.1.70. Decide whether they are on the same subnet. [3 marks]

The mask 255.255.255.192 is /26, so only the last octet needs the AND, with 192 = 11000000. [B1]

130 is 10000010, and the AND is 10000000 = 128, so the network address of the first computer is 192.168.1.128. 70 is 01000110, and the AND is 01000000 = 64, so the network address of the second is 192.168.1.64. [B1]

The network addresses differ, so the computers are on different subnets, and the data must go through the router. [B1]
:::

### Subnetting

**Subnetting** means dividing one network into smaller networks. You take some of the host bits and use them as extra network bits.

:::def Subnetting
Dividing a network into smaller networks (subnets) by using some of the host bits of the address as extra network bits, so that the subnet mask has more 1s.
:::

Why subnet? A big network has too much traffic, because every broadcast goes to every device. Subnets keep local traffic inside their own subnet, which improves performance. A router sits between the subnets, so the network manager can control what passes between them, such as keeping the student network apart from the staff network, which improves security. Subnets also make a large network easier to manage, and they use addresses more efficiently.

Take the network 192.168.1.0/24, which has 8 host bits. To make 4 subnets we need 2 extra network bits (\(2^2 = 4\)). The prefix becomes \(24 + 2 = 26\), the mask 255.255.255.192, and each subnet has 6 host bits, so \(2^6 - 2 = 62\) usable addresses. The last octet of each subnet starts at a multiple of 64.

```python
for n in range(4):
    start = n * 64
    print(f"192.168.1.{start}/26 hosts 192.168.1.{start + 1} to 192.168.1.{start + 62}, broadcast 192.168.1.{start + 63}")
```

Output:

```output
192.168.1.0/26 hosts 192.168.1.1 to 192.168.1.62, broadcast 192.168.1.63
192.168.1.64/26 hosts 192.168.1.65 to 192.168.1.126, broadcast 192.168.1.127
192.168.1.128/26 hosts 192.168.1.129 to 192.168.1.190, broadcast 192.168.1.191
192.168.1.192/26 hosts 192.168.1.193 to 192.168.1.254, broadcast 192.168.1.255
```

Notice the cost of subnetting: the original network had 254 usable hosts, and the four subnets have \(4 \times 62 = 248\), because each subnet loses its own network and broadcast address.

## Public and private, static and dynamic addresses

### Public and private IP addresses

:::def Public IP address
An IP address that is unique across the whole internet and can be reached directly from any other device on the internet. It is given by an internet service provider.
:::

:::def Private IP address
An IP address that is used inside a local network and is not allowed to be routed across the internet. Many networks can use the same private addresses at the same time, because they never meet on the internet.
:::

Three blocks of addresses are set aside for private use:

| Range | Prefix | Number of addresses |
|---|---|---|
| 10.0.0.0 to 10.255.255.255 | 10.0.0.0/8 | 16 777 216 |
| 172.16.0.0 to 172.31.255.255 | 172.16.0.0/12 | 1 048 576 |
| 192.168.0.0 to 192.168.255.255 | 192.168.0.0/16 | 65 536 |

Any other address is a public address. Notice that 172.32.0.1 is public although it starts with 172: the private block stops at 172.31.255.255.

The devices in a home or school LAN have private addresses. The router has one public address on the side facing the internet, and it uses **network address translation (NAT)** to share that one address between all the devices. When a device sends a request, the router replaces its private source address with the router's public address and remembers which device asked. When the reply comes back, it passes the reply to that device. A packet that arrives from the internet that nobody asked for has no device to go to, so it is not delivered.

**Security.** A device with a private address cannot be reached directly from the internet, so an attacker cannot send traffic straight to it. This makes a LAN safer, but it does not make it safe: the devices can still be attacked through the requests they make, for example by a harmful web page, so a firewall and updates are still needed. A device with a public address, such as a web server, can be contacted by anyone on the internet, so it is exposed to attack and needs to be protected carefully.

### Static and dynamic IP addresses

:::def Static IP address
An IP address that is set by hand for a device and stays the same every time the device connects.
:::

:::def Dynamic IP address
An IP address that is given to a device automatically each time it connects to the network, usually by a DHCP server, and that can be different each time.
:::

:::def DHCP
Dynamic Host Configuration Protocol. A service, usually in the router, that gives an IP address from a pool of free addresses to each device that joins the network, for a period of time called a lease.
:::

When a laptop joins the network, it asks for an address, the DHCP server gives it a free address from its pool, and the laptop uses that address until the lease ends. When the laptop leaves, the address goes back to the pool and another device can use it.

| | Static | Dynamic |
|---|---|---|
| Set by | a person, once | the DHCP server, automatically |
| Changes? | never, unless changed by hand | may be different each time |
| Good for | servers, printers, routers, web servers that others must find at a fixed address | laptops, phones and other devices that come and go |
| Benefit | other devices can always find it | no set-up work, and addresses are reused so fewer are needed |
| Drawback | someone must set it, and two devices set to the same address will conflict | the address can change, so the device cannot be found reliably at one address |

:::eg Justifying a static address
A school network has a print server that all teachers' computers use. Justify the use of a static IP address for the print server. [3 marks]

- A static address never changes, so every computer can be set to send print jobs to the same address, and it always finds the print server. [B1]
- With a dynamic address, the print server's address could change after a restart, and the print jobs would then be sent to an address with no printer, or to a different device. [B1]
- The server is always switched on and always on the same network, so it does not need an address that is handed out and taken back. [B1]
:::

:::eg Public or private?
A hospital in Karachi has a LAN with 200 computers that use private IP addresses, and one web server with a public IP address. Explain the security implications of this choice. [4 marks]

- The computers have private addresses, so they cannot be reached directly from the internet, which protects them from attacks that come from outside. [B1]
- The router uses NAT to share one public address and only passes in replies to requests that a computer made, so unrequested traffic is not delivered to the computers. [B1]
- The web server has a public address, so anyone on the internet can contact it. [B1]
- It is therefore exposed to attack, so it needs protection, such as a firewall and regular updates. [B1]
:::

## URLs and the Domain Name Service

### Uniform resource locators

People use names such as `www.example.org`, but routers use numbers. A URL (a web address) names a resource, and the Domain Name Service turns the name into the number.

:::def Uniform Resource Locator (URL)
A text address that identifies a resource on the World Wide Web, such as a page or an image, and says how to reach it. It is made of a protocol, a domain name, a path and a file name.
:::

Take this URL:

```text
https://www.example.org/lessons/year9/timetable.html
```

| Part | Example | Meaning |
|---|---|---|
| Protocol | `https` | the set of rules the browser uses to ask for the resource (HTTP, or HTTPS, which is HTTP with encryption) |
| Domain name | `www.example.org` | the name of the web server's computer, read from right to left: the top-level domain `org`, the domain `example`, and the host name `www` |
| Path | `/lessons/year9/` | the folders on the server in which the resource is held |
| File name | `timetable.html` | the resource asked for |

A URL can also include a port number after the domain name, a query after `?` and a fragment after `#`. Those parts are not needed in the exam.

### The Domain Name Service

:::def Domain Name Service (DNS)
A system of servers that keeps the records that link domain names to IP addresses. A computer asks a DNS server for the IP address that belongs to a domain name, and the server replies with it.
:::

The DNS works like a phone book of the internet: you look up a name and find a number. It does **not** store the web pages. It stores only the link between a name and an IP address. The DNS is spread over many servers in a hierarchy, so that no single server has to hold every name: **root servers** know where to find the servers for each **top-level domain** (such as `.org`, `.com` or `.uk`), and the servers for a domain know the addresses of the names in that domain.

:::html
<figure class="fig small"><svg viewBox="0 0 340 185" role="img" aria-label="A DNS lookup drawn as six numbered arrows between four boxes. 1: the browser asks the resolver for the IP address of the name. 2: the resolver asks the DNS servers. 3: the DNS servers reply with the IP address. 4: the resolver passes the IP address to the browser. 5: the browser requests the page from the web server. 6: the web server sends the page back. Solid arrows are requests and dashed arrows are replies."><rect class="fm s-acc sw2" x="14" y="20" width="84" height="34"/><text class="tl tc" x="56" y="42">Browser</text><rect class="fm s-acc sw2" x="242" y="20" width="84" height="34"/><text class="tl tc" x="284" y="42">Resolver</text><rect class="f1 s-acc sw2" x="14" y="136" width="84" height="34"/><text class="tl tc" x="56" y="158">Web server</text><rect class="fm s-acc sw2" x="242" y="136" width="84" height="34"/><text class="tl tc" x="284" y="158">DNS servers</text><line class="c1 sw2" x1="106" y1="30" x2="234" y2="30" marker-end="url(#ah)"/><text class="tl tc" x="170" y="22">1</text><line class="ln-m dash" x1="234" y1="46" x2="106" y2="46" marker-end="url(#ahm)"/><text class="tl tc" x="170" y="62">4</text><line class="c1 sw2" x1="268" y1="62" x2="268" y2="128" marker-end="url(#ah)"/><text class="tl te" x="259" y="99">2</text><line class="ln-m dash" x1="300" y1="128" x2="300" y2="62" marker-end="url(#ahm)"/><text class="tl" x="308" y="99">3</text><line class="c1 sw2" x1="28" y1="62" x2="28" y2="128" marker-end="url(#ah)"/><text class="tl te" x="20" y="99">5</text><line class="ln-m dash" x1="70" y1="128" x2="70" y2="62" marker-end="url(#ahm)"/><text class="tl" x="78" y="99">6</text></svg><figcaption>The six steps of a DNS lookup. The numbers match the list below; solid arrows are requests and dashed arrows are replies.</figcaption></figure>
:::

The steps, in order:

:::steps
1. The user types a URL. The browser extracts the domain name, `www.example.org`, and checks whether it already knows the IP address from an earlier visit (its cache). If it does not, it asks a DNS resolver, usually run by the ISP.
2. The resolver checks its own cache. If the address is not there, it asks the DNS servers, starting with a root server, which sends it to the `.org` servers, which send it to the servers for `example.org`.
3. The DNS server for the domain finds the record for `www.example.org` and returns its IP address to the resolver.
4. The resolver keeps a copy of the IP address in its cache, for later requests, and returns the IP address to the browser.
5. The browser sends a request for the page to the web server at that IP address, using the protocol in the URL.
6. The web server sends the page back, and the browser displays it.
:::

This program imitates the steps with a dictionary of records. The first request goes to the DNS servers, the second is answered from the resolver's cache, and the third shows that a name that does not exist gets no address.

```python
dns_servers = {"www.example.org": "203.0.113.25", "www.example.com": "198.51.100.7"}
resolver_cache = {}

def look_up(name):
    if name in resolver_cache:
        print("Resolver cache hit for", name)
        return resolver_cache[name]
    print("Resolver asks the DNS servers for", name)
    if name in dns_servers:
        resolver_cache[name] = dns_servers[name]
        return dns_servers[name]
    print("No such domain name")
    return None

print(look_up("www.example.org"))
print(look_up("www.example.org"))
print(look_up("www.nosuch.org"))
```

Output:

```output
Resolver asks the DNS servers for www.example.org
203.0.113.25
Resolver cache hit for www.example.org
203.0.113.25
Resolver asks the DNS servers for www.nosuch.org
No such domain name
None
```

The addresses here are invented (they come from blocks reserved for examples). The cache is the reason popular names are found quickly: only the first request has to go through the hierarchy.

:::eg Explaining how DNS finds a web page
A student types `https://www.example.org/maps.html` into a browser. Explain how the Domain Name Service is used to find the web page. [5 marks]

- The browser takes the domain name from the URL and asks a DNS resolver (or looks in its own cache) for the IP address that belongs to it. [B1]
- If the resolver does not have it in its cache, it asks the DNS servers, which are arranged in a hierarchy, starting with the root and the top-level domain servers. [B1]
- The DNS server for the domain looks up the domain name in its records and returns the IP address. [B1]
- The IP address is returned to the browser (and the resolver stores it in its cache). [B1]
- The browser sends a request for the page, using the protocol in the URL, to the web server at that IP address, and the server returns the page. [B1]
:::

:::warn Common slips about the DNS
The DNS does not store the website, and it does not send you the web page. It only returns an IP address. Also, a MAC address is not an IP address, and an IP address is not a URL: a URL contains a domain name, and the DNS turns the domain name into an IP address.
:::

:::exam Describe, explain, justify
Cambridge uses command words precisely. "State" and "name" need a short answer. "Describe" needs the main features. "Explain" needs a reason, with the word "because" or "so". "Justify" needs a reason taken from the scenario in the question. In the DNS question, five separate steps earn five separate marks, so write the steps in order, one per sentence.
:::

:::eg Spot the error: shortening an IPv6 address
Question: Write this IPv6 address in its shortest form. [3 marks]

```text
2001:0db8:0000:0042:0000:0000:0000:0001
```

A student wrote `2001:db8::42::1`.

The leading zeros of the groups have been removed correctly (`0db8` to `db8`, `0042` to `42`, `0001` to `1`) [B1]. The longest run of zero groups (the three groups before the final group) has been replaced by `::` correctly [B1]. **The single zero group `0000` between `db8` and `42` has also been replaced by `::`. `::` may be used only once, so the address is not valid** [B0]. The answer scores 2 out of 3.

The correct short form is `2001:db8:0:42::1`: the single zero group is written as `0`.
:::

:::try Start easy, finish at exam standard
Q: State the difference between the internet and the World Wide Web.
A: The internet is the global network of connected networks (the hardware and protocols). The World Wide Web is a collection of web pages and other resources that are accessed over the internet, using URLs and HTTP.
Q: State what a modem does.
A: It converts digital data from a computer into a signal that can be sent over a telephone or cable line, and converts the incoming signal back to digital data.
Q: A video is streamed at 4 Mbps. How many bits are sent in 30 seconds?
A: \(4 \times 10^6 \times 30 = 120 \times 10^6 = 120\,000\,000\) bits.
Q: A file of 600 MB is downloaded at 8 Mbps. How many seconds does it take, if the full speed is used?
A: 600 MB is \(600 \times 8 = 4800\) megabits. At 8 megabits per second this takes \(4800 \div 8 = 600\) s, which is 10 minutes.
Q: How many bits are in an IPv4 address and how many in an IPv6 address?
A: 32 bits in IPv4 and 128 bits in IPv6.
Q: Is `255.255.255.0` a valid IPv4 address? Is `300.1.1.1`?
A: Yes, each number is from 0 to 255 (it is also often used as a subnet mask). No, 300 is greater than 255.
Q: State the network address of the device 192.168.5.37 with the subnet mask 255.255.255.0.
A: The mask keeps the first three numbers and sets the last to 0, so the network address is 192.168.5.0.
Q: How many usable host addresses are there in a subnet with 5 host bits?
A: \(2^5 - 2 = 32 - 2 = 30\).
Q: Is 172.20.14.9 a public or a private address? Give a reason.
A: Private: it is in the block 172.16.0.0 to 172.31.255.255.
Q: State one device that should have a static IP address and one that can have a dynamic address.
A: Static: a web server, a print server or a router (it must be found at a fixed address). Dynamic: a student's laptop or phone (it joins and leaves the network).
Q: Identify the protocol, the domain name, the path and the file name in `http://example.com/news/today.html`.
A: Protocol `http`; domain name `example.com`; path `/news/`; file name `today.html`.
Q: Use `::` to shorten the address `fe80:0:0:0:202:b3ff:fe1e:8329`.
A: `fe80::202:b3ff:fe1e:8329`. The three groups of zeros in a row are replaced by `::`, used once.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ State whether each address is a valid IPv4 or IPv6 address, and give a reason if it is not valid.

(a) `10.256.4.1` [1]

(b) `192.168.0.1` [1]

(c) `2001:db8::8a2e::7334` [1]

(d) `172.16.5` [1]
A: (a) Not valid: 256 is greater than 255 [B1]. (b) Valid IPv4 address [B1]. (c) Not valid: `::` is used twice [B1]. (d) Not valid: it has only three numbers, and an IPv4 address has four [B1].

Q: [5 marks] ★★ Explain how a web browser finds the web server for the URL `https://www.example.org/news.html`.
H: The answer is the DNS lookup, in order: five points.
H: Say what is looked up, where, and what comes back.
A: One mark for each step.

- The browser sends the domain name `www.example.org` from the URL to a DNS resolver (after checking its own cache) [B1]
- The resolver looks in its cache for the IP address and, if it is not there, asks the DNS servers [B1]
- The DNS servers, arranged in a hierarchy, find the record for the domain name [B1]
- The IP address is returned to the resolver and then to the browser [B1]
- The browser uses the IP address to send a request to the web server [B1]

Q: [3 marks] ★★ A company in Dhaka hosts its website on its own web server. Justify the use of a static public IP address for the web server.
A: One mark for each justified point.

- A static address does not change, so the web server is always found at the same address [B1]
- The DNS record that links the company's domain name to the server's IP address would be wrong if the address changed, so customers could not reach the site [B1]
- A public address is needed because customers on the internet must be able to reach the server directly [B1]

Q: [5 marks] ★★ A teacher streams a live lesson at 4 Mbps. (a) Explain why the lesson will pause if the school's connection can deliver only 3 Mbps. [2] (b) A recorded lesson of 30 minutes is stored at 4 Mbps. Calculate its size in megabytes. [3]
H: (b) Find the number of bits first, then convert to bytes.
A: (a) The stream needs 4 Mbps but only 3 Mbps arrive, so the bits arrive more slowly than the player uses them [B1], so the buffer empties and the video pauses or drops in quality; a live stream cannot be downloaded ahead [B1].

(b) 30 minutes is 1800 s, so the number of bits is \(4 \times 10^6 \times 1800 = 7.2 \times 10^9\) [M1]; divide by 8 to give bytes, \(7.2 \times 10^9 \div 8 = 900 \times 10^6\) [M1]; the size is 900 MB [A1].

Q: [5 marks] ★★ A device has the IP address 192.168.40.150 and the subnet mask 255.255.255.224.

(a) State the prefix length. [1]

(b) Find the network address, showing your working. [2]

(c) Calculate the number of usable host addresses in the subnet. [2]
H: 224 is 11100000, so how many 1s are there in the mask?
H: The AND only changes the last octet: 150 is 10010110.
A: (a) \(8 + 8 + 8 + 3 = 27\), so the prefix is /27 [B1].

(b) The last octet: 150 is 10010110 and 224 is 11100000, so the AND is 10000000, which is 128 [M1]; the network address is 192.168.40.128 [A1].

(c) There are \(32 - 27 = 5\) host bits [M1], so there are \(2^5 - 2 = 30\) usable host addresses [A1].

Q: [4 marks] ★★ Explain the difference between a public and a private IP address, and why a computer that has a private address is more difficult for an attacker to contact than a computer that has a public one.
A: One mark for each point.

- A public IP address is unique on the internet and can be reached directly from any device on the internet [B1]
- A private IP address is used only inside a local network and is not routed across the internet [B1]
- A computer with a private address sits behind a router that uses NAT [B1]
- Traffic that arrives from the internet and that the computer did not ask for is not delivered to it, so the attacker cannot contact it directly [B1]

Q: [4 marks] ★★ Describe the difference between the internet and the World Wide Web.
A: One mark for each point.

- The internet is a worldwide network of networks, made of hardware such as routers and cables, and protocols [B1]
- The World Wide Web is a collection of web pages and other resources held on web servers [B1]
- The web is accessed using a browser, URLs and the HTTP or HTTPS protocol [B1]
- The web is one service that runs on the internet; the internet also carries email and other services [B1]

Q: [8 marks] ★★★ A call centre in Karachi has 120 staff in one office. It needs a connection to the internet, and a link to a data centre in another city that must keep working at the same speed all day.

(a) Describe how a modem is used to connect a computer to the internet over the PSTN. [3]

(b) Justify the use of a dedicated line for the link to the data centre. [3]

(c) The managers use their phones on the cell phone network when they travel. Describe how the cell phone network connects a moving phone to the internet. [2]
H: For (c), say what a cell is and what happens when the phone moves.
A: (a) The computer produces digital data [B1]; the modem converts it to analogue signals that the telephone line can carry [B1]; the modem also converts the incoming analogue signals back into digital data for the computer [B1].

(b) A dedicated line is used only by the company, so its speed does not vary with the other customers' use during the day [B1]; it has a fixed, guaranteed bandwidth, which suits a link that must keep working at the same speed all day [B1]; it is a private, reliable connection between the two cities, which is not shared with other users [B1].

(c) The area is divided into cells, each with a base station, and the phone connects by radio to the base station in the cell it is in [B1]; as the phone moves into another cell, the connection is handed over to that cell's base station, and the base stations are connected to the internet [B1].
:::

:::try Stretch for A*
Q: A company has been given the network 192.168.5.0/24. It has 4 departments, each with at most 50 devices, and wants one subnet for each department. (a) Which prefix length should it use, and why is /27 not enough? (b) Write the network address and the range of usable addresses of each subnet. (c) How many addresses are wasted in each subnet?
H: Four subnets need 2 extra network bits. How many host bits are left?
H: Each subnet needs at least 52 addresses (50 devices, a network address and a broadcast address).
A: (a) Four subnets need 2 extra network bits, so the prefix is \(24 + 2 = 26\), which leaves 6 host bits and \(2^6 - 2 = 62\) usable addresses, enough for 50 devices. A /27 prefix leaves 5 host bits and only \(2^5 - 2 = 30\) usable addresses, which is fewer than 50. (b) The subnets are 192.168.5.0/26 (usable 192.168.5.1 to 192.168.5.62), 192.168.5.64/26 (usable .65 to .126), 192.168.5.128/26 (usable .129 to .190) and 192.168.5.192/26 (usable .193 to .254). (c) Each subnet has 62 usable addresses and a department uses at most 50, so at least \(62 - 50 = 12\) addresses are unused.

Q: A film of 10 minutes is stored on a server at 5 Mbps. A viewer's connection delivers 3 Mbps. (a) How long would the viewer need to wait before starting to play, so that the film plays from start to finish without pausing? (b) Show that this answer is the total download time minus the length of the film.
H: Let the viewer wait \(w\) seconds. After \(w + t\) seconds the player has received \(3(w + t)\) megabits, and playing for \(t\) seconds needs \(5t\) megabits.
H: The most difficult moment is the end of the film.
A: (a) At time \(t\) into the film, the data needed is \(5t\) Mb and the data received is \(3(w + t)\) Mb. Playing must never run out of data, so \(3(w + t) \ge 5t\), which gives \(w \ge \tfrac{2}{3}t\). The largest value of \(t\) is the length of the film, 600 s, so \(w \ge \tfrac{2}{3} \times 600 = 400\) s. (b) The film has \(5 \times 600 = 3000\) Mb, which takes \(3000 \div 3 = 1000\) s to download. \(1000 - 600 = 400\) s. If the whole film has arrived by the time it finishes playing, the data has never run out before then, because the connection is slower than the film, so the end is the hardest moment.
:::

:::quiz
? Which statement about the internet and the World Wide Web is correct?
- They are two names for the same thing.
- The internet is a service that runs on the World Wide Web.
+ The World Wide Web is a service that runs on the internet.
- The internet is only the set of web pages.
> The internet is the network of networks. The web (pages, URLs, HTTP) is one of the services that use it, as email is another.
? What does a modem do?
- It forwards packets between networks using IP addresses.
- It stores web pages.
+ It converts digital data to a signal that a telephone or cable line can carry, and back again.
- It turns a domain name into an IP address.
> A modem modulates and demodulates. Forwarding by IP address is the router's role and name lookup is done by the DNS.
? A connection delivers 10 Mbps. What is the maximum amount of data it can download in one second?
- 10 MB
- 80 MB
+ 1.25 MB
- 12.5 MB
> 10 megabits is \(10 \div 8 = 1.25\) megabytes. The answer 10 MB confuses bits and bytes.
? Why is a real-time (live) stream more likely to pause than an on-demand stream when the connection slows down?
- A live stream has a higher bit rate.
- A live stream is stored on a slower server.
+ It cannot be downloaded ahead, so its buffer is small and empties quickly.
- A live stream does not use a buffer.
> A live stream is sent as it happens, so there is no extra data to put into a large buffer. An on-demand player can fill its buffer ahead.
? Which of these is a valid IPv4 address?
- 192.168.1
- 192.168.1.1.1
- 192.168.1.256
+ 192.168.1.255
> An IPv4 address has four numbers from 0 to 255. 255 is allowed in the last position, although a broadcast address is not given to a device.
? Why can `::` be used only once in an IPv6 address?
- Because it stands for a colon.
+ Because otherwise the number of zero groups each `::` stands for could not be known.
- Because IPv6 addresses have only one group of zeros.
- Because a second `::` would make the address too long.
> The groups that are left out are found by counting the groups that are shown. With two `::` the count could be split between them in many ways.
? What is the network address of 10.1.150.20 with the mask 255.255.192.0?
- 10.1.192.0
- 10.1.150.0
+ 10.1.128.0
- 10.1.0.0
> The network address is the address ANDed with the mask. In the third octet, 150 is 10010110 and 192 is 11000000, which gives 10000000 = 128, and the fourth octet becomes 0.
? Which address is a private IP address?
- 172.32.0.5
- 11.0.0.1
+ 192.168.100.4
- 8.8.8.8
> The private blocks are 10.x.x.x, 172.16.x.x to 172.31.x.x and 192.168.x.x. 172.32.0.5 is outside the 172.16.0.0/12 block.
? What does the DNS return when a browser asks for the address of `www.example.org`?
- the web page
- the MAC address of the web server
+ the IP address that belongs to the domain name
- the path to the file
> The DNS only links names to IP addresses. The browser then asks the web server at that address for the page.
? When is a static IP address the better choice?
- For a visitor's phone that joins the network for an hour.
+ For a web server that must always be found at the same address.
- For any device on a network that uses NAT.
- When the network has no router.
> A static address is set by hand and never changes, so other devices and the DNS can rely on it. Devices that come and go suit dynamic addresses.
:::

:::checklist What you can now do
- [ ] I can describe real-time and on-demand bit streaming and explain why bit rate and broadband speed matter.
- [ ] I can calculate the data used by a stream and whether a connection can keep up, keeping bits and bytes apart.
- [ ] I can explain the difference between the internet and the World Wide Web.
- [ ] I can describe the hardware that supports the internet: modems, the PSTN, dedicated lines and the cell phone network.
- [ ] I can describe the format of IPv4 and IPv6 addresses, check whether an address is valid, and shorten an IPv6 address.
- [ ] I can use a subnet mask to find the network address, the broadcast address and the number of usable hosts, and explain why networks are divided into subnets.
- [ ] I can explain how an IP address is associated with a device on a network.
- [ ] I can explain the difference between public and private IP addresses and the security implications.
- [ ] I can explain the difference between static and dynamic IP addresses and justify a choice.
- [ ] I can explain how a URL locates a resource and the role of the DNS.
:::

:::recap
- The internet is the global network of networks; the World Wide Web is the pages and resources (URLs, HTTP) that run on it. A modem converts between digital data and the signals of a telephone line; the PSTN is the telephone network; a dedicated line is a private leased link; the cell phone network uses base stations in cells.
- Bit streaming plays data as it arrives, using a buffer. Real-time (live) cannot be skipped; on-demand is stored and can be paused. The connection's bit rate must be at least the stream's, or the stream buffers. Mbps are bits; MB are bytes; divide by 8.
- IPv4: 32 bits, four numbers from 0 to 255 (about 4.3 billion addresses). IPv6: 128 bits, eight groups of four hex digits, leading zeros dropped, `::` for one run of zero groups, used once only.
- A subnet mask (or prefix) splits an address into network and host parts. Network address = address AND mask. Usable hosts = \(2^h - 2\). Subnetting divides a network into smaller ones, for performance, security and management.
- Public addresses are unique on the internet and reachable directly. Private addresses (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) are used inside LANs behind a NAT router and cannot be reached directly from the internet.
- Static addresses are set by hand and never change (servers, printers). Dynamic addresses are given by DHCP and can change (phones, laptops).
- A URL has a protocol, a domain name, a path and a file name. The DNS turns a domain name into an IP address: browser, resolver, DNS servers, IP address back, then the request to the web server.
:::

:::links
- practise: [Networks and the internet: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/2-communication-/networks-and-the-internet/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- read: [What is a URL?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL) · MDN · the parts of a URL, explained clearly
- read: [An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) · MDN · how a browser and a web server talk
- read: [Computers and the internet](https://www.khanacademy.org/computing/computers-and-internet) · Khan Academy · free lessons on IP addresses, DNS and how the internet works
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos on the internet and DNS by university computer scientists

Links checked 13 November 2026.
:::

Next: [Computers and their components](#cs.hardware)
