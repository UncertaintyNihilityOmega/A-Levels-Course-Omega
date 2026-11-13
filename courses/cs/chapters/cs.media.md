@chapter cs.media
@title Images, sound and compression
@level as
@paper CAIE 9618 Paper 1
@time 4–6 hours
@summary How a computer stores pictures and sound: bitmap images (pixels, resolution, colour depth, file header) and vector graphics (drawing lists), sampled sound (sampling rate and resolution), how to calculate file sizes by hand, and how lossless and lossy compression, including run-length encoding, make files smaller.

:::why
Photos, videos, music and voice calls are most of what people store and send, and every one of them is a long run of bits. Knowing how many bits a picture or a recording needs lets you explain why files are large, why they are compressed, and what quality you give up when you shrink them. Paper 1 asks you to estimate file sizes with no calculator and to justify a choice of format, so both skills are practised in this chapter.
:::

**Before you start**, you should be comfortable with bits, bytes and the binary prefixes (KiB, MiB) from [Number systems and binary arithmetic](#cs.data).

:::try Warm-up
Q: How many bytes are in 4 KiB? (from [Number systems and binary arithmetic](#cs.data))
A: \(4 \times 1024 = 4096\) bytes, because 1 KiB = \(2^{10} = 1024\) bytes.
Q: How many different patterns can 3 bits form? (from [Number systems and binary arithmetic](#cs.data))
A: \(2^3 = 8\) patterns, from 000 to 111.
Q: Convert 1011 to denary and to hexadecimal. (from [Number systems and binary arithmetic](#cs.data))
A: \(8 + 2 + 1 = 11\), which is B in hexadecimal.
:::

## Bitmap images

Look closely at a photo on a screen and you find it is a grid of tiny squares of single colours. A computer stores a picture in exactly that way: a rectangular grid, with a number for the colour of each square.

:::def Bitmap image
An image stored as a grid of pixels, in which each pixel is stored as a binary code for its colour.
:::

:::def Pixel
Short for "picture element": the smallest single point of an image, which has one colour.
:::

:::def Colour depth
The number of bits used to store the colour of each pixel. It is also called bit depth.
:::

:::def Image resolution
The number of pixels in an image, written as width × height, for example 1024 × 768. More pixels mean more detail.
:::

:::def Screen resolution
The number of pixels a screen can display, written as width × height, for example 1920 × 1080.
:::

:::def File header
Data stored at the start of a file that describes the file, so that a program can read the rest of it. For a bitmap it includes the image's width and height in pixels, its colour depth and the file type.
:::

### Colour depth: bits per pixel

Each pixel's colour is stored as a binary code. With 1 bit per pixel there are only two codes, 0 and 1, so the image can have two colours, such as black and white. Every extra bit doubles the number of colours, so a colour depth of \(n\) bits allows \(2^n\) colours.

| Colour depth (bits) | 1 | 2 | 4 | 8 | 16 | 24 |
|---|---|---|---|---|---|---|
| Number of colours | 2 | 4 | 16 | 256 | 65 536 | 16 777 216 |

A depth of 24 bits is 8 bits for each of red, green and blue, which is why web colours such as `#FF8000` (see [Number systems and binary arithmetic](#cs.data)) have three bytes. To find the colour depth needed for a given number of colours, find the smallest \(n\) with \(2^n\) at least that big: 200 colours need 8 bits, because \(2^7 = 128\) is too few and \(2^8 = 256\) is enough.

:::warn Colour depth is not the number of colours
Colour depth is **bits per pixel**, such as 8. The number of colours is \(2^8 = 256\). If a question says "colour depth of 256" something has gone wrong; if it says "256 colours", the colour depth is 8 bits.
:::

:::eg What a small bitmap stores
A 4 × 4 image uses a colour depth of 2 bits, with the codes 00 = white, 01 = red, 10 = green and 11 = blue. The pixel codes, row by row from the top, are shown. State the data stored for the image, and its size in bits and bytes.

| | Column 1 | Column 2 | Column 3 | Column 4 |
|---|---|---|---|---|
| Row 1 | 00 | 00 | 01 | 01 |
| Row 2 | 00 | 10 | 10 | 01 |
| Row 3 | 11 | 10 | 10 | 00 |
| Row 4 | 11 | 11 | 00 | 00 |

The pixels are stored one row after another: 0000 0101, 0010 1001, 1110 1000, 1111 0000. [B1] There are \(4 \times 4 = 16\) pixels at 2 bits each, so the pixel data is \(16 \times 2 = 32\) bits, which is \(32 \div 8 = 4\) bytes. [B1] The file header stores the width (4), the height (4) and the colour depth (2), so the program knows how to cut the stream of bits back into rows of pixels. [B1]
:::

### Bitmap file size

The pixel data of a bitmap has one code of `colour depth` bits for every pixel, so its size follows directly.

:::key Bitmap file size
- Size in bits = width × height × colour depth (all in pixels and bits per pixel).
- Size in bytes = size in bits ÷ 8. Then ÷ 1024 for KiB and ÷ 1024 again for MiB (use ÷ 1000 only if the question uses kB and MB).
- Ignore the file header unless the question says how big it is. Say "ignoring the header" in your working.
:::

Without a calculator, break each number into a power of 2 and a small factor. For 1024 × 768 with a colour depth of 24 bits: \(1024 = 2^{10}\), \(768 = 3 \times 2^8\) and 24 bits = \(3\) bytes, so the size is \(2^{10} \times 3 \times 2^8 \times 3 = 9 \times 2^{18}\) bytes. Dividing by \(2^{10}\) gives \(9 \times 2^8 = 2304\) KiB.

:::eg Estimating a file size (exam style)
A photograph is 1024 pixels wide and 768 pixels high, with a colour depth of 24 bits. Calculate the file size in bytes, in KiB and in MiB, ignoring the header. [4 marks]

Size in bits = \(1024 \times 768 \times 24\) [M1]

\(1024 \times 768 = 786\,432\) pixels. Each pixel is 24 bits = 3 bytes, so the size in bytes is \(786\,432 \times 3 = 2\,359\,296\) bytes. [A1]

In KiB: \(2\,359\,296 \div 1024 = 2304\) KiB. [B1]

In MiB: \(2304 \div 1024 = 2.25\) MiB. [B1]
:::

```python
def bitmap_size_bytes(width, height, colour_depth):
    return width * height * colour_depth // 8


size = bitmap_size_bytes(1024, 768, 24)
print(size, "bytes")
print(size / 1024, "KiB")
print(size / 1024 / 1024, "MiB")
```

Output:

```output
2359296 bytes
2304.0 KiB
2.25 MiB
```

### Changing resolution and colour depth

Both settings trade quality against file size, and the size formula tells you exactly how.

| Change | Effect on quality | Effect on file size |
|---|---|---|
| Higher image resolution (more pixels) | more detail, sharper when enlarged | larger: size is proportional to width × height |
| Lower image resolution | less detail; edges look blocky if the image is enlarged | smaller |
| Higher colour depth | more colours, smoother shading | larger: size is proportional to colour depth |
| Lower colour depth | fewer colours; smooth gradients show visible bands | smaller |

If the image resolution is higher than the screen resolution, the screen cannot show every pixel, so the picture is scaled down and some detail is lost, even though the file is large. If it is lower, the picture is enlarged to fill the screen and looks blocky.

:::eg Changing the settings of an image
A 640 × 480 image has a colour depth of 16 bits. (a) Find its size in KiB. (b) The width and height are both halved. Find the new size. (c) From the original image, the colour depth is instead reduced to 8 bits. Find the new size.

(a) \(640 \times 480 \times 16 = 4\,915\,200\) bits \(= 614\,400\) bytes \(= 600\) KiB. [B1]

(b) The new image is 320 × 240. Halving both dimensions gives a quarter of the pixels, so the size is a quarter: \(600 \div 4 = 150\) KiB. [B1]

(c) Halving the colour depth halves the size: \(600 \div 2 = 300\) KiB. [B1] (Both changes lose quality: the first loses detail and the second loses colours.)
:::

:::warn Bits and bytes
Colour depth and sampling resolution are in **bits**. Memory sizes are in **bytes**. The most common lost mark in a file-size question is the missing division by 8. After multiplying, ask yourself: "is this bits or bytes?"
:::

## Vector graphics

A bitmap stores every pixel. A vector graphic stores instructions for drawing the picture instead. A logo made of a circle, a rectangle and a line can be described in a few lines, however large it is drawn.

:::def Vector graphic
An image stored as a list of mathematical descriptions of shapes (such as lines, circles and rectangles) which the computer uses to draw the picture.
:::

:::def Drawing object
One shape in a vector graphic, such as a line, a circle or a rectangle.
:::

:::def Property
A value that describes one feature of a drawing object, such as its position, size, line width, line colour or fill colour.
:::

:::def Drawing list
The list of every drawing object in a vector graphic together with the properties of each, which is stored in the file and used to redraw the image.
:::

A drawing list for a small road sign might look like this (this is an illustration, not a real file format):

```text
RECTANGLE  top-left (10, 10)  width 80  height 50  fill yellow  line colour black  line width 2
CIRCLE     centre (50, 35)  radius 15  fill red  line colour black  line width 2
LINE       from (10, 70) to (90, 70)  line colour black  line width 3
```

Each line is one drawing object, and the words after it are its properties. For the circle, the properties are the centre, the radius, the fill colour, the line colour and the line width.

Because the picture is a description, you can change it by editing a property. If the radius of the circle is changed from 15 to 30, the program redraws a larger circle. To scale the whole picture to twice the size, the program multiplies every position and size by 2: the circle's centre (50, 35) becomes (100, 70) and its radius becomes 30. The result is drawn at the new size from the instructions, so **there is no loss of quality when a vector graphic is enlarged**. Enlarging a bitmap only makes each pixel bigger, so it looks blocky.

| | Bitmap | Vector graphic |
|---|---|---|
| Stored as | a grid of pixel colours | a drawing list of objects and their properties |
| Enlarging | blocky: loses quality | no loss: redrawn at the new size |
| File size | set by width × height × colour depth, however simple the picture | set by the number of objects; very small for a simple drawing |
| Editing | change individual pixels | change a whole object by editing a property |
| Best for | photographs and scanned pictures | logos, diagrams, maps, plans and text in fonts |
| Not suited to | pictures that must be enlarged without loss | photographs: far too many tiny objects would be needed |

:::eg Justify bitmap or vector
(a) A firm in Nairobi wants its logo, a simple shape of three colours, on business cards and on a large roadside sign. Which type of image should it use? (b) A photographer in Lima stores a photograph of a mountain. Which type should be used?

(a) Vector. [B1] The logo can be enlarged to the size of the sign with no loss of quality, because it is redrawn from its drawing list. [B1] The file is also small, because a simple logo needs only a few objects. [B1]

(b) Bitmap. [B1] A photograph has continuous changes of colour that would need millions of objects to describe. A grid of pixels records them directly. [B1]
:::

:::exam Justify means use the scenario
"Vector because it is better" earns nothing. "Vector, because the logo is printed at two very different sizes and a vector graphic does not lose quality when scaled" earns the mark. Always tie the property of the format (scaling, size, detail) to the facts in the question.
:::

## Sound

Sound is a wave of pressure in the air. Its size and speed change smoothly and continuously, so it is **analogue**: it can take any value, not just fixed steps. A computer can only store numbers, so a sound has to be turned into **digital** data, by measuring the wave again and again.

:::def Analogue data
Data that varies continuously and can take any value within a range, such as a sound wave.
:::

:::def Digital data
Data stored as a series of separate values, in a computer as binary numbers.
:::

:::def Sampling
Measuring the amplitude (height) of a sound wave at regular intervals and storing each measurement as a binary number, to turn an analogue sound into digital data.
:::

:::def Sampling rate
The number of samples taken each second, measured in hertz (Hz). A rate of 8000 Hz means 8000 samples per second.
:::

:::def Sampling resolution
The number of bits used to store each sample. It is also called bit depth, and it sets how many different levels can be recorded: \(n\) bits give \(2^n\) levels.
:::

A microphone converts the sound to a varying electrical signal, and an analogue-to-digital converter measures it at regular intervals. Playback reverses the process: a digital-to-analogue converter turns the stored numbers back into a signal for the speaker.

:::html
<figure class="fig small"><svg viewBox="0 0 340 222" role="img" aria-label="A smooth wave over one cycle, sampled twelve times at equal time intervals. The stored levels, on a scale from 0 to 7, are 4, 5, 7, 7, 7, 5, 4, 2, 0, 0, 0 and 2. The stepped line of stored levels follows the wave but is not smooth, because each sample is rounded to one of eight levels. A legend names the analogue wave, the sample points and the stored level."><line class="ax" x1="36" y1="22" x2="36" y2="160"/><line class="ax" x1="36" y1="160" x2="324" y2="160"/><text class="tl tc" x="36" y="14">level</text><text class="ts te" x="30" y="34">7</text><text class="ts te" x="30" y="154">0</text><text class="ts" x="294" y="174">time</text><polyline class="c1" fill="none" points="36.0,90.0 41.8,82.2 47.7,74.5 53.5,67.0 59.3,60.0 65.2,53.5 71.0,47.6 76.8,42.4 82.7,38.0 88.5,34.6 94.3,32.0 100.2,30.5 106.0,30.0 111.8,30.5 117.7,32.0 123.5,34.6 129.3,38.0 135.2,42.4 141.0,47.6 146.8,53.5 152.7,60.0 158.5,67.0 164.3,74.5 170.2,82.2 176.0,90.0 181.8,97.8 187.7,105.5 193.5,113.0 199.3,120.0 205.2,126.5 211.0,132.4 216.8,137.6 222.7,142.0 228.5,145.4 234.3,148.0 240.2,149.5 246.0,150.0 251.8,149.5 257.7,148.0 263.5,145.4 269.3,142.0 275.2,137.6 281.0,132.4 286.8,126.5 292.7,120.0 298.5,113.0 304.3,105.5 310.2,97.8 316.0,90.0"/><path class="c2 sw2" fill="none" d="M36.0,81.4 H59.3 V64.3 H82.7 V30.0 H106.0 V30.0 H129.3 V30.0 H152.7 V64.3 H176.0 V81.4 H199.3 V115.7 H222.7 V150.0 H246.0 V150.0 H269.3 V150.0 H292.7 V115.7 H316.0"/><circle class="fa" cx="36.0" cy="90.0" r="3.5"/><circle class="fa" cx="59.3" cy="60.0" r="3.5"/><circle class="fa" cx="82.7" cy="38.0" r="3.5"/><circle class="fa" cx="106.0" cy="30.0" r="3.5"/><circle class="fa" cx="129.3" cy="38.0" r="3.5"/><circle class="fa" cx="152.7" cy="60.0" r="3.5"/><circle class="fa" cx="176.0" cy="90.0" r="3.5"/><circle class="fa" cx="199.3" cy="120.0" r="3.5"/><circle class="fa" cx="222.7" cy="142.0" r="3.5"/><circle class="fa" cx="246.0" cy="150.0" r="3.5"/><circle class="fa" cx="269.3" cy="142.0" r="3.5"/><circle class="fa" cx="292.7" cy="120.0" r="3.5"/><line class="c1" x1="36" y1="188" x2="60" y2="188"/><text class="tl" x="68" y="192">analogue wave</text><circle class="fa" cx="48" cy="204" r="3.5"/><text class="tl" x="68" y="208">sample point</text><line class="c2 sw2" x1="186" y1="188" x2="210" y2="188"/><text class="tl" x="218" y="192">stored level</text></svg><figcaption>One cycle of a wave sampled 12 times, with a sampling resolution of 3 bits (8 levels, 0 to 7). The stored levels are 4, 5, 7, 7, 7, 5, 4, 2, 0, 0, 0, 2: close to the wave, but not exactly on it.</figcaption></figure>
:::

The figure shows both settings at work. The **sampling rate** decides how often the wave is measured, so a higher rate follows the wave more closely in time. The **sampling resolution** decides how finely each measurement is rounded: with only 8 levels the stored value is often a little different from the true height of the wave. A higher rate and a higher resolution both make the digital sound a truer copy of the original.

```python
import math

levels = []
for t in range(12):
    height = math.sin(2 * math.pi * t / 12)
    levels.append(round((height + 1) / 2 * 7))
print(levels)
```

Output:

```output
[4, 5, 7, 7, 7, 5, 4, 2, 0, 0, 0, 2]
```

This program takes 12 samples of one cycle of a sine wave, whose height runs from −1 to 1, and rounds each to one of the levels 0 to 7. It prints the stored levels of the figure.

### Sound file size

Each second holds `sampling rate` samples, and each sample takes `sampling resolution` bits.

:::key Sound file size
- Size in bits = sampling rate (Hz) × sampling resolution (bits) × time (seconds).
- For stereo, or any number of channels, multiply by the number of channels.
- Divide by 8 for bytes, then by 1024 for KiB, and so on. Ignore the header unless told.
:::

:::eg Calculating a sound file size
A voice message lasts 60 seconds, recorded in mono with a sampling rate of 8000 Hz and a sampling resolution of 16 bits. Calculate the file size in bytes and in KiB. How large would the file be in stereo?

Size in bits = \(8000 \times 16 \times 60\) [M1] \(= 7\,680\,000\) bits.

Size in bytes = \(7\,680\,000 \div 8 = 960\,000\) bytes. [A1]

In KiB: \(960\,000 \div 1024 = 937.5\) KiB. [B1]

Stereo has two channels, so the size doubles: \(1\,920\,000\) bytes. [B1]
:::

```python
def sound_size_bytes(rate, resolution, seconds, channels=1):
    return rate * resolution * seconds * channels // 8


size = sound_size_bytes(8000, 16, 60)
print(size, "bytes")
print(size / 1024, "KiB")
print(sound_size_bytes(8000, 16, 60, 2), "bytes in stereo")
```

Output:

```output
960000 bytes
937.5 KiB
1920000 bytes in stereo
```

### Effects of changing the rate and resolution

| Change | Effect on the sound | Effect on file size |
|---|---|---|
| Higher sampling rate | follows the wave more closely, so a more accurate sound and a wider range of high pitches | larger, in proportion |
| Lower sampling rate | less accurate; high-pitched sounds are lost | smaller |
| Higher sampling resolution | each sample is closer to the true height, so quieter details and smoother sound | larger, in proportion |
| Lower sampling resolution | more rounding error, heard as a rough or noisy sound | smaller |

The size is in proportion to each of the three numbers, so doubling the rate doubles the file, and doubling the rate and the resolution together makes it four times as large. Longer recordings and more channels also make bigger files.

:::warn Rate and resolution are different settings
The sampling rate is **how many** samples per second (Hz). The sampling resolution is **how many bits** each sample uses. A question about "accuracy" can mean either: say which one you are changing. Changing the rate affects accuracy along the time axis; changing the resolution affects accuracy up the amplitude axis.
:::

## Compression

The calculations above show how fast files grow. A 3-minute stereo recording at 44 100 Hz and 16 bits uses about 32 MB (31 752 000 bytes). Large files fill storage, take a long time to send and need more bandwidth to stream. **Compression** reduces the size of a file.

:::def Compression
Reducing the size of a file by encoding its data using fewer bits.
:::

Reasons for compressing a file:

- it uses less storage space, so more files fit on a device;
- it takes less time to send or download, and uses less bandwidth, so streaming is smoother;
- it costs less where data is paid for or limited, such as an email attachment or a mobile data plan.

There are two kinds, and the difference is whether the original can be rebuilt exactly.

:::def Lossless compression
Compression in which no data is lost, so the original file can be rebuilt exactly from the compressed file.
:::

:::def Lossy compression
Compression that permanently removes some of the data, so the original cannot be rebuilt exactly. The data removed is chosen so that the loss is unlikely to be noticed.
:::

| | Lossless | Lossy |
|---|---|---|
| Original data | rebuilt exactly | some data is lost for ever |
| Compressed size | larger than with lossy | smaller, often much smaller |
| Quality | no change | lower, more so with more compression |
| Use when | every bit matters: text, programs, spreadsheets, medical or legal images, a file to be edited again | a small loss is acceptable: photographs on a web page, music or video for streaming |

### Compressing each kind of file

| File type | Lossless methods | Lossy methods |
|---|---|---|
| Text | run-length encoding where there are runs of the same character; replacing repeated words or patterns with shorter codes held in a dictionary | not suitable: changing any character changes the text |
| Bitmap image | run-length encoding (works well where there are large areas of one colour) | reducing the colour depth; reducing the resolution; removing fine detail that the eye does not notice (for example JPEG) |
| Vector graphic | a drawing list is small, and the file can also be compressed as text | rarely used |
| Sound | lossless methods that rebuild every sample | reducing the sampling rate or resolution; removing sounds that people are unlikely to hear, such as very high or very low pitches or quiet sounds masked by louder ones (for example MP3) |

Notice that the decision follows from the data. Text and programs must be lossless, because a program with a changed instruction, or a spreadsheet with one changed digit, is wrong. Pictures and sound can lose detail that people cannot see or hear.

:::eg Choosing lossy or lossless
(a) A music app in Cape Town streams songs to phones. (b) A clinic in Accra stores a spreadsheet of patient records. Say which type of compression each should use, with a reason.

(a) Lossy. [B1] The files are much smaller, so they download faster and stream without stopping, and the lost detail is unlikely to be heard on a phone. [B1]

(b) Lossless. [B1] Any lost or changed data would make the records wrong, so the original must be rebuilt exactly. [B1]
:::

### Run-length encoding (RLE)

Many files contain **runs**: the same value repeated many times in a row, such as a patch of blue sky in a picture. Run-length encoding stores each run as a count and the value, instead of repeating the value.

:::def Run-length encoding (RLE)
A lossless compression method that replaces each run of identical values by a count of the run followed by the value, so that the run is stored once.
:::

For example, the row of pixels WWWWWWWBBBBBWWWW (W = white, B = black) has 16 pixels. It has three runs: 7 white, 5 black and 4 white, so the RLE is 7W 5B 4W. To decode, repeat each value by its count and join them: the original appears exactly, so RLE is lossless.

:::html
<figure class="fig small"><svg viewBox="0 0 330 170" role="img" aria-label="A grid of 12 columns and 5 rows of pixels. Rows 1 and 5 are all light. Rows 2 and 4 have four light pixels, four dark pixels and four light pixels. Row 3 has two light pixels, eight dark pixels and two light pixels. The run-length encoding of each row is written beside it: 12L, 4L 4D 4L, 2L 8D 2L, 4L 4D 4L and 12L."><text class="tl ti" x="14" y="16">12 × 5 pixel image</text><text class="tl ti" x="242" y="16">RLE</text><rect class="fm s-acc" x="14" y="30" width="216" height="90"/><rect class="fa s-acc" x="86" y="48" width="72" height="18"/><rect class="fa s-acc" x="50" y="66" width="144" height="18"/><rect class="fa s-acc" x="86" y="84" width="72" height="18"/><line class="ln-m thin" x1="32" y1="30" x2="32" y2="120"/><line class="ln-m thin" x1="50" y1="30" x2="50" y2="120"/><line class="ln-m thin" x1="68" y1="30" x2="68" y2="120"/><line class="ln-m thin" x1="86" y1="30" x2="86" y2="120"/><line class="ln-m thin" x1="104" y1="30" x2="104" y2="120"/><line class="ln-m thin" x1="122" y1="30" x2="122" y2="120"/><line class="ln-m thin" x1="140" y1="30" x2="140" y2="120"/><line class="ln-m thin" x1="158" y1="30" x2="158" y2="120"/><line class="ln-m thin" x1="176" y1="30" x2="176" y2="120"/><line class="ln-m thin" x1="194" y1="30" x2="194" y2="120"/><line class="ln-m thin" x1="212" y1="30" x2="212" y2="120"/><line class="ln-m thin" x1="14" y1="48" x2="230" y2="48"/><line class="ln-m thin" x1="14" y1="66" x2="230" y2="66"/><line class="ln-m thin" x1="14" y1="84" x2="230" y2="84"/><line class="ln-m thin" x1="14" y1="102" x2="230" y2="102"/><text class="tl" x="242" y="43">12L</text><text class="tl" x="242" y="61">4L 4D 4L</text><text class="tl" x="242" y="79">2L 8D 2L</text><text class="tl" x="242" y="97">4L 4D 4L</text><text class="tl" x="242" y="115">12L</text><text class="tl" x="14" y="142">L = light pixel, D = dark pixel</text><text class="tl" x="14" y="160">Each row is encoded on its own.</text></svg><figcaption>A 12 × 5 image and the RLE of each row. Long runs, such as 12 light pixels in one row, shrink to a count and a value.</figcaption></figure>
:::

```python
def rle_encode(data):
    runs = []
    for item in data:
        if runs and runs[-1][1] == item:
            runs[-1][0] = runs[-1][0] + 1
        else:
            runs.append([1, item])
    return runs


def rle_decode(runs):
    data = ""
    for count, item in runs:
        data = data + item * count
    return data


row = "WWWWWWWBBBBBWWWW"
runs = rle_encode(row)
print(runs)
print("".join(str(count) + item for count, item in runs))
print(rle_decode(runs) == row)
print(rle_encode("ABCD"))
```

Output:

```output
[[7, 'W'], [5, 'B'], [4, 'W']]
7W5B4W
True
[[1, 'A'], [1, 'B'], [1, 'C'], [1, 'D']]
```

The encoder walks along the data. If the item matches the last run, it adds 1 to that run's count; otherwise it starts a new run. The decoder repeats each item by its count. The last line shows the weakness: with no runs, every item becomes its own run with a count of 1.

### When RLE saves space, and when it does not

To judge the saving, count bits. Suppose each run is stored as a count of 8 bits followed by the pixel colour, and the picture has a colour depth of 8 bits. Then each run takes \(8 + 8 = 16\) bits.

- The 12 × 5 image in the figure, stored in 8-bit colour, takes \(60 \times 8 = 480\) bits without compression. It has 11 runs, so with RLE it takes \(11 \times 16 = 176\) bits, which is about 37% of the original size.
- A row of 16 pixels that alternate in colour has no runs longer than 1. Without compression it takes \(16 \times 8 = 128\) bits. With RLE there are 16 runs, so \(16 \times 16 = 256\) bits: **the compressed file is twice as large**.

:::warn RLE can make a file bigger
RLE only helps when there are long runs. It suits a cartoon, a diagram or a scan of a page, with large areas of one colour. It does not suit a photograph, where neighbouring pixels almost always differ a little, nor ordinary text, where most letters do not repeat. Say "RLE works best on data with long runs of repeated values".
:::

:::eg RLE on text
(a) Apply RLE to the text AAAABBBCCD. (b) Decode 3X1Y4Z. (c) State what happens if RLE is used on the text ABCD.

(a) The runs are 4 A, 3 B, 2 C and 1 D, so the code is **4A3B2C1D**. [B1] (This has 8 characters, saved from 10.) [B1]

(b) Three X, one Y, four Z: **XXXYZZZZ**. [B1]

(c) Each letter is a run of 1, so the code is 1A1B1C1D: twice as long as the original. [B1]
:::

### Dictionary compression for text

Real text repeats words and phrases, not single characters. A dictionary method finds repeated patterns, stores each once in a table (the dictionary), and replaces each occurrence by a short code. To read the file again, the codes are looked up in the dictionary, so it is lossless. For example, with the dictionary 1 = "to" and 2 = "be", the message "to be or not to be" is stored as "1 2 or not 1 2". The dictionary has to be stored with the file, so the saving is only worthwhile when the patterns repeat often enough.

:::eg Spot the error: bitmap file size
Question: A bitmap image is 800 pixels wide and 600 pixels high, with a colour depth of 24 bits. Calculate its file size in KiB, ignoring the header. [3 marks]

A student wrote:

```text
01  800 × 600 × 24 = 11 520 000
02  11 520 000 ÷ 1024 = 11 250 KiB
```

Line 01 multiplies width, height and colour depth correctly [M1]. **Line 02 divides by 1024 and never divides by 8**: 11 520 000 is a number of **bits**, so the answer is 8 times too large [M0]. The final answer is therefore wrong [A0]. The answer scores 1 out of 3.

The correct working: \(11\,520\,000 \div 8 = 1\,440\,000\) bytes, and \(1\,440\,000 \div 1024 = 1406.25\) KiB.
:::

:::eg Spot the error: run-length encoding
Question: Show the run-length encoding of AAABBBBCCA. [4 marks]

A student wrote: `3A4B2C`.

The run of three A is correct [B1], the run of four B is correct [B1] and the run of two C is correct [B1]. **The final A is a run of 1 that the student has left out** [B0]. The student has stopped at the last run that repeats, and has forgotten that a single value is a run of length 1. The answer scores 3 out of 4. The correct code is 3A4B2C1A. Decoding is a good check: the student's code gives AAABBBBCC, with one letter fewer than the original.
:::

:::try Start easy, finish at exam standard
Q: How many colours can be shown with a colour depth of 5 bits? How many bits are needed for 100 colours?
A: \(2^5 = 32\) colours. For 100 colours, \(2^6 = 64\) is too few and \(2^7 = 128\) is enough, so 7 bits.
Q: A 100 × 50 image has a colour depth of 1 bit. Find the size of its pixel data in bits and in bytes.
A: \(100 \times 50 \times 1 = 5000\) bits, and \(5000 \div 8 = 625\) bytes.
Q: A 4 × 4 image has a colour depth of 3 bits. How many bytes of pixel data are there?
A: \(4 \times 4 \times 3 = 48\) bits, which is \(48 \div 8 = 6\) bytes.
Q: A screen shows 1920 × 1080 pixels. How many pixels is that?
A: \(1920 \times 1080 = 2\,073\,600\) pixels. (\(1920 \times 1000 = 1\,920\,000\) and \(1920 \times 80 = 153\,600\).)
Q: A sound is recorded at 10 000 Hz with 8 bits per sample for 5 seconds, in mono. Find the size in bytes.
A: \(10\,000 \times 8 \times 5 = 400\,000\) bits, and \(400\,000 \div 8 = 50\,000\) bytes.
Q: The sampling rate and the sampling resolution of a recording are both doubled. What happens to the file size?
A: Each doubling doubles the size, so together the file is \(2 \times 2 = 4\) times as large.
Q: Give the RLE of AAAAABBC and decode 2X3Y1Z.
A: 5A2B1C. And 2X3Y1Z gives XXYYYZ.
Q: Say whether a bitmap or a vector graphic suits each: (a) a photograph of a street, (b) a plan of a house to be printed at several sizes.
A: (a) Bitmap: a photograph has continuous detail that a pixel grid records directly. (b) Vector: the plan is made of lines that can be redrawn at any size without loss.
Q: Say whether lossy or lossless compression suits each: (a) a legal contract stored as text, (b) a holiday photograph on a web page, (c) a program file.
A: (a) Lossless: no character may change. (b) Lossy: smaller and the loss is hard to see. (c) Lossless: a changed instruction would make the program wrong.
Q: A circle in a drawing list has centre (20, 30) and radius 10. The picture is enlarged to three times its size. State the new centre and radius.
A: Multiply every position and size by 3: the centre is (60, 90) and the radius is 30. No quality is lost.
Q: Define the term sampling rate, and say what its unit is.
A: The number of samples of a sound wave taken each second. Its unit is the hertz (Hz).
Q: State what a file header holds for a bitmap, giving two items.
A: For example the width and height in pixels, the colour depth and the file type. Any two.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ State the meaning of each of these terms: (a) pixel, (b) colour depth, (c) file header.
A: (a) The smallest single point (element) of a bitmap image, with one colour. [B1]

(b) The number of bits used to store the colour of each pixel. [B1]

(c) Data at the start of a file that describes it, such as the width, height and colour depth of an image. [B1]

Q: [4 marks] ★ A photograph is 1280 pixels wide and 720 pixels high, with a colour depth of 8 bits. (a) Calculate its file size in bytes, ignoring the header. [2] (b) Give the size in KiB. [1] (c) State the effect on the size of doubling the colour depth. [1]
H: Bits first, then divide by 8.
A: (a) \(1280 \times 720 \times 8\) bits [M1] \(= 7\,372\,800\) bits \(= 921\,600\) bytes. [A1]

(b) \(921\,600 \div 1024 = 900\) KiB. [B1]

(c) The file size doubles (to 1800 KiB). [B1]

Q: [5 marks] ★★ A school in Sydney scans its old photographs as bitmap images. (a) State two items of data that are stored in the file header of a bitmap. [2] (b) Explain the difference between image resolution and screen resolution. [2] (c) State one effect on quality of reducing the image resolution. [1]
A: (a) Any two of: the width in pixels; the height in pixels; the colour depth; the file type. [B1] [B1]

(b) Image resolution is the number of pixels in the image (width × height). [B1] Screen resolution is the number of pixels the screen can display. [B1]

(c) There is less detail, so the image looks blocky when it is enlarged. [B1]

Q: [6 marks] ★★ A radio station in Lagos records a 20 second speech clip in mono, with a sampling rate of 16 000 Hz and a sampling resolution of 8 bits. (a) State what is meant by sampling rate. [1] (b) Calculate the file size in bytes, ignoring the header. [2] (c) Give the size in KiB. [1] (d) State the effect on accuracy and on file size of doubling the sampling resolution. [2]
H: Rate × resolution × seconds, then ÷ 8.
A: (a) The number of samples of the sound taken each second (measured in Hz). [B1]

(b) \(16\,000 \times 8 \times 20\) bits [M1] \(= 2\,560\,000\) bits \(= 320\,000\) bytes. [A1]

(c) \(320\,000 \div 1024 = 312.5\) KiB. [B1]

(d) Each sample is stored more accurately (a truer copy of the sound). [B1] The file size doubles. [B1]

Q: [4 marks] ★★ (a) A row of pixels is WWWWBBWWWWWWWWBB (W = white, B = black). Show its run-length encoding. [2] (b) Decode 3R5G4R into the pixels it represents. [1] (c) State one disadvantage of run-length encoding. [1]
A: (a) The runs are 4 W, 2 B, 8 W and 2 B, so the code is 4W2B8W2B. [B1] [B1] (one mark for the first two runs correct, one for all four)

(b) RRRGGGGGRRRR. [B1]

(c) If there are few or no runs (neighbouring values differ) the encoded data can be larger than the original. [B1]

Q: [5 marks] ★★ A company stores its logo as a vector graphic. (a) Explain what is stored in the drawing list. [2] (b) Give one property of a circle in the drawing list. [1] (c) Explain why a vector graphic suits the logo when it is printed at different sizes. [1] (d) Explain why a vector graphic does not suit a photograph. [1]
A: (a) Each drawing object (shape) in the image [B1] together with the properties of each, such as its position, size and colours. [B1]

(b) Any one of: centre, radius, fill colour, line colour, line width. [B1]

(c) It is redrawn at the new size from the drawing list, so there is no loss of quality. [B1]

(d) A photograph has continuous detail that would need an enormous number of objects to describe. [B1]

Q: [8 marks] ★★★ A film company in Mumbai streams films to customers and stores its accounts in spreadsheet files. (a) Describe the difference between lossy and lossless compression. [2] (b) Justify the use of lossy compression for the streamed films. [2] (c) Justify the use of lossless compression for the spreadsheets. [2] (d) Describe how lossy compression can reduce the size of a sound file. [2]
H: Use the words of the scenario in (b) and (c): "streamed" and "accounts".
A: (a) Lossless compression keeps all the data, so the original can be rebuilt exactly. [B1] Lossy compression permanently removes some data, so the original cannot be rebuilt. [B1]

(b) The files are much smaller, so they can be sent over the internet quickly and played without stopping. [B1] Viewers are unlikely to notice the small loss in quality. [B1]

(c) Every digit in the accounts must be exact, so no data can be lost. [B1] A change to one number would make the accounts wrong, so the original must be rebuilt exactly. [B1]

(d) Reduce the sampling rate or the sampling resolution, so there are fewer bits per second. [B1] Remove the sounds that people are unlikely to hear (for example very high pitches, or quiet sounds masked by louder ones). [B1]

Q: [8 marks] ★★★ An architect in Nairobi stores a bitmap plan with an image resolution of 2048 × 1024 pixels and a colour depth of 4 bits. (a) State the number of colours the image can show. [1] (b) Calculate the file size in MiB, ignoring the header. [3] (c) The width and the height are both halved. Calculate the new file size in KiB. [2] (d) Explain why this reduces the quality of the image. [1] (e) Explain why RLE suits a plan made mostly of white areas. [1]
H: \(2048 = 2^{11}\) and \(1024 = 2^{10}\): work with powers of 2.
A: (a) \(2^4 = 16\) colours. [B1]

(b) \(2048 \times 1024 \times 4 = 8\,388\,608\) bits [M1] \(= 1\,048\,576\) bytes [A1] \(= 1\) MiB. [A1]

(c) The new image is 1024 × 512, with a quarter of the pixels, so \(1024 \div 4 = 256\) KiB. [B1] [B1] (one mark for 1024 × 512 or a quarter of the pixels, one for 256 KiB)

(d) There are fewer pixels, so less detail is stored and the image looks blocky when it is enlarged. [B1]

(e) White areas make long runs of identical pixels, which RLE stores as one count and one value each. [B1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ A 1-bit image row has 64 pixels: the first 40 are white and the last 24 are black. RLE stores each run as an 8-bit count followed by the 1-bit colour. (a) Calculate the size of the row without compression and with RLE. [2] (b) Another row of 64 pixels alternates white, black, white, black and so on. Calculate the size of this row with RLE, and state how many times larger it is than without compression. [2] (c) State the conclusion about when RLE is worthwhile. [1]
H: Each run takes 9 bits.
H: In (b), how many runs are there?
A: (a) Without compression the row is 64 bits. [B1] With RLE there are 2 runs of 9 bits, which is 18 bits. [B1]

(b) The row has 64 runs of 9 bits each: \(64 \times 9 = 576\) bits [B1], which is \(576 \div 64 = 9\) times larger than 64 bits. [B1]

(c) RLE is worthwhile only when runs are long compared with the bits needed to store a count; with short runs the compressed data can be larger. [B1]

Q: [5 marks] ★★★ A student says: "I can keep a recording the same size by doubling the sampling rate and halving the sampling resolution." (a) Show that the file size stays the same. [2] (b) Explain why the recording is nevertheless not the same quality. [3]
H: Think about what each setting controls: when the wave is measured, or how finely it is measured.
A: (a) Size = rate × resolution × time. [B1] Doubling the rate and halving the resolution multiplies the size by \(2 \times \tfrac12 = 1\), so the size is unchanged. [B1]

(b) The doubled rate means the wave is measured twice as often, so quick changes in the sound are followed more closely. [B1] The halved resolution means each sample is rounded to far fewer levels, \(2^{n}\) become \(2^{n-1}\), so there is more rounding error. [B1] The two effects are different and do not cancel: the result is a different mix of accuracy in time and accuracy in loudness. [B1]
:::

:::quiz
? A bitmap image has a colour depth of 8 bits. How many different colours can each pixel have?
- 8
+ 256
- 64
- 1024
> \(2^8 = 256\). Eight is the number of bits, not the number of colours.
? An image is 100 pixels wide and 50 pixels high and has a colour depth of 2 bits. What is the size of the pixel data in bytes?
- 10 000
- 5000
+ 1250
- 625
> \(100 \times 50 \times 2 = 10\,000\) bits, and \(10\,000 \div 8 = 1250\) bytes. The answer 10 000 forgets to divide by 8.
? What is the effect of halving both the width and the height of a bitmap image, with the colour depth unchanged?
- The file size is halved.
+ The file size is a quarter of what it was.
- The file size is unchanged.
- The file size is doubled.
> The number of pixels is \(\tfrac12 \times \tfrac12 = \tfrac14\) of the original, so the size is a quarter.
? Why does a vector graphic not lose quality when it is enlarged?
- Because each pixel is stored in more bits.
- Because vector graphics are compressed.
+ Because the image is redrawn from its drawing list at the new size.
- Because vector graphics have a higher colour depth.
> A vector graphic is a set of instructions, not a grid of pixels, so the shapes are recalculated and redrawn at any size.
? A sound is recorded at 8000 Hz with 16 bits per sample. How many bits are stored per second in mono?
- 8000
+ 128 000
- 16 000
- 24 000
> \(8000 \times 16 = 128\,000\) bits each second. 8000 is the rate alone, without the 16 bits of each sample; 16 000 and 24 000 do not multiply the rate by the resolution.
? What does a higher sampling rate do?
- It stores each sample with more bits.
+ It takes more samples each second, so the sound is a closer copy and the file is larger.
- It makes the file smaller.
- It removes sounds that cannot be heard.
> The sampling rate is the number of samples per second. The number of bits per sample is the sampling resolution.
? Which method is lossless?
- Reducing the colour depth of an image.
+ Run-length encoding.
- Removing sounds too quiet to hear.
- Reducing the sampling rate of a recording.
> RLE can be reversed to give the exact original. The other three remove data that cannot be recovered.
? The text of a school report must be compressed. Which type is suitable, and why?
- Lossy, because the text is small.
+ Lossless, because the original text must be rebuilt exactly.
- Lossy, because no one notices a changed letter.
- Neither: text cannot be compressed.
> Changing characters changes the meaning, so text needs lossless compression. Methods such as RLE and dictionary coding work on text.
:::

:::checklist What you can now do
- [ ] I can explain how a bitmap image is stored, using the terms pixel, image resolution, screen resolution, colour depth and file header.
- [ ] I can calculate a bitmap file size in bits, bytes, KiB and MiB, by hand.
- [ ] I can explain the effect of changing the resolution or colour depth on quality and size.
- [ ] I can describe a vector graphic using the terms drawing object, property and drawing list.
- [ ] I can justify the use of a bitmap or a vector graphic in a given situation.
- [ ] I can explain how sound is sampled, using the terms analogue, digital, sampling rate and sampling resolution.
- [ ] I can calculate the size of a sound file, by hand.
- [ ] I can explain the effect of changing the sampling rate or the sampling resolution on size and accuracy.
- [ ] I can explain why files are compressed, and describe lossy and lossless compression.
- [ ] I can justify lossy or lossless compression for a given file, and describe how text, bitmap, vector and sound files can be compressed.
- [ ] I can encode and decode with run-length encoding, and say when it does not help.
:::

:::recap
- A bitmap is a grid of pixels; colour depth is bits per pixel, giving \(2^n\) colours. The header stores the width, height and colour depth.
- Bitmap size in bits = width × height × colour depth. Divide by 8 for bytes, then by 1024 for KiB. Halving both dimensions gives a quarter of the size.
- A vector graphic is a drawing list: objects with properties. It scales with no loss and suits logos, diagrams and plans; photographs need bitmaps.
- Sound is analogue; sampling measures it at regular intervals. Sampling rate is samples per second (Hz); sampling resolution is bits per sample.
- Sound size in bits = rate × resolution × seconds (× channels). Higher rate or resolution: more accurate, bigger file.
- Compression makes files smaller: less storage, faster transfer, less bandwidth.
- Lossless keeps every bit (text, programs, spreadsheets). Lossy removes data nobody is likely to notice (photos, music, video).
- RLE stores runs as count and value (WWWBB is 3W2B). It is lossless, works well on long runs and makes data bigger when there are none.
:::

:::links
- practise: [Multimedia: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/1-information-representation/multimedia/exam-questions/) · Save My Exams · 9618-style questions on images and sound with mark schemes [paid]
- practise: [Compression: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/1-information-representation/compression/exam-questions/) · Save My Exams · lossy, lossless and RLE questions with mark schemes [paid]
- read: [Bits, bytes and the internet](https://www.khanacademy.org/computing/computers-and-internet) · Khan Academy · free lessons on how images and sound become bits
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos by university computer scientists, including on compression and images

Links checked 13 November 2026.
:::

Next: [Networks: models, topologies and hardware](#cs.networks)
