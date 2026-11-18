# READER: Computer Science

## cs.overview
Taught: the four 9618 papers (times, marks, how answered), AS vs A Level, the topic map by chapter, assessment objectives AO1-AO3, command words (State, Identify, Describe, Explain, Justify, Complete, Write, Draw), the study order.
Assumed: nothing (a few terms are only named: pseudocode, trace table, cache, MAR).

## cs.f.basics
Taught: program, algorithm, input-process-output, source code, interpreter, sequence/selection/iteration, pseudocode, OUTPUT/print, strings and quotes, comments (// and #), variable, assignment (← and =), DECLARE, constant, data types INTEGER/REAL/STRING/BOOLEAN, int()/float()/str(), + - * / DIV MOD (// %), operator order and brackets, INPUT/input(), comparisons (= <> and == !=), AND OR NOT, IF/ELSE/ENDIF and elif, FOR/WHILE/REPEAT-UNTIL and range, running total, infinite loop, LENGTH/MID/& and len/slice/upper, syntax/run-time/logic errors, reading a Python error, trace table, random numbers (RAND, randint).
Assumed: nothing.

## cs.data
Taught: bit, byte, nibble, 2^n patterns, MSB/LSB, place values, KiB/MiB/GiB/TiB and kB/MB/GB/TB, binary-denary and denary-binary (place values and repeated division), hexadecimal and its uses, BCD, one's and two's complement, range of n-bit two's complement, binary addition, subtraction by adding the two's complement, overflow (signed and unsigned), ASCII/extended ASCII/Unicode, character codes in order.
Assumed: functions (def/return), bitwise &, list comprehensions and .encode (Python blocks); register, MAC address, memory address, assembly language and ASC (named in passing).

## cs.media
Taught: bitmap, pixel, colour depth, image and screen resolution, file header, bitmap size = width x height x depth, effects of changing them, vector graphic (drawing object, property, drawing list) and when to use it, analogue/digital, sampling, sampling rate and resolution, sound size, lossless vs lossy, RLE, dictionary compression.
Assumed: mono/stereo/channels, bandwidth, streaming (used undefined); Python def, lists of lists and tuple unpacking (code blocks).

## cs.networks
Taught: network, LAN/WAN, client-server and peer-to-peer, thin/thick client, topology, bus/star/mesh/hybrid (and how a frame travels), frame vs packet, links in a full mesh, transmission media (copper, fibre, radio, microwave, satellite), bandwidth, NIC/WNIC/MAC address, switch (learning table), WAP, bridge, repeater, router, default gateway, Ethernet, collision, CSMA/CD, CSMA/CA, cloud computing (public/private).
Assumed: CALL and procedures (CSMA/CD pseudocode); f-strings, list comprehensions, tuples and sorted(key=) (code blocks); IP address and routing table (used in the topology section before the router section).

## cs.internet
Taught: internet vs World Wide Web, ISP, modem, PSTN, dedicated line, cell phone network, bit streaming (real-time vs on-demand), buffer, bit rate and Mbps vs MB, IPv4 and IPv6 (validity, shortening with ::), network and host part, subnet mask and prefix, network address (AND), broadcast address, usable hosts 2^h - 2, same-subnet test, subnetting, public and private addresses, NAT, static and dynamic addresses, DHCP, URL parts, DNS lookup (resolver, cache).
Assumed: arrays (Octets[Index] in the pseudocode); functions, split/join and the ipaddress module (code blocks); what a broadcast is at first use; firewall (named).

## cs.hardware
Taught: input/output devices, primary memory vs secondary storage, removable storage, laser printer, 3D printer, speaker, VR headset, microphone, capacitive/resistive/infra-red touchscreens, hard disk (platters, tracks, sectors, seek time, latency), flash/SSD (floating gate, wear levelling), optical disc (pits and lands), choosing storage, buffer and its size, RAM/ROM, volatile, bootstrap, firmware, SRAM/DRAM, PROM/EPROM/EEPROM, embedded system, sensor, actuator, ADC/DAC, monitoring vs control system, feedback, two-limit control loop.
Assumed: flip-flop and cache (used in the SRAM definition), BIOS, relay; CALL and function calls (pseudocode loop); f-string format specs (Python).
