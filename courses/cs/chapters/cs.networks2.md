@chapter cs.networks2
@title Protocols, TCP/IP and packet switching
@level a2
@paper CAIE 9618 Paper 3
@time 4–6 hours
@summary Why computers need protocols, how a protocol stack divides the work into layers, the four layers of the TCP/IP suite and what each does when a message crosses the internet, the purpose of HTTP, FTP, SMTP, POP3, IMAP and BitTorrent, and how circuit switching and packet switching send messages, including the work of a router.

:::why
When you open a web page, send an email or download a game, thousands of devices made by different companies, running different software, cooperate without ever having met. They can only do this because every one of them follows the same published rules, called protocols. Paper 3 asks you to explain why protocols matter, to say what each layer of the TCP/IP suite does as a message travels from one host to another, to give the purpose of the common protocols, and to compare circuit switching with packet switching. Each of these is a "describe" or "explain" question that is won one precise point at a time, and this chapter gives you the points in the right order.
:::

**Before you start**, you should know what a router does and what a MAC address is, from [Networks: models, topologies and hardware](#cs.networks), and what an IP address, a URL and the Domain Name Service are, from [The internet: IP addresses, DNS and streaming](#cs.internet).

:::try Warm-up
Q: A switch delivers a frame using one kind of address, and a router forwards a packet using another. Name each. (from [Networks: models, topologies and hardware](#cs.networks))
A: A switch uses the destination MAC address in the frame. A router uses the destination IP address in the packet.
Q: What does the Domain Name Service do when you type a web address into a browser? (from [The internet: IP addresses, DNS and streaming](#cs.internet))
A: It looks up the domain name and returns the IP address of the web server, so that the browser knows where to send its request.
Q: A message is 12 000 bits long. How many bytes is that? (from [Number systems and binary arithmetic](#cs.data))
A: \(12\,000 \div 8 = 1500\) bytes.
:::

## Why protocols are essential

Two people can only talk if they share a language, take turns, and agree what to do when they do not hear each other ("Sorry, could you repeat that?"). Computers are no different, except that they cannot guess. A computer that receives a stream of 1s and 0s has no idea whether it is a web page, a picture or the first half of an email, where one message ends and the next begins, or whether a part of it was damaged on the way. Everything must be agreed in advance.

:::def Protocol
A set of rules that two or more devices follow so that they can communicate. A protocol states the format of the data, the order and timing in which messages are sent, how devices address each other, and what to do when something goes wrong.
:::

A protocol answers questions of five kinds.

| Question | What the protocol fixes | Example |
|---|---|---|
| What does the data look like? | The format: which bits are the address, which are the data, how long each part is | A packet has a header, then the data |
| Who is it for? | Addressing: how the sender and the receiver are named | An IP address or a MAC address in the header |
| In what order and when? | Order and timing: who speaks first, how long to wait | A browser sends a request, then the server sends a reply |
| What if it goes wrong? | Error handling: how damage or loss is detected and repaired | The receiver asks for a missing piece to be sent again |
| How fast? | Flow control: how much the sender may send before the receiver is ready | A slow phone tells a fast server to wait |

:::key Why protocols are essential
- Devices from different makers, with different hardware and operating systems, can only understand each other if they follow the **same agreed rules**.
- The rules say what each part of a message **means** (format and addressing), the **order and timing** of messages, and how **errors** and **speed differences** are dealt with.
- Because the rules are published as standards, anyone can build a device or a program that works with all the others.
:::

:::eg Why protocols are essential (exam style)
Explain why protocols are essential for communication between computers. [3 marks]

- Computers made by different manufacturers, and running different software, need agreed rules so that each one can understand the data it receives [B1]
- The protocol defines the format of the data and the addresses, so that the receiver knows which bits are the destination, the source and the data [B1]
- The protocol defines the order and timing of messages and how errors are detected and repaired, so that damaged or lost data can be sent again [B1]
:::

The examiner wants the idea of **agreement between different devices**, then at least one thing that is agreed. "So that computers can communicate" alone repeats the question and scores nothing.

## The protocol stack

Sending a web page across the world involves many separate jobs: deciding what the request says, cutting a large reply into pieces, finding a route, and turning bits into electrical, light or radio signals. One protocol that did all of this would be huge and hard to change. Instead, the work is divided into **layers**, and each layer has its own protocols.

:::def Protocol stack
A set of protocols arranged in layers, in which each layer has its own function. A layer uses the services of the layer below it and provides services to the layer above it.
:::

:::analogy Posting a parcel
You write a letter (the top layer), put it in an envelope with an address (the next layer), and hand it to the post office, which puts it in a sack with others, which a lorry takes to a sorting office. You do not need to know how the lorry is driven, and the lorry driver does not read your letter. Each stage does one job and relies on the stage below it. If the post office swaps its lorries for trains, your letter is unchanged.
:::

The stack has three benefits that appear again and again in mark schemes.

- **Each layer has one job**, so each protocol is simpler to design, test and fix.
- **A layer can be changed without changing the others.** A laptop that moves from a cable to Wi-Fi changes only its lowest layer. Your browser and the rest of the stack carry on as before.
- **Standard interfaces let different makers' products work together**: a network card from one company, an operating system from another and a browser from a third.

When a message is sent, it goes **down** the layers on the sending host. Each layer adds its own control information, called a **header**, in front of the data it was given. At the receiving host it goes **up**, and each layer removes the header that its partner layer added and uses it. Adding a header on the way down is called **encapsulation**. The layers never talk to the layer above or below except through the agreed interface, but each layer behaves as though it were talking directly to the same layer on the other host.

## The TCP/IP suite

The protocols that run the internet are known as the **TCP/IP suite**, after its two best-known members.

:::def TCP/IP protocol suite
The set of protocols used on the internet, arranged as a four-layer stack: the Application layer, the Transport layer, the Internet layer and the Link layer. It is named after the Transmission Control Protocol (TCP) and the Internet Protocol (IP).
:::

:::html
<figure class="fig"><svg viewBox="0 0 600 250" role="img" aria-label="The four TCP/IP layers on two hosts and a router. Host A and host B each have four boxes from top to bottom: Application, Transport, Internet, Link. The router between them has only Internet and Link. Dashed lines join the Application layers (HTTP request and reply) and the Transport layers (TCP segments) of the two hosts, passing the router. Dashed lines labelled IP join the Internet layers of host A and the router and of the router and host B. Solid lines labelled frames join the Link layers. A downward arrow beside host A shows data going down the stack and an upward arrow beside host B shows data going up."><text class="tl tc" x="95" y="32">Host A</text><rect class="fm s-acc sw2" x="20" y="45" width="150" height="40"/><text class="tl tc" x="95" y="70">Application</text><rect class="fm s-acc sw2" x="20" y="95" width="150" height="40"/><text class="tl tc" x="95" y="120">Transport</text><rect class="fm s-acc sw2" x="20" y="145" width="150" height="40"/><text class="tl tc" x="95" y="170">Internet</text><rect class="fm s-acc sw2" x="20" y="195" width="150" height="40"/><text class="tl tc" x="95" y="220">Link</text><text class="tl tc" x="505" y="32">Host B</text><rect class="fm s-acc sw2" x="430" y="45" width="150" height="40"/><text class="tl tc" x="505" y="70">Application</text><rect class="fm s-acc sw2" x="430" y="95" width="150" height="40"/><text class="tl tc" x="505" y="120">Transport</text><rect class="fm s-acc sw2" x="430" y="145" width="150" height="40"/><text class="tl tc" x="505" y="170">Internet</text><rect class="fm s-acc sw2" x="430" y="195" width="150" height="40"/><text class="tl tc" x="505" y="220">Link</text><text class="tl tc" x="300" y="137">Router</text><rect class="fm2 s-acc sw2" x="225" y="145" width="150" height="40"/><text class="tl tc" x="300" y="170">Internet</text><rect class="fm2 s-acc sw2" x="225" y="195" width="150" height="40"/><text class="tl tc" x="300" y="220">Link</text><path class="ln-m thin dash" d="M170 65 L430 65"/><text class="tl tc" x="300" y="57">HTTP request and reply</text><path class="ln-m thin dash" d="M170 115 L430 115"/><text class="tl tc" x="300" y="107">TCP segments</text><path class="ln-m thin dash" d="M170 165 L225 165"/><path class="ln-m thin dash" d="M375 165 L430 165"/><text class="tl tc" x="197" y="157">IP</text><text class="tl tc" x="403" y="157">IP</text><path class="c1 sw2" d="M170 215 L225 215"/><path class="c1 sw2" d="M375 215 L430 215"/><text class="tl tc" x="197" y="207">frames</text><text class="tl tc" x="403" y="207">frames</text><path class="ln" d="M8 48 L8 232" marker-end="url(#ah)"/><path class="ln" d="M592 232 L592 48" marker-end="url(#ah)"/></svg><figcaption>A message goes down the four layers of host A, crosses the network as frames, and goes up the layers of host B. The router reads only as far as the Internet layer. The dashed lines are the conversation each layer believes it is having.</figcaption></figure>
:::

Read the figure from the top left. The Application layer of host A believes it is talking to the Application layer of host B (the top dashed line), and so does every other layer. In reality the data goes down host A's four boxes, crosses a solid link as a frame to the router, and climbs only as far as the router's Internet layer, where the router decides where to send it next. It then goes down again, across the next link, and up through all four layers of host B. **A router has no Transport or Application layer**: it never opens the data it forwards.

| Layer | Its job | Example protocols | Address it uses | Unit of data |
|---|---|---|---|---|
| Application | Provides the network services that programs use, and defines the messages of each service | HTTP, FTP, SMTP, POP3, IMAP, BitTorrent, DNS | A name such as a domain name | Message |
| Transport | Splits the data into pieces, numbers them, delivers them to the right program, and makes the delivery reliable | TCP, UDP | A port number | Segment |
| Internet | Adds the source and destination IP addresses and chooses the route across networks | IP | IP address | Packet |
| Link | Sends the data across one physical link to the next device | Ethernet, Wi-Fi | MAC address | Frame |

In an answer, use the specific names in the table (segment, packet, frame) when you are sure of the layer, and the general word "packet" for a piece of data when the question does not say which layer it means.

:::def Application layer
The top layer of the TCP/IP suite. It contains the protocols that programs use to provide network services to users, such as HTTP for web pages and SMTP for sending email. It prepares the data to be sent and interprets the data received.
:::

:::def Transport layer
The layer that breaks the data from the Application layer into segments, adds a port number and a sequence number to each, and manages delivery between the two hosts: reassembly in the right order, acknowledgements, resending of lost segments and flow control.
:::

:::def Internet layer
The layer that adds the source and destination IP addresses to each segment to make a packet, and that routes the packets across the networks, from router to router, towards the destination host.
:::

:::def Link layer
The lowest layer. It puts each packet into a frame with the MAC addresses of the next device on the same link, and sends the frame as signals over the physical medium (cable, radio or light), one hop at a time.
:::

### The Application layer

The Application layer is the only layer that the user's programs deal with directly. A web browser does not know how to cut data into pieces or find a route. It builds an HTTP request and hands it to the layer below. When the reply comes back, the Application layer turns the received data into something the program can use, such as a web page to draw. The next section gives the purpose of each Application layer protocol in the syllabus.

### The Transport layer

The Transport layer is the one that makes the internet dependable, even though the layers below do not guarantee anything. Its main protocol is the **Transmission Control Protocol (TCP)**. For one message, TCP does these jobs.

:::key What TCP does
1. **Connection set-up.** Before data flows, the two hosts exchange three short messages (SYN, SYN-ACK and ACK, "the three-way handshake") to agree to talk.
2. **Segmenting.** It breaks a large message into **segments** small enough to travel across the network.
3. **Port numbers.** Each segment carries the **port number** of the sending program and of the receiving program, so that the data goes to the right application on the host.
4. **Sequence numbers.** Each segment is numbered, so that the receiver can put the segments back in order even if they arrive out of order.
5. **Acknowledgements.** The receiver sends back an acknowledgement for the data it has received. If the sender does not get one in time, it assumes the segment was lost and **sends it again** (retransmission).
6. **Flow control.** The receiver tells the sender how much data it can accept at once, so that a fast sender does not swamp a slow receiver.
7. **Error checking.** A check value in each segment lets the receiver detect damage; a damaged segment is not acknowledged and is sent again.
:::

:::def Port number
A number in the header of a segment that says which program or service on the host the data is for. A web server listens on port 80 for HTTP (443 for HTTPS), an email server on port 25 for SMTP, and an FTP server on port 21.
:::

An IP address chooses the **host**, and the port number chooses the **program on that host**, in the way that a street address chooses a building and a flat number chooses a household inside it.

TCP is called **connection-oriented** and **reliable**. The Transport layer has a second protocol, the **User Datagram Protocol (UDP)**, which does none of the reliability work: no handshake, no acknowledgements, no resending. UDP is faster and has less overhead, so it suits live voice, live video and online games, where a late packet is worthless and resending it would only make things worse, and also short queries such as a DNS lookup. UDP is not named in the syllabus, but a good answer on why a live video call does not use TCP's resending relies on it.

:::eg A lost segment
A sender uses TCP to send five segments, numbered 1 to 5. In this example the receiver acknowledges by saying which segment it expects next. Segment 3 is lost on the way. Describe what happens.

| Event | What the receiver holds | Acknowledgement sent |
|---|---|---|
| Segment 1 arrives | 1 | expecting 2 |
| Segment 2 arrives | 1, 2 | expecting 3 |
| Segment 3 is lost | | |
| Segment 4 arrives | 1, 2, 4 | expecting 3 |
| Segment 5 arrives | 1, 2, 4, 5 | expecting 3 |
| The sender's timer for segment 3 runs out, so it sends segment 3 again | | |
| Segment 3 arrives | 1, 2, 3, 4, 5 | expecting 6 |

The receiver keeps asking for segment 3. When it finally arrives, the receiver has all five segments and can pass the complete message, in order, to the Application layer. Real TCP numbers every byte rather than every segment, and has more refinements, but the idea is the same: **numbers, acknowledgements, a timer and resending.**
:::

### The Internet layer

The Internet layer provides **addressing and routing**. It takes each segment and adds a header with the **source IP address** and the **destination IP address**, making a **packet**. Its protocol is the **Internet Protocol (IP)**. The routers that carry the packet across the internet look only at this header. Each packet also carries a **time to live** (TTL) or hop count, a number that each router reduces by 1. If it reaches 0, the router discards the packet. This stops a packet that is lost in a loop of routers from circulating for ever.

IP is **best-effort**: it does its best to deliver each packet, but it does not promise delivery, order or freedom from errors. A packet may be lost, delayed, copied or delivered after a later one. That is exactly why TCP, in the layer above, adds numbering and acknowledgements.

### The Link layer

The Link layer deals with one hop at a time: from a host to the router, from router to router, or from the last router to the destination host. It puts the packet inside a **frame**, whose header holds the **MAC address** of the next device on the same link, and it turns the bits into signals for the cable or the radio waves.

A point that causes lost marks: **the IP addresses in a packet stay the same all the way from the source to the destination, but the MAC addresses in the frame change at every hop**, because a MAC address only has meaning on one local link. The table below follows one packet from host A, across one router, to host B.

| Hop | Source IP | Destination IP | Source MAC | Destination MAC |
|---|---|---|---|---|
| Host A to the router | Host A | Host B | Host A | the router (its interface facing A) |
| Router to host B | Host A | Host B | the router (its interface facing B) | Host B |

### A message's journey, layer by layer

Here is the whole path for one request, in the order the examiners want it. A student in a school in Accra opens a page on a server in another country. The browser, host A, sends an HTTP request. Follow it through the stack, and then through the reply.

:::steps
1. **Application layer (host A).** The browser builds an HTTP request for the page and passes it down. The Domain Name Service has already turned the server's name into an IP address.
2. **Transport layer (host A).** TCP sets up the connection, breaks the data into segments, and adds a port number (for example 80 for the web server) and a sequence number to each.
3. **Internet layer (host A).** IP adds the source IP address and the destination IP address to each segment, making packets.
4. **Link layer (host A).** Each packet goes into a frame with the MAC address of the school's router, and the frame is sent over the cable or the radio link.
5. **Router.** The Link layer receives the frame and takes the packet out. The Internet layer reads the destination IP address, looks in the routing table, reduces the TTL by 1 and chooses the next router. The Link layer puts the packet into a new frame addressed to that next device. This repeats at every router on the way.
6. **Link and Internet layers (host B).** The server's Link layer receives the frame and removes it. The Internet layer checks that the destination IP address is its own and passes the segment up.
7. **Transport layer (host B).** TCP uses the sequence numbers to put the segments in order, sends acknowledgements, asks for any missing segment to be sent again, and uses the port number to choose the web server program.
8. **Application layer (host B).** The web server reads the HTTP request and builds the reply, which makes the same trip in the opposite direction.
:::

:::eg Layer by layer (exam style)
A student in a school in Accra opens a web page held on a server in another country. Describe what happens to the request at each layer of the TCP/IP suite in the student's computer, and what the router does with it on the way. [6 marks]

- Application layer: the browser creates the HTTP request for the page [B1]
- Transport layer: TCP breaks the data into segments and adds a port number and a sequence number to each [B1]
- Internet layer: IP adds the source and destination IP addresses, making packets [B1]
- Link layer: each packet is put in a frame with the MAC address of the next device (the router) and sent as signals [B1]
- Router: reads the destination IP address in the packet, looks it up in its routing table and forwards the packet to the next router [B1]
- The router removes the old frame and builds a new one for the next link, and it does not open the segment, because it has only the Internet and Link layers [B1]
:::

#### Splitting a message into segments

How many segments does the Transport layer make? Suppose the reply from the server is 5200 bytes and each segment may carry at most 1000 bytes of data. Each segment also has a TCP header of at least 20 bytes, and each packet an IP header of at least 20 bytes. This program works out the segments and the size of each packet. In Python:

```python
message_size = 5200
max_data = 1000
segments = []
number = 1
remaining = message_size
while remaining > 0:
    size = min(max_data, remaining)
    segments.append((number, size))
    remaining = remaining - size
    number = number + 1
for number, size in segments:
    print("Segment", number, "carries", size, "bytes; packet size", size + 40, "bytes")
print("Segments:", len(segments))
print("Total bytes sent:", sum(size + 40 for number, size in segments))
```

Output:

```output
Segment 1 carries 1000 bytes; packet size 1040 bytes
Segment 2 carries 1000 bytes; packet size 1040 bytes
Segment 3 carries 1000 bytes; packet size 1040 bytes
Segment 4 carries 1000 bytes; packet size 1040 bytes
Segment 5 carries 1000 bytes; packet size 1040 bytes
Segment 6 carries 200 bytes; packet size 240 bytes
Segments: 6
Total bytes sent: 5440
```

Five segments are full and the sixth holds the remaining 200 bytes. The 40 bytes of headers on each of the six packets add 240 bytes, so 5440 bytes cross the network to deliver 5200 bytes of data. This is the **overhead** of layering: control information costs capacity, and it buys reliability and addressing.

:::warn Mixing up the Transport and Internet layers
TCP is the Transport layer and IP is the Internet layer. Port numbers, sequence numbers and acknowledgements belong to the Transport layer. IP addresses and routing belong to the Internet layer. MAC addresses belong to the Link layer. A very common slip is to say "the Transport layer adds the IP address".
:::

:::eg Spot the error: the Transport layer
Question: Describe the purpose of the Transport layer of the TCP/IP suite. [4 marks]

A student wrote:

```text
01  It breaks the data into segments.
02  It adds a sequence number to each segment so that they can be put back in order.
03  It adds the source and destination IP addresses so that the segments can be routed.
04  It sends an acknowledgement and asks for a segment to be sent again if one is missing.
```

Line 01 gives the splitting [B1]. Line 02 gives the numbering [B1]. **Line 03 is wrong: IP addresses are added by the Internet layer, not the Transport layer. The Transport layer adds port numbers** [B0]. Line 04 gives acknowledgements and retransmission [B1]. The answer scores 3 out of 4.

The corrected line 03 is: "It adds the port numbers of the sending and receiving programs so that the data reaches the right application."
:::

## Application layer protocols

Every Application layer protocol is a set of rules for one kind of service. The syllabus names six. For each, learn the purpose in one sentence, and learn whether it **sends** or **retrieves**.

:::def HTTP
Hypertext Transfer Protocol: the protocol that a web browser uses to request web pages and other resources from a web server, and that the server uses to send them back. HTTPS is HTTP carried inside an encrypted connection.
:::

:::def FTP
File Transfer Protocol: a protocol for transferring files between a client and a server over a network, in either direction. The user normally has to log in with a user name and a password.
:::

:::def SMTP
Simple Mail Transfer Protocol: the protocol used to **send** email from a mail client to a mail server, and from one mail server to another.
:::

:::def POP3
Post Office Protocol version 3: a protocol used by a mail client to **retrieve** email from a mail server. The messages are normally downloaded to the client's device and then deleted from the server.
:::

:::def IMAP
Internet Message Access Protocol: a protocol used by a mail client to **retrieve** email from a mail server while the messages stay on the server. The client shows the server's copy, so several devices always see the same mailbox.
:::

:::def BitTorrent
A protocol for **peer-to-peer file sharing**. A large file is shared in small pieces by many computers (peers), each of which downloads pieces from other peers and uploads pieces to them.
:::

| Protocol | Purpose | Direction | Standard port |
|---|---|---|---|
| HTTP | Request and send web pages and web resources | Browser asks, server replies | 80 |
| HTTPS | HTTP with encryption (see the security chapters) | Browser asks, server replies | 443 |
| FTP | Upload and download files | Both ways | 21 |
| SMTP | Send email | Client to server, server to server | 25 |
| POP3 | Retrieve email, downloading it | Server to client | not examined |
| IMAP | Retrieve email, leaving it on the server | Server to client | not examined |
| BitTorrent | Share large files between peers | Peer to peer | not examined |

The port numbers are given for HTTP, HTTPS, FTP and SMTP because they are the standard ones and appear in many textbooks. The syllabus does not ask you to learn them, so learn the purposes first.

### HTTP

HTTP works on a **request and reply** pattern. The client sends a request that names the resource. The two requests to know are **GET** (give me this page) and **POST** (here is some data, for example a form that the user filled in). The server answers with a **status code** and, if all is well, the resource. Code 200 means "OK" and 404 means that the resource was not found. HTTP is **stateless**: the server treats each request as new, which is why websites use cookies to remember who you are.

### FTP

FTP is used when the whole point is to move files: a web designer uploads the files of a site to the web server, or a company downloads a large data file from a supplier. An FTP client logs in to an FTP server, lists the files, and uploads or downloads them. Because a plain FTP session sends the password as ordinary text, a secure version is used for anything important.

### Email: SMTP, POP3 and IMAP

Email uses one protocol to send and a different one to retrieve, and that difference is a favourite exam question. Suppose Ama in Accra sends an email to Kofi in Kumasi.

:::steps
1. Ama writes the message in her mail client. The client uses **SMTP** to send it to her mail server.
2. Ama's mail server uses **SMTP** to send the message to Kofi's mail server, which stores it in Kofi's mailbox.
3. Later, Kofi's mail client uses **POP3** or **IMAP** to **retrieve** the message from the mail server.
:::

:::cols
:::col POP3
- Downloads the message to the device, then (normally) deletes it from the server
- The mail is on one device only
- Works offline once downloaded
- Suits one device and a small mailbox
:::
:::col IMAP
- Leaves the message on the server and shows the server's copy
- Every device sees the same mailbox and the same read or unread state
- Needs a connection to read mail that is not cached
- Suits a phone, a laptop and a tablet used together
:::
:::

:::eg Choosing POP3 or IMAP
Fatima, a nurse in Lahore, reads her work email on a phone, on a tablet and on the ward computer. She says that mail she has read on the phone still appears as unread on the tablet. State the protocol her mail clients should use to retrieve email, and explain why. [3 marks]

- IMAP [B1]
- IMAP leaves the messages on the server, so every device shows the same mailbox [B1]
- an email read or deleted on one device is then also marked as read or deleted on the others, whereas POP3 downloads the message to one device only [B1]
:::

:::warn SMTP sends, POP3 and IMAP retrieve
SMTP is for **sending** email. POP3 and IMAP are for **retrieving** it. No answer should say that SMTP "receives mail on a phone" or that POP3 "sends the email to the server". (A mail server does *receive* mail from other servers using SMTP, which is why the pair of servers use SMTP between them.)
:::

### BitTorrent and peer-to-peer file sharing

In the client-server model a single server sends the file to every client, so the server's connection is shared by all of them, and the more people who want the file, the slower each download becomes. BitTorrent turns this around: **the more people who want a file, the more people there are to supply it.** It is a **peer-to-peer** protocol, which means that every computer taking part is both a client and a server.

:::def Peer
A computer taking part in a BitTorrent file share. A peer downloads pieces of the file from other peers and uploads the pieces it already has to them.
:::

:::def Seed
A peer that has the complete file and uploads it to others without needing to download anything. A file needs at least one seed (or enough peers who between them hold every piece) to be completed.
:::

:::def Tracker
A server that keeps a list of the peers sharing a file and tells a new peer which peers to contact. (Some newer systems find peers without a tracker, by asking other peers.)
:::

:::def Swarm
The group of all the peers, seeds and the downloading peers, sharing one file at one time.
:::

How a download works:

:::steps
1. A small **torrent file** describes the shared file: its name, its size, the number of pieces, a **hash** (a short fingerprint) for each piece, and the address of the tracker.
2. The BitTorrent client reads the torrent file and asks the **tracker** for a list of peers in the **swarm**.
3. The shared file is divided into many equal **pieces**. The client connects to several peers at once and asks each for **different pieces**, so it downloads from many peers in parallel.
4. Each piece that arrives is checked against its **hash**. A piece that is damaged, or has been tampered with, does not match, is thrown away and is requested again.
5. As soon as the client has a piece, it **uploads** that piece to other peers who need it. It does not have to wait for the whole file.
6. When the client has every piece, it can put them together in the right order, and it becomes a **seed** for others.
:::

:::eg How many pieces?
A video file of 1 GiB is shared with pieces of 256 KiB. How many pieces are there? Peer P2 holds pieces 3 and 4 of a six-piece file, and needs the rest. The swarm is shown below. From where can P2 get each piece it needs?

| Participant | Pieces it holds |
|---|---|
| Seed S | 1, 2, 3, 4, 5, 6 |
| Peer P1 | 1, 2, 3 |
| Peer P2 | 3, 4 |
| Peer P3 | 2, 5 |

The number of pieces is \(1\ \text{GiB} \div 256\ \text{KiB} = 2^{30} \div 2^{18} = 2^{12} = 4096\) pieces.

P2 needs pieces 1, 2, 5 and 6.

- Piece 1: from S or P1.
- Piece 2: from S, P1 or P3.
- Piece 5: from S or P3.
- Piece 6: only from S, because no other peer has it yet.

P2 asks different peers for different pieces at the same time, and once it holds a piece, others may take it from P2 as well. Piece 6 will spread to the other peers once someone has downloaded it from the seed.
:::

Benefits of BitTorrent: the work of sending is **shared among the peers**, so no single server is overloaded and the publisher needs little bandwidth; downloads often get faster as more peers join; the system is **resilient**, since it does not depend on one machine; and the hash check protects the integrity of the file. Drawbacks: a file with no seed and missing pieces cannot be completed; a download may start slowly while the client finds peers; every peer's IP address is visible to the others; and the peers are strangers, so the hash is essential for safety. BitTorrent is a **protocol**, a perfectly legal technology that is widely used to share large open files such as free operating systems, game updates and scientific data. Whether a particular file may be shared depends on its copyright, not on the protocol.

:::exam Explaining BitTorrent
A question "explain how BitTorrent shares a large file" wants the process in order: the file is split into **pieces**; a **tracker** tells the client which **peers** to contact; pieces are downloaded **from many peers at the same time**; each piece is **checked with a hash**; and the client **uploads** the pieces it has to others. Use the terms peer, seed, tracker and swarm, and always say that it is **peer-to-peer**.
:::

## Circuit switching and packet switching

Whichever protocols are used, a message has to cross a network of many links and many devices. There are two basic ways to organise that crossing.

### Circuit switching

:::def Circuit switching
A method of sending data in which a dedicated communication path (a circuit) is set up between the sender and the receiver before any data is sent, and the whole path is reserved for that one communication until it ends.
:::

A circuit-switched communication has three phases: **set up** (the path is built through the exchanges, and the capacity along it is reserved), **transfer** (all the data follows the same path, in order, with a constant bandwidth), and **close down** (the path is released for others to use). The traditional landline telephone network works like this: when you dial, a line is connected from your phone to the other phone for the whole call.

:::cols
:::col Benefits
- The bandwidth is **guaranteed and constant**, so the quality does not change during the call
- The delay is small and constant (no jitter)
- All the data takes the **same path** and arrives **in order**, so nothing needs to be put back together
- There is no need for each piece of data to carry address information after the set-up
:::
:::col Drawbacks
- There is a **set-up time** before any data can be sent
- The **capacity is reserved** even when nobody is speaking or sending data, and nobody else can use it
- The number of circuits is limited, so a call may be **blocked** when all are in use
- If one link on the path fails, the connection is **lost** and must be set up again
:::
:::

**Where it is applicable:** a continuous, steady stream of data between two ends for a known time, where a guaranteed quality matters more than efficiency: a traditional telephone call, and a dedicated private line between two sites.

### Packet switching

:::def Packet switching
A method of sending data in which the message is broken into packets, each with a header containing the destination address and a sequence number. Each packet is sent separately, and the routers choose its route one hop at a time. The packets may take different routes and arrive out of order, and they are put back in order at the destination.
:::

:::def Packet
A small unit of data sent across a network. It has a header (which includes the source and destination addresses, the packet number and a time to live), the data, and often a check value for detecting errors.
:::

No connection is set up and no capacity is reserved. A router that receives a packet looks at its destination address and sends it towards the next router. The next packet of the same message may be sent by a different route, because a link may have become busy or failed in the meantime. At the destination, the packets are **reassembled** into the message, using their sequence numbers.

:::html
<figure class="fig"><svg viewBox="0 0 600 262" role="img" aria-label="A network with Host A on the left, then router R1, then two routes to router R4, then Host B on the right. The upper route goes R1, R2, R4 and is a solid line; its links take 12 ms and 10 ms, and packets 1, 3 and 4 use it. The lower route goes R1, R3, R4 and is dashed; its links take 20 ms and 25 ms, and packet 2 uses it. The link from Host A to R1 and the link from R4 to Host B each take 5 ms."><rect class="fm s-acc sw2" x="15" y="105" width="64" height="40"/><text class="tl tc" x="47.0" y="130.0">Host A</text><rect class="fm2 s-acc sw2" x="130" y="110" width="50" height="30"/><text class="tl tc" x="155.0" y="130.0">R1</text><rect class="fm2 s-acc sw2" x="270" y="35" width="50" height="30"/><text class="tl tc" x="295.0" y="55.0">R2</text><rect class="fm2 s-acc sw2" x="270" y="185" width="50" height="30"/><text class="tl tc" x="295.0" y="205.0">R3</text><rect class="fm2 s-acc sw2" x="410" y="110" width="50" height="30"/><text class="tl tc" x="435.0" y="130.0">R4</text><rect class="fm s-acc sw2" x="521" y="105" width="64" height="40"/><text class="tl tc" x="553.0" y="130.0">Host B</text><path class="c1 sw2" d="M79 125 L130 125"/><path class="c1 sw2" d="M180 118 L270 52"/><path class="c1 sw2" d="M320 52 L410 118"/><path class="c1 sw2 dash" d="M180 132 L270 198"/><path class="c1 sw2 dash" d="M320 198 L410 132"/><path class="c1 sw2" d="M460 125 L521 125"/><text class="tl tc" x="104" y="118">5 ms</text><text class="tl te" x="210" y="78">12 ms</text><text class="tl" x="372" y="78">10 ms</text><text class="tl te" x="210" y="172">20 ms</text><text class="tl" x="372" y="180">25 ms</text><text class="tl tc" x="490" y="118">5 ms</text><text class="tl tc" x="295" y="25">Packets 1, 3 and 4</text><text class="tl tc" x="295" y="236">Packet 2 (dashed route)</text></svg><figcaption>Packet switching: R1 sends packet 2 by the dashed lower route and the other three by the solid upper route. The upper route takes 5 + 12 + 10 + 5 = 32 ms and the lower route takes 5 + 20 + 25 + 5 = 55 ms.</figcaption></figure>
:::

:::eg Following four packets
Host A sends a message as four packets, one every 4 milliseconds (ms) from time 0: packet 1 at 0 ms, packet 2 at 4 ms, packet 3 at 8 ms and packet 4 at 12 ms. In the figure, R1 sends packets 1, 3 and 4 by the upper route and packet 2 by the lower route, because the upper route was busy when packet 2 arrived. When does each packet arrive, in what order, and when can host B pass the whole message on?

The upper route takes \(5 + 12 + 10 + 5 = 32\) ms and the lower route takes \(5 + 20 + 25 + 5 = 55\) ms.

| Packet | Sent at (ms) | Route | Route time (ms) | Arrives at (ms) |
|---|---|---|---|---|
| 1 | 0 | upper | 32 | 32 |
| 2 | 4 | lower | 55 | 59 |
| 3 | 8 | upper | 32 | 40 |
| 4 | 12 | upper | 32 | 44 |

The packets arrive in the order 1, 3, 4, 2. Packet 2 arrives last, because it took the longer route. Host B cannot pass the complete message up until 59 ms, when packet 2 has arrived and the sequence numbers show that nothing is missing. The program below does what the Transport layer at host B does: it records the packets as they arrive and reports how much is ready to pass on.
:::

In Python:

```python
arrivals = [(32, 1), (40, 3), (44, 4), (59, 2)]
received = []
next_needed = 1
for time, number in arrivals:
    received.append(number)
    while next_needed in received:
        next_needed = next_needed + 1
    print("At", time, "ms packet", number, "arrives. Ready to pass up:", list(range(1, next_needed)))
```

Output:

```output
At 32 ms packet 1 arrives. Ready to pass up: [1]
At 40 ms packet 3 arrives. Ready to pass up: [1]
At 44 ms packet 4 arrives. Ready to pass up: [1]
At 59 ms packet 2 arrives. Ready to pass up: [1, 2, 3, 4]
```

Packets 3 and 4 have to wait until packet 2 arrives. This waiting, and the variation in how long packets take, is why a video call over a packet-switched network can stutter unless the receiver keeps a small **buffer** of data before it starts playing.

:::cols
:::col Benefits of packet switching
- The links are **shared**, so the capacity is used efficiently: a link is idle only when no packet is using it
- No set-up time, and no capacity reserved for silent periods
- **Resilient**: if a link or router fails, later packets are sent by another route
- Many users can share the network, so it is cheap to run
- Damaged or lost packets can be sent again without repeating the whole message
:::
:::col Drawbacks of packet switching
- **Variable delay** (jitter), because packets take routes of different lengths and queue at routers
- Packets can arrive **out of order, late or not at all**, so they must be reassembled and may need resending
- Every packet carries a header, so there is **overhead**
- No guaranteed quality: a busy network is slow for everybody
:::
:::

**Where it is applicable:** data that comes in bursts and does not need a guaranteed rate: web pages, email, file transfers, and the internet in general. The internet is packet switched, and so are voice and video calls made over it.

:::key Circuit switching or packet switching?
| | Circuit switching | Packet switching |
|---|---|---|
| Path | One dedicated path for the whole communication | Each packet is routed separately; routes may differ |
| Set-up | Needed before any data is sent | None |
| Capacity | Reserved, even when idle | Shared, used only when packets are sent |
| Order of data | Always in order | May arrive out of order and be reassembled |
| Delay | Constant | Variable |
| If a link fails | The connection is lost | Packets are sent another way |
| Used for | Traditional telephone calls, private lines | The internet: web, email, files, voice and video over IP |
:::

:::eg Video call (exam style)
A company uses video calls for meetings between its offices. Compare the use of circuit switching and packet switching for the calls. [4 marks]

- Circuit switching gives a dedicated path for the whole call, so the bandwidth and delay are constant and the picture and sound arrive in order [B1]
- However, the capacity stays reserved when nobody is speaking, there is a set-up time, and the call is lost if a link on the path fails [B1]
- Packet switching shares the links, so the capacity is used efficiently, and the packets can be sent by different routes if there is a fault [B1]
- However, the packets take different times, so the delay varies and packets may arrive out of order or late, which can make the video stutter [B1]
:::

### The router in packet switching

:::def Router
A device that joins two or more networks and forwards packets between them. It reads the destination IP address of each packet, uses its routing table to choose the next hop, and sends the packet out of the matching interface.
:::

:::def Hop
One step of a packet's journey, from one router to the next (or from the last router to the destination). The number of routers crossed is the hop count.
:::

Every router performs the same loop for every packet.

:::key What a router does with each packet
1. Receive the frame on one interface and take the packet out of it.
2. Reduce the **time to live** (hop count) by 1. If it is now 0, **discard** the packet.
3. Read the **destination IP address** in the header.
4. Look up the address in the **routing table**, which lists networks and the next hop for each, and choose the best match.
5. Put the packet into a new frame for the next link and send it out of the right **interface**.
:::

A routing table is a list of networks and where to send packets for each. Routers swap information with their neighbours so that the tables are kept up to date: if a link fails, the tables change and packets use another route. The last entry is usually a **default route**, which is used when no other entry matches, for example "send everything else to the internet service provider". Here is a small table for router R1 in the figure (in this simplified example it also holds an entry for the network on the other side).

| Destination network | Next hop |
|---|---|
| 203.0.113.0/24 | R2 |
| 198.51.100.0/24 | R3 |
| 0.0.0.0/0 (everything else) | R4 |

If more than one entry matches, a real router uses the most specific one (the one with the longest network part). In Python:

```python
import ipaddress
table = [("203.0.113.0/24", "R2"), ("198.51.100.0/24", "R3"), ("0.0.0.0/0", "R4")]
def next_hop(destination):
    address = ipaddress.ip_address(destination)
    best = None
    for network, router in table:
        net = ipaddress.ip_network(network)
        if address in net and (best is None or net.prefixlen > best[0]):
            best = (net.prefixlen, router)
    return best[1]
for d in ["203.0.113.77", "198.51.100.9", "192.0.2.5"]:
    print(d, "-> next hop", next_hop(d))
```

Output:

```output
203.0.113.77 -> next hop R2
198.51.100.9 -> next hop R3
192.0.2.5 -> next hop R4
```

The first address is in the network 203.0.113.0/24, the second is in 198.51.100.0/24, and the third matches only the default route. (The notation /24 means that the first 24 bits are the network part, as in [The internet: IP addresses, DNS and streaming](#cs.internet).)

Now the time to live. A packet leaves a host with a time to live of 64 and crosses 5 routers. Each router reduces it by 1, so it arrives with \(64 - 5 = 59\). A packet that leaves with a time to live of 3 and has to cross 5 routers is reduced to 2 at the first router, 1 at the second and 0 at the third, which discards it. A router that is part of a loop therefore cannot keep a packet alive for ever.

:::warn "All the packets take the same route"
That is true of circuit switching, not of packet switching. In packet switching each packet is routed separately and may take a different route. A packet-switched message does **not** reach the destination in order, and it is the Transport layer at the destination, using the sequence numbers, that puts it right.
:::

## Practice

:::try Start easy, finish at exam standard
Q: List the four layers of the TCP/IP suite from the top to the bottom.
A: Application, Transport, Internet, Link.
Q: Which layer adds the IP addresses to a segment? Which layer puts the packet in a frame with a MAC address?
A: The Internet layer adds the IP addresses. The Link layer puts the packet in a frame with a MAC address.
Q: A reply of 3500 bytes is sent in segments that carry at most 1000 bytes of data each. How many segments are there, and how many data bytes are in the last one?
A: \(3500 \div 1000 = 3.5\), so 4 segments: three full ones (3000 bytes) and a last one of \(3500 - 3000 = 500\) bytes.
Q: State which protocol is used (a) to send an email to the server, (b) to retrieve email and leave it on the server, (c) to upload web site files to a web server.
A: (a) SMTP. (b) IMAP. (c) FTP.
Q: A packet leaves a host with a time to live of 5 and has to cross 6 routers. What happens to it?
A: Each router reduces the time to live by 1, so it reaches 0 at the fifth router, which discards the packet.
Q: A file of 2 MiB is shared with BitTorrent in pieces of 128 KiB. How many pieces are there?
A: \(2\ \text{MiB} = 2^{21}\) bytes and \(128\ \text{KiB} = 2^{17}\) bytes, so \(2^{21} \div 2^{17} = 2^4 = 16\) pieces.
Q: Say whether each uses circuit switching or packet switching: (a) a traditional landline telephone call, (b) loading a web page.
A: (a) Circuit switching, with a path reserved for the whole call. (b) Packet switching, since the page is sent as packets that share the links of the internet.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ State the purpose of each of these protocols: (a) HTTP (b) FTP (c) SMTP (d) POP3.
A: One mark each.

- (a) HTTP is used by a browser to request web pages from a web server, and by the server to send them back [B1]
- (b) FTP is used to transfer (upload and download) files between a client and a server [B1]
- (c) SMTP is used to send email from a client to a mail server and between mail servers [B1]
- (d) POP3 is used to retrieve email from a mail server, downloading it to the client device [B1]

Q: [4 marks] ★★ The Application layer and the Transport layer are two layers of the TCP/IP suite. Describe the purpose of each.
H: Think of what each layer hands to the layer below, and what each layer adds.
A: Two marks for each layer.

- Application layer: provides the protocols (such as HTTP or SMTP) that programs use to send and receive data over the network [B1]; it prepares the data from the program for sending, and interprets the data received for the program [B1]
- Transport layer: breaks the data into segments, adding a sequence number and a port number to each [B1]; it checks that the segments arrive (acknowledgement and resending of lost segments) and puts them back in order at the destination [B1]

Q: [3 marks] ★★ Pedro in Lima uses a phone and a laptop to read the same mailbox. Explain why IMAP is a better protocol than POP3 for him, and state which protocol he uses to send mail.
A: One mark per point.

- IMAP keeps the messages on the server, so both devices show the same mailbox [B1]
- POP3 downloads the messages to one device, so the other device would not show them (or the read and deleted state would differ) [B1]
- SMTP is used to send the mail [B1]

Q: [5 marks] ★★ Explain how BitTorrent is used to share a large file.
H: Use the words tracker, peers, pieces, hash and seed.
A: One mark per point, up to five.

- the file is divided into many small pieces [B1]
- a tracker (or similar) gives the new peer a list of other peers that are sharing the file (the swarm) [B1]
- the client downloads different pieces from several peers at the same time [B1]
- each piece is checked with its hash, and a damaged piece is requested again [B1]
- the client uploads the pieces it has already got to other peers, and a peer with the whole file (a seed) continues to upload it [B1]

Q: [4 marks] ★★ A telephone company sends each call over a dedicated circuit, but an internet voice service sends calls as packets. Compare the two methods for a voice call.
A: One mark per point, up to four.

- circuit switching reserves a path and a constant bandwidth for the whole call, so the quality is steady and the voice arrives in order [B1]
- the circuit is reserved even when nobody speaks, and it takes time to set up, so it uses capacity inefficiently [B1]
- packet switching shares the links among many users, so it uses capacity efficiently and can send packets round a fault [B1]
- the delay varies and packets can arrive late or out of order, so the voice may break up [B1]

Q: [6 marks] ★★★ A packet is sent from a laptop to a web server through a router. (a) State the layer at which each of these is added: a port number, an IP address, a MAC address. [3 marks] (b) The packet passes through the router. State two things that change or are done by the router, and one thing that stays the same. [3 marks]
H: The router reads the Internet layer only.
A: (a) One mark each.

- port number: the Transport layer [B1]
- IP address: the Internet layer [B1]
- MAC address: the Link layer [B1]

(b) One mark each.

- the router reduces the time to live by 1 (or builds a new frame with a new MAC address for the next link) [B1]
- the router uses the destination IP address and the routing table to choose the next hop [B1]
- the source and destination IP addresses stay the same all the way to the destination [B1]

Q: [6 marks] ★★★ Router R1 has this routing table.

| Destination network | Next hop |
|---|---|
| 203.0.113.0/24 | R2 |
| 198.51.100.0/24 | R3 |
| 0.0.0.0/0 | R4 |

(a) A packet for 198.51.100.9 reaches R1. State the next hop and the reason. [2 marks] (b) A packet for 192.0.2.5 reaches R1. State the next hop and the reason. [2 marks] (c) The packet in (b) left its source with a time to live of 3, and has already passed through two routers before R1. Explain what R1 does. [2 marks]
H: R1 is the third router on the path.
A: (a) The next hop is R3 [B1], because the address is in the network 198.51.100.0/24 [B1].

(b) The next hop is R4 [B1], because the address matches no other entry, so the default route is used [B1].

(c) R1 is the third router, so it reduces the time to live from 1 to 0 [B1] and discards the packet instead of forwarding it [B1].
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A sender sends segments 1 to 8 with TCP. The receiver acknowledges by naming the next segment it expects. Segments 4 and 6 are lost on the way, and all the others arrive. (a) Give the acknowledgement that the receiver sends after each of the six segments that do arrive, in the order they arrive. [2 marks] (b) The sender's timers expire and it sends segments 4 and 6 again. Both arrive, segment 4 first. State the acknowledgement for each. [2 marks] (c) Explain why TCP could not do this if it did not number the segments. [2 marks]
H: The next segment expected is the lowest number the receiver does not yet have.
A: (a) The segments that arrive are 1, 2, 3, 5, 7 and 8, in that order. The acknowledgements are: expecting 2, expecting 3 and expecting 4 for the first three [B1], then expecting 4 three times more, because segment 4 is still missing [B1].

(b) When segment 4 arrives, the receiver holds 1, 2, 3, 4, 5, 7, 8, so the next one it needs is 6: expecting 6 [B1]. When segment 6 arrives, it holds all eight: expecting 9 [B1].

(c) Without numbers, the receiver could not tell which segment was missing, so it could not ask for it [B1], nor put the segments back in the right order when 4 and 6 arrive after the later ones [B1].

Q: [6 marks] ★★★ A hospital uses a remote link so that a specialist can watch an operation live and speak to the surgeon, and it also uses the same link to send patient records to the specialist's centre. A network engineer proposes circuit switching for the live link and packet switching for the records. Justify the engineer's choice, using the features of each method.
H: Match each use to the property it needs: steady quality for the live link, and efficiency for bursts of data for the records.
A: One mark per point, up to six.

- the live video and voice need a steady bandwidth and a small, constant delay, which a dedicated circuit provides [B1]
- the data arrives in order and nothing has to be reassembled, so the picture and sound cannot stutter because of late packets [B1]
- the capacity being reserved is acceptable, because the link is in constant use for the whole operation [B1]
- the records are sent in bursts and do not need a constant rate, so reserving a circuit for them would waste capacity [B1]
- packet switching lets the records share the links with other users, and a lost or damaged packet is resent, so the records arrive correct [B1]
- a delay in the arrival of the records does not matter, unlike a delay in the live link, and packet switching can use another route if a link fails [B1]
:::

:::quiz
? Which layer of the TCP/IP suite adds the source and destination IP addresses?
- Application
- Transport
+ Internet
- Link
> The Internet layer adds the IP addresses and routes the packets. The Transport layer adds port numbers and sequence numbers, and the Link layer adds MAC addresses.
? What is the main reason for dividing a protocol into layers?
- It makes the data travel faster.
+ Each layer has its own job and can be changed without changing the others.
- It makes the messages shorter.
- It removes the need for addresses.
> Layering splits the work into separate jobs with agreed interfaces, which makes the protocols simpler and lets one layer be replaced (for example Wi-Fi in place of a cable) without changing the rest. It adds headers, so it does not make messages shorter.
? Which protocol is used to send an email from a client to a mail server?
- POP3
- IMAP
+ SMTP
- FTP
> SMTP sends mail. POP3 and IMAP retrieve it, and FTP transfers files.
? What is the difference between POP3 and IMAP?
- POP3 sends email and IMAP receives it.
- IMAP downloads the messages and deletes them from the server.
+ POP3 normally downloads messages and removes them from the server, and IMAP leaves them on the server.
- IMAP can only be used by one device.
> POP3 normally downloads the messages to one device, while IMAP leaves them on the server so that several devices share one mailbox. Both retrieve mail, and neither sends it.
? In BitTorrent, what is a seed?
- A server that keeps the list of peers.
- A peer that has no pieces of the file.
+ A peer that has the complete file and uploads it.
- The small file that describes the shared file.
> A seed holds every piece. The list of peers is kept by the tracker, and the small file that describes the shared file is the torrent file.
? What happens to the IP addresses and the MAC addresses as a packet crosses a router?
- Both stay the same.
- Both change.
+ The IP addresses stay the same and the MAC addresses change.
- The IP addresses change and the MAC addresses stay the same.
> The IP addresses name the source and the destination hosts for the whole journey. A MAC address is only meaningful on one link, so each hop has a new frame with new MAC addresses.
? Which statement describes packet switching?
- All the packets of a message follow one reserved path.
+ Each packet is routed separately, and the packets are put in order at the destination.
- No packet can be lost.
- The bandwidth is guaranteed for the whole message.
> In packet switching the packets may take different routes and arrive out of order, so they are numbered and reassembled. A reserved path and a guaranteed bandwidth belong to circuit switching.
? A packet reaches a router with a time to live of 1. What does the router do?
- It forwards the packet and does not change the time to live.
- It sets the time to live to 64.
+ It reduces the time to live to 0 and discards the packet.
- It sends the packet back to the source.
> Each router reduces the time to live by 1 and discards the packet when it reaches 0. This stops a packet from circulating in a loop of routers for ever.
:::

:::checklist What you can now do
- [ ] I can explain why protocols are essential for communication between computers.
- [ ] I can explain how a protocol stack divides the work into layers, and why that is useful.
- [ ] I can name the four layers of the TCP/IP suite and state the purpose and function of each.
- [ ] I can describe what happens at each layer when a message is sent from one host to another across the internet, including the router.
- [ ] I can state the purpose of HTTP, FTP, SMTP, POP3, IMAP and BitTorrent, and explain how BitTorrent shares a file.
- [ ] I can describe circuit switching and packet switching, with benefits, drawbacks and where each is used.
- [ ] I can describe the function of a router in packet switching and explain how packets cross a network, including the internet.
:::

:::recap
- A protocol is a set of agreed rules for format, addressing, order and timing, error handling and flow control. Without protocols, devices from different makers could not understand each other.
- A protocol stack divides the work into layers: each layer has its own job, uses the layer below and serves the layer above, and can be changed on its own. Headers are added on the way down (encapsulation) and removed on the way up.
- TCP/IP layers: **Application** (protocols for programs), **Transport** (segments, port numbers, sequence numbers, acknowledgements, resending, flow control; TCP or UDP), **Internet** (IP addresses and routing; time to live), **Link** (frames, MAC addresses, the physical link).
- IP addresses stay the same from source to destination; MAC addresses change at every hop. A router has only the Internet and Link layers.
- HTTP requests web pages. FTP transfers files. SMTP sends email. POP3 retrieves email by downloading it. IMAP retrieves email and leaves it on the server. BitTorrent shares large files peer to peer, in pieces, with a tracker, a swarm, seeds and hash checks.
- Circuit switching: a dedicated path set up first and held for the whole call; constant bandwidth and order, but wasteful and slow to set up (the traditional telephone network).
- Packet switching: packets routed separately, perhaps by different routes, and reassembled by sequence number; efficient and resilient, but variable delay and possible loss (the internet).
- A router reads the destination IP address, looks in its routing table, reduces the time to live, and forwards the packet to the next hop.
:::

:::links
- practise: [Protocols: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/14-communication-and-internet-technologies-/protocols/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- practise: [Circuit and packet switching: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/14-communication-and-internet-technologies-/circuit-switching-packet-switching/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- read: [An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) · MDN · how requests and replies work
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos on networks and the internet by university computer scientists
- read: [Computers and the internet](https://www.khanacademy.org/computing/computers-and-internet) · Khan Academy · how the internet moves packets (free)

Links checked 13 November 2026.
:::

Next: [Processors, parallel processing and virtual machines](#cs.hardware2)
