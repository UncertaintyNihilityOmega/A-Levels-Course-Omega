@chapter cs.security2
@title Encryption, SSL/TLS and digital certificates
@level a2
@paper CAIE 9618 Paper 3
@time 4–6 hours
@summary How symmetric and asymmetric encryption work, how public and private keys give confidentiality and digital signatures, how a digital certificate lets you trust a public key, how SSL/TLS protects a client-server session, and what quantum cryptography offers.

:::why
Every time you log in to a school portal, pay for a bus ticket on a phone or send a message in a chat app, your data crosses networks that strangers can listen to. Encryption is what makes that safe. Paper 3 asks you to explain which key does what, how a digital signature is made and checked, why a certificate is needed, and how a secure web session is set up. The same few ideas answer all of these questions, so the topic rewards a clear picture more than memorised lists.
:::

**Before you start**, you should know why data needs protecting and what encryption is from [Security, privacy and data integrity](#cs.security), and how a browser talks to a server from [The internet: IP addresses, DNS and streaming](#cs.internet).

:::try Warm-up
Q: What is encryption, and does it stop a criminal from intercepting data? (from [Security, privacy and data integrity](#cs.security))
A: Encryption scrambles data using a key so that it cannot be understood without the right key. It does not stop interception, but what the criminal gets is unreadable.
Q: What does `https` at the start of a web address mean, compared with `http`? (from [The internet: IP addresses, DNS and streaming](#cs.internet))
A: HTTPS is HTTP with encryption, so the data sent between the browser and the web server is encrypted.
Q: What is `17 MOD 5`? (from [Programming from zero: Python and pseudocode](#cs.f.basics))
A: 2. Seventeen divided by 5 is 3 remainder 2, and MOD gives the remainder.
:::

## Plain text, cipher text and keys

Encryption means changing data into a form that only the right person can read. A few words describe every part of the process, and an exam answer needs them exactly.

:::def Plain text
Data in its original, readable form, before it is encrypted. It is also called plaintext.
:::

:::def Cipher text
The unreadable data that is produced when plain text is encrypted. It is also called ciphertext.
:::

:::def Encryption
The process of converting plain text into cipher text using an algorithm and a key, so that the data cannot be understood by anyone who does not have the right key. Turning the cipher text back into plain text is called decryption.
:::

:::def Key
A value, usually a long string of bits, that the encryption algorithm uses to turn plain text into cipher text (and back). Without the right key, the cipher text cannot be decrypted.
:::

The algorithm is not secret: everyone can read how the standard methods work. The key is the secret. Security depends on the length of the key, because a key of \(n\) bits has \(2^n\) possible values and an attacker who does not know the key must try them. An 8-bit key has \(2^8 = 256\) values and a 16-bit key has \(2^{16} = 65\,536\). Each extra bit doubles the number of keys to try. Keys in real use are 128 bits or more, and \(2^{128}\) is a number with 39 digits, which is why trying every key is not realistic.

:::key The pattern of every encryption
- plain text + encryption algorithm + key \(\rightarrow\) cipher text
- cipher text + decryption algorithm + the right key \(\rightarrow\) plain text
- The two big families differ in how many keys there are and who holds them: **symmetric** (one shared key) and **asymmetric** (a pair of keys).
:::

## Symmetric encryption

:::def Symmetric encryption
Encryption in which the same secret key is used to encrypt the plain text and to decrypt the cipher text.
:::

Think of a padlocked box with one key. You lock the box and post it. The person who receives it can open it only if they already have a copy of the same key.

The program below is a tiny symmetric cipher. It combines each byte of the message with a byte of the key using XOR (the logic operation from [Logic gates and logic circuits](#cs.logic)), repeating the key as needed. XOR has a useful property: doing it twice with the same value gives back the original, so the same function and the same key both encrypt and decrypt.

A note on the Python (an optional check, not examined here): `b"..."` is a string of bytes rather than of characters, `^` is XOR in Python (the same operation as the XOR gate, applied to every bit of two bytes), `enumerate(data)` gives each byte together with its position `i` so that the key can be repeated with `i % len(key)`, and `.hex()` shows a row of bytes as hexadecimal digits so that you can read it.

:::warn A toy, not a secure cipher
This cipher, and the others in this chapter's Python programs, are written to show an idea. They are not secure: never use them to protect real data. Real systems use standard, carefully tested algorithms.
:::

```python
def xor_cipher(data, key):
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


plain_text = b"MEET AT NOON"
key = b"K7"
cipher_text = xor_cipher(plain_text, key)
print(cipher_text.hex())
print(xor_cipher(cipher_text, key))
```

Output:

```output
06720e636b761f1705780479
b'MEET AT NOON'
```

The cipher text is shown in hexadecimal because most of its bytes are not printable characters. Running the same function again with the same key returns the plain text.

**Benefits of symmetric encryption.** It is fast and needs little processing, so it suits large amounts of data such as whole files, video and a long web session. The algorithms are simple and well understood.

**Drawbacks.** There is a **key distribution problem**: before two people can communicate securely, they must both have the key, and the key must reach the other person without anyone else seeing it. If you send the key over the network that you are trying to protect, an eavesdropper has it too. There is also a **key management problem**: every pair of people who want private communication needs their own key. For \(n\) people, that is

\[
\frac{n(n - 1)}{2} \text{ keys},
\]

so 10 people need \(\frac{10 \times 9}{2} = 45\) keys, and a company of 40 needs 780. The number grows much faster than the number of people.

## Asymmetric encryption

Asymmetric encryption solves the key distribution problem by using two different keys that belong together.

:::def Asymmetric encryption
Encryption that uses a pair of related keys: a public key and a private key. Data encrypted with one key of the pair can be decrypted only with the other key of the pair.
:::

:::def Public key
The key of a pair that its owner publishes, so that anyone can have it. It is used by other people to encrypt messages for the owner, or by anyone to check the owner's digital signature.
:::

:::def Private key
The key of a pair that its owner keeps secret and never shares. It is used by the owner to decrypt messages sent to them, and to create their digital signature.
:::

The two keys are linked by mathematics, but knowing the public key does not let you work out the private key in any realistic time. This is the whole idea: a public key can be given to the entire world, because it can only lock, and the private key stays with its owner, because it is the only thing that can unlock.

:::analogy
A public key is like an open padlock that you hand out freely. Anyone can snap it shut on a box addressed to you, but only your private key opens it. Handing out padlocks costs nothing, because no copy of the opening key ever leaves your pocket.
:::

### Sending a private message to a person or organisation

This is what happens when a customer sends confidential details to a bank.

:::steps
1. The bank creates a key pair and publishes its **public** key. It keeps its **private** key secret.
2. The customer's software gets the bank's public key.
3. The customer's software encrypts the message (the plain text) with the **bank's public key**. The result is cipher text.
4. The cipher text is sent across the network. Anyone who intercepts it sees only cipher text.
5. The bank decrypts the cipher text with its own **private key**. Only the bank holds that key, so only the bank can read the message.
:::

Nothing secret had to be shared beforehand. The customer never needs the bank's private key, and the bank never needs anything from the customer to read the message.

:::key Which key does what
- To send a **private** message to Priya: encrypt with **Priya's public key**. Priya decrypts with **Priya's private key**.
- To send a **verified** message that everyone can check came from you: use **your private key** to sign (next section). The receiver uses **your public key** to check.
- A private key is never sent to anyone, never put in a certificate and never needed by the sender of a message.
:::

The program below shows the idea with a tiny pair of keys. It is an RSA-style toy: the numbers are tiny so that you can follow them, and the real thing uses keys with hundreds of digits. The arithmetic is not examined. What matters is the pattern: the public key \((e, n)\) encrypts, the private key \((d, n)\) decrypts, and a wrong key gives rubbish.

```python
p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17
d = pow(e, -1, phi)
print("n =", n, " e =", e, " d =", d)

message = "HI"
codes = [ord(letter) for letter in message]
cipher = [pow(code, e, n) for code in codes]
print("cipher text:", cipher)
print("decrypted:", "".join(chr(pow(c, d, n)) for c in cipher))
print("wrong key:", [pow(c, 2753 + 2, n) for c in cipher])
```

Output:

```output
n = 3233  e = 17  d = 2753
cipher text: [3000, 1486]
decrypted: HI
wrong key: [111, 928]
```

Each letter's code is raised to a power and reduced with a remainder (`pow(code, e, n)` is \(\text{code}^e \bmod n\)). The public key \((17, 3233)\) turns `H` and `I` into 3000 and 1486. The private key \((2753, 3233)\) turns them back. A key that is only slightly wrong, 2755, gives 111 and 928, which are not the original letters.

:::eg Sending a confidential message (exam style)
A laboratory in Nairobi must send test results to a clinic over the internet, and nobody else must be able to read them. Explain how the laboratory can do this using asymmetric encryption. [4 marks]

Name the key pair, say who holds each key, and say which key encrypts and which decrypts.

- The clinic has a key pair, a public key and a private key. [B1]
- The clinic's public key is given to the laboratory, and the clinic keeps its private key secret. [B1]
- The laboratory encrypts the results with the clinic's public key and sends the cipher text. [B1]
- The clinic decrypts it with its private key, which only the clinic has, so anyone who intercepts the cipher text cannot read it. [B1]
:::

### Symmetric and asymmetric compared

:::cols
:::col Symmetric
- One key, shared by both people.
- Fast: suits large amounts of data.
- The key must be sent securely first (key distribution problem).
- Many keys are needed for many pairs of people.
:::
:::col Asymmetric
- Two keys: public (shared) and private (secret).
- Slower, because the calculations are heavier: used for small amounts of data such as keys and digests.
- No secret has to be shared in advance: only the public key is given out.
- Each person needs just one key pair.
:::
:::

You will see below that real systems use **both**: asymmetric encryption to set up a connection and swap a key, then symmetric encryption for the bulk of the data.

:::warn Do not mix up the keys
"The public key decrypts a message that was encrypted with the public key" is wrong. A message encrypted with a public key can be decrypted only with the matching private key. If one key could decrypt what it had just encrypted, anyone who knew the public key could read the secret message.
:::

## Hashing and message digests

Before you can understand a digital signature you need one more tool.

:::def Hash function
A function that takes data of any length and produces a value of fixed length from it. The same data always gives the same value, and it is not realistic to work out the original data from the value.
:::

:::def Message digest
The fixed-length value produced by applying a hash function to a message. It is also called a hash value or hash. It acts like a fingerprint of the message.
:::

A good hash function has these properties.

- **Fixed length.** A one-line message and a whole book both give a digest of the same size.
- **Repeatable.** The same message always gives the same digest.
- **Sensitive.** Changing one character gives a completely different digest.
- **One-way.** You cannot work backwards from the digest to the message.

```python
import hashlib


def digest(message):
    return hashlib.sha256(message.encode()).hexdigest()


first = digest("Pay Ana 100")
print(first[:16])
print(digest("Pay Ana 900")[:16])
print(first == digest("Pay Ana 100"))
print(len(first), "hex digits,", len(first) * 4, "bits")
print(len(digest("x" * 10000)), "hex digits")
```

Output:

```output
ecd0d31ecc3e04e0
2173670831b6a35b
True
64 hex digits, 256 bits
64 hex digits
```

Only the first 16 of the 64 hexadecimal digits are printed. Changing `100` to `900` changed the digest completely, the same message gave the same digest, and a message of ten thousand characters gave a digest of the same 256 bits.

:::warn Hashing is not encryption
Encryption uses a key and can be reversed by the key's owner. A hash uses no key and cannot be reversed. A digest cannot be turned back into the message, and its purpose is to check that a message has not changed.
:::

## Digital signatures

Here the pair of keys is used the other way round from the last section: the private key **encrypts** (signs) and the public key **decrypts** (checks). Either key of a pair can undo what the other did; what makes a signature work is that only the owner holds the private key, so only the owner can produce a value that the public key will unlock.

Encrypting with a public key gives a **private** message. A digital signature does something else: it proves **who** sent a message and that it has **not been changed**. It is how a verified message is sent to the public, for example a ministry that publishes an official notice which anyone can check.

:::def Digital signature
A value produced by encrypting the digest of a message with the sender's private key. Anyone with the sender's public key can use it to check that the message came from the sender and has not been changed.
:::

:::key Producing and checking a digital signature
Sender:
1. Apply a hash function to the message to produce a digest.
2. Encrypt the digest with the **sender's private key**. The result is the digital signature.
3. Send the message together with the signature.

Receiver:
4. Decrypt the signature with the **sender's public key** to recover the digest (Digest 2).
5. Apply the same hash function to the message that arrived to produce a digest (Digest 1).
6. Compare the two. If they are the same, the message is genuine and unchanged. If they are different, the message was changed or did not come from the sender, and must not be trusted.
:::

:::html
<figure class="fig"><svg viewBox="0 0 600 270" role="img" aria-label="Producing and checking a digital signature. Sender row: the message goes through a hash function to give a digest, the digest is encrypted with the sender's private key, and the result is the digital signature. The message and the signature are sent to the receiver. Receiver rows: the received message goes through the same hash function to give Digest 1; the received signature is decrypted with the sender's public key to give Digest 2. The receiver compares the two digests. If they are the same the message is genuine and unchanged; if they are different it must not be trusted."><text class="tl tb" x="8" y="18">Sender: signs with their own private key</text><text class="tl tc" x="300" y="106">the message and the signature are sent to the receiver</text><text class="tl tb" x="8" y="138">Receiver: checks with the sender's public key</text><text class="tl tc" x="500" y="246">Same: genuine and unchanged</text><text class="tl tc" x="500" y="264">Different: do not trust it</text><path class="ln-m thin dash" d="M8 114 H592"/><rect class="fm s-acc sw2" x="8" y="30" width="96" height="44"/><text class="tl tc" x="56" y="56">Message</text><rect class="f2 s-acc sw2" x="128" y="30" width="96" height="44"/><text class="tl tc" x="176" y="50">Hash</text><text class="tl tc" x="176" y="65">function</text><rect class="fm s-acc sw2" x="248" y="30" width="96" height="44"/><text class="tl tc" x="296" y="56">Digest</text><rect class="f2 s-acc sw2" x="368" y="30" width="96" height="44"/><text class="tl tc" x="416" y="50">Encrypt with</text><text class="tl tc" x="416" y="65">private key</text><rect class="fm s-acc sw2" x="488" y="30" width="96" height="44"/><text class="tl tc" x="536" y="50">Digital</text><text class="tl tc" x="536" y="65">signature</text><rect class="fm s-acc sw2" x="8" y="148" width="96" height="44"/><text class="tl tc" x="56" y="168">Message</text><text class="tl tc" x="56" y="183">received</text><rect class="f2 s-acc sw2" x="128" y="148" width="96" height="44"/><text class="tl tc" x="176" y="168">Hash</text><text class="tl tc" x="176" y="183">function</text><rect class="fm s-acc sw2" x="248" y="148" width="96" height="44"/><text class="tl tc" x="296" y="174">Digest 1</text><rect class="fm s-acc sw2" x="8" y="210" width="96" height="44"/><text class="tl tc" x="56" y="230">Digital</text><text class="tl tc" x="56" y="245">signature</text><rect class="f2 s-acc sw2" x="128" y="210" width="96" height="44"/><text class="tl tc" x="176" y="230">Decrypt with</text><text class="tl tc" x="176" y="245">public key</text><rect class="fm s-acc sw2" x="248" y="210" width="96" height="44"/><text class="tl tc" x="296" y="236">Digest 2</text><rect class="f2 s-acc sw2" x="410" y="180" width="180" height="44"/><text class="tl tc" x="500" y="200">Compare Digest 1</text><text class="tl tc" x="500" y="215">with Digest 2</text><path class="ln" d="M104 52 L126 52" marker-end="url(#ah)"/><path class="ln" d="M224 52 L246 52" marker-end="url(#ah)"/><path class="ln" d="M344 52 L366 52" marker-end="url(#ah)"/><path class="ln" d="M464 52 L486 52" marker-end="url(#ah)"/><path class="ln" d="M104 170 L126 170" marker-end="url(#ah)"/><path class="ln" d="M224 170 L246 170" marker-end="url(#ah)"/><path class="ln" d="M104 232 L126 232" marker-end="url(#ah)"/><path class="ln" d="M224 232 L246 232" marker-end="url(#ah)"/><path class="ln" d="M344 170 L408 194" marker-end="url(#ah)"/><path class="ln" d="M344 232 L408 210" marker-end="url(#ah)"/></svg><figcaption>A digital signature is the digest of a message, encrypted with the sender's private key. The receiver decrypts the signature with the sender's public key and compares the result with a digest of the message they received. The message itself is not encrypted.</figcaption></figure>
:::

The signature works because only the sender's private key could have produced something that the sender's public key decrypts into the right digest. And if even one character of the message changed on the way, the digest of the received message (Digest 1) would no longer match the digest in the signature (Digest 2).

The toy keys from before can sign too. This program reduces the digest to a small number so that the toy keys can handle it. The pattern is the real one: sign with the private exponent, check with the public exponent.

```python
import hashlib

n, e, d = 3233, 17, 2753


def short_digest(message):
    return int(hashlib.sha256(message.encode()).hexdigest(), 16) % n


def sign(message):
    return pow(short_digest(message), d, n)


def verify(message, signature):
    return pow(signature, e, n) == short_digest(message)


order = "Pay Ana 100"
signature = sign(order)
print("signature:", signature)
print("genuine message:", verify(order, signature))
print("changed message:", verify("Pay Ana 900", signature))
print("wrong signature:", verify(order, signature + 1))
```

Output:

```output
signature: 994
genuine message: True
changed message: False
wrong signature: False
```

:::warn A signature does not hide the message
The message in a digital signature is sent as ordinary plain text, and anyone can read it. The signature proves who sent it and that it is unchanged. To make the message private as well, the sender also encrypts it with the receiver's public key.
:::

:::eg Producing and checking a digital signature (exam style)
Describe how a digital signature is produced by the sender and how it is checked by the receiver. [5 marks]

Give the sender's steps first, then the receiver's. Name the key used at each step.

- The sender applies a hash function to the message to produce a digest. [B1]
- The sender encrypts the digest with the sender's private key to produce the digital signature. [B1]
- The message and the signature are sent to the receiver. [B1]
- The receiver decrypts the signature with the sender's public key to get the digest, and applies the same hash function to the message received. [B1]
- If the two digests are the same, the message is genuine and has not been changed. [B1]
:::

## Digital certificates

Look again at the first step of the bank example: "The customer's software gets the bank's public key." How does the customer know that the key really belongs to the bank? A criminal could publish a public key and claim it is the bank's. If the customer used it, the criminal would be able to read everything. The same is true for signatures: a signature checks out against a public key, but whose public key is it?

A **digital certificate** solves this. It ties a public key to the identity of its owner, and a trusted third party vouches for the tie.

:::def Digital certificate
An electronic document that links a public key to the identity of its owner. It is issued and digitally signed by a certificate authority.
:::

:::def Certificate authority (CA)
A trusted organisation that checks the identity of an applicant, issues digital certificates and signs each one with its own private key.
:::

### How an organisation gets a certificate

:::steps
1. The organisation generates a key pair. The private key stays with the organisation.
2. It sends the **public key**, with details of its identity (such as its name and web address), to a certificate authority. This is a request for a certificate.
3. The CA checks that the applicant really is who they say they are.
4. The CA creates the certificate and **signs it with the CA's private key**.
5. The CA sends the certificate back, and the organisation installs it, for example on its web server.
:::

A certificate contains:

- the owner's name (the identity of the organisation or person),
- the owner's **public key**,
- a serial number,
- the dates between which it is valid,
- the name of the CA that issued it,
- the CA's digital signature.

A certificate never contains the owner's private key.

### How a browser uses a certificate

Your browser and operating system come with the public keys of many certificate authorities that they trust. When a website sends its certificate, the browser:

1. checks the CA's digital signature, by decrypting it with the CA's public key and comparing it with a digest of the certificate (exactly the signature check above), so it knows the certificate is genuine and unaltered,
2. checks that the name in the certificate matches the website it is visiting,
3. checks that today's date is within the dates for which the certificate is valid (and that it has not been withdrawn).

If all of these succeed, the browser trusts that the public key in the certificate belongs to that organisation, and uses it. If any fails, the browser warns the user.

:::eg Checking a certificate (exam style)
A browser receives a digital certificate from the website of a bank. Explain how the browser decides to trust it. [4 marks]

The question is about trust, so explain what is checked and why the check can be relied on.

- The certificate was issued by a certificate authority that the browser trusts (the browser holds the CA's public key). [B1]
- The browser uses the CA's public key to check the CA's digital signature on the certificate, which shows that it is genuine and has not been altered. [B1]
- It checks that the name in the certificate matches the website, and that the dates show the certificate is still valid. [B1]
- If the checks succeed, the public key in the certificate can be trusted to belong to the bank. [B1]
:::

### Certificates and digital signatures

A signature is only as trustworthy as the public key used to check it. A company that signs its documents sends its certificate (or makes it available) as well. The receiver first checks the certificate, using the CA's public key, to be sure that the public key belongs to the company. Then the receiver uses that public key to check the company's digital signature. So the certificate links a signature to a real identity.

## SSL/TLS

:::def SSL/TLS
Security protocols (Secure Sockets Layer and its successor Transport Layer Security) that make a communication between a client and a server private and trustworthy. They use a digital certificate to prove the server's identity and encryption to protect the data.
:::

SSL/TLS gives a client-server connection three things: the data cannot be read by anyone listening (confidentiality), it cannot be changed without being noticed (integrity), and the client knows it is talking to the real server (authentication, using the server's certificate). Because TLS replaced SSL, the older name SSL is still used in many places. When a web address starts with `https`, HTTP is running over SSL/TLS, and the browser usually shows a padlock.

The handshake is the first part of the session, where the two computers agree how to protect it. In outline:

:::steps
1. **Client hello.** The client (a browser) asks the server for a secure connection and says which encryption methods it supports.
2. **Server hello and certificate.** The server replies with the method it has chosen and sends its digital certificate, which contains its public key.
3. **The client checks the certificate** (as in the section above). If it fails, the browser warns the user.
4. **A session key is agreed using asymmetric encryption.** The client creates a random session key and sends it to the server encrypted with the server's public key. Only the server's private key can decrypt it, so both sides now share a secret that nobody else knows. (Newer versions of TLS agree the key in a slightly different way, with the same aim.)
5. **Both sides switch to symmetric encryption.** For the rest of the session, all data is encrypted and decrypted with the session key.
:::

This is the pattern from earlier in the chapter. Asymmetric encryption solves the key distribution problem, but it is slow, so it is used only for the handshake. Symmetric encryption is fast, so it carries the data. The key is used for this session only.

:::warn TLS uses both kinds of encryption
Do not say that TLS "uses asymmetric encryption" or "uses symmetric encryption". It uses asymmetric encryption (with the certificate) in the handshake to agree a session key, then symmetric encryption with that key for the data.
:::

**When SSL/TLS is appropriate.** Use it whenever the data sent between a client and a server is private or valuable:

- online banking and shopping, where card numbers and passwords are sent,
- logging in to any account, because the password must not be overheard,
- sending and receiving email between an email program and a mail server,
- voice and video calls over the internet (VoIP),
- sending personal or medical details, for example in a form on a clinic's website.

It matters less for a public page that sends no personal data, such as a page of opening times, although many websites use it for every page anyway. The costs are small: some extra processing time for the handshake and the encryption, and the need to obtain and renew a certificate.

:::eg Securing a session with TLS (exam style)
Explain how SSL/TLS protects the data sent between a customer's browser and an online shop. [5 marks]

Cover the proof of identity, the key and the encryption of the data.

- The browser asks the shop's server for a secure connection, and the server sends its digital certificate. [B1]
- The browser checks the certificate to confirm the server is genuine. [B1]
- The browser and server agree a session key, sent using asymmetric encryption (the browser encrypts it with the server's public key). [B1]
- The session key is a shared secret that only the browser and the server know. [B1]
- The rest of the session uses symmetric encryption with the session key, so any data intercepted is unreadable. [B1]
:::

## Quantum cryptography

Symmetric encryption needs both sides to share a key without anyone else getting it. Quantum cryptography is a method of sharing that key which uses the laws of physics instead of the difficulty of a calculation.

:::def Quantum cryptography
The use of the behaviour of individual particles of light (photons) to share an encryption key between two people. Observing a quantum state changes it, so an eavesdropper who tries to copy the key can be detected. It is also called quantum key distribution.
:::

In outline, the sender sends a stream of photons, each prepared in one of several states that stand for bits, along an optical fibre. The receiver measures them. The two then compare, over an ordinary channel, a sample of what was sent and what was received, without revealing the key itself. If someone has been listening, measuring the photons will have disturbed some of them, and the sample shows errors. The two then throw the key away and try again. If there are no errors, they keep the remaining bits as a secret key, and use it for symmetric encryption of the data.

**Benefits.**
- An attempt to eavesdrop on the key can be detected.
- Its security depends on physics, not on a calculation that a faster computer might one day solve.

**Drawbacks.**
- It needs special, expensive equipment, such as dedicated optical fibre.
- It works only over limited distances, because photons are lost along a fibre.
- The technology is still developing, and it shares only the key: the data itself is still encrypted with a conventional method.

Quantum cryptography is not the same thing as a quantum computer: the first is a way of sharing keys, the second is a different kind of computer.

:::eg Quantum cryptography (exam style)
Describe how quantum cryptography allows two people to find out whether someone has been eavesdropping while they share a key. [3 marks]

The answer is about what the observer changes, and what the two parties do about it.

- The key is sent as a series of photons, each in a quantum state that stands for a bit. [B1]
- Measuring a photon changes its state, so an eavesdropper who reads the photons introduces errors. [B1]
- The two people compare part of the data, and if there are errors they know it was intercepted and do not use the key. [B1]
:::

## Putting the tools together

Each tool solves one problem, and each depends on the one before.

| Problem | Tool | Key used |
|---|---|---|
| Keep a message private from everyone except the receiver | Asymmetric encryption | encrypt with the **receiver's public** key; decrypt with their **private** key |
| Keep lots of data private quickly | Symmetric encryption | one shared secret key |
| Prove who sent a message and that it is unchanged | Digital signature | sign with the **sender's private** key; check with their **public** key |
| Be sure a public key belongs to who it says | Digital certificate | signed by the CA's private key; checked with the CA's public key |
| Protect a whole client-server session | SSL/TLS | certificate and asymmetric encryption to agree a key, then symmetric encryption |
| Share a key so that eavesdropping is detected | Quantum cryptography | photons |

:::exam Key words that earn the marks
Name the key every time: "encrypts with the **receiver's public key**", "**decrypts** with the **private key**", "signature = **digest** encrypted with the **sender's private key**". An answer that says "encrypted with a key" earns nothing. A digital signature uses a **hash**. A certificate holds a **public** key, never a private key. TLS uses **both** kinds of encryption.
:::

:::eg Spot the error: reversing the keys
Question: A customer sends confidential details to a bank using asymmetric encryption. Explain how. [4 marks]

A student wrote: "The customer encrypts the message with their own private key. The bank has the customer's public key, so it uses that to decrypt the message."

The message is encrypted before it is sent, so anything intercepted is cipher text [B1]. **The keys are the wrong way round. The customer must encrypt with the bank's public key, and the student used the customer's private key: that mark is lost** [B0]. The bank must decrypt with its own private key, not the customer's public key [B0]. The last mark, that only the bank holds the private key and so only the bank can read the message, is lost too, because the student's method would let anyone with the customer's public key read it [B0]. The answer scores 1 out of 4.

The correct answer: the customer encrypts with the **bank's public key**, sends the cipher text, and the bank decrypts with the **bank's private key**.
:::

:::eg Spot the error: what a certificate contains
Question: Describe what is in a digital certificate and who issues it. [3 marks]

A student wrote: "A digital certificate is issued by a certificate authority. It contains the organisation's name and the dates it is valid. It also contains the organisation's private key so that browsers can decrypt messages."

The issuer is correct [B1]. The name and the dates are correct contents [B1]. **A certificate never contains a private key. The mark for the public key is lost, and the claim shows a misunderstanding that would give the secret away** [B0]. The answer scores 2 out of 3. The correct line is: "It also contains the organisation's public key."
:::

:::try Start easy, finish at exam standard
Q: State the difference between the keys used in symmetric and asymmetric encryption.
A: Symmetric encryption uses one key, shared by both people, to encrypt and decrypt. Asymmetric encryption uses a pair of keys, a public key and a private key, and what one encrypts only the other decrypts.
Q: Which key does Dara use to encrypt a message that only Lina must be able to read, and which key does Lina use to read it?
A: Dara uses Lina's public key. Lina decrypts with her own private key.
Q: A message is encrypted with a key of 10 bits. How many different keys could an attacker have to try?
A: \(2^{10} = 1024\) keys.
Q: Give two properties of a hash function.
A: Any two of: the digest is always the same length whatever the size of the message; the same message always gives the same digest; a small change to the message changes the digest completely; the message cannot be worked out from the digest.
Q: Is the message in a digital signature encrypted? Explain.
A: No. Only the digest is encrypted (with the sender's private key). The message is sent as plain text, so a signature proves who sent it and that it is unchanged but does not keep it secret.
Q: Name the organisation that issues a digital certificate and the key it uses to sign the certificate.
A: A certificate authority (CA). It signs the certificate with the CA's private key.
Q: Why does TLS use symmetric encryption for the data after the handshake?
A: Symmetric encryption is much faster than asymmetric encryption, so it can encrypt large amounts of data without slowing the session. The asymmetric encryption is needed only to agree the session key safely.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ A company has 12 staff. Every pair of staff needs their own symmetric key for private messages. Calculate the number of keys needed.
A: The number of pairs among \(n\) people is \(\frac{n(n-1)}{2}\), so \(\frac{12 \times 11}{2}\) [M1] = 66 keys [A1]

Q: [4 marks] ★★ A school in Accra sends exam results to the exam board over the internet. The results must stay confidential. Explain how the school can use asymmetric encryption to do this.
H: Say which party has the key pair and which key goes to the other party.
H: Name the key used to encrypt and the key used to decrypt.
A: One possible answer:

- the exam board has a public key and a private key [B1]
- the exam board's public key is given to the school and the private key is kept secret [B1]
- the school encrypts the results with the exam board's public key before sending them [B1]
- the exam board decrypts them with its private key, which nobody else has, so anyone intercepting the cipher text cannot read it [B1]

Q: [3 marks] ★★ A news agency in Manila signs every press release with a digital signature. Explain why the signature does not keep the press release secret, and how the agency could also make a release confidential for one newspaper.
A: The signature is a digest encrypted with the agency's private key, and the press release itself is sent as plain text, so anyone can read it [B1]. To make it confidential the agency also encrypts the press release with the newspaper's public key [B1], and only the newspaper's private key can decrypt it [B1].

Q: [3 marks] ★★ A message digest is produced before a message is signed. (a) State what a message digest is. [1] (b) Give two reasons why the digest, and not the whole message, is encrypted to make the signature. [2]
A: (a) The fixed-length value produced when a hash function is applied to the message [B1]

(b) Two of:

- the digest is much shorter than the message, so encrypting it with the slow asymmetric method is much quicker [B1]
- the digest is always the same length, whatever the size of the message [B1]

(Accept also: the message can then be read without decrypting anything.)

Q: [4 marks] ★★ A shop in Quito wants a digital certificate for its website. Describe how it obtains one.
A: One possible answer:

- the shop generates a pair of keys, a public key and a private key [B1]
- it sends its public key and its identity details to a certificate authority [B1]
- the certificate authority checks the identity of the shop [B1]
- the CA signs the certificate with its private key and sends it to the shop to install on its web server [B1]

Q: [5 marks] ★★★ A school in Lagos builds a website where parents pay fees. (a) State two reasons why SSL/TLS should be used on the payment pages. [2] (b) Explain why, after the handshake, the session uses symmetric encryption rather than asymmetric encryption. [3]
H: In (a), think about what an eavesdropper could steal and what a fake site could do.
H: In (b), compare the speed of the two methods and say what the asymmetric method was used for.
A: (a) Two of:

- card details and personal data sent to the server are encrypted, so an eavesdropper cannot read them [B1]
- the server's certificate shows parents that the site is genuine [B1]

(Accept also: the data cannot be altered on the way without being detected.)

(b)

- symmetric encryption is much faster than asymmetric encryption [B1]
- so it can encrypt the large amount of data in the session without slowing it down [B1]
- asymmetric encryption was needed only to agree the session key safely, since the key is now a shared secret [B1]

Q: [2 marks] ★ Give one benefit and one drawback of quantum cryptography.
A: Benefit: an eavesdropper on the key exchange can be detected (or: its security depends on physics, not on a calculation that could be broken) [B1]. Drawback: it needs expensive special equipment (or: it works only over a limited distance) [B1]

Q: [6 marks] ★★★ A bank sends each customer a statement with a digital signature. (a) Explain how the customer's software checks the signature. [3] (b) Explain why the software also needs the bank's digital certificate. [3]
H: In (a), name the key used and what is compared.
H: In (b), ask how the customer knows the public key really belongs to the bank.
A: (a)

- it decrypts the signature with the bank's public key to get a digest [B1]
- it applies the same hash function to the statement received to make a second digest [B1]
- if the two digests are the same, the statement is genuine and unchanged [B1]

(b)

- anyone could publish a public key and claim to be the bank, so the customer needs to know that the key really belongs to the bank [B1]
- the certificate contains the bank's public key and name and is signed by a certificate authority that the software trusts [B1]
- the software checks the certificate before using the key, so a forged signature made with another person's key would be detected [B1]
:::

:::try Stretch for A*
Q: [4 marks] ★★★ (Not on the syllabus: an optional look at the arithmetic.) A toy key pair has public key \((e, n) = (7, 33)\) and private key \((d, n) = (3, 33)\). Encrypting a number \(m\) gives \(m^e \bmod n\); decrypting a number \(c\) gives \(c^d \bmod n\). (a) Encrypt the message 5 with the public key. (b) Decrypt your answer with the private key. (c) The digest of a message is 8. Create the signature, using the private key, and show that the public key recovers the digest. (d) A forger changes the message so that its digest is 9 but keeps the same signature. What does the receiver's check find?
H: Work out the powers first: \(5^7 = 78\,125\). Then find the remainder when you divide by 33.
H: Signing is the same sum as decrypting: use the private key on the digest.
A: (a) \(5^7 = 78\,125 = 33 \times 2367 + 14\), so the cipher text is 14 [B1]

(b) \(14^3 = 2744 = 33 \times 83 + 5\), so the plain text is 5 again [B1]

(c) Signature: \(8^3 = 512 = 33 \times 15 + 17\), so the signature is 17. Checking with the public key: \(17^7 \bmod 33 = 8\), the digest [B1]

(d) The check still gives 8 from the signature, but the digest of the changed message is 9. They are different, so the change is detected and the message is rejected [B1]

Q: [5 marks] ★★★ A company with 40 branches wants every branch to be able to send private messages to every other branch. (a) Compare the number of keys needed using symmetric encryption (one key for each pair of branches) with the number of key pairs needed using asymmetric encryption (one pair for each branch). [2] (b) Explain how this shows why TLS uses both kinds of encryption. [3]
H: Use \(\frac{n(n-1)}{2}\) for the symmetric case.
A: (a) Symmetric: \(\frac{40 \times 39}{2} = 780\) keys [B1]; asymmetric: 40 key pairs, one for each branch [B1]

(b)

- asymmetric encryption needs far fewer keys, and no secret has to be shared in advance, which solves the key distribution problem [B1]
- but it is slow, so it is not suited to encrypting all the data [B1]
- so asymmetric encryption is used to agree a session key, and fast symmetric encryption with that key carries the data [B1]
:::

:::quiz
? Priya publishes her public key. Which key should a friend use to encrypt a message that only Priya can read?
- Priya's private key
+ Priya's public key
- the friend's private key
- the friend's public key
> Anyone may use Priya's public key to lock a message, and only her private key can unlock it. Her private key is secret, so the friend does not have it.
? What is the purpose of a digital signature?
- To keep the message secret from everyone except the receiver
+ To show who sent the message and that it has not been changed
- To make the message shorter
- To prove that the receiver's computer is secure
> The message is sent as plain text. The signature is an encrypted digest, which lets the receiver check the sender and the message.
? Which of these does a digital certificate contain?
- The owner's private key
+ The owner's public key
- The CA's private key
- The customer's password
> A certificate holds the owner's public key, the owner's name, dates and a serial number, signed by the CA. Private keys are never shared.
? Once an SSL/TLS handshake is complete, how is the data in the session encrypted?
- Asymmetrically, with the server's public key
- Asymmetrically, with the client's private key
+ Symmetrically, with the session key
- It is not encrypted again
> The handshake uses asymmetric encryption to agree the session key. The data is then encrypted symmetrically with that key, because it is much faster.
? Which is a drawback of symmetric encryption?
- It is much slower than asymmetric encryption
- It needs a different key for every message
+ The shared key has to be passed to the other person without anyone else seeing it
- It cannot be used for large amounts of data
> Symmetric encryption is fast and works on large data. The trouble is sharing the key safely: the key distribution problem.
? How many symmetric keys do 10 people need, if every pair has its own key?
+ 45
- 90
- 100
- 10
> \(\frac{10 \times 9}{2} = 45\). 90 counts each pair twice, and 100 counts every person with every person, including themselves.
? Why can an eavesdropper on a quantum key exchange be detected?
- The photons are too slow to be copied
+ Measuring the photons changes their states, which causes errors the two people can see
- The key is sent in two halves
- The photons only travel in one direction
> Observing a quantum state changes it, so an eavesdropper introduces errors. The two people notice them when they compare part of their data.
:::

:::checklist What you can now do
- [ ] I can define plain text, cipher text, encryption, key, public key and private key.
- [ ] I can explain symmetric encryption, and its benefit (speed) and its drawback (sharing the key).
- [ ] I can explain asymmetric encryption, and say which key encrypts and which decrypts to send a private message to a person or an organisation.
- [ ] I can explain what a hash function and a message digest are.
- [ ] I can describe how a digital signature is produced and checked, to send a verified message.
- [ ] I can describe how a digital certificate is acquired from a certificate authority, what it contains and how a browser checks it.
- [ ] I can explain the purpose of SSL/TLS, describe the handshake in outline and say when it is appropriate.
- [ ] I can explain why TLS uses asymmetric encryption first and symmetric encryption for the data.
- [ ] I can describe quantum cryptography and give a benefit and a drawback.
:::

:::recap
- Plain text + algorithm + key gives cipher text. The key is the secret; a key of \(n\) bits has \(2^n\) possible values.
- Symmetric encryption: one shared key. Fast, but the key must be shared safely, and \(\frac{n(n-1)}{2}\) keys are needed for \(n\) people.
- Asymmetric encryption: a public key and a private key. Encrypt with the **receiver's public key** to send a private message; the receiver decrypts with their **private key**. It is slower.
- A hash function gives a fixed-length digest that changes completely if the message changes and cannot be reversed. A hash is not encryption.
- Digital signature: hash the message, encrypt the digest with the **sender's private key**, send both. The receiver decrypts with the sender's **public key** and compares it with a digest of the message received. The message is not hidden.
- A digital certificate links a public key to an identity and is signed by a certificate authority. It holds the owner's name, public key, serial number, dates and the CA's signature, and never a private key. A browser checks it using the CA's public key.
- SSL/TLS: certificate checked, session key agreed with asymmetric encryption, then symmetric encryption for the data. It suits banking, shopping, logins, email and calls.
- Quantum cryptography shares a key using photons, and eavesdropping is detectable because measuring changes the state. It needs special equipment and works over limited distances.
:::

:::links
- practise: [Encryption and digital certificates: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/17-security-/encryption-encryption-protocols-and-digital-certificates/exam-questions/) · Save My Exams · 9618-style questions on keys, signatures, TLS and certificates with mark schemes [paid]
- read: [Khan Academy: cryptography](https://www.khanacademy.org/computing/computer-science/cryptography) · Khan Academy · from simple ciphers to public key cryptography, with exercises
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos by university computer scientists on public keys, certificates and TLS
- read: [9618 revision notes](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/) · Save My Exams · notes on every 9618 topic [paid]

Links checked 13 November 2026.
:::

Next: [Graphs and pathfinding: Dijkstra and A*](#cs.ai)
