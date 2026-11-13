@chapter cs.hardware
@title Computers and their components
@level as
@paper CAIE 9618 Paper 1
@time 5–7 hours
@summary The devices a computer needs to take data in, store it and send results out, and how each one works: printers, microphones, touchscreens, disks, flash memory and optical discs. You will also learn the types of memory (RAM, ROM, SRAM, DRAM, PROM, EPROM, EEPROM), buffers, embedded systems, and how monitoring and control systems use sensors, actuators and feedback.

:::why
Paper 1 asks you to describe how real devices work, one step per mark, and to explain why one kind of memory or storage suits a job better than another. Those marks are easy to win if you have the steps in the right order and the right technical word for each one. The same ideas run through the whole course: the memory types return in the processor chapter, and the control loop is a pattern you will meet again in programming.
:::

**Before you start**, you should know what a byte is and how binary data is measured, from [Data representation](#cs.data), and how sound becomes numbers, from [Multimedia](#cs.media). Nothing else is needed.

:::try Warm-up
Q: How many bytes are in 1 KiB, and how many bits are in 1 byte? (from [Data representation](#cs.data))
A: 1 KiB is \(2^{10} = 1024\) bytes, and 1 byte is 8 bits.
Q: Name the device that turns an analogue sound signal into numbers, and the device that turns numbers back into a signal for a speaker. (from [Multimedia](#cs.media))
A: An analogue-to-digital converter (ADC) turns the signal into numbers, and a digital-to-analogue converter (DAC) turns numbers back into a signal.
Q: A video is 5 minutes (300 seconds) long and each second needs 2 MB of data. How many MB is the whole video? (from [Data representation](#cs.data))
A: \(300 \times 2 = 600\) MB.
:::

## Input, output and storage

A computer is only useful if it can take data in, keep it, and give results back. Every computer system, from a phone to a bank's server, is built from the same four kinds of part:

- **input devices**, which take data from the outside world into the computer;
- **processor and primary memory**, where programs run and data is worked on;
- **secondary storage**, which keeps programs and data when the power is off;
- **output devices**, which present the results to a person or another machine.

:::def Input device
A hardware device that sends data to a computer from the outside world, converting it into digital form, such as a keyboard, a microphone or a touchscreen.
:::

:::def Output device
A hardware device that receives data from a computer and presents it in a form a person or another machine can use, such as a monitor, a speaker or a printer.
:::

Why does a computer need both? A processor can only work on binary data. Something has to convert a key press, a sound or a temperature into binary (input), and something has to convert binary back into a picture, a sound or a printed page (output). Without input a computer has nothing to work on; without output nobody can see what it did.

### Primary memory and secondary storage

Memory comes in two groups, and the exam wording matters.

:::def Primary memory
Memory that the processor can access directly. It holds the programs and data that are in use. RAM and ROM are both primary memory.
:::

:::def Secondary storage
Storage that the processor cannot access directly. It is non-volatile, so it keeps programs and data when the power is off, and it has a much larger capacity than primary memory. A hard disk, a solid state drive and an optical disc are examples.
:::

A program has to be copied from secondary storage into primary memory before the processor can run it. That is why you wait for a game to load: the data is being copied from a slow, large store to a fast, small one.

So why have both? Primary memory is fast enough for the processor to use but loses its contents when the power goes off (RAM) or cannot be changed (ROM). Secondary storage is slower, but it is cheaper per gigabyte, it holds far more, and it keeps your files safe when you switch off. The computer needs both: speed from one and permanence from the other.

:::def Removable storage
Secondary storage that can be taken out of the computer and used in another one, such as a USB flash drive, a memory card, an external hard disk or an optical disc.
:::

Removable storage is used to move files between computers, to keep a **backup** away from the computer that might fail, and to distribute software or media. Its drawbacks are that it is easy to lose or steal, and that a small device is easy to damage.

| Group | Examples | Direction of data |
|---|---|---|
| Input | keyboard, mouse, microphone, touchscreen, scanner, camera, sensors | outside world to computer |
| Output | monitor, speakers, laser printer, 3D printer, VR headset | computer to outside world |
| Both | touchscreen (input from touches, output as a display), VR headset (head tracking in, pictures out) | both |
| Secondary storage | magnetic hard disk, solid state drive, optical disc, memory card | computer to storage and back |

The rest of this chapter explains how the devices on Paper 1's list work. For each one, learn the **order of the steps**: examiners award one mark per step, and a correct step in the wrong place often loses its mark.

## How output devices work

### The laser printer

A laser printer prints a whole page at once. It uses static electricity to make toner (a fine powder of plastic and pigment) stick to the paper in the shape of the page.

:::steps
1. The data for the page is sent from the computer and held in the printer's memory (its buffer).
2. A rotating **drum** is given an electrostatic charge over its whole surface.
3. A **laser** scans across the drum. Where the laser touches, the charge is removed, so the drum now carries an electrostatic image of the page.
4. The drum rolls past the **toner**. The toner has the opposite charge to the remaining charge on the drum, so it sticks only to the areas the laser discharged.
5. The paper is given a charge and rolls past the drum. The paper pulls the toner off the drum, so the image is transferred to the paper.
6. The paper passes through a **fuser**: heated rollers melt the toner and press it into the paper, so it is fixed and will not smudge.
7. The drum is discharged and cleaned, ready for the next page.
:::

Colour printers repeat the process for four toners (cyan, magenta, yellow and black).

:::eg Describe how a laser printer prints a page (exam style)
Describe how a laser printer produces a printed page from data sent by a computer. [5 marks]

Take the steps in order and name each part. Five marks means five different correct steps, so do not spend two sentences on one.

- The data for the page is stored in the printer's memory (buffer) before printing starts. [B1]
- The drum is given an electrostatic charge. [B1]
- A laser scans the drum and removes the charge from the areas that will be printed, so the drum carries an image of the page. [B1]
- Toner with the opposite charge is attracted to the discharged areas of the drum. [B1]
- Charged paper pulls the toner from the drum, and the paper then passes through a fuser, which uses heat and pressure to fix the toner. [B1]

(The drum being discharged and cleaned for the next page is a further correct point. Marks are only awarded up to the maximum of 5.)
:::

### The 3D printer

A 3D printer builds a solid object from a 3D design. It is **additive**: it adds material, layer by layer, instead of cutting material away from a block. A common type works like this.

:::steps
1. A 3D design (a model made on a computer) is divided into thin horizontal layers by software.
2. A **print head** (extruder) heats a plastic filament until it melts.
3. The print head moves in the x and y directions, controlled by motors, and deposits the melted plastic where the first layer should be.
4. The plastic cools and hardens. The platform moves down (or the head moves up) by one layer's thickness.
5. The next layer is deposited on top of the last, and it fuses to it. The steps repeat until the object is complete.
:::

Other types of 3D printer harden a liquid resin with light or fuse a powder, but all of them build in layers. 3D printers are used for prototypes, for custom parts such as prosthetics, and for objects that are hard to make any other way.

### The speaker

A speaker turns a digital signal back into sound. You met the first step in [Multimedia](#cs.media).

:::steps
1. The digital sound data goes to a **digital-to-analogue converter (DAC)**, which produces a varying electrical (analogue) signal.
2. The signal is amplified and passed through a **coil of wire** that is attached to a cone and sits next to a **permanent magnet**.
3. The changing current makes the coil an electromagnet whose strength and direction keep changing. It is attracted to and repelled by the permanent magnet, so the coil moves backwards and forwards.
4. The coil moves the **cone** with it. The cone vibrates and pushes the air in front of it, which creates sound waves.
:::

A bigger signal makes the cone move further, which makes a louder sound. A faster change in the signal makes a higher pitch.

### The virtual reality (VR) headset

A VR headset makes the wearer feel they are inside a computer-generated scene. It is an output device (pictures and sound) and an input device (head movement) together.

:::steps
1. Two small **screens**, one in front of each eye, show slightly different images of the scene. The brain combines them into a 3D picture.
2. **Lenses** between the eyes and the screens focus the image and make it fill the wearer's field of view.
3. **Sensors** in the headset (a gyroscope for rotation and an accelerometer for movement) detect how the head moves. Some systems also use cameras to track position.
4. The computer uses the sensor data to update the pictures straight away, so the scene turns when the head turns. This is **head tracking**.
5. Speakers or headphones play sound that changes with the position of the wearer. Hand controllers, which also have sensors, let the wearer touch and move virtual objects.
:::

If the pictures lag behind the head movement, the wearer can feel sick, so the update must be very fast.

## How input devices work

### The microphone

A microphone turns sound waves into an electrical signal. This describes a **dynamic** microphone, which is the one Paper 1 expects.

:::steps
1. Sound waves hit a thin **diaphragm**, which vibrates with the sound.
2. The diaphragm is attached to a **coil of wire** that sits in the field of a **permanent magnet**, so the coil moves with it.
3. A coil that moves in a magnetic field has a current **induced** in it. The size and direction of the current follow the vibration.
4. The result is a continuously varying (analogue) electrical signal.
5. An **analogue-to-digital converter (ADC)** samples the signal at regular intervals and stores each sample as a binary number, so the computer can process and store the sound.
:::

Notice that a microphone and a speaker are the same idea run in opposite directions: one uses sound to move a coil and make a signal, the other uses a signal to move a coil and make sound.

### Touchscreens

A touchscreen is an input device that is also a display. It finds **where** you touched the screen, and the computer treats the position as the input. You should know three types.

:::cols
:::col Capacitive
The screen has a layer of material that conducts electricity and holds a small charge. Your finger also conducts, so when it touches (or nears) the screen it draws a little charge away, which changes the **capacitance** at that point. A controller measures the change at many points and works out the position. It supports **multi-touch** (several fingers), but it does not work with a plain plastic stylus or with most gloves, because they do not conduct.
:::
:::col Resistive
Two thin layers, each with a conductive coating, are held a tiny distance apart. Pressing makes the top layer touch the bottom one at that point, which completes a circuit. The controller measures the voltage at the contact point to find the position. It works with a finger, a glove or a stylus because it responds to **pressure**, but it is less sharp and does not handle multi-touch as well.
:::
:::col Infra-red
A frame around the screen has a row of infra-red LEDs on two sides and a matching row of sensors on the opposite sides, making a grid of invisible beams across the screen. A touching finger **breaks** some beams, and the crossing of the broken beams gives the position. It works with any object and is used on large screens, but dust or a bright light can upset the sensors.
:::
:::

:::warn Do not mix up capacitive and resistive
Capacitive screens sense the **electrical** property of a finger, so they need something that conducts. Resistive screens sense **pressure** from any object. A common wrong answer says that a capacitive screen "senses pressure".
:::

:::eg Choosing a touchscreen (short answer)
A market trader in Accra wears work gloves and takes payments on a tablet. Explain why a resistive touchscreen may suit the trader better than a capacitive one. [2 marks]

- A resistive screen works by pressure, so a gloved finger or a stylus presses the layers together and registers [B1]
- a capacitive screen needs a conductive finger to change the capacitance, so a gloved finger may not register [B1]
:::

## How storage devices work

You must be able to describe three kinds of secondary storage: magnetic, solid state and optical.

### The magnetic hard disk

A magnetic hard disk drive (HDD) stores data as tiny magnetised areas on spinning metal or glass disks.

:::steps
1. One or more circular **platters** coated with magnetic material spin at a constant speed on a spindle (for example 7200 revolutions per minute).
2. Each surface is divided into circular **tracks**, and each track is divided into **sectors**. A sector is the smallest unit that is read or written.
3. A **read/write head** on the end of an **arm** hovers a tiny distance above each surface. The arm swings the head across the platter to the correct track.
4. To **write**, the head magnetises a very small area of the surface. One direction of magnetisation stands for 0 and the opposite direction stands for 1.
5. To **read**, the head senses the direction of magnetisation of each area as it passes underneath, and turns that into a stream of 0s and 1s.
:::

Two delays make up the access time. The **seek time** is the time to move the head to the right track. The **latency** is the time spent waiting for the platter to spin until the right sector is under the head. A faster rotation speed reduces the latency. Because the head is so close to the surface, a knock while the disk is spinning can damage it, which is a weakness in portable devices.

### Solid state (flash) memory

A solid state drive (SSD), a USB flash drive and a memory card all use **flash memory**. They have no moving parts. Most flash memory is **NAND flash**, which is built from a very large number of transistors with a special extra layer.

:::steps
1. Each memory cell is a transistor with a **floating gate**: a small piece of conductor completely surrounded by insulator, between the control gate and the channel.
2. To **write**, a voltage on the control gate pushes electrons through the insulator so they become trapped on the floating gate. The trapped charge stays for years without power.
3. Whether the floating gate holds charge or not changes how easily the transistor conducts, and that difference stands for a 0 or a 1.
4. To **read**, the controller checks whether the transistor conducts at a test voltage, which shows whether the gate holds charge.
5. To **erase**, a voltage removes the trapped electrons. Flash memory is erased in **blocks**, not one bit at a time, so a block must be erased before any of it is rewritten.
:::

Each erase wears out the insulator a little, so every cell can only be written a limited number of times (a **limited number of write cycles**). A controller uses **wear levelling** to spread the writes evenly over all the cells, so no cell wears out far ahead of the others.

### Optical discs

CDs, DVDs and Blu-ray discs store data as a pattern of **pits** and **lands** in a single spiral track that runs from the centre of the disc outwards.

:::steps
1. The disc spins in the drive while a **laser** shines on the track.
2. A **land** is a flat area, which reflects the light strongly back towards a light sensor. A **pit** is a small dent that scatters the light, so much less is reflected.
3. The sensor detects the change in the reflected light as the track passes. The changes are decoded into binary data.
4. To **write** a recordable disc, a more powerful laser changes the disc surface along the track (it burns spots into a layer of dye, or it heats a special alloy so it changes between a shiny and a dull state). A rewritable disc can change the alloy back, so it can be erased and written again.
:::

A shorter wavelength of laser light gives a smaller spot, so smaller pits can be read and more data fits on a disc. That is why a Blu-ray disc, which uses a blue-violet laser, holds more than a DVD, which holds more than a CD.

### Choosing between storage types

:::key Storage compared
| | Magnetic hard disk | Solid state (flash) | Optical disc |
|---|---|---|---|
| How data is held | magnetised areas on platters | charge trapped in floating gates | pits and lands read by a laser |
| Moving parts | yes: platters and a head | none | yes: the disc spins |
| Access speed | slower (seek time and latency) | fastest of the three | slowest |
| Shock and noise | can be damaged by knocks; makes noise | robust and silent | scratches damage the surface |
| Cost per gigabyte | low | higher | very low per disc |
| Capacity | very large | large, and growing | small (about 25 GB for Blu-ray) |
| Lifetime | wear in moving parts | limited write cycles | long if stored well |
| Typical use | bulk storage of files and backups | laptops, phones, cameras | distributing films and software, archives |
:::

A "justify" question wants the choice tied to the scenario. A camera that is carried around needs storage that survives being dropped, so flash memory is a better choice than a hard disk; an archive of rarely used files that must be as cheap as possible suits a hard disk or optical discs.

:::eg Choosing storage for a scenario (exam style)
A wildlife researcher in Kenya carries a handheld recorder in a rucksack across rough ground and records sound for several hours a day. Justify the choice of flash memory rather than a magnetic hard disk for the recorder. [3 marks]

- Flash memory has no moving parts, so it is not damaged by knocks and vibration while the recorder is carried [B1]
- it uses less power and is silent, so it will not add noise to the recordings or flatten the battery [B1]
- it is small and light, and it gives fast reading and writing for continuous recording [B1]
:::

## Buffers

Devices work at very different speeds. A processor can send data to a printer in a fraction of a second, but the printer takes many seconds to print it. A hard disk can supply data in bursts, while a video player needs a steady flow. A **buffer** sits between two parts that work at different speeds and smooths out the difference.

:::def Buffer
A temporary storage area in memory that holds data while it is being transferred between two devices or processes that work at different speeds.
:::

:::analogy
A buffer is like a tank between a tap and a bath. The tap fills it in bursts, and the bath takes water at its own steady rate. The tank stops the water from being wasted when the tap is faster, and keeps water flowing when the tap pauses.
:::

Two examples are worth knowing well.

- **Printing.** The computer sends the whole document into the printer's buffer quickly. The computer is then free to do other work while the printer takes data from its buffer at its own slow speed.
- **Streaming video or audio.** The player loads several seconds of the stream into a buffer before it starts playing. If the network slows down or stutters, the player carries on from what is in the buffer. If the buffer empties, the video freezes until it fills again.

:::eg How big must a streaming buffer be? (calculation)
A video player receives a stream at a bit rate of 4 Mbit/s. It keeps a buffer that must hold 10 seconds of video. How many megabytes does the buffer need? Use 1 megabit = 10⁶ bits and 1 MB = 10⁶ bytes, and ignore any overheads.

Data in 10 seconds is bit rate × time: \(4 \times 10 = 40\) Mbit. A byte is 8 bits, so divide by 8: \(40 \div 8 = 5\) MB.

The buffer needs at least 5 MB. This holds 10 seconds of playing time, so a network stall of up to 10 seconds will not interrupt the video.
:::

The same calculation in Python:

```python
bit_rate = 4          # megabits per second
seconds = 10
buffer_megabits = bit_rate * seconds
buffer_megabytes = buffer_megabits / 8
print(buffer_megabits, "Mbit =", buffer_megabytes, "MB")
```

Output:

```output
40 Mbit = 5.0 MB
```

## Memory: RAM and ROM

Primary memory is made of chips that the processor can read and write directly. There are two main groups.

:::def RAM (random access memory)
Primary memory that can be read and written. It holds the programs and data that are currently in use, and it is **volatile**: it loses its contents when the power is switched off.
:::

:::def ROM (read-only memory)
Primary memory whose contents are fixed in manufacture, or are changed only by special means. It is **non-volatile**: it keeps its contents when the power is off.
:::

Any item in RAM can be read in the same time whichever address it has, which is why it is called "random access". Use the two together: ROM is read-only, so a program that is stored in it is safe from being overwritten by mistake or by a virus, and RAM is read/write, so it can hold the changing data of the programs you run.

| | RAM | ROM |
|---|---|---|
| Read and write | both | read only (in normal use) |
| Volatile | yes, contents lost without power | no, contents kept |
| Typical contents | the operating system and programs that are running, and their data | the **bootstrap** program and the firmware of a device |
| Capacity in a PC | large (gibibytes) | small (kibibytes to mebibytes) |

The **bootstrap** is the short program that runs when you switch the computer on. It tests the hardware and then loads the operating system from secondary storage into RAM. It has to be in ROM because RAM is empty at start-up. Washing machines, remote controls and printers keep their **firmware** (the permanent program that makes the device work) in ROM or similar non-volatile memory.

:::warn ROM does not hold the operating system
A PC's operating system is stored on secondary storage (a disk) and copied into RAM. On a PC, the ROM holds only the bootstrap and the basic firmware. "ROM stores the operating system and your files" is wrong for a computer, even though a small embedded device may keep its whole program in ROM.
:::

### SRAM and DRAM

RAM is built in two ways. You need to know both, and the reasons they are used where they are.

:::def SRAM (static RAM)
RAM in which each bit is stored in a flip-flop circuit made of several transistors. It keeps its data as long as power is supplied and does not need refreshing. It is faster, uses more chip area per bit and costs more than DRAM.
:::

:::def DRAM (dynamic RAM)
RAM in which each bit is stored as a charge in a tiny capacitor, with one transistor. The charge leaks away, so every cell must be **refreshed** (read and rewritten) many times a second. It is slower than SRAM, but it is cheaper and more compact, so it is used for large amounts of memory.
:::

| | SRAM | DRAM |
|---|---|---|
| Stores a bit in | a flip-flop (several transistors) | a capacitor (and one transistor) |
| Needs refreshing | no | yes, many times a second |
| Speed | faster | slower |
| Cost per bit | higher | lower |
| Density (bits per chip area) | lower | higher |
| Typical use | **cache memory** inside or next to the processor | **main memory**: the RAM sticks in a computer |

The difference follows from the design. A flip-flop switches almost instantly and holds its state, so SRAM is fast, but it takes several transistors per bit, so it is big and expensive. A capacitor-based cell takes much less space, so DRAM can offer gibibytes cheaply, but its charge leaks and reading it takes longer. A computer therefore uses a **small amount of SRAM** for the data the processor needs most often (the cache, in [Processor fundamentals and the fetch-execute cycle](#cs.processor)) and a **large amount of DRAM** for main memory.

:::warn "Static" does not mean the data never changes
SRAM can be written and rewritten as often as you like. "Static" only means that it does not need to be refreshed while the power is on. It is still volatile: when the power goes off, an SRAM cell loses its data as well.
:::

:::eg Explain a design choice (exam style)
A computer uses SRAM for its cache memory and DRAM for its main memory. Explain why. [4 marks]

- Cache memory is accessed constantly by the processor, so it must be as fast as possible, and SRAM is faster than DRAM [B1]
- SRAM does not need to be refreshed, so it is always ready to be read [B1]
- SRAM costs more per bit and uses more space, so only a small cache can be made from it [B1]
- main memory needs a large capacity at a lower cost, and DRAM is cheaper and denser, so it is used even though it is slower and needs refreshing [B1]
:::

### PROM, EPROM and EEPROM

ROM chips are made in several forms. The differences are in **how the contents are put in** and whether they can ever be changed.

:::def PROM (programmable read-only memory)
A ROM chip that is blank when it is made and can be programmed once, after manufacture, using a special device. After that its contents cannot be changed.
:::

:::def EPROM (erasable programmable read-only memory)
A ROM chip that can be programmed, erased by exposing it to strong ultraviolet light through a window in the chip, and then programmed again. It has to be taken out of the device to be erased.
:::

:::def EEPROM (electrically erasable programmable read-only memory)
A ROM chip that can be erased and rewritten using electrical signals, without removing it from the device. Flash memory is a development of EEPROM that is erased in blocks, not one byte at a time.
:::

| Type | Programmed | Erased | Typical use |
|---|---|---|---|
| ROM (mask ROM) | at manufacture | never | a fixed program made in large numbers |
| PROM | once, by the user or manufacturer | never | a small run of a fixed program |
| EPROM | many times | by ultraviolet light, out of the device | developing and testing firmware |
| EEPROM | many times | electrically, in place | settings and firmware that must be updated, such as a device's BIOS or a car key's data |

The pattern is that each type is easier to change than the one before it, and each costs more per bit. A device maker chooses by asking how often the contents will change and who will change them. Firmware that may need a bug fix after sale is put in EEPROM or flash, so it can be updated without opening the device.

## Embedded systems

Most computers you meet do not look like computers. A washing machine, a microwave oven, a car's engine controller and a digital watch each contain a small computer built in as one part of a larger machine.

:::def Embedded system
A computer system built into a larger device to carry out one dedicated function (or a small number of fixed functions), usually with its program stored in ROM or similar memory.
:::

A general-purpose computer, such as a laptop, can run any program you install. An embedded system does one job: a washing machine's controller reads the buttons and sensors, runs the motor and pumps through the programme you chose, and does nothing else.

:::eg Why a car engine uses an embedded system (exam style)
Explain why the control of a car's engine is carried out by an embedded system and not by a general-purpose computer. [4 marks]

- The system has one dedicated task (controlling fuel and ignition), so it needs only the hardware for that task [B1]
- it can be small, light and cheap enough to be fitted into every car [B1]
- its program is stored in ROM (or similar), so it starts at once when the engine is switched on and is not lost when the power is off [B1]
- it can respond in a very short time, so the engine is controlled reliably, because it does not share the processor with other programs [B1]
:::

:::cols
:::col Benefits
- Small, light and low-cost to make in large numbers.
- Uses little power, so it can run from a small battery.
- Designed for one task, so it can be made fast and very reliable.
- Starts immediately: no operating system to load.
- Easier to use: the user only presses a few buttons.
:::
:::col Drawbacks
- Cannot be used for anything but its dedicated job.
- Limited memory and processing power, so little room for new features.
- Hard to update, and the whole device may have to be replaced to fix a fault.
- Hard to repair: the processor is built into the product.
- A flaw in the program is hard to correct after the device is sold.
:::
:::

## Monitoring and control systems

Many computers do not just store and show data. They watch the real world and sometimes act on it. Two ideas describe this: **monitoring** and **control**.

:::def Sensor
An input device that measures a physical quantity from the environment, such as temperature, pressure, light, sound or the presence of a person, and produces an electrical signal that depends on it.
:::

:::def Actuator
An output device that causes a physical change in the world when the processor sends it a signal, such as a heater, a motor, a valve, a pump or a lamp.
:::

Common sensors on the syllabus are:

- **temperature**: a thermistor, whose resistance changes with temperature, used in ovens, greenhouses and weather stations;
- **pressure**: measures how hard something presses or how much gas pressure there is, used in tyres, burglar alarms (pressure pads) and weighing scales;
- **infra-red**: detects infra-red radiation, either heat from a person's body (a movement detector) or a beam that something breaks, used in automatic doors and security lights;
- **sound**: a microphone, used in alarms that react to breaking glass and in baby monitors.

Most sensors produce an **analogue** signal, and a computer needs digital data. The signal therefore passes through an **analogue-to-digital converter (ADC)** before the processor can use it. Most actuators need an **analogue** signal or a higher power than a processor can supply, so the output passes through a **digital-to-analogue converter (DAC)** (and an amplifier or relay) on the way.

:::def Monitoring system
A system that uses sensors to measure a quantity and a processor to record it, display it or raise a warning, but that does not change the thing it is measuring.
:::

:::def Control system
A system that uses sensors to measure a quantity, a processor to decide what to do, and actuators that change the process being measured, so that the quantity stays at the value wanted.
:::

A hospital heart monitor is a **monitoring** system: sensors read the patient's heart rate, the processor shows it and sounds an alarm if it is too high, but the monitor does not change the heart rate. A central heating thermostat is a **control** system: it measures the room temperature and switches the boiler on and off to keep the room at the set value. The test is whether an **actuator** changes what the sensor measures.

:::def Feedback
The use of the output of a system as part of its next input: here, the sensor measures the result of the actuator's last action, and the processor uses that reading to decide the next action.
:::

Feedback is what makes control work. The processor does not just heat for a set time and hope. It heats, **measures again**, and adjusts.

:::html
<figure class="fig"><svg viewBox="0 0 580 205" role="img" aria-label="A control loop drawn as a row of five boxes joined by arrows: Sensor (analogue), ADC (digital), Processor (decides), DAC (analogue) and Actuator (acts). Below them is a box labelled The greenhouse air. An arrow labelled heats the air runs from the actuator down and left to this box. An arrow labelled senses the air runs from this box left and up to the sensor. A label under the loop reads Feedback: the new temperature is measured again."><rect class="fm s-acc sw2" x="10" y="30" width="80" height="50" rx="4"/><text class="tl tc tb" x="50" y="52">Sensor</text><text class="tl tc" x="50" y="69">analogue</text><rect class="fm s-acc sw2" x="130" y="30" width="80" height="50" rx="4"/><text class="tl tc tb" x="170" y="52">ADC</text><text class="tl tc" x="170" y="69">digital</text><rect class="f1 s-acc sw2" x="250" y="30" width="80" height="50" rx="4"/><text class="tl tc tb" x="290" y="52">Processor</text><text class="tl tc" x="290" y="69">decides</text><rect class="fm s-acc sw2" x="370" y="30" width="80" height="50" rx="4"/><text class="tl tc tb" x="410" y="52">DAC</text><text class="tl tc" x="410" y="69">analogue</text><rect class="fm s-acc sw2" x="490" y="30" width="80" height="50" rx="4"/><text class="tl tc tb" x="530" y="52">Actuator</text><text class="tl tc" x="530" y="69">acts</text><path class="ln" fill="none" d="M90 55 H128" marker-end="url(#ah)"/><path class="ln" fill="none" d="M210 55 H248" marker-end="url(#ah)"/><path class="ln" fill="none" d="M330 55 H368" marker-end="url(#ah)"/><path class="ln" fill="none" d="M450 55 H488" marker-end="url(#ah)"/><rect class="fm2 s-acc sw2" x="210" y="125" width="160" height="40" rx="4"/><text class="tl tc" x="290" y="150">The greenhouse air</text><path class="ln" fill="none" d="M530 80 V145 H372" marker-end="url(#ah)"/><path class="ln" fill="none" d="M208 145 H50 V82" marker-end="url(#ah)"/><text class="tl tc" x="450" y="136">heats the air</text><text class="tl tc" x="130" y="136">senses the air</text><text class="tl tc tb" x="290" y="192">Feedback: the new temperature is measured again</text></svg><figcaption>The control loop of a greenhouse heater. The sensor measures the air, the processor decides, and the actuator changes the air. The sensor then measures the new temperature, which closes the loop.</figcaption></figure>
:::

The figure shows the loop in the order you should write it in an exam: sensor, ADC, processor, DAC, actuator, then the changed process measured again.

:::key A control system, step by step
1. A **sensor** measures the quantity (the temperature) and produces an analogue signal.
2. An **ADC** converts the signal to digital data.
3. The **processor** compares the reading with the stored target (or limits) and decides what to do.
4. If action is needed, the processor sends a signal to the **actuator**, through a **DAC** if the actuator needs an analogue signal.
5. The actuator changes the process (the heater warms the air).
6. The sensor measures again, and the loop repeats: this is **feedback**.
:::

### A control loop as an algorithm

A greenhouse in Pretoria should stay between 18 °C and 22 °C. A heater that switches on at exactly 18 and off at exactly 18 would flicker on and off all the time. A better rule uses **two limits**: switch the heater on below 18 and off above 22, and leave it as it is in between. In pseudocode, a question would tell you the names of the commands that talk to the hardware; the names here are made up for the example.

```pseudocode
CONSTANT LowLimit = 18.0
CONSTANT HighLimit = 22.0
DECLARE Temperature : REAL
DECLARE HeaterOn : BOOLEAN

HeaterOn ← FALSE
WHILE SystemRunning = TRUE
   Temperature ← ReadTemperature()
   IF Temperature < LowLimit THEN
      HeaterOn ← TRUE
   ENDIF
   IF Temperature > HighLimit THEN
      HeaterOn ← FALSE
   ENDIF
   CALL SetHeater(HeaterOn)
   CALL Wait(60)
ENDWHILE
```

`ReadTemperature` stands for the sensor and the ADC, and `SetHeater` stands for the DAC and the actuator. The loop is the feedback: each pass takes a new reading that shows the effect of the last pass. The heater changes state only when a limit is crossed, so between 18 and 22 the heater keeps whatever state it had.

To see it work, the Python program below uses a very simple model of the greenhouse in place of the real sensor: the air gains 2.0 °C in a minute when the heater is on and loses 1.0 °C in a minute when it is off. It starts at 19.0 °C.

```python
LOW_LIMIT = 18.0
HIGH_LIMIT = 22.0
temperature = 19.0
heater_on = False
for minute in range(1, 13):
    if temperature < LOW_LIMIT:
        heater_on = True
    if temperature > HIGH_LIMIT:
        heater_on = False
    if heater_on:
        state = "ON"
    else:
        state = "OFF"
    print(f"Minute {minute:2}: {temperature:.1f} C, heater {state}")
    if heater_on:
        temperature = temperature + 2.0
    else:
        temperature = temperature - 1.0
```

Output:

```output
Minute  1: 19.0 C, heater OFF
Minute  2: 18.0 C, heater OFF
Minute  3: 17.0 C, heater ON
Minute  4: 19.0 C, heater ON
Minute  5: 21.0 C, heater ON
Minute  6: 23.0 C, heater OFF
Minute  7: 22.0 C, heater OFF
Minute  8: 21.0 C, heater OFF
Minute  9: 20.0 C, heater OFF
Minute 10: 19.0 C, heater OFF
Minute 11: 18.0 C, heater OFF
Minute 12: 17.0 C, heater ON
```

Read the output as a trace. At minute 3 the temperature has fallen to 17.0, below the low limit, so the heater switches on. It stays on through minutes 4 and 5 (19.0 and 21.0 are between the limits) and switches off at minute 6, when the reading of 23.0 is above 22.0. The temperature then falls for six minutes until the next switch-on. At minute 2 the reading is exactly 18.0, which is not below 18.0, so nothing changes: the comparison is strictly less than.

:::eg Describe a control system with feedback (exam style)
A greenhouse in Pretoria has a heater and a window opener. Describe how a computer control system keeps the greenhouse at a suitable temperature, using the terms sensor, actuator and feedback. [6 marks]

- A temperature sensor measures the air temperature at regular intervals [B1]
- the analogue signal from the sensor is converted to digital by an ADC [B1]
- the processor compares the reading with the stored limits (or target temperature) [B1]
- if the reading is too low, the processor sends a signal (through a DAC if needed) to the actuator that switches the heater on; if it is too high, to the actuator that opens the window [B1]
- the actuator changes the temperature of the air [B1]
- feedback: the sensor measures the new temperature and the processor uses it to decide the next action, so the loop repeats [B1]
:::

:::warn A sensor measures; it does not control
"The sensor switches the heater on" earns no mark. A sensor only produces a signal. The **processor** decides, and the **actuator** acts. Write "the sensor sends the reading to the processor", never "the sensor turns on the heater". In the same way, a monitoring system that sounds an alarm is not a control system, because the alarm does not change the thing being measured.
:::

## Spot the error

:::eg Spot the error: a corridor light
Question: A school corridor light switches on automatically when a person walks past. Describe how the control system works. [4 marks]

A student wrote:

```text
01  An infra-red sensor detects the heat from the person's body.
02  The sensor switches the lamp on.
03  The lamp lights the corridor, so the person can see.
04  When the person has gone, the sensor stops detecting them and the lamp switches off.
```

Line 01 is correct: an infra-red sensor detects the person [B1]. **Line 02 is wrong: a sensor cannot switch anything. It sends its signal to the processor (through an ADC), and the processor decides to send a signal to the actuator that switches the lamp on** [B0]. Line 03 describes the result, not how the system works, so it earns nothing [B0]. Line 04 is correct as far as it goes, because the sensor no longer detects the person, but it should say that the processor then switches the lamp off [B1]. The answer scores 2 out of 4.

A full four-mark answer names every part. The infra-red sensor detects the person. The signal goes through an ADC to the processor. The processor sends a signal to an actuator (a switch or relay) that switches the lamp on. The sensor keeps taking readings, so the processor switches the lamp off when no one is detected: that is the feedback.
:::

:::try Start easy, finish at exam standard
Q: State the difference between primary memory and secondary storage.
A: Primary memory is accessed directly by the processor and holds programs and data in use (RAM and ROM). Secondary storage is not accessed directly, is non-volatile, and is used for long-term storage of programs and data.
Q: Give two examples of removable storage and one reason someone might use it.
A: A USB flash drive and an external hard disk (a memory card or optical disc also count). It is used to move files between computers or to keep a backup somewhere safe.
Q: Name the part of a laser printer that carries the image of the page as an electrostatic charge, and the part that makes the toner stay on the paper.
A: The drum carries the image. The fuser, which uses heat and pressure, makes the toner stay on the paper.
Q: Put these four steps of a microphone in the correct order: the coil moves in a magnetic field; the diaphragm vibrates; an ADC samples the signal; a current is induced.
A: The diaphragm vibrates; the coil moves in a magnetic field; a current is induced; an ADC samples the signal.
Q: What is stored on the floating gate of a flash memory cell, and what happens to it when a block is erased?
A: Electrons are trapped on the floating gate. The erase voltage removes the trapped electrons from every cell in the block.
Q: A hard disk spins at 7200 revolutions per minute. How many revolutions is that in one second, and how long is one revolution?
A: \(7200 \div 60 = 120\) revolutions per second, so one revolution takes \(1 \div 120\) of a second, about 8.3 ms. On average the platter must turn half a revolution to bring a sector under the head, so the average latency is about 4.2 ms.
Q: State whether each is volatile or non-volatile: RAM, ROM, a flash drive, SRAM.
A: RAM: volatile. ROM: non-volatile. Flash drive: non-volatile. SRAM: volatile (it is a type of RAM).
Q: Which type of ROM can be erased with ultraviolet light, and which can be erased electrically without being removed from the device?
A: EPROM is erased with ultraviolet light; EEPROM is erased electrically in the device.
Q: A baby monitor uses a sound sensor to send an alarm to a parent's phone when the baby cries. Is it a monitoring system or a control system? Give a reason.
A: A monitoring system. It measures sound and raises a warning, but it does not change anything about the baby or the room.
Q: A student writes a pseudocode loop for a fish tank heater but forgets to read the sensor again inside the loop. What feature of a control system has been left out, and what will go wrong?
A: Feedback. The processor keeps using the first reading, so it cannot see the effect of the heater and will never switch it off (or on) when the temperature changes.
:::

:::try Exam practice ★ to ★★★
Q: [4 marks] ★ A tablet computer has both RAM and ROM. Describe two differences between RAM and ROM, and state one thing that is stored in each.
A: Two differences, with one stored item for each:

- RAM can be read and written, but ROM is normally read-only [B1]
- RAM is volatile, so it loses its contents when the power is off, but ROM is non-volatile [B1]
- RAM stores the programs and data that are being used, for example the running application [B1]
- ROM stores the bootstrap (start-up program) or the device's firmware [B1]

Q: [4 marks] ★ A designer is building a processor with a cache. Compare SRAM and DRAM, and say which one is used for the cache.
H: Give two points about each, and link them to the cache's job.
A: One possible answer:

- SRAM stores each bit in a flip-flop, but DRAM stores it as a charge in a capacitor [B1]
- DRAM must be refreshed regularly because the charge leaks, but SRAM does not need refreshing [B1]
- SRAM is faster, but more expensive and less dense than DRAM [B1]
- SRAM is used for the cache, because the cache must be very fast and only a small amount is needed [B1]

Q: [5 marks] ★★ (#cs.hardware) Describe how a solid state drive stores data and why it can only be written to a limited number of times.
H: Think about what is in each cell, how the data is read, and what an erase does.
H: The limit on writing is a physical wear effect on the cells.
A: One possible answer:

- the drive is made of flash memory with cells built from transistors with a floating gate [B1]
- writing traps electrons (charge) on the floating gate [B1]
- the presence or absence of trapped charge represents a 0 or a 1 [B1]
- each erase and rewrite wears the insulation around the gate a little [B1]
- after many write cycles a cell can no longer hold its charge reliably, so there is a limit on the number of writes [B1]

Q: [4 marks] ★★ Describe how a capacitive touchscreen finds the position of a finger.
A: One possible answer:

- the screen has a layer that conducts electricity and holds a charge [B1]
- the finger is a conductor, so touching the screen draws charge away at that point [B1]
- this changes the capacitance at that point, and the controller measures the change at many places on the screen [B1]
- the controller works out the coordinates of the touch from where the change is largest [B1]

Q: [4 marks] ★★ A manufacturer of pressure cookers includes an embedded system in each cooker. Explain two benefits and two drawbacks of using an embedded system here.
A: Two benefits and two drawbacks, each with a reason:

- benefit: it is small and cheap, so it can be built into every cooker [B1]
- benefit: it is designed for one job, so it reacts quickly and reliably to the pressure [B1]
- drawback: the program is hard to change, so a fault in it may not be fixable after the cooker is sold [B1]
- drawback: it has limited memory and processing power, so extra features cannot easily be added [B1]

Q: [5 marks] ★★ (#cs.data) A music streaming app receives audio at a bit rate of 2 Mbit/s. It builds a buffer that holds 30 seconds of audio before playback starts. (a) Explain why a buffer is used for streaming. [2] (b) Calculate the size of the buffer in megabytes (1 megabit = 10⁶ bits; 1 MB = 10⁶ bytes). [3]
H: Bits per second times seconds gives bits; divide by 8 for bytes.
A: (a) The data arrives at an uneven speed because the network varies [B1]. The buffer stores audio ahead, so playback continues smoothly if the network slows or stops for a short time [B1].

(b) Data in 30 seconds: \(2 \times 30 = 60\) Mbit [B1]. Divide by 8 to convert bits to bytes: \(60 \div 8\) [B1] = 7.5 MB [B1].

Q: [6 marks] ★★★ An automatic car park barrier in Dubai raises when a car stops at it. A pressure sensor under the road detects the car. (a) State what type of system this is and give a reason. [2] (b) Describe how the system uses the sensor, a processor and an actuator, and how feedback makes the barrier close at the right time. [4]
H: Ask whether something physical is changed by the output.
H: Part (b) is the six-step control loop, cut down to the parts this system has.
A: (a) A control system [B1], because the processor's output moves the barrier, an actuator, which changes the situation being measured, as it lets the car go [B1].

(b) The pressure sensor detects the weight of the car and sends a signal, through an ADC, to the processor [B1]. The processor sends a signal to the actuator (a motor), which raises the barrier [B1]. The sensor keeps measuring the pressure: when the car drives away, the pressure falls to zero [B1], and this reading is fed back to the processor, which tells the motor to lower the barrier [B1].

Q: [6 marks] ★★★ A bus company in Lima fits each bus with a camera that records video to a storage device while the bus is moving over rough roads. The company is choosing between a magnetic hard disk and a solid state drive. Justify a choice for the storage device, and state two disadvantages of your choice.
H: Use the scenario: movement, vibration, hours of recording, cost of replacing devices.
A: One possible answer, choosing a solid state drive:

- an SSD has no moving parts, so it will not be damaged by the vibration and knocks of the bus [B1]
- a hard disk has a read/write head very close to a spinning platter, so a knock can damage the disk and lose recordings [B1]
- an SSD writes data quickly, so it can record continuous video [B1]
- an SSD uses little power and makes no noise, so it will not drain the bus's power supply [B1]
- disadvantage: an SSD costs more per gigabyte than a hard disk, so storing many days of video is more expensive [B1]
- disadvantage: each cell can only be written a limited number of times, so a drive that records all day could wear out, and the company may have to replace it [B1]

(A choice of the hard disk is acceptable only if it is justified from the scenario, for example by cost for a very large capacity; the vibration point then has to be answered as a disadvantage.)
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A data logger left on a glacier records the air temperature every hour for two years, with no one to visit it. It has a program that must never be lost, settings that a scientist may change by radio, and a small working memory for the readings it has not yet saved. State a suitable type of memory for each of the three things (program, settings, working memory) and give a reason for each.
H: Ask of each item: must it survive a loss of power, and must it be changeable in place?
H: Remember that DRAM needs refreshing and uses power all the time.
A: One possible answer:

- program: ROM (or PROM), because it must not be lost or changed, and it is not changed once the logger is made [B1]; the reason is that ROM is non-volatile, so it survives a total loss of power [B1]
- settings: EEPROM (or flash), because they must be changed in place by a signal from the scientist, with no one there to remove a chip [B1]; the reason is that EEPROM is also non-volatile, so the settings survive if the battery fails [B1]
- working memory: RAM, because the readings change all the time and need fast reading and writing [B1]; the reason is that RAM can be written as often as needed, and an SRAM cell does not need refreshing, so it saves power on a small battery [B1]

(Accept DRAM with a reason; EPROM is not suitable because it has to be removed from the device to be erased.)

Q: [6 marks] ★★★ A fish tank in a school has a heater and a thermometer sensor. The computer should keep the water between 24.0 °C and 26.0 °C. (a) Write pseudocode for the loop that does this, using the made-up commands `ReadTemperature()` (returns a REAL) and `SetHeater(State)` (State is a BOOLEAN) and the style of the greenhouse loop. [4] (b) Explain why the loop uses two limits instead of switching the heater on and off at one value, such as 25.0 °C. [2]
H: The heater state changes only when a limit is crossed; between the limits it keeps its state.
H: For (b), think about what the heater would do if the temperature hovered around 25.0 °C.
A: (a) One possible answer:

```pseudocode
WHILE SystemRunning = TRUE
   Temperature ← ReadTemperature()
   IF Temperature < 24.0 THEN
      CALL SetHeater(TRUE)
   ENDIF
   IF Temperature > 26.0 THEN
      CALL SetHeater(FALSE)
   ENDIF
ENDWHILE
```

- a loop that repeats while the system is running [B1]
- reads the temperature inside the loop on every pass (feedback) [B1]
- switches the heater on when below 24.0 [B1]
- switches the heater off when above 26.0 [B1]

(b) With one value the heater would switch on and off every time the temperature crossed it, which could be many times a minute [B1]. That wears the heater and its switch and wastes energy, but with two limits the heater changes state much less often, because the temperature has to travel all the way across the gap between them [B1].
:::

:::quiz
? Which statement about RAM is correct?
- It keeps its contents when the power is switched off.
+ It can be read and written and loses its contents when the power is switched off.
- It can only be read, and it stores the bootstrap.
- It is secondary storage that holds files.
> RAM is volatile primary memory that can be read and written. Keeping contents without power describes ROM or secondary storage; the bootstrap is held in ROM.
? Why is SRAM used for cache memory rather than DRAM?
- It is cheaper per bit.
- It stores more data in the same area.
+ It is faster and does not need refreshing.
- It is non-volatile.
> SRAM is faster and needs no refresh, but it costs more per bit and takes more space, so only a small cache is built from it. DRAM is the cheaper, denser one. SRAM is volatile like all RAM.
? What does the laser do in a laser printer?
- It melts the toner onto the paper.
+ It removes the charge from the parts of the drum that will be printed.
- It heats the paper so the toner sticks.
- It sprays ink onto the paper.
> The laser draws the image on the charged drum by discharging it. Melting the toner is the job of the fuser, and a laser printer uses toner, not ink.
? Which device is made of cells with a floating gate?
- an optical disc
- a magnetic hard disk
+ a solid state drive
- a dynamic microphone
> A floating-gate transistor traps electrons to store a bit in flash memory, which is the basis of an SSD. The hard disk uses magnetised areas and the optical disc uses pits and lands.
? What is the function of a buffer?
- It makes a slow device work faster.
- It stores a program permanently.
+ It holds data temporarily between two devices that work at different speeds.
- It converts analogue data to digital data.
> A buffer is temporary storage that smooths out a speed difference. It does not make the slow device any faster; it stops the fast device having to wait. Converting analogue to digital data is the job of an ADC.
? Which type of ROM can be erased and rewritten electrically without taking the chip out of the device?
- PROM
- EPROM
+ EEPROM
- mask ROM
> EEPROM is erased by electrical signals in place. EPROM needs ultraviolet light and has to be removed, PROM can be programmed only once, and mask ROM is fixed in manufacture.
? A system measures a room's temperature and records it on a screen, but it controls nothing. What is it?
- a control system
+ a monitoring system
- an embedded system with feedback
- a buffer
> With no actuator that changes the room, the system only measures and displays, which is monitoring. A control system would use an actuator to change the temperature.
? Which statement describes a resistive touchscreen?
- It senses the electrical charge of a finger.
- It uses a grid of infra-red beams.
+ It detects pressure that pushes two conductive layers together.
- It works only with a bare finger.
> A resistive screen responds to pressure, so a glove or stylus also works. Sensing charge is capacitive, and a grid of beams is infra-red.
:::

:::checklist What you can now do
- [ ] I can explain the need for input and output devices, primary memory and secondary (including removable) storage.
- [ ] I can describe the principal operation of a laser printer, a 3D printer, a microphone and a speaker.
- [ ] I can describe how capacitive and resistive touchscreens find a touch, and how a VR headset works.
- [ ] I can describe the operation of a magnetic hard disk, solid state (flash) memory and an optical disc, and choose between them for a scenario.
- [ ] I can explain what a buffer is and why one is used, and calculate its size from a bit rate and a time.
- [ ] I can state the differences between RAM and ROM and give a use of each.
- [ ] I can compare SRAM and DRAM and explain where each is used and why.
- [ ] I can describe PROM, EPROM and EEPROM.
- [ ] I can describe an embedded system and give its benefits and drawbacks.
- [ ] I can explain the difference between a monitoring system and a control system, name sensors and actuators, and describe feedback.
:::

:::recap
- Input devices bring data in; output devices send results out; primary memory (RAM, ROM) is accessed directly by the processor; secondary storage is non-volatile and has a large capacity; removable storage can be carried between computers.
- Laser printer: charged drum, laser discharges the image, toner sticks to the discharged areas, charged paper takes the toner, fuser fixes it. 3D printer: additive, layer by layer. Speaker: DAC, coil in a magnetic field, cone vibrates. Microphone: diaphragm, coil in a magnetic field, induced current, ADC. VR headset: two screens, lenses, motion sensors, head tracking.
- Capacitive touchscreens sense a finger's conductivity (multi-touch); resistive ones sense pressure (any object); infra-red ones sense broken beams.
- Hard disk: spinning platters, tracks and sectors, a head on an arm, magnetised areas, seek time and latency. SSD: NAND flash, floating gates trap charge, no moving parts, limited write cycles, erased in blocks. Optical: laser, pits and lands, reflected light.
- A buffer holds data temporarily between devices of different speeds. Buffer size in bytes = bit rate × seconds ÷ 8.
- RAM: read/write, volatile, holds running programs and data. ROM: non-volatile, holds the bootstrap and firmware. SRAM: flip-flops, fast, no refresh, costly, for cache. DRAM: capacitors, refreshed, cheaper, dense, for main memory.
- PROM is programmed once; EPROM is erased by ultraviolet light; EEPROM is erased electrically in place (flash is a block-erased type).
- An embedded system is a computer built into a device for one dedicated job: small, cheap, reliable, but fixed in function and hard to update.
- A sensor measures; the processor decides; an actuator acts. A monitoring system does not change the process; a control system does. Feedback is the new measurement used for the next decision.
:::

:::links
- practise: [Computers and components: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/3-hardware-/computers-and-components/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos on memory, disks and how hardware works
- read: [Computers and the internet](https://www.khanacademy.org/computing/computers-and-internet) · Khan Academy · a free second explanation of how computers are built
- read: [Ada Computer Science](https://adacomputerscience.org/) · Ada Computer Science · free explanations and questions on hardware and memory
- read: [ZNotes AS Computer Science 9618](https://znotes.org/caie/as-level/computer-science-9618/) · ZNotes · free summary notes for the whole AS course

Links checked 13 November 2026.
:::

Next: [Logic gates and logic circuits](#cs.logic)
