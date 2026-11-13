@chapter cs.networks
@title Networks: models, topologies and hardware
@level as
@paper CAIE 9618 Paper 1
@time 5–7 hours
@summary Why computers are networked, how LANs and WANs differ, the client-server and peer-to-peer models, thin and thick clients, the bus, star, mesh and hybrid topologies and how a packet crosses each, cloud computing, wired and wireless transmission media, LAN hardware, the router, and how Ethernet detects and avoids collisions with CSMA/CD.

:::why
Almost every device you use is part of a network: a school's computers share printers and files, a phone reaches the internet through a router, and a company's customer records may live in a data centre on another continent. Paper 1 asks you to describe these systems, compare them and choose the right one for a scenario, so you need exact terms and reasons that fit the scenario. This chapter builds the vocabulary; [the next chapter](#cs.internet) explains how the internet itself finds and delivers data.
:::

**Before you start**, you should know how binary and hexadecimal work, from [Number systems and binary arithmetic](#cs.data). You should also be able to read a short Python program, from [Programming from zero](#cs.f.basics).

:::try Warm-up
Q: How many bits are there in 4 bytes? (from [Number systems and binary arithmetic](#cs.data))
A: One byte is 8 bits, so 4 bytes is \(4 \times 8 = 32\) bits.
Q: Which hexadecimal digit stands for the binary number 1111, and what is the denary value? (from [Number systems and binary arithmetic](#cs.data))
A: F, which is 15 in denary. Hexadecimal digits are used again later in this chapter, because a MAC address is written in hexadecimal.
Q: What does this Python print? `n = 5`, then `if n * 2 > 8:`, `print("big")`, `else:`, `print("small")` (from [Programming from zero](#cs.f.basics))
A: `big`, because \(5 \times 2 = 10\), and 10 is greater than 8.
:::

## Why computers are networked

A **network** is a group of computers and other devices that are connected so they can exchange data. A single computer on its own is useful. The same computer on a network can do much more.

:::def Network
Two or more computing devices connected together, by cables or by wireless links, so that they can exchange data and share resources.
:::

The purpose and benefits of networking are the first thing Paper 1 may ask about. Learn them as a list of specific, different points:

- **Share files and data.** Staff work on the same documents without copying them on to memory sticks, and a change made by one person is seen by everyone.
- **Share hardware.** One printer, scanner or large storage drive can serve a whole office, so you buy fewer devices.
- **Share an internet connection.** One connection into the building serves every device.
- **Communicate.** Email, messaging and video calls between users on the network.
- **Central management, backup and security.** One person can install updates, make backups of everyone's files and decide who may open what, instead of visiting every computer.
- **Share software.** A licence can be held centrally and used by many computers.

Networks also have drawbacks: the equipment costs money, a fault in a main link or server can stop many users at once, and a connected network can be attacked from outside, so it needs security measures.

## LANs and WANs

Networks are described first by how far they reach.

:::def Local area network (LAN)
A network that connects computers and devices in a small geographical area, such as one building or one site, usually owned, managed and wired by the organisation that uses it.
:::

:::def Wide area network (WAN)
A network that connects computers and LANs over a large geographical area, such as between cities or countries, usually using telecommunications links that the organisation leases or that belong to the public network.
:::

| Feature | LAN | WAN |
|---|---|---|
| Area covered | one room, building or site | a city, a country or the world |
| Who owns the cables | the organisation | telecoms companies (leased or public lines) |
| Typical speed | high | lower for the same cost, and often shared |
| Cost to build and run | lower | higher |
| Example | the computers in a school in Lagos | the links joining a bank's branches in four countries |

The internet is the best-known WAN: it joins millions of LANs together. A company with offices in two cities usually has a LAN in each office and a WAN link between them. Notice that "big" is not the test. A network is a LAN because it covers one site and the organisation owns its cabling, not because it has few computers.

## Client-server and peer-to-peer

Within a network, each computer has a role. There are two main models.

:::def Client-server model
A network model in which one or more powerful computers, called servers, provide services (such as file storage, printing, email or web pages) and other computers, called clients, request those services over the network.
:::

:::def Server
A computer on a network that provides a service to other computers, such as storing files, managing printers, sending email or hosting web pages.
:::

:::def Client
A computer or program that requests a service from a server. A user's desktop computer is a typical client.
:::

A client-server network usually has several servers, each with a job: a **file server** stores users' files, a **print server** manages the printers and their queues, a **web server** delivers web pages, and an **email server** stores and forwards messages. Users log in with an account on a central server, which decides what each user may see. The clients ask; the servers answer.

:::def Peer-to-peer model
A network model in which every computer has the same status and can act as both client and server, sharing its own files and devices directly with the other computers, with no central server controlling the network.
:::

In a peer-to-peer network there is no central server. If Amira's computer holds a folder of photographs and she shares it, Bilal's computer is the client when he opens it, and her computer is the server for that moment. A moment later the roles can reverse.

:::cols
:::col Client-server: benefits
- Security and permissions are managed centrally, in one place.
- Files are backed up centrally, so users' work is safe.
- Easy to add users and to manage a large network.
- Servers are powerful, so many clients can be served at once.
:::
:::col Client-server: drawbacks
- Servers, software and the network equipment cost a lot.
- A skilled administrator is needed.
- If the server fails, clients that depend on it cannot work (a single point of failure).
- Many clients at once can overload the server or the network.
:::
:::

:::cols
:::col Peer-to-peer: benefits
- No server to buy, so it is cheap and simple to set up.
- No specialist administrator needed for a small network.
- If one computer fails, the others still work.
:::
:::col Peer-to-peer: drawbacks
- No central security: each user sets the permissions on their own computer.
- No central backup: each computer must be backed up separately.
- A computer being used by someone else slows down when others access its files.
- Becomes hard to manage as the number of computers grows.
:::
:::

A large client-server network is often built from **subnetworks**: smaller networks, for example one for each floor of an office or each department, joined to the rest by a router. Local traffic stays within its subnetwork, which keeps it fast and makes the network easier to manage and secure. Each subnetwork may have its own servers. The addressing of subnetworks is covered in [The internet: IP addresses, DNS and streaming](#cs.internet).

:::eg Justifying peer-to-peer for a small studio
A design studio in Lima has five employees, each with a computer. They want to share project files and one printer. The studio has no IT technician. Justify the use of a peer-to-peer network. [4 marks]

"Justify" means each point must be supported by something in the scenario. Pick four facts from the scenario and tie a benefit to each.

- With only five computers, the load of other users opening files on any one computer is small, so no powerful server is needed. [B1]
- There is no server to buy or maintain, so the cost is low for a small business. [B1]
- Nobody on the staff is an IT specialist, and a peer-to-peer network is simple enough that each user can share their own folders and the printer. [B1]
- Every computer can share files and the printer directly with the others, which is all the studio needs. [B1]

A drawback, such as the lack of central backup, does not earn a mark in a "justify" question unless you say how it can be managed (for example, by saving to one external drive each week). Always make the argument for the model you are asked to justify.
:::

### Thin clients and thick clients

Clients also differ in how much work they do themselves.

:::def Thin client
A client computer that depends on a server to do most of its processing and to store its programs and files. It has little processing power or storage of its own and needs the network connection to be useful.
:::

:::def Thick client
A client computer that has its own processor, memory, storage and software, so it does most of its processing locally. It uses the server mainly for shared files and services and can often work without the network.
:::

| | Thin client | Thick client |
|---|---|---|
| Processing | on the server | on the client itself |
| Storage | on the server | on the local drive (and the server) |
| Cost per computer | low | higher |
| If the network or server fails | cannot work | can often keep working on local files |
| Updating software | once, on the server | on every computer (or by a central tool) |
| Load on the server | high | lower |
| Example | a library terminal that boots from the server | a student's laptop with its own software |

Thin clients suit places where many identical computers are used for the same tasks, such as a call centre, a library or a school computer room, and where the organisation wants central control. A thick client suits someone who needs to work away from the network, such as a video editor with large local files.

## Network topologies

A **topology** is the layout of a network: which devices are connected to which. A topology has two forms: the *physical* layout of the cables and the *logical* way the data flows. This course uses the physical layout, drawn as a diagram. In every diagram the devices are called hosts or nodes.

:::def Topology
The arrangement of the devices (nodes) and the connections between them in a network.
:::

Data crosses a network in small pieces. Each piece has a **header**, which includes the address of the destination, and a part that carries the data. On a local network the piece is called a **frame** and the address is a MAC address (later in this chapter). On the internet it is called a **packet** and the address is an IP address. The detail of packets and how they are routed belongs to [Protocols, TCP/IP and packet switching](#cs.networks2); for now treat "packet" and "frame" as a piece of data with the destination's address on it.

### Bus topology

In a **bus** network all the hosts are connected to one shared cable, called the **backbone**. At each end of the cable is a **terminator**, a small device that absorbs the signal so that it does not bounce back along the cable.

:::html
<figure class="fig small"><svg viewBox="0 0 340 125" role="img" aria-label="A bus network. One horizontal backbone cable has a terminator at each end. Four hosts, A, B, C and D, hang from the cable by short drop cables. The shared cable is labelled."><line class="c1 sw3" x1="22" y1="78" x2="318" y2="78"/><rect class="f1 s-acc sw2" x="14" y="68" width="8" height="20"/><rect class="f1 s-acc sw2" x="318" y="68" width="8" height="20"/><line class="c1 sw2" x1="55" y1="50" x2="55" y2="78"/><line class="c1 sw2" x1="135" y1="50" x2="135" y2="78"/><line class="c1 sw2" x1="215" y1="50" x2="215" y2="78"/><line class="c1 sw2" x1="295" y1="50" x2="295" y2="78"/><rect class="fm s-acc sw2" x="33" y="24" width="44" height="26"/><text class="tl tc" x="55" y="42">A</text><rect class="fm s-acc sw2" x="113" y="24" width="44" height="26"/><text class="tl tc" x="135" y="42">B</text><rect class="fm s-acc sw2" x="193" y="24" width="44" height="26"/><text class="tl tc" x="215" y="42">C</text><rect class="fm s-acc sw2" x="273" y="24" width="44" height="26"/><text class="tl tc" x="295" y="42">D</text><text class="tl" x="4" y="112">terminator</text><text class="tl tc" x="175" y="112">shared cable</text><text class="tl te" x="336" y="112">terminator</text></svg><figcaption>A bus network: four hosts share one backbone cable, with a terminator at each end.</figcaption></figure>
:::

**How a frame travels.** When A sends a frame to D, A puts the signal on the shared cable. The signal travels both ways along the cable, so it passes every host. Each host's network card reads the destination address, and the hosts B and C ignore a frame that is not addressed to them; only D accepts it. The terminators absorb the signal when it reaches the ends. Only one host can send at a time: if two send together, their signals overlap and are corrupted, which is a **collision** (see CSMA/CD later in this chapter).

| Benefits | Drawbacks |
|---|---|
| Needs little cable, so it is cheap | Every host sees every frame, so a host can read data meant for others |
| Simple to set up for a few hosts | Collisions rise as hosts are added, so performance falls quickly |
| Easy to add a host along the cable | A break in the backbone splits the network, and a fault is hard to locate |

### Star topology

In a **star** network every host has its own cable to a central device, usually a **switch**.

:::html
<figure class="fig small"><svg viewBox="0 0 340 150" role="img" aria-label="A star network. A central switch is connected by its own cable to each of four hosts: A at top left, B at top right, C at bottom left and D at bottom right."><line class="c1 sw2" x1="42" y1="27" x2="170" y2="75"/><line class="c1 sw2" x1="298" y1="27" x2="170" y2="75"/><line class="c1 sw2" x1="42" y1="123" x2="170" y2="75"/><line class="c1 sw2" x1="298" y1="123" x2="170" y2="75"/><rect class="fm s-acc sw2" x="20" y="14" width="44" height="26"/><text class="tl tc" x="42" y="32">A</text><rect class="fm s-acc sw2" x="276" y="14" width="44" height="26"/><text class="tl tc" x="298" y="32">B</text><rect class="fm s-acc sw2" x="20" y="110" width="44" height="26"/><text class="tl tc" x="42" y="128">C</text><rect class="fm s-acc sw2" x="276" y="110" width="44" height="26"/><text class="tl tc" x="298" y="128">D</text><rect class="f1 s-acc sw2" x="140" y="57" width="60" height="36"/><text class="tl tc" x="170" y="80">switch</text></svg><figcaption>A star network: each host has its own cable to the central switch.</figcaption></figure>
:::

**How a frame travels.** When A sends a frame to D, it goes along A's own cable to the switch. The switch reads the destination MAC address in the frame, finds which port D is connected to, and sends the frame out of that port only. B and C never receive it. Because each cable carries traffic for one host only, there are no collisions on the host cables, and the hosts cannot read each other's frames.

| Benefits | Drawbacks |
|---|---|
| A fault in one cable affects only one host | If the switch fails, the whole network stops |
| No collisions between hosts, so it keeps its speed as hosts are added | More cable is needed than for a bus, and a switch costs money |
| Easy to add or remove a host and to find a fault | The switch must have enough ports for every host |

### Mesh topology

In a **mesh** network there are several connections between hosts, so there is more than one route between two hosts. In a **full mesh**, every host has a direct link to every other host; in a **partial mesh**, only some hosts are linked directly.

:::html
<figure class="fig small"><svg viewBox="0 0 340 150" role="img" aria-label="A full mesh of four hosts, A, B, C and D. Every host is joined by a direct link to each of the other three hosts, giving six links, including two diagonals that cross in the middle."><line class="c1 sw2" x1="60" y1="27" x2="280" y2="27"/><line class="c1 sw2" x1="60" y1="123" x2="280" y2="123"/><line class="c1 sw2" x1="60" y1="27" x2="60" y2="123"/><line class="c1 sw2" x1="280" y1="27" x2="280" y2="123"/><line class="c1 sw2" x1="60" y1="27" x2="280" y2="123"/><line class="c1 sw2" x1="280" y1="27" x2="60" y2="123"/><rect class="fm s-acc sw2" x="38" y="14" width="44" height="26"/><text class="tl tc" x="60" y="32">A</text><rect class="fm s-acc sw2" x="258" y="14" width="44" height="26"/><text class="tl tc" x="280" y="32">B</text><rect class="fm s-acc sw2" x="38" y="110" width="44" height="26"/><text class="tl tc" x="60" y="128">C</text><rect class="fm s-acc sw2" x="258" y="110" width="44" height="26"/><text class="tl tc" x="280" y="128">D</text></svg><figcaption>A full mesh of four hosts needs six links, so every host can reach every other directly.</figcaption></figure>
:::

**How a frame travels.** In a full mesh, A sends a frame to D straight down the A–D link. In a partial mesh, the frame may have to pass through other hosts, and a device with a **routing table** chooses the next link towards the destination. If a link fails, a frame is sent by another route, for example from A to B to D, so the network keeps working.

The number of links in a full mesh grows quickly. With \(n\) hosts, every host links to the other \(n - 1\), but each link is shared by two hosts, so the number of links is \(\dfrac{n(n-1)}{2}\). This program prints it for four sizes of network:

```python
for hosts in [4, 5, 6, 10]:
    links = hosts * (hosts - 1) // 2
    print(hosts, "hosts need", links, "links")
```

Output:

```output
4 hosts need 6 links
5 hosts need 10 links
6 hosts need 15 links
10 hosts need 45 links
```

That growth is why a full mesh is used only where reliability matters more than cost, such as the core of a WAN, and why most LANs use a star.

| Benefits | Drawbacks |
|---|---|
| Very reliable: if a link or host fails, another route exists | Very expensive: many cables and many network cards |
| Traffic can be shared between routes, so it is fast | Complicated to install and manage |
| Hard for one fault to stop the network | A full mesh does not scale: 10 hosts need 45 links |

### Hybrid topology

A **hybrid** network combines two or more topologies. The common example is several star networks (one per floor or department) joined by a bus or by links between their switches.

:::html
<figure class="fig small"><svg viewBox="0 0 340 150" role="img" aria-label="A hybrid network of two stars. Hosts A and B are connected to the left switch, hosts C and D to the right switch, and the two switches are joined by a link."><line class="c1 sw2" x1="30" y1="25" x2="95" y2="75"/><line class="c1 sw2" x1="30" y1="125" x2="95" y2="75"/><line class="c1 sw2" x1="310" y1="25" x2="245" y2="75"/><line class="c1 sw2" x1="310" y1="125" x2="245" y2="75"/><line class="c1 sw3" x1="95" y1="75" x2="245" y2="75"/><rect class="fm s-acc sw2" x="8" y="12" width="44" height="26"/><text class="tl tc" x="30" y="30">A</text><rect class="fm s-acc sw2" x="8" y="112" width="44" height="26"/><text class="tl tc" x="30" y="130">B</text><rect class="fm s-acc sw2" x="288" y="12" width="44" height="26"/><text class="tl tc" x="310" y="30">C</text><rect class="fm s-acc sw2" x="288" y="112" width="44" height="26"/><text class="tl tc" x="310" y="130">D</text><rect class="f1 s-acc sw2" x="60" y="59" width="70" height="32"/><text class="tl tc" x="95" y="80">switch 1</text><rect class="f1 s-acc sw2" x="210" y="59" width="70" height="32"/><text class="tl tc" x="245" y="80">switch 2</text><text class="tl tc" x="170" y="65">link</text></svg><figcaption>A hybrid network: two star networks joined by a link between their switches.</figcaption></figure>
:::

**How a frame travels.** A frame from A to B stays inside the left star: it goes to switch 1, which sends it out of B's port only. A frame from A to D goes to switch 1, which forwards it over the link to switch 2 (the only way to reach D), and switch 2 delivers it to D. Local traffic stays local.

A hybrid network can grow in sections, a fault in one section leaves the others working, and each section can use the topology that suits it. It is more complex and costs more than a single star.

:::key Topologies at a glance
- **Bus:** one shared cable; every host sees every frame; collisions; the backbone is a single point of failure.
- **Star:** a cable from each host to a central switch; the switch sends each frame only to its destination; the switch is a single point of failure.
- **Mesh:** many links; frames can take other routes; very reliable and very costly; a full mesh of \(n\) hosts needs \(\tfrac{n(n-1)}{2}\) links.
- **Hybrid:** two or more topologies combined, for example stars joined by a backbone.
:::

:::warn A star still depends on one device
It is true that if one cable in a star breaks, only that host loses its connection. It is also true that if the **switch** fails, every host loses its connection. An answer that says "a star never fails" loses the mark. Give both sides when you compare topologies.
:::

:::eg How a frame travels in a star network
In the star network in the figure, host A sends a file to host D. Describe how the data travels from A to D. [4 marks]

Follow the frame along its path and say what each device does.

- The file is split into frames, each with the destination MAC address (D's) and the source MAC address (A's) in the header. [B1]
- A's network card sends each frame along A's own cable to the switch. [B1]
- The switch reads the destination MAC address and looks it up in its table to find the port that D is connected to. [B1]
- The switch forwards the frame out of that port only, so B and C do not receive it, and D's network card accepts it. [B1]
:::

:::eg Choosing a topology for a school
A school in Nairobi is setting up a new computer room with 30 computers and 1 server. The computers will be used all day by students, and the school wants the room to keep working if one computer's cable is damaged. Justify the use of a star topology. [3 marks]

- Each computer has its own cable to the switch, so if one cable is damaged only that computer loses its connection and the other 29 keep working. [B1]
- Frames are sent only to the destination port, so 30 computers in use all day do not cause collisions, and the network stays fast. [B1]
- A computer can be added or removed by connecting or disconnecting one cable, which suits a room where machines are replaced, and a fault is found by checking one cable. [B1]

A bus would fail this scenario: one break in the backbone could stop the whole room. A full mesh would need \(\tfrac{31 \times 30}{2} = 465\) links, which is far too many.
:::

## Wired and wireless transmission

Data travels between devices in a **transmission medium**, either a cable (wired) or the air (wireless). The medium decides the speed, the range, the cost and how secure and reliable the link is.

### Wired or wireless?

| | Wired | Wireless |
|---|---|---|
| Speed | usually higher and steady | usually lower, and varies with distance and walls |
| Reliability | little interference | affected by walls, distance and other devices |
| Security | harder to intercept: an attacker needs to reach the cable | signals can be picked up by anyone in range, so the data must be encrypted |
| Mobility | devices stay near a socket | devices can move around |
| Installation | cables to lay, which is slow and costly in old buildings | no cable, easy to add a device |
| Cost | cheap for short links in a new building | cheap for a few devices, but needs access points |

Neither is better in every case. A hospital might use wired links for fixed equipment, which needs speed and reliability, and wireless for staff who carry tablets from ward to ward.

### The five media you must know

| Medium | What carries the data | Characteristics |
|---|---|---|
| Copper cable | electrical signals along copper wires (twisted pair, coaxial) | cheap and easy to install; used for most LAN cabling; Ethernet cable runs up to about 100 m; the signal weakens over distance; affected by electrical interference from motors and other cables |
| Fibre-optic cable | pulses of light along glass or plastic strands | very high bandwidth; carries data over long distances with little loss; not affected by electrical interference; hard to tap, so secure; more costly and harder to install and repair |
| Radio waves (including WiFi) | radio signals through the air | no cables, so devices can move; range of tens of metres indoors for WiFi; walls, distance and other devices reduce the signal; can be intercepted, so needs encryption |
| Microwaves | a narrow beam between two dishes on towers | high bandwidth; needs a clear line of sight; links tens of kilometres; useful where laying cable is costly; weather and obstacles can affect it |
| Satellites | signals beamed up to a satellite and down to a receiver | covers huge areas and remote places; high cost; weather can affect it; long delay (latency) because the signal travels thousands of kilometres |

:::def Bandwidth
The amount of data that a transmission medium can carry in a given time, measured in bits per second. A medium with a higher bandwidth can carry more data per second.
:::

The delay with a satellite is worth a calculation, because it explains why satellite links are poor for fast, interactive use. A satellite in a geostationary orbit stays above one point on the Earth at a height of about 35 786 km. A signal from the ground goes up to the satellite and down again, and the reply goes up and down again, so it travels at least four times the height. Radio waves travel at about 299 792 km per second.

```python
height_km = 35786
speed_km_per_s = 299792
delay = 4 * height_km / speed_km_per_s
print(f"{delay:.3f} seconds")
```

Output:

```output
0.477 seconds
```

Nearly half a second of delay before any reply even starts is noticeable in a phone call or an online game. A fibre link between two continents has a much smaller delay, because the cable runs along the Earth's surface rather than out to space.

:::eg Choosing a medium
For each situation, name a suitable medium and give one reason. [3 marks]

(a) The cable run in a workshop full of large electric motors.
(b) A village in the mountains that has no cable or mobile signal.
(c) Staff who carry tablets around a large hotel.

- (a) Fibre-optic cable, because it is not affected by the electrical interference from the motors. [B1]
- (b) Satellite, because it can reach a remote place without laying any cable. [B1]
- (c) Radio waves (WiFi), because the staff can move around and stay connected without a cable. [B1]
:::

## Hardware that supports a LAN

A LAN is built from a small set of devices. You must describe the role of each.

:::def Network interface card (NIC)
The hardware inside a device, usually a circuit board or chip, that connects the device to a wired network. It has a unique MAC address.
:::

:::def Wireless network interface card (WNIC)
A network interface card that uses radio waves instead of a cable, so the device can connect to a wireless network. Phones and laptops have one built in.
:::

:::def MAC address
A unique address given to a network interface card by its manufacturer, written as six pairs of hexadecimal digits (for example `3C-5A-B4-1F-0E-27`). A switch uses it to deliver a frame to the right device in a LAN.
:::

:::def Switch
A device that connects the devices in a LAN and sends each frame only out of the port to which the destination device is connected, using the MAC address in the frame.
:::

:::def Wireless access point (WAP)
A device that lets wireless devices join a wired network by radio. It connects to a switch with a cable.
:::

:::def Bridge
A device that connects two LANs, or two parts of one LAN, so that they work as one network. It forwards only the frames that need to cross from one side to the other.
:::

:::def Repeater
A device that receives a signal, restores it to its original strength and shape, and sends it on, so that the signal can travel further than the cable would normally allow.
:::

:::def Router
A device that connects two or more different networks, such as a LAN and the internet, and forwards packets between them using their IP addresses.
:::

| Device | Role in a LAN |
|---|---|
| Server | provides a service: files, printing, email, web pages |
| NIC | connects a computer to the wired network; holds its MAC address |
| WNIC | connects a device to the network by radio |
| Switch | connects the hosts of a LAN; forwards each frame to the destination port only |
| WAP | gives wireless devices access to the wired LAN |
| Cables | carry the signals: copper (twisted pair) or fibre |
| Bridge | joins two LANs or LAN segments, passing across only the frames meant for the other side |
| Repeater | boosts a signal to extend the distance it can travel |
| Router | connects the LAN to other networks (such as the internet) |

### How a switch works

A switch keeps a table that links each **MAC address** to the port the device is connected to. It builds the table by **learning**: each time a frame arrives, the switch notes its source address and the port it arrived on. To forward a frame, it looks up the destination address. If the destination is in the table, the frame goes out of that port only. If it is not yet in the table, the switch sends the frame out of every port except the one it arrived on, and the reply will teach the switch where the device is.

:::html
<figure class="fig small"><svg viewBox="0 0 340 120" role="img" aria-label="A simplified Ethernet frame drawn as four boxes in a row, left to right: destination address, source address, data, and error check."><text class="tl ti" x="15" y="18">Ethernet frame (simplified)</text><rect class="fm s-acc sw2" x="15" y="30" width="85" height="46"/><text class="tl tc" x="57" y="50">Destination</text><text class="tl tc" x="57" y="68">address</text><rect class="fm s-acc sw2" x="100" y="30" width="85" height="46"/><text class="tl tc" x="142" y="50">Source</text><text class="tl tc" x="142" y="68">address</text><rect class="f1 s-acc sw2" x="185" y="30" width="85" height="46"/><text class="tl tc" x="227" y="58">Data</text><rect class="fm s-acc sw2" x="270" y="30" width="55" height="46"/><text class="tl tc" x="297" y="50">Error</text><text class="tl tc" x="297" y="68">check</text><text class="tl tc" x="170" y="104">sent from left to right as one unit</text></svg><figcaption>An Ethernet frame carries the destination and source MAC addresses, the data and an error check. Real frames have a few more fields.</figcaption></figure>
:::

The Python program below follows a switch with four hosts, A to D, on ports 1 to 4. A **dictionary** stores pairs of a key and a value: here the key is the host's name and the value is its port number. The program learns each source, then forwards or floods each frame.

```python
ports = {"A": 1, "B": 2, "C": 3, "D": 4}
frames = [("A", "D"), ("D", "A"), ("A", "B"), ("B", "A"), ("C", "A")]
table = {}
for source, destination in frames:
    table[source] = ports[source]
    line = "Frame " + source + " to " + destination + ": "
    if destination in table:
        line = line + "forward to port " + str(table[destination])
    else:
        others = [str(p) for p in ports.values() if p != ports[source]]
        line = line + "destination unknown, send out of ports " + ", ".join(others)
    print(line)
print("Table:", table)
```

Output:

```output
Frame A to D: destination unknown, send out of ports 2, 3, 4
Frame D to A: forward to port 1
Frame A to B: destination unknown, send out of ports 2, 3, 4
Frame B to A: forward to port 1
Frame C to A: forward to port 1
Table: {'A': 1, 'D': 4, 'B': 2, 'C': 3}
```

The first frame, from A to D, reaches every other port because the switch has not yet seen D. D's reply teaches the switch that D is on port 4. After that, frames for A go only to port 1, and the table fills in as hosts speak.

### Switch or router?

These two devices cause more lost marks than any others, because both "forward things".

:::analogy
A switch is the mail room inside one office building. It delivers each envelope to the right desk by the name on it. A router is the sorting office between towns. It reads the town and street address and sends the parcel on towards the right place, handing it from one office's mail room to another.
:::

:::key Switch and router
- **Switch:** connects hosts **within one network**, using **MAC addresses**.
- **Router:** connects **different networks**, using **IP addresses**, and has a **routing table** to choose the next step towards the destination.
:::

A router has a connection (an interface) into each network it joins. When a packet arrives, the router reads the destination IP address, looks in its **routing table** for the best next link, and forwards the packet. A router in a home or office also usually provides the connection to the internet and passes a packet whose destination is outside the LAN to the internet service provider. That role is called the **default gateway**. Home routers also commonly include a switch, a WAP and a firewall in one box; the exam asks about the router's own function, joining networks and forwarding by IP address. The router's use of private and public IP addresses is covered in [The internet: IP addresses, DNS and streaming](#cs.internet).

An older device called a hub copies every frame to every port. It is not in the syllabus list, and a switch replaces it because a switch does not copy frames to hosts that do not need them.

:::eg Spot the error: switch and router
Question: Explain the difference between a switch and a router. [4 marks]

A student wrote:

```text
01  A switch connects the devices in one LAN.
02  It reads the MAC address in each frame and sends it only to the port of the destination device.
03  A router connects a LAN to other networks, such as the internet.
04  It reads the MAC address in each packet and forwards it.
```

Line 01 says what the switch connects [B1]. Line 02 says how it decides, with the MAC address and the single destination port [B1]. Line 03 says what the router connects [B1]. **Line 04 is wrong: a router uses the destination IP address, not the MAC address, to choose where to send a packet** [B0]. The answer scores 3 out of 4.

The corrected line 04 is: "It reads the destination IP address in each packet, looks it up in its routing table and forwards the packet towards the destination network."
:::

## Ethernet and CSMA/CD

**Ethernet** is the standard that most wired LANs use. It defines the cables, how devices connect and the format of the frame, and it was designed for a network where many hosts share one medium, such as a bus. When many hosts share a medium, there must be a rule for who may send.

:::def Ethernet
A set of standards for wired local area networks. It defines the cabling, the format of a frame (with the MAC addresses of the destination and the source) and the method by which devices share the medium.
:::

:::def Collision
What happens when two devices send at the same time on a shared medium, so that their signals overlap and the data in both is corrupted.
:::

:::def CSMA/CD
Carrier Sense Multiple Access with Collision Detection. A method used by Ethernet on a shared medium. A device listens to check that the medium is idle before it sends (carrier sense), any device may send when it is idle (multiple access), and if a collision happens the devices detect it and resend after a random wait.
:::

:::steps
1. **Listen.** The device checks whether another device is transmitting on the cable.
2. **Transmit if idle.** If the cable is idle, the device starts to send its frame. If it is busy, the device waits until it becomes idle.
3. **Detect a collision.** While sending, the device checks the signal on the cable. If it finds its signal has been corrupted by another, a collision has happened.
4. **Jam signal.** The device stops sending its data and sends a short jam signal so that every device knows that a collision happened.
5. **Random back-off.** Each device waits for a random time before it tries again. The time is random so that the two devices are unlikely to choose the same wait.
6. **Retry.** The device listens again and resends the frame. After a set number of failed attempts (16 in Ethernet) it gives up and reports an error.
:::

The same procedure in pseudocode, with the actions written as procedures:

```pseudocode
Attempts ← 0
Sent ← FALSE
REPEAT
   CALL WaitUntilCableIdle
   CALL StartSending
   IF Collision = TRUE THEN
      CALL SendJamSignal
      Attempts ← Attempts + 1
      CALL WaitRandomTime
   ELSE
      Sent ← TRUE
   ENDIF
UNTIL Sent = TRUE OR Attempts = 16
```

Suppose hosts A and B start sending at the same moment and each picks a random wait, A picking 2 time slots and B picking 1. B has the shorter wait, so it listens first, finds the cable idle and sends. A's wait ends later; by then B is sending, so A listens, finds the cable busy and waits. The program below shows that order.

```python
waits = {"A": 2, "B": 1}
print("Collision detected: A and B stop and send a jam signal")
print("Random waits in slots: A =", waits["A"], ", B =", waits["B"])
order = sorted(waits, key=waits.get)
print(order[0], "listens: cable idle, so it transmits")
print(order[1], "listens: cable busy, so it waits")
```

Output:

```output
Collision detected: A and B stop and send a jam signal
Random waits in slots: A = 2 , B = 1
B listens: cable idle, so it transmits
A listens: cable busy, so it waits
```

**Avoiding collisions.** Carrier sense is itself a way of avoiding collisions: a device that listens before it sends does not start while another is sending, so collisions only happen when two start at nearly the same moment. A switch avoids them more completely, because each host has its own cable to the switch. A modern wired LAN built with switches has few or no collisions, but CSMA/CD is still the method the syllabus asks for.

**Wireless networks.** A wireless device cannot easily listen while it is sending, so it cannot detect a collision. WiFi therefore uses a method that *avoids* collisions called **CSMA/CA** (collision avoidance). The device listens; if the channel is idle it waits a short random time, then sends. The receiver sends an acknowledgement. If no acknowledgement arrives, the sender assumes a collision and tries again after another random wait.

:::eg Describing CSMA/CD
Describe how CSMA/CD is used on an Ethernet network to deal with collisions. [5 marks]

Give the steps in the order they happen, with the technical word for each.

- A device listens to the cable (carrier sense) to check whether it is idle before it transmits. [B1]
- If the cable is idle, it transmits its frame, and if it is busy it waits. [B1]
- While transmitting, it monitors the cable, and a corrupted signal shows that a collision has been detected. [B1]
- The devices that collided stop and send a jam signal to tell every device. [B1]
- Each device waits a random time before it tries to resend, so they are unlikely to collide again. [B1]
:::

## Cloud computing

Instead of owning servers, an organisation can use someone else's. **Cloud computing** provides storage, software and processing power over the internet from a provider's data centres.

:::def Cloud computing
The delivery of computing services, such as data storage, software and processing, over the internet from servers owned by a provider, so that users do not own or manage those servers themselves.
:::

:::def Public cloud
Cloud services that a provider offers over the internet to many customers, who share the same underlying infrastructure and pay for what they use.
:::

:::def Private cloud
Cloud infrastructure that is used by one organisation only. It can be on the organisation's own site or run for it by a provider, but it is not shared with other customers.
:::

:::cols
:::col Benefits
- No large purchase of servers: costs are a regular fee, often based on use.
- Capacity can be increased or reduced quickly as needs change (scalability).
- Staff can reach their data from any device with an internet connection.
- The provider looks after hardware maintenance, updates and backups.
:::
:::col Drawbacks
- The service needs a working internet connection.
- The data is held by another company, which raises privacy and legal concerns.
- The organisation has less control, and an outage at the provider affects all its customers.
- Fees continue for as long as the service is used and can grow with use.
:::
:::

A **private** cloud gives the organisation more control and more privacy, because no other customer shares the infrastructure, but it must pay for and manage the equipment. It is chosen when data is sensitive, as in a hospital or a bank. A **public** cloud is cheaper and more flexible, so it suits a business that needs to scale quickly. A common mistake is to say that a private cloud is "encrypted" or "secure" and a public cloud is not. The difference is who uses the infrastructure.

:::eg Cloud computing for a school
A school in Colombo stores all its student files on a server in the school office. It is considering moving them to a public cloud service. Describe two benefits and two drawbacks of the move. [4 marks]

- Benefit: the school does not need to buy or replace its own server, so it saves the capital cost. [B1]
- Benefit: teachers and students can open files from home, because the files are reached over the internet. [B1]
- Drawback: the files cannot be opened if the school's internet connection fails. [B1]
- Drawback: the student data is stored by another company, so the school has less control over who can access it, and the fee is paid for as long as the service is used. [B1]
:::

:::eg Spot the error: choosing a topology
Question: A small office has 6 computers. The manager says: "If a cable breaks, only one computer must lose its connection." State the most suitable topology and justify it. [3 marks]

A student wrote:

```text
01  A star topology.
02  Each computer has its own cable to the switch, so a broken cable affects only that computer.
03  This is better than a bus because if the switch breaks, only one computer is affected.
```

Line 01 names the topology that meets the manager's requirement [B1]. Line 02 gives the reason that answers the manager's point [B1]. **Line 03 is wrong: if the switch breaks, every computer loses its connection, because every cable goes to the switch. The switch is the single point of failure of a star** [B0]. The answer scores 2 out of 3. Line 03 also adds nothing that a mark could be given for, so the student should have stopped after line 02.

The corrected line 03 is: "It is better than a bus, where a break in the shared cable can stop all the computers."
:::

:::try Start easy, finish at exam standard
Q: State two benefits of connecting computers in a network.
A: Any two of: users can share files; users can share hardware such as printers; one internet connection can be shared; users can communicate; backups and security can be managed centrally.
Q: State one feature that makes a network a LAN rather than a WAN.
A: It covers a small area such as one building or site, and the organisation owns the cabling.
Q: In a peer-to-peer network, what is the role of each computer?
A: Each computer can act as both a client and a server, sharing its own resources and using the resources of the others.
Q: A library has 40 identical computers that all load their programs from one central server. Is each computer a thin client or a thick client? Give a reason.
A: A thin client, because it depends on the server for its processing and programs rather than doing them locally.
Q: How many links does a full mesh of 7 hosts need?
A: \(\dfrac{7 \times 6}{2} = 21\) links.
Q: State what the terminator at each end of a bus network does.
A: It absorbs the signal when it reaches the end of the cable so that the signal does not bounce back along the cable.
Q: Name the device that connects a LAN to the internet and state the type of address it uses to forward packets.
A: A router, which uses the destination IP address.
Q: A wired LAN is replaced by a wireless one. State one benefit and one drawback.
A: Benefit: devices can move around and no cables are needed. Drawback: the signals can be intercepted by anyone in range, so the data must be encrypted (or: speed is lower or the signal is affected by walls).
Q: Describe the purpose of a repeater.
A: It receives a weakened signal, restores it and sends it on, so that the signal can travel further than the cable would normally allow.
Q: In a switch's table, host P is on port 3 and host Q is on port 5. A frame from P to Q arrives. On which port does it leave?
A: Port 5 only, because the switch forwards the frame to the port of the destination host.
Q: Put these CSMA/CD steps in order: jam signal; transmit; random wait; listen; collision detected.
A: Listen, transmit, collision detected, jam signal, random wait.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ A school connects the computers in its science department in a LAN. Describe three benefits to the school of connecting the computers in a network.
A: One mark for each benefit that is described, not just named.

- Teachers and students can share files, so everyone works from the same up-to-date copy [B1]
- Computers can share one printer, so the school buys fewer printers [B1]
- Files can be backed up from one place, and the network manager can control who can open what [B1]

(Accept: a shared internet connection; communication between users.)

Q: [4 marks] ★ A small network has a bus topology with four hosts, P, Q, R and S. Describe how a frame is sent from P to S.
H: Think about which hosts receive the signal on a bus.
H: Mention the destination address and what the other hosts do.
A: One mark for each point.

- P puts the frame, with S's address in its header, on to the shared cable (the backbone) [B1]
- The signal travels along the cable in both directions, so it reaches every host [B1]
- Each host's network card checks the destination address, and Q and R ignore a frame that is not addressed to them [B1]
- S accepts the frame, and the terminators at the ends absorb the signal [B1]

Q: [4 marks] ★★ A college in Accra has 300 students and 25 staff, spread over three buildings. Justify the use of a client-server network, rather than a peer-to-peer network.
H: Use facts from the scenario: the number of users and the three buildings.
A: One mark for each justified point.

- With 325 users, a central server can manage user accounts and permissions in one place, which would be impractical with each computer setting its own [B1]
- Files can be stored and backed up centrally, so students' and staff work is safe [B1]
- A powerful server can serve many clients at the same time, which a peer-to-peer computer could not do for 300 students [B1]
- A network manager can control access to the buildings' shared resources, for example restricting students from staff records [B1]

(A drawback of client-server, such as cost, earns no mark in a "justify" question.)

Q: [5 marks] ★★ Describe how CSMA/CD is used when two devices on a shared Ethernet cable try to send at the same time.
H: Five points, in order: listen, send, detect, jam, wait.
A: One mark for each point.

- Each device listens to the cable to check it is idle before sending [B1]
- Both find it idle and start to send, so their signals collide [B1]
- The devices detect the collision, because the signal on the cable is corrupted [B1]
- They stop sending and send a jam signal to tell every device [B1]
- Each waits a random time before listening and resending, so they are unlikely to collide again [B1]

Q: [6 marks] ★★ A chain of bakeries in Lima wants to move its customer orders and stock database from servers in its head office to a public cloud. Describe three benefits and three drawbacks of this move.
H: Think about cost, access, control and the internet connection.
A: Up to three benefits and up to three drawbacks, one mark for each.

- Benefit: no need to buy or replace servers, so the capital cost is saved [B1]
- Benefit: capacity can be increased quickly when orders rise, for example in a festival week [B1]
- Benefit: the provider does the maintenance and backups, so the chain needs fewer IT staff [B1]
- Drawback: the bakeries cannot reach the orders database without a working internet connection [B1]
- Drawback: the customer data is held by another company, which raises privacy and legal concerns [B1]
- Drawback: the monthly fee continues for as long as the service is used, and can grow with use [B1]

Q: [6 marks] ★★ Name a suitable transmission medium for each situation and give a reason for each choice.

(a) Connecting two buildings 30 km apart across hilly farmland, where it is too costly to lay cable. [2]

(b) Joining two data centres in the same city that need to transfer very large amounts of data. [2]

(c) A school hall where students bring their own devices and move around. [2]
A: (a) Microwaves [B1], because a narrow beam between two dishes can link places in line of sight without laying cable [B1].

(b) Fibre-optic cable [B1], because it has a very high bandwidth and carries data over long distances with little loss [B1].

(c) Radio waves (WiFi) [B1], because devices can move around and connect without cables [B1].

Q: [5 marks] ★★ Complete the table by naming the device that matches each description.

| Description | Device |
|---|---|
| Joins two LANs and passes across only the frames meant for the other side | |
| Restores a weak signal so it can travel further | |
| Lets wireless devices join a wired LAN | |
| Sends each frame out of the port of its destination MAC address | |
| Connects a LAN to the internet using IP addresses | |
A: Bridge [B1]; repeater [B1]; wireless access point [B1]; switch [B1]; router [B1].

Q: [8 marks] ★★★ A hospital in Accra is installing a network in a new building with 4 wards, with 60 fixed computers and 80 tablets that nurses carry between beds.

(a) Explain the difference between a LAN and a WAN. [2]

(b) The hospital wants the network in each ward to keep working if one computer's cable fails. Justify a star topology. [3]

(c) Describe one benefit and two drawbacks of connecting the nurses' tablets by radio waves rather than by cable. [3]
H: For (c), think about what the nurses do and about who can receive a radio signal.
A: (a) A LAN covers a small area, such as one building or site, and the organisation owns the cabling [B1]; a WAN covers a large area, such as between cities or countries, and uses telecommunications links leased from or belonging to others [B1].

(b) Each computer has its own cable to the switch, so a failed cable affects only that computer [B1]; the other computers on the ward keep working [B1]; and no collisions occur between hosts, so the network remains fast with 60 computers [B1].

(c) Benefit: the nurses can move between beds and stay connected, without being limited by a cable [B1]. Drawback: radio signals can be intercepted by anyone in range, so the patient data must be encrypted [B1]. Drawback: the signal can be weakened by walls and by other devices, so the connection may be slower or less reliable [B1].
:::

:::try Stretch for A*
Q: A switch with four ports has an empty table. Hosts W, X, Y and Z are on ports 1, 2, 3 and 4. These frames arrive in order: (W to X), (X to W), (Z to X), (Y to Z), (W to Y). For each frame, state whether the switch forwards it to one port or sends it out of several, and give the table after the last frame.
H: Add the source of each frame to the table before you look up the destination.
H: A destination that is not yet in the table makes the switch send the frame out of every port except the arrival port.
A: Frame 1 (W to X): learn W on port 1. X is not in the table, so it is sent out of ports 2, 3 and 4. Frame 2 (X to W): learn X on port 2. W is in the table, so it is forwarded to port 1 only. Frame 3 (Z to X): learn Z on port 4. X is on port 2, so it is forwarded to port 2 only. Frame 4 (Y to Z): learn Y on port 3. Z is on port 4, so it is forwarded to port 4 only. Frame 5 (W to Y): W is already known. Y is on port 3, so it is forwarded to port 3 only. The final table is W: port 1, X: port 2, Z: port 4, Y: port 3.

Q: A company sends data from London to Sydney over a link of 16 000 km. Compare the time taken by the signal on (a) a fibre-optic link and (b) a geostationary satellite link, in one direction only. Take the signal speed in fibre as \(2 \times 10^5\) km per second, and for the satellite link take the signal speed as \(3 \times 10^5\) km per second, the satellite height as 36 000 km, and assume the signal goes up to the satellite and down again (a path of twice the height). Which has the shorter delay, and by how much?
H: Time = distance ÷ speed.
H: The satellite path is \(2 \times 36\,000\) km. The ground distance is not added.
A: (a) Fibre: \(16\,000 \div 200\,000 = 0.08\) s, which is 80 ms. (b) Satellite: the path is \(2 \times 36\,000 = 72\,000\) km, and \(72\,000 \div 300\,000 = 0.24\) s, which is 240 ms. The fibre link has the shorter delay, by \(240 - 80 = 160\) ms. The satellite path is three times as long in time, because the signal travels up and down 36 000 km, and radio waves in air are faster than light in glass.
:::

:::quiz
? Which statement describes a peer-to-peer network?
- A server stores all the files and controls the users' accounts.
+ Every computer can share its own files and also use the files of the others.
- Every computer is a thin client that depends on one central computer.
- Computers are connected only through a router to the internet.
> In a peer-to-peer network every computer can act as both client and server, and no central server controls the network.
? A star network has 8 hosts connected to one switch. The cable to host 5 is cut. What happens?
- The whole network stops working.
- Host 5 and the host next to it stop working.
+ Only host 5 loses its connection.
- Every host has to be rebooted to reconnect.
> Each host has its own cable to the switch, so a break affects only that host. The switch itself is the single point of failure.
? Why can two hosts on a bus network cause a collision?
- Their MAC addresses are the same.
- The terminators do not absorb the signal.
+ They both send at the same time on the shared cable, so the signals overlap.
- The backbone cable is too long.
> Only one signal can be on the shared cable at a time. If two hosts send at once, the signals overlap and the data is corrupted.
? How many links does a full mesh of 9 hosts need?
- 9
- 18
- 72
+ 36
> The number of links is \(\tfrac{n(n-1)}{2}\), which is \(\tfrac{9 \times 8}{2} = 36\). The answer 72 forgets that each link is shared by two hosts.
? What is the main difference between a switch and a router?
- A switch is wireless and a router uses cables.
+ A switch connects devices within a network using MAC addresses; a router connects different networks using IP addresses.
- A switch uses IP addresses and a router uses MAC addresses.
- A switch is for the internet and a router is for a LAN.
> A switch forwards frames by MAC address inside one LAN. A router forwards packets by IP address between networks.
? Which transmission medium is not affected by electrical interference?
- copper cable
+ fibre-optic cable
- twisted pair
- coaxial cable
> Fibre-optic cable carries pulses of light, so electrical interference has no effect. Twisted pair and coaxial cable are both copper cables.
? What is the purpose of a jam signal in CSMA/CD?
- It tells a device that the cable is idle.
- It sends a copy of the frame to every host.
+ It tells every device that a collision has happened, so they stop sending.
- It chooses the random time that each device waits.
> After detecting a collision, the device sends a short jam signal so that all devices know the data has been corrupted. The random wait comes after it.
? A company uses a private cloud. What is true?
- Its data is encrypted automatically.
+ The infrastructure is used by one organisation only.
- It is run on servers shared with other customers.
- It does not need staff to manage it.
> "Private" means that one organisation uses the infrastructure. It does not mean encrypted, and the organisation (or its provider) must still manage it.
? In a thin-client network, where is most of the processing done?
- On the client computer.
- On the router.
+ On the server.
- On the switch.
> A thin client depends on the server for processing and for storage, which is why it needs the network.
:::

:::checklist What you can now do
- [ ] I can state the purpose and benefits of networking.
- [ ] I can describe the characteristics of a LAN and a WAN.
- [ ] I can explain the client-server and peer-to-peer models, the roles of the computers in each, and justify a choice for a scenario.
- [ ] I can explain the difference between a thin client and a thick client.
- [ ] I can describe the bus, star, mesh and hybrid topologies, how a frame travels in each, and justify a topology for a scenario.
- [ ] I can describe cloud computing, public and private clouds, and their benefits and drawbacks.
- [ ] I can compare wired and wireless networks.
- [ ] I can describe the characteristics of copper cable, fibre-optic cable, radio waves (including WiFi), microwaves and satellites.
- [ ] I can describe the role of a switch, server, NIC, WNIC, WAP, cables, bridge, repeater and router.
- [ ] I can explain how Ethernet uses CSMA/CD to detect and avoid collisions.
:::

:::recap
- A network lets computers share files, hardware, an internet connection and communication, and be managed centrally. A LAN covers one site and is owned by the organisation; a WAN covers a wide area and uses leased or public links.
- Client-server: servers provide services to clients, with central security and backup but a high cost and a single point of failure. Peer-to-peer: every computer is both client and server, cheap but hard to manage and secure. A thin client depends on the server; a thick client processes locally.
- Bus: one shared cable, every host sees every frame, collisions. Star: each host has its own cable to a switch, which forwards to the destination port only. Mesh: many links, very reliable and costly, with \(\tfrac{n(n-1)}{2}\) links in a full mesh. Hybrid: topologies combined.
- Cloud computing: services over the internet from a provider's servers. Public: shared by many customers. Private: one organisation only.
- Wired media: copper (cheap, interference, about 100 m for Ethernet) and fibre (high bandwidth, long distance, immune to electrical interference, costly). Wireless: radio waves and WiFi, microwaves (line of sight) and satellites (wide area, long delay).
- NIC and WNIC connect a device and hold its MAC address. A switch forwards by MAC address within a network. A router connects different networks and forwards by IP address. A WAP gives wireless access. A bridge joins LANs. A repeater restores a signal.
- CSMA/CD: listen, transmit if idle, detect a collision, send a jam signal, wait a random time, retry. WiFi uses CSMA/CA to avoid collisions.
:::

:::links
- practise: [Networks and the internet: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/2-communication-/networks-and-the-internet/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- read: [Computers and the internet](https://www.khanacademy.org/computing/computers-and-internet) · Khan Academy · free lessons on how networks and the internet work
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos on networking by university computer scientists
- read: [9618 revision notes](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/) · Save My Exams · notes on each syllabus topic [paid]

Links checked 13 November 2026.
:::

Next: [The internet: IP addresses, DNS and streaming](#cs.internet)
