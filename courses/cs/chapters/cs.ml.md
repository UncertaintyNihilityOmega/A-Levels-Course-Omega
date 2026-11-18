@chapter cs.ml
@title Machine learning and neural networks
@level a2
@paper CAIE 9618 Paper 3
@time 4–6 hours
@summary Machine learning lets a computer improve at a task from data instead of from rules a programmer wrote. You will learn the difference between AI, machine learning and deep learning, the three kinds of learning (supervised, unsupervised and reinforcement), how an artificial neural network calculates its output and learns by back propagation of errors, and what regression does.

:::why
Spam filters, voice assistants, medical image checks and recommendation systems are all machine learning. Nobody wrote a rule for "what a cat looks like": the system was shown many examples and adjusted itself. Paper 3 asks you to name and compare the types of learning, to describe how a neural network is trained, and to explain why a method suits a scenario. The ideas are small and exact, and a few hand calculations make them concrete.
:::

**Before you start**, you should be able to follow the A* and Dijkstra tables in [Graphs and pathfinding: Dijkstra and A*](#cs.ai), where a computer searches for an answer using rules you can see. This chapter is about the opposite case, where the rules are learned. Logic gates from [Logic gates and logic circuits](#cs.logic) and the social effects of AI from [Ethics, ownership and the impact of AI](#cs.ethics) also help.

:::try Warm-up
Q: Complete the truth table of an XOR gate for the inputs 00, 01, 10 and 11. (from [Logic gates and logic circuits](#cs.logic))
A: The outputs are 0, 1, 1, 0. XOR is true when exactly one of its two inputs is 1.
Q: In A*, a vertex has \(g = 6\) and \(h = 3\). What is its f-cost, and what do g and h stand for? (from [Graphs and pathfinding: Dijkstra and A*](#cs.ai))
A: \(f = g + h = 9\). g is the cost of the path from the start so far, and h is the heuristic estimate of the cost from the vertex to the destination.
Q: In Python, `scores = [4, 6, 5]`. What does `scores[1]` give, and what does `sum(scores)` give? (from [Data types, records and arrays](#cs.datatypes))
A: `scores[1]` is 6, because Python counts from 0. `sum(scores)` is 15.
:::

:::note What the syllabus asks
You must understand how artificial neural networks have helped with machine learning; deep learning, machine learning and reinforcement learning and the reasons for using them; the machine learning categories, including supervised learning and unsupervised learning; and back propagation of errors and regression methods. These are understanding outcomes: Cambridge asks you to describe, explain and justify. The small calculations in this chapter are there so that the words mean something. The code in this chapter is not examined.
:::

## Artificial intelligence, machine learning and deep learning

You met **artificial intelligence (AI)** in [Ethics, ownership and the impact of AI](#cs.ethics): computer systems that do tasks that normally need human intelligence. The pathfinding in [Graphs and pathfinding: Dijkstra and A*](#cs.ai) is AI too, even though it never learns anything: a programmer wrote the rules. So AI is a wide field, and learning is one way of building it.

:::def Machine learning
A branch of AI in which a computer system improves at a task by finding patterns in data, instead of being given every rule by a programmer. The more (and better) the data, the better the system usually becomes.
:::

:::def Deep learning
A kind of machine learning that uses artificial neural networks with many hidden layers. The layers let the system learn its own features from raw data, such as the pixels of an image, in stages.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 236" role="img" aria-label="Three nested ellipses. The largest is labelled Artificial intelligence. Inside it is Machine learning. Inside that is Deep learning."><ellipse class="fp s-acc sw2" cx="170" cy="118" rx="160" ry="108"/><ellipse class="fm s-acc sw2" cx="170" cy="140" rx="118" ry="72"/><ellipse class="f1 s-acc sw2" cx="170" cy="158" rx="72" ry="38"/><text class="tl tc tb" x="170" y="42">Artificial intelligence</text><text class="tl tc tb" x="170" y="88">Machine learning</text><text class="tl tc tb" x="170" y="162">Deep learning</text></svg><figcaption>Deep learning is one kind of machine learning, and machine learning is one way of building artificial intelligence. Each inner idea is part of the one around it.</figcaption></figure>
:::

Why use machine learning at all? Because for some problems nobody can write the rules.

- **The rules are too hard to write.** Describing in code what makes a handwritten 7 different from a 1 for every writer on Earth is hopeless. Showing a system 60,000 examples is not.
- **The task changes.** Spam writers change their tricks every week. A system that keeps learning from new examples can follow them; fixed rules go out of date.
- **There is a lot of data.** Patterns in millions of records are beyond what a person can spot by eye.

There are also reasons to be careful, which come back at the end of the chapter: learning needs a lot of data, the data may be biased, and the result can be hard to explain.

## Three kinds of machine learning

Machine learning methods are grouped by what the system is given to learn from.

### Supervised learning

:::def Supervised learning
Machine learning from **labelled** training data: every example comes with the correct answer. The system learns a rule that maps inputs to outputs, and then predicts the output for new inputs it has not seen.
:::

:::def Training data
The set of examples used to train a machine learning system. In supervised learning each example is an input together with its correct output (its label).
:::

A spam filter is trained on thousands of emails that people have already marked "spam" or "not spam". The marks are the labels, and they are the "supervision": a teacher has supplied the right answers. Supervised learning has two main jobs:

- **Classification** predicts a category: spam or not spam, which of ten digits, whether a scan shows a disease.
- **Regression** predicts a number: the price of a house, tomorrow's temperature, the time a delivery will take. Regression is covered later in this chapter.

### Unsupervised learning

:::def Unsupervised learning
Machine learning from **unlabelled** data. There are no correct answers to learn from; the system looks for structure in the data by itself, such as groups of similar items (clustering).
:::

A shop has the purchase records of 50,000 customers but no categories. An unsupervised method can group customers who buy in similar ways, and the shop can then look at each group and decide what it is (students, families, regular buyers of baby products). The program found the groups; a person gave them meaning.

### Reinforcement learning

:::def Reinforcement learning
Machine learning in which an **agent** learns by trial and error in an **environment**. It chooses actions, receives **rewards** (or penalties), and learns which actions bring the most reward over time. There are no labelled correct answers.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 320 210" role="img" aria-label="A loop between an agent and its environment. An arrow labelled action points down from the agent to the environment. An arrow labelled reward and new state points up from the environment to the agent."><rect class="fm s-acc sw2" x="90" y="16" width="140" height="42"/><text class="tl tc tb" x="160" y="42">Agent</text><rect class="fm s-acc sw2" x="90" y="150" width="140" height="42"/><text class="tl tc tb" x="160" y="176">Environment</text><line class="c1 sw2" x1="118" y1="62" x2="118" y2="146" marker-end="url(#ah)"/><text class="tl te" x="108" y="108">action</text><line class="c2 sw2" x1="202" y1="146" x2="202" y2="62" marker-end="url(#ah)"/><text class="tl" x="212" y="98">reward</text><text class="tl" x="212" y="116">new state</text></svg><figcaption>The reinforcement learning loop: the agent acts, and the environment answers with a reward and a new state.</figcaption></figure>
:::

Think of training a robot to walk, or a program to play a board game against itself. The **agent** is the learner (the robot or program). The **environment** is everything it acts on (the floor, the game). Each **action** (a step, a move) changes the **state** of the environment, and the agent receives a **reward** (a positive number for staying upright or winning, a negative number for falling). Its **policy**, the rule it uses to choose an action in each state, improves because actions that led to good rewards become more likely.

:::eg Which kind of learning?
For each system, state the type of machine learning and give a reason from the scenario. [3 marks]

(a) A mail company in Nairobi trains a program on 20,000 emails that staff have already marked "junk" or "genuine", so that it can mark new emails itself.

(b) A supermarket gives a program the shopping records of its customers, with no other information, and asks it to find groups of customers who shop alike.

(c) A program plays a chess variant against copies of itself, receiving +1 for a win and −1 for a loss, and gradually improves its moves.

- (a) Supervised learning, because the emails are labelled with the correct answer ("junk" or "genuine"). [B1]
- (b) Unsupervised learning, because the data are unlabelled and the program must find the groups itself. [B1]
- (c) Reinforcement learning, because the program learns from rewards for its actions by trial and error, with no labelled answers. [B1]
:::

:::warn Reinforcement learning is not supervised learning
In supervised learning, every example carries the right answer. In reinforcement learning, nobody tells the agent the right move. It only receives a reward, often late (a win comes at the end of the game), and has to work out which of its earlier actions deserve the credit.
:::

The table sums up the three methods.

| | Supervised | Unsupervised | Reinforcement |
|---|---|---|---|
| Data | labelled examples | unlabelled data | rewards from an environment |
| Learns | to predict the label | patterns and groups | which actions give most reward |
| Typical output | a category (classification) or a number (regression) | clusters, unusual items | a policy: what to do in each state |
| Example | spam filter, price prediction | customer groups | game player, robot walking |
| Use it when | you have many labelled examples | you have data but no labels | you can try actions and score the result |

### A small taste of learning from rewards

Here is the idea behind reinforcement learning in numbers. A delivery robot can drive route X or route Y. After each trip it gets a reward: the minutes it saved. It keeps an estimate V of how good route X is, starting at 0, and after each trip moves the estimate half of the way towards the reward it just received:

\[V \leftarrow V + 0.5 \times (\text{reward} - V)\]

The rewards for three trips along X are 10, 10 and 6. After the first trip \(V = 0 + 0.5 \times (10 - 0) = 5\). After the second, \(V = 5 + 0.5 \times (10 - 5) = 7.5\). After the third, \(V = 7.5 + 0.5 \times (6 - 7.5) = 6.75\). The estimate follows the rewards. If route Y's estimate is lower, the robot's policy is to choose X most of the time, and it still tries Y now and then in case things have changed. This is a simplified model; real systems also use the state and look ahead, but they use the same idea of nudging an estimate towards what happened.

## Artificial neural networks

An **artificial neural network (ANN)** is a machine learning model made of many small calculators called nodes, joined in layers. It is loosely inspired by the way brain cells connect, but it is just arithmetic.

:::def Artificial neural network
A machine learning model made of layers of connected **nodes** (neurons). Each connection has a **weight**. A node adds up its weighted inputs, and passes the total through an **activation function** to produce its output, which goes on to the nodes in the next layer.
:::

:::def Node (neuron)
One processing unit of a neural network. It receives numbers from the previous layer, multiplies each by a weight, adds them up (with a bias), and outputs the result of its activation function.
:::

:::def Weight
A number on a connection between two nodes. It sets how strongly the sending node affects the receiving node. A large positive weight pushes the receiver up, a negative weight pushes it down. Learning is the process of changing the weights.
:::

:::def Activation function
A function applied to a node's weighted sum to decide its output. A **step** function outputs 1 if the sum is 0 or more and 0 otherwise. A **ReLU** function outputs the sum if it is positive and 0 if it is not. Other activation functions give smooth values between 0 and 1.
:::

:::def Hidden layer
A layer of nodes between the input layer and the output layer. Its outputs are not shown to the user; they are used by the next layer. A network with at least one hidden layer can learn patterns that a network without one cannot.
:::

A network has an **input layer** (one node for each input value, such as one for each pixel), one or more **hidden layers**, and an **output layer** (one node for each answer, such as one for each possible digit). Here is a small network.

:::html
<figure class="fig small"><svg viewBox="0 0 340 256" role="img" aria-label="A neural network with three layers. The input layer has three nodes x1, x2 and x3. The hidden layer has four nodes h1 to h4. The output layer has two nodes y1 and y2. Every node in one layer is joined by a connection to every node in the next layer, which is 12 connections from the input layer to the hidden layer and 8 from the hidden layer to the output layer."><line class="ln-m thin" x1="60" y1="70" x2="170" y2="45"/><line class="ln-m thin" x1="60" y1="70" x2="170" y2="100"/><line class="ln-m thin" x1="60" y1="70" x2="170" y2="155"/><line class="ln-m thin" x1="60" y1="70" x2="170" y2="210"/><line class="ln-m thin" x1="60" y1="125" x2="170" y2="45"/><line class="ln-m thin" x1="60" y1="125" x2="170" y2="100"/><line class="ln-m thin" x1="60" y1="125" x2="170" y2="155"/><line class="ln-m thin" x1="60" y1="125" x2="170" y2="210"/><line class="ln-m thin" x1="60" y1="180" x2="170" y2="45"/><line class="ln-m thin" x1="60" y1="180" x2="170" y2="100"/><line class="ln-m thin" x1="60" y1="180" x2="170" y2="155"/><line class="ln-m thin" x1="60" y1="180" x2="170" y2="210"/><line class="ln-m thin" x1="170" y1="45" x2="280" y2="85"/><line class="ln-m thin" x1="170" y1="45" x2="280" y2="165"/><line class="ln-m thin" x1="170" y1="100" x2="280" y2="85"/><line class="ln-m thin" x1="170" y1="100" x2="280" y2="165"/><line class="ln-m thin" x1="170" y1="155" x2="280" y2="85"/><line class="ln-m thin" x1="170" y1="155" x2="280" y2="165"/><line class="ln-m thin" x1="170" y1="210" x2="280" y2="85"/><line class="ln-m thin" x1="170" y1="210" x2="280" y2="165"/><circle class="f1 s-acc sw2" cx="60" cy="70" r="14"/><text class="tl tc tb" x="60" y="74">x1</text><circle class="f1 s-acc sw2" cx="60" cy="125" r="14"/><text class="tl tc tb" x="60" y="129">x2</text><circle class="f1 s-acc sw2" cx="60" cy="180" r="14"/><text class="tl tc tb" x="60" y="184">x3</text><circle class="f1 s-acc sw2" cx="170" cy="45" r="14"/><text class="tl tc tb" x="170" y="49">h1</text><circle class="f1 s-acc sw2" cx="170" cy="100" r="14"/><text class="tl tc tb" x="170" y="104">h2</text><circle class="f1 s-acc sw2" cx="170" cy="155" r="14"/><text class="tl tc tb" x="170" y="159">h3</text><circle class="f1 s-acc sw2" cx="170" cy="210" r="14"/><text class="tl tc tb" x="170" y="214">h4</text><circle class="f1 s-acc sw2" cx="280" cy="85" r="14"/><text class="tl tc tb" x="280" y="89">y1</text><circle class="f1 s-acc sw2" cx="280" cy="165" r="14"/><text class="tl tc tb" x="280" y="169">y2</text><text class="tl tc" x="60" y="242">Input layer</text><text class="tl tc" x="170" y="242">Hidden layer</text><text class="tl tc" x="280" y="242">Output layer</text></svg><figcaption>A 3-4-2 network: three inputs, four hidden nodes and two outputs. Each of the 20 lines is a connection with its own weight.</figcaption></figure>
:::

Every node in one layer connects to every node in the next. The numbers of connections are \(3 \times 4 = 12\) from the inputs to the hidden layer and \(4 \times 2 = 8\) from the hidden layer to the outputs: 20 weights in all. Each node has one more adjustable number, its **bias**, which shifts the total up or down so that the node fires more or less easily. (The syllabus does not use the word "bias", but the 9618/31 June 2025 mark scheme speaks of adjusting "the weights/biases" of the connections. A question that needs a bias gives its value.) A real image-recognition network has millions of weights.

### What one node calculates

:::key The calculation of one node
1. Multiply each input by the weight of its connection.
2. Add the products together, then add the node's bias. This is the **weighted sum**: \(S = w_1 x_1 + w_2 x_2 + \dots + b\).
3. Pass \(S\) through the activation function. Step: output 1 if \(S \ge 0\), otherwise 0. ReLU: output \(S\) if \(S > 0\), otherwise 0.
4. Send the output along the connections to the next layer.
:::

:::eg A single node
A greenhouse controller has one node. Its inputs are \(x_1 = 1\) if the temperature is high (0 if not) and \(x_2 = 1\) if the humidity is high (0 if not). The weights are \(w_1 = 2\) and \(w_2 = 1\), the bias is \(-2\), and the activation function is a step: output 1 (open the window) if \(S \ge 0\), otherwise 0. Work out the output for each of the four input combinations. [2 marks]

| Temp high x1 | Humid high x2 | Sum S = 2·x1 + 1·x2 − 2 | Output |
|---|---|---|---|
| 0 | 0 | 0 + 0 − 2 = −2 | 0 |
| 0 | 1 | 0 + 1 − 2 = −1 | 0 |
| 1 | 0 | 2 + 0 − 2 = 0 | 1 |
| 1 | 1 | 2 + 1 − 2 = 1 | 1 |

- Each weighted sum is worked out as weight × input for every input, added together with the bias. [B1]
- The step function gives 1 when \(S \ge 0\) and 0 otherwise, so the window opens when the temperature is high, whatever the humidity. [B1]

The weights decide how much each input matters. Temperature has weight 2, enough on its own to cancel the bias; humidity has weight 1, which is not. Learning means finding good weights.
:::

A computer calculates the weighted sum with a loop. In pseudocode, for three inputs held in the arrays Inputs and Weights, a bias Bias and a step activation:

```pseudocode
DECLARE Sum : REAL
DECLARE Index, Result : INTEGER

Sum ← Bias
FOR Index ← 1 TO 3
   Sum ← Sum + Inputs[Index] * Weights[Index]
NEXT Index
IF Sum >= 0.0 THEN
   Result ← 1
ELSE
   Result ← 0
ENDIF
```

For Inputs 3, 2 and 1, Weights 2, −1 and 4, and Bias −7, the sum is \(-7 + 6 - 2 + 4 = 1\), so Result is 1. The same calculation in Python, with the two activation functions as small functions, also runs the greenhouse node and a ReLU node:

```python
def step(total):
    return 1 if total >= 0 else 0


def relu(total):
    return max(0, total)


def neuron(inputs, weights, bias, activation):
    total = bias
    for x, w in zip(inputs, weights):
        total = total + x * w
    return activation(total)


print(neuron([1, 0], [2, 1], -2, step))
print(neuron([0, 1], [2, 1], -2, step))
print(neuron([3, 2], [2, -1], -3, relu))
```

Output:

```output
1
0
1
```

The first two lines are the greenhouse rows (1, 0) and (0, 1) from the table. The third is a ReLU node: \(S = 6 - 2 - 3 = 1\), which is positive, so the output is 1.

### Why a hidden layer matters

One node can only draw a single straight dividing line between its inputs. It can copy the OR gate or the AND gate, but it cannot copy XOR, which is 1 only when exactly one input is 1. A network with a hidden layer can. In the network below, the first hidden node behaves like OR (bias −1), the second like AND (bias −2), and the output node fires only when the first is on and the second is off.

:::html
<figure class="fig small"><svg viewBox="20 22 305 190" role="img" aria-label="A neural network with two inputs x1 and x2, two hidden nodes h1 and h2, and one output node o. Every input is joined to both hidden nodes with weight 1. The hidden node h1 has bias minus 1 and h2 has bias minus 2. The weight from h1 to o is 1 and from h2 to o is minus 1. The output node has bias minus 1."><line class="ln" x1="50" y1="70" x2="170" y2="70"/><line class="ln" x1="50" y1="70" x2="170" y2="160"/><line class="ln" x1="50" y1="160" x2="170" y2="70"/><line class="ln" x1="50" y1="160" x2="170" y2="160"/><line class="ln" x1="170" y1="70" x2="290" y2="115"/><line class="ln" x1="170" y1="160" x2="290" y2="115"/><text class="tl tc tb halo" x="110" y="74">1</text><text class="tl tc tb halo" x="74" y="92">1</text><text class="tl tc tb halo" x="74" y="146">1</text><text class="tl tc tb halo" x="110" y="164">1</text><text class="tl tc tb halo" x="230" y="96">1</text><text class="tl tc tb halo" x="230" y="142">−1</text><circle class="f1 s-acc sw2" cx="50" cy="70" r="18"/><text class="tl tc tb" x="50" y="74">x1</text><circle class="f1 s-acc sw2" cx="50" cy="160" r="18"/><text class="tl tc tb" x="50" y="164">x2</text><circle class="f1 s-acc sw2" cx="170" cy="70" r="18"/><text class="tl tc tb" x="170" y="74">h1</text><circle class="f1 s-acc sw2" cx="170" cy="160" r="18"/><text class="tl tc tb" x="170" y="164">h2</text><circle class="f1 s-acc sw2" cx="290" cy="115" r="18"/><text class="tl tc tb" x="290" y="119">o</text><text class="tl tc" x="170" y="40">bias −1</text><text class="tl tc" x="170" y="198">bias −2</text><text class="tl tc" x="290" y="160">bias −1</text></svg><figcaption>A 2-2-1 network with every weight and bias written on it. Each node adds up its weighted inputs and its bias, then outputs 1 if the total is 0 or more, and 0 otherwise.</figcaption></figure>
:::

:::eg A network with a hidden layer
The network in the figure uses a step activation (output 1 if the sum is 0 or more, otherwise 0). Work through all four input pairs and state what the network computes. [4 marks]

The sums are \(h_1: x_1 + x_2 - 1\), \(h_2: x_1 + x_2 - 2\) and \(o: h_1 - h_2 - 1\).

| x1 | x2 | h1 sum | h1 | h2 sum | h2 | o sum | o |
|---|---|---|---|---|---|---|---|
| 0 | 0 | −1 | 0 | −2 | 0 | −1 | 0 |
| 0 | 1 | 0 | 1 | −1 | 0 | 0 | 1 |
| 1 | 0 | 0 | 1 | −1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 | 1 | −1 | 0 |

- Hidden node \(h_1\) outputs 1 when at least one input is 1 (it is an OR). [B1]
- Hidden node \(h_2\) outputs 1 only when both inputs are 1 (it is an AND). [B1]
- The output node has sum \(h_1 - h_2 - 1\), which is 0 or more only when \(h_1 = 1\) and \(h_2 = 0\). [B1]
- The outputs 0, 1, 1, 0 are those of an XOR gate, so the network computes XOR. [B1]

No single node can do this, which is the reason networks have hidden layers: each layer builds on the one before.
:::

The same network in Python, checking the four inputs. This block has its own copy of the two helper functions so that it runs on its own:

```python
def step(total):
    return 1 if total >= 0 else 0


def neuron(inputs, weights, bias, activation):
    total = bias
    for x, w in zip(inputs, weights):
        total = total + x * w
    return activation(total)


def xor_network(x1, x2):
    h1 = neuron([x1, x2], [1, 1], -1, step)
    h2 = neuron([x1, x2], [1, 1], -2, step)
    return neuron([h1, h2], [1, -1], -1, step)


for x1 in (0, 1):
    for x2 in (0, 1):
        print(x1, x2, xor_network(x1, x2))
```

Output:

```output
0 0 0
0 1 1
1 0 1
1 1 0
```

### How neural networks have helped machine learning

Before neural networks, engineers often had to decide by hand which features of the data mattered (the length of a word, the number of corners in a shape) and write code to measure them. A neural network can start from the raw numbers (the pixels, the sound samples) and **learn which combinations matter**, because its weights are adjusted automatically during training. This has made problems such as recognising speech, translating languages and spotting disease in scans solvable by learning, where hand-written rules had failed. The cost is that a network needs a lot of training data and computing power, and that it is hard to say why it gave a particular answer.

## Training a network: back propagation

At the start the weights are small random numbers, so the network's answers are poor. **Training** adjusts the weights until the answers are good. This takes four ideas.

- **Error:** how far the network's output is from the correct answer for a training example. For a target of 10 and an output of 8 the error is \(10 - 8 = 2\).
- **Learning rate:** a small number that sets the size of each adjustment. Too small and learning is slow; too large and the weights overshoot.
- **Gradient descent:** adjusting every weight a small step in the direction that makes the error smaller, like walking downhill on a landscape whose height is the error. Repeating the steps reaches a low point.
- **Epoch:** one pass through the whole set of training examples. Training takes many epochs.

The difficulty is the hidden layers. The error is known only at the output, so it is not clear how much blame each hidden weight deserves. **Back propagation** solves this by working backwards.

:::def Back propagation of errors
The method used to train a neural network. After a forward pass gives an output, the error at the output is calculated and then passed backwards through the network, layer by layer, to work out how much each weight contributed to it. Each weight is then adjusted slightly to reduce the error.
:::

:::key Training a network by back propagation
1. Start with small random weights.
2. **Forward pass:** feed a training example in; each layer calculates its outputs, from the input layer to the output layer.
3. **Error:** compare the network's output with the correct output.
4. **Back propagation:** work backwards from the output layer to the input layer, finding how much each weight contributed to the error.
5. **Adjust** every weight by a small step (set by the learning rate) in the direction that reduces the error.
6. Repeat for every training example, and for many epochs, until the error is small enough.
:::

:::warn What goes backwards is the error, not the data
The data go forwards, from input to output. Back propagation does not send the data backwards. It sends the **error** backwards, so that each weight can be changed in proportion to its share of the blame.
:::

### One weight update by hand

For a node with no activation function (its output is just the weighted sum), the adjustment has a simple form:

:::formula One step of learning
\[w_{\text{new}} = w + \text{rate} \times \text{error} \times x\]
\(w\) is a weight, \(x\) is the input on that connection, error \(=\) target \(-\) output, and rate is the learning rate. A weight on a bigger input changes more, because it had more influence on the output; if the output was too small (positive error) every weight on a positive input rises.
:::

:::eg Training a node by hand
A node has two inputs, \(x_1 = 2\) and \(x_2 = 3\), and starts with weights \(w_1 = 1\) and \(w_2 = 2\). It has no bias and no activation function. The target output is 10 and the learning rate is 0.05. Carry out the first two training steps. [6 marks]

Step 1. The output is \(1 \times 2 + 2 \times 3 = 8\), so the error is \(10 - 8 = 2\). [B1] The new weights are \(w_1 = 1 + 0.05 \times 2 \times 2 = 1.2\) and \(w_2 = 2 + 0.05 \times 2 \times 3 = 2.3\). [B1] [B1]

Step 2. The output is \(1.2 \times 2 + 2.3 \times 3 = 9.3\), so the error is \(10 - 9.3 = 0.7\). [B1] The new weights are \(w_1 = 1.2 + 0.05 \times 0.7 \times 2 = 1.27\) and \(w_2 = 2.3 + 0.05 \times 0.7 \times 3 = 2.405\). [B1] [B1]

The error has fallen from 2 to 0.7 in one step, and the next output is \(1.27 \times 2 + 2.405 \times 3 = 9.755\), an error of 0.245. Each step shrinks the error.
:::

The Python below repeats the same steps with exact fractions, so the numbers match the working above.

```python
from fractions import Fraction

inputs = [2, 3]
weights = [Fraction(1), Fraction(2)]
target = 10
rate = Fraction(1, 20)

for step_number in range(1, 4):
    output = sum(w * x for w, x in zip(weights, inputs))
    error = target - output
    print("step", step_number, "weights", [float(w) for w in weights], "output", float(output), "error", float(error))
    weights = [w + rate * error * x for w, x in zip(weights, inputs)]
```

Output:

```output
step 1 weights [1.0, 2.0] output 8.0 error 2.0
step 2 weights [1.2, 2.3] output 9.3 error 0.7
step 3 weights [1.27, 2.405] output 9.755 error 0.245
```

:::warn A bigger learning rate is not always better
With a rate of 0.1 instead of 0.05, step 1 would give \(w_1 = 1.4\) and \(w_2 = 2.6\), and the new output would be \(1.4 \times 2 + 2.6 \times 3 = 10.6\). That overshoots the target of 10. If the rate is too large the weights can jump back and forth and the error may grow instead of shrinking.
:::

With hidden layers the same idea applies at every layer: back propagation gives each hidden weight its share of the output error, and the weights are all adjusted in the same way. This is what lets a deep network learn.

## Deep learning

A network with one or two hidden layers is a "shallow" network. A **deep** network has many hidden layers, sometimes hundreds. Each layer works on the output of the one before, so the layers learn in stages. In an image recogniser, the first layers learn to detect edges and small patterns, the middle layers combine these into shapes such as an eye or a wheel, and the last layers combine shapes into whole objects such as a face or a car. Nobody programs these stages: they emerge from training.

:::eg Why deep learning suits image recognition
A company wants to identify faulty parts from photographs on a factory line. Explain why deep learning is suitable. [2 marks]

- An image contains a very large number of pixel values, and the features that show a fault (a crack, a dent) are hard to describe as rules, but a deep network can learn these features itself from examples. [B1]
- Its many layers learn in stages, from edges to shapes to whole objects, which gives accurate recognition when there are enough labelled photographs and enough computing power. [B1]
:::

Reasons for choosing deep learning: the data are complex (images, sound, text); there is plenty of training data; accuracy matters more than being able to explain every decision; and the computing power is available. Reasons against: it needs large amounts of data and processing time, and it is hard to explain why it gave an answer.

## Regression

**Regression** is the part of supervised learning that predicts a number. You give the system training examples, each with inputs and a known numerical answer, and it learns a rule to predict the answer for new inputs.

:::def Regression
A machine learning method that fits a line or curve to training data in order to predict a continuous numerical value, such as a price, a temperature or a time. It is a supervised method because the training examples include the correct values.
:::

**Linear regression** fits a straight line \(y = mx + c\), where \(m\) is the slope (how much \(y\) changes when \(x\) rises by 1) and \(c\) is the intercept (the value of \(y\) when \(x = 0\)). Many lines could be drawn through a scatter of points. The **least squares** method picks the one that makes the total of the squared vertical gaps between the points and the line as small as possible.

:::formula Least squares line
\[m = \frac{\sum (x - \bar{x})(y - \bar{y})}{\sum (x - \bar{x})^2}, \qquad c = \bar{y} - m\bar{x}\]
\(\bar{x}\) and \(\bar{y}\) are the means of the \(x\) and \(y\) values. You will not need to calculate this in the exam; the worked example shows what "best fit" means.
:::

:::eg Fitting a line to data
Five students recorded their weekly revision hours \(x\) and their test mark \(y\) out of 10: (1, 3), (2, 5), (3, 4), (4, 7), (5, 6). Find the least squares line and use it to predict the mark for 3.5 hours. [5 marks]

The means are \(\bar{x} = 3\) and \(\bar{y} = 5\). The two sums are

\[\begin{aligned} \sum (x - \bar{x})(y - \bar{y}) &= (-2)(-2) + (-1)(0) + (0)(-1) + (1)(2) + (2)(1) = 8 \\ \sum (x - \bar{x})^2 &= 4 + 1 + 0 + 1 + 4 = 10 \end{aligned}\]

[B1]

The slope is \(m = 8 \div 10 = 0.8\). [B1] The intercept is \(c = 5 - 0.8 \times 3 = 2.6\). [B1] The line is \(y = 0.8x + 2.6\). [B1]

For 3.5 hours the predicted mark is \(0.8 \times 3.5 + 2.6 = 5.4\). [B1]

The line is a model: each extra hour of revision is linked to 0.8 extra marks, within the range of the data.
:::

:::plot The least squares line \(y = 0.8x + 2.6\) through the five revision points.
--f "0.8*x+2.6" --x 0 6.5 --y 0 9 --pt "1,3" --pt "2,5" --pt "3,4" --pt "4,7" --pt "5,6" --label "y = 0.8x + 2.6" --xlabel "hours" --ylabel "mark" --legend tr --alt "A straight line rising from 2.6 at 0 hours to 7.4 at 6 hours, with five points scattered close to it: (1, 3), (2, 5), (3, 4), (4, 7) and (5, 6)."
:::

The line misses most points by a little. The gaps (called errors or residuals) are \(-0.4, 0.8, -1.0, 1.2\) and \(-0.6\), and their squares add up to 3.6, the smallest total any straight line can give for these points. The Python below confirms the slope, the intercept, the prediction and the 3.6, using exact fractions.

```python
from fractions import Fraction

hours = [1, 2, 3, 4, 5]
marks = [3, 5, 4, 7, 6]
n = len(hours)
mean_x = Fraction(sum(hours), n)
mean_y = Fraction(sum(marks), n)
sxy = sum((x - mean_x) * (y - mean_y) for x, y in zip(hours, marks))
sxx = sum((x - mean_x) ** 2 for x in hours)
slope = sxy / sxx
intercept = mean_y - slope * mean_x
print("slope", slope, "intercept", intercept)
print("prediction for 3.5 hours:", slope * Fraction(7, 2) + intercept)
print("sum of squared errors:", sum((y - (slope * x + intercept)) ** 2 for x, y in zip(hours, marks)))
```

Output:

```output
slope 4/5 intercept 13/5
prediction for 3.5 hours: 27/5
sum of squared errors: 18/5
```

The fractions are \(0.8\), \(2.6\), \(5.4\) and \(3.6\). Linear regression is a very simple "model" with two adjustable numbers, \(m\) and \(c\), and it is trained by the same idea as a neural network: choose the numbers that make the squared error as small as possible.

:::warn Regression predicts numbers; classification predicts categories
"Will this email be spam?" has a category as its answer (spam or not spam), so it is **classification**. "How many minutes will this delivery take?" has a number as its answer, so it is **regression**. Both are supervised learning, because both are trained on labelled examples. A regression line should also be used only for \(x\) values inside the range of the training data: far outside it the straight line may be nonsense.
:::

## Choosing a method, and the limits

| Situation | Method | Reason |
|---|---|---|
| Past records with known correct outcomes, predict a category | supervised classification | learns from labelled examples |
| Past records with a known number, predict a number | regression (supervised) | fits a line or curve to labelled numbers |
| Data with no labels, find groups | unsupervised learning | finds structure without answers |
| No data, but actions can be tried and scored | reinforcement learning | learns from rewards |
| Images, sound or text with a lot of data | deep learning | learns features itself, in layers |

Machine learning has limits that you should be able to describe.

- **Data quality:** a system can only learn what its data show. Mistakes, gaps and out-of-date records are learned too.
- **Bias:** if the training data under-represent some group of people, or record earlier unfair decisions, the system repeats them. This links to [Ethics, ownership and the impact of AI](#cs.ethics).
- **Explainability:** a deep network may be accurate, but it is hard to say why it decided as it did, which matters when the decision affects a person (a loan, a medical diagnosis).
- **Cost:** training a large network needs a great deal of data, time and electricity.
- **Privacy:** training data often contain personal information, which must be protected.

:::exam How to write machine learning answers
- Name the type exactly (supervised, unsupervised, reinforcement) and give a reason taken from the scenario: "the emails are labelled", "no labels", "it receives rewards".
- For back propagation, say that the **error** is passed backwards and the **weights** are adjusted. Do not say that data or the inputs go backwards.
- For "describe how a network is trained", write the loop in order: forward pass, compare with the target, propagate the error back, adjust the weights, repeat.
- For "justify" questions, tie each point to the data in the scenario (how much data there is, whether it is labelled, whether an explanation is needed).
- For calculations, show the weighted sum with every term, then apply the activation function, as in the worked examples.
:::

:::eg Spot the error: describing back propagation
Question: Describe how an artificial neural network is trained using back propagation. [4 marks]

A student wrote: "A training example is fed into the network and it gives an output. The output is compared with the correct answer to find the error. Back propagation then sends the input data backwards through the network from the output to the input. The weights are adjusted to make the error smaller."

The first sentence describes a forward pass that gives an output [B1]. The second compares the output with the correct answer to find an error [B1]. **The third sentence says the input data go backwards. What goes backwards is the error: it is passed back through the layers to work out how much each weight contributed, so this mark point is not earned** [B0]. The last sentence, adjusting the weights to reduce the error, is correct [B1]. The answer scores 3 out of 4. (The mark scheme also credits saying that the process is repeated for many examples, so the student could have recovered the mark by adding that.)

A corrected third sentence: "The error is then passed backwards through the network, layer by layer, to find how much each weight contributed to it."
:::

:::try Start easy, finish at exam standard
Q: State whether each task is classification or regression: (a) deciding whether a bank transaction is fraudulent; (b) predicting the number of litres of water a farm will use next week; (c) saying which of 26 letters a handwritten character is.
A: (a) Classification: the answer is a category (fraud or not). (b) Regression: the answer is a number. (c) Classification: the answer is one of 26 categories.
Q: A node has inputs 2 and 5, weights 3 and −1, and bias −1, and uses a step activation (1 if the sum is 0 or more, otherwise 0). Work out its output.
A: \(S = 3 \times 2 + (-1) \times 5 + (-1) = 6 - 5 - 1 = 0\). The sum is 0, which is 0 or more, so the output is 1.
Q: A node has inputs 3 and 1, weights −2 and 1, and bias 0, and uses ReLU. Work out its output.
A: \(S = (-2) \times 3 + 1 \times 1 + 0 = -5\). ReLU gives 0 for a negative sum, so the output is 0.
Q: A node (no bias, no activation) has inputs 1 and 2 and weights 3 and 1. The target is 4 and the learning rate is 0.1. Work out the output, the error and the new weights after one step.
A: Output \(3 \times 1 + 1 \times 2 = 5\). Error \(4 - 5 = -1\). \(w_1 = 3 + 0.1 \times (-1) \times 1 = 2.9\) and \(w_2 = 1 + 0.1 \times (-1) \times 2 = 0.8\). The new output is \(2.9 + 1.6 = 4.5\), closer to 4 than 5 was.
Q: How many weights does a network with 4 input nodes, 5 hidden nodes and 3 output nodes have (ignoring biases)?
A: \(4 \times 5 = 20\) from the inputs to the hidden layer and \(5 \times 3 = 15\) from the hidden layer to the outputs: 35 weights.
Q: A regression line for the time to cook a roast is \(y = 3x + 4\), where \(x\) is its mass in kg and \(y\) is the time in minutes. Predict the time for 5 kg, and say what the 4 means.
A: \(y = 3 \times 5 + 4 = 19\) minutes. The 4 is the intercept: the value of \(y\) when \(x = 0\) (a fixed amount of time that does not depend on mass).
Q: A robot learns to sort parcels. It tries a way of picking up each parcel and receives +1 if the parcel is placed in the correct bin and −1 if not. Name the agent, the environment, an action and the reward.
A: The agent is the robot's control program. The environment is the sorting area with the parcels and bins. An action is a way of picking up or placing a parcel. The reward is +1 or −1.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ State the type of machine learning (supervised, unsupervised or reinforcement) in each case. (a) A streaming service groups its viewers by their watching habits, with no group names given. (b) A program predicts a student's final grade from the records of past students, whose final grades are known. (c) A robot arm learns to stack boxes by trying actions and receiving a score for each tower that stays upright.
A: One mark each:

- (a) unsupervised learning [B1]
- (b) supervised learning [B1]
- (c) reinforcement learning [B1]

Q: [2 marks] ★ Explain why deep learning is suitable for a system that recognises spoken words.
A: Two points:

- speech sounds contain a great deal of data and the features that separate one word from another are hard to write as rules, so the network learns the features itself [B1]
- the many layers learn in stages (small sound patterns, then syllables, then words), which gives accurate recognition when there is plenty of training data [B1]

Q: [2 marks] ★ A node has inputs 3 and 2, weights 2 and −1, and bias −3. It uses a step activation, outputting 1 if the weighted sum is 0 or more and 0 otherwise. Work out the weighted sum and the output.
A: The weighted sum is \(2 \times 3 + (-1) \times 2 + (-3) = 6 - 2 - 3 = 1\) [B1]. This is 0 or more, so the output is 1 [B1].

Q: [5 marks] ★★ Describe how an artificial neural network is trained using back propagation of errors.
H: Think of a loop: what goes forwards, what is compared, what goes backwards, what changes, and how long it continues.
A: One mark for each of five points:

- the weights start as small random values [B1]
- a training example is fed forward through the layers to produce an output [B1]
- the output is compared with the correct (target) output to calculate the error [B1]
- the error is passed backwards through the layers, to find how much each weight contributed to it, and each weight is adjusted by a small amount (the learning rate) to reduce the error [B1]
- the process is repeated for all the training examples, many times (epochs), until the error is small [B1]

Q: [4 marks] ★★ A delivery company uses the regression line \(y = 2.5x + 10\) to predict delivery time \(y\) in minutes from distance \(x\) in km. (a) Predict the time for a delivery of 8 km. [1] (b) Explain why training this line is an example of supervised learning. [1] (c) State why this is regression and not classification. [1] (d) State one type of output that would make it a classification problem. [1]
A: (a) \(2.5 \times 8 + 10 = 30\) minutes [B1]. (b) The line was fitted to past deliveries where both the distance and the actual time were known, which are labelled examples [B1]. (c) The output is a number (a continuous value) [B1]. (d) A category, such as "late" or "on time" [B1].

Q: [4 marks] ★★ A network has two inputs \(x_1 = 2\) and \(x_2 = 1\), two hidden nodes and one output node, all using ReLU (the output is the weighted sum if it is positive, otherwise 0). Hidden node \(h_1\) has weights 1 and 2 and bias 0. Hidden node \(h_2\) has weights −3 and 1 and bias 1. The output node has weights 2 (from \(h_1\)) and 5 (from \(h_2\)) and bias −1. Work out the output of the network.
H: Do the hidden nodes first, then use their outputs as the inputs of the output node.
A: \(h_1\): \(1 \times 2 + 2 \times 1 + 0 = 4\), and ReLU gives 4 [B1]. \(h_2\): \(-3 \times 2 + 1 \times 1 + 1 = -4\), and ReLU gives 0 [B1]. Output node: \(2 \times 4 + 5 \times 0 - 1 = 7\) [B1]. ReLU gives 7, so the output is 7 [B1].

Q: [6 marks] ★★★ A hospital in Accra has 40,000 chest X-ray images. A doctor has labelled each image "normal" or "needs review". The hospital wants a system to flag images for doctors. Justify the use of a deep learning (neural network) approach, and state one limitation the hospital should plan for.
H: Think about what the data look like, whether they are labelled, and what the network learns.
H: A limitation could be about explanation, bias or data.
A: One mark for each of six points:

- the images are labelled, so supervised learning can be used to train the network [B1]
- there is a large amount of data (40,000 images), which deep learning needs to work well [B1]
- an image has a very large number of pixel values, and the signs of disease are hard to describe as rules [B1]
- a deep network can learn the important features itself, from simple edges to complex shapes [B1]
- it can learn to flag images accurately and quickly, so doctors see the urgent cases first [B1]
- limitation: the decisions are hard to explain, so a doctor must check flagged and unflagged images (or the images may come from one group of patients, which gives a biased system; or training needs a lot of computing power) [B1]

Q: [5 marks] ★★★ A node has two inputs \(x_1 = 4\) and \(x_2 = 1\) and starts with weights \(w_1 = 2\) and \(w_2 = 3\). It has no bias and no activation function, so its output is the weighted sum. The target output is 15 and the learning rate is 0.05. Using \(w_{\text{new}} = w + \text{rate} \times \text{error} \times x\), (a) work out the output and the error before training. [2] (b) Work out the new weights after one step. [2] (c) Work out the new output and state what has happened to the error. [1]
H: The error is target minus output.
A: (a) Output \(2 \times 4 + 3 \times 1 = 11\) [B1]. Error \(15 - 11 = 4\) [B1].

(b) \(w_1 = 2 + 0.05 \times 4 \times 4 = 2.8\) [B1]. \(w_2 = 3 + 0.05 \times 4 \times 1 = 3.2\) [B1].

(c) New output \(2.8 \times 4 + 3.2 \times 1 = 14.4\), so the error has fallen from 4 to 0.6 [B1].
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A solar farm records the hours of sunshine per day \(x\) and the electricity generated \(y\) (in kWh): (2, 10), (4, 14), (6, 13), (8, 19). Use the least squares formulas to find the regression line, then predict the output for 7 hours of sunshine. Work with exact values.
H: Find the means first: \(\bar{x}\) is the average of the four \(x\) values.
H: The slope is \(\sum (x - \bar{x})(y - \bar{y})\) divided by \(\sum (x - \bar{x})^2\).
A: \(\bar{x} = (2 + 4 + 6 + 8) \div 4 = 5\) and \(\bar{y} = (10 + 14 + 13 + 19) \div 4 = 14\) [B1] [B1].

\(\sum (x - \bar{x})^2 = 9 + 1 + 1 + 9 = 20\) [B1].

\[\sum (x - \bar{x})(y - \bar{y}) = (-3)(-4) + (-1)(0) + (1)(-1) + (3)(5) = 26\]

[B1]

The slope is \(26 \div 20 = 1.3\) and the intercept is \(14 - 1.3 \times 5 = 7.5\), so \(y = 1.3x + 7.5\) [B1].

For 7 hours, \(y = 1.3 \times 7 + 7.5 = 16.6\) kWh [B1].

Q: [5 marks] ★★★ A robot vacuum cleaner learns whether to clean the kitchen first. It keeps an estimate \(V\) of the value of that choice, starting at 0, and after each day it updates \(V \leftarrow V + 0.25 \times (\text{reward} - V)\). The rewards on three days are 8, 8 and 4. (a) Work out \(V\) after each day. [3] (b) State the type of machine learning and explain why it is not supervised learning. [2]
H: Use the new \(V\) each time as the old \(V\) for the next day.
A: (a) Day 1: \(V = 0 + 0.25 \times (8 - 0) = 2\) [B1]. Day 2: \(V = 2 + 0.25 \times (8 - 2) = 3.5\) [B1]. Day 3: \(V = 3.5 + 0.25 \times (4 - 3.5) = 3.625\) [B1].

(b) Reinforcement learning [B1], because the robot learns from rewards for what it tries, with no labelled correct answers telling it the right choice in advance [B1].
:::

:::quiz
? Which statement about AI, machine learning and deep learning is correct?
- Machine learning is a kind of deep learning.
+ Deep learning is a kind of machine learning, which is a way of building AI.
- Deep learning and AI are the same thing.
- AI always involves learning from data.
> The three ideas are nested: deep learning inside machine learning inside AI. Systems such as the A* route finder are AI without any learning, so AI does not always involve learning.
? Which type of machine learning needs labelled training data?
+ Supervised learning
- Unsupervised learning
- Clustering
- Reinforcement learning
> Supervised learning learns from examples that include the correct answer. Unsupervised learning (including clustering) works without labels, and reinforcement learning uses rewards instead.
? In reinforcement learning, what does the agent learn from?
- A set of labelled examples.
- Groups found in unlabelled data.
+ Rewards and penalties for the actions it tries.
- A programmer's list of rules.
> The agent tries actions in an environment and is rewarded or penalised. There is no labelled correct answer, which is why it is not supervised learning.
? A node has inputs 1 and 1, weights 2 and 1, and bias −2, with a step activation (1 if the sum is 0 or more). What is its output?
- 3
- 0
+ 1
- −2
> The weighted sum is \(2 + 1 - 2 = 1\), which is 0 or more, so the output is 1. The answer 3 is the sum without the bias, and −2 is the bias on its own.
? What does back propagation send backwards through the network?
- The input data.
+ The error, to work out how much each weight contributed to it.
- The final answer, to be used as a new input.
- The training examples, in reverse order.
> The data go forwards from input to output. The error is calculated at the output and passed backwards so that every weight can be adjusted by its share.
? What does regression predict?
- A category, such as spam or not spam.
- A group of similar items.
+ A number, such as a price or a time.
- A reward.
> Regression predicts a continuous numerical value. Predicting a category is classification, and finding groups is unsupervised learning.
? What does the word "deep" in deep learning refer to?
- The network understands the data deeply.
+ The network has many hidden layers.
- The network is stored deep in memory.
- The network needs deep knowledge of the subject.
> A deep network is one with many hidden layers, which let it learn features in stages.
? A loan system trained on past decisions rejects applicants from one area far more often than similar applicants from elsewhere. What is the most likely cause?
- The learning rate was too small.
+ The training data contained earlier unfair decisions, which the system learned.
- Neural networks cannot process addresses.
- The system used reinforcement learning.
> A system learns whatever patterns its data contain, including unfair ones. This is bias in the training data, and it is a common limit of machine learning.
? A node with no bias has inputs 2 and 3, weights 1 and 2 and a target of 10. With a learning rate of 0.1 the weights become 1.4 and 2.6. What is wrong with this learning rate?
- Nothing: the output now equals the target.
+ It is too large: the new output is 10.6, which overshoots the target of 10.
- It is too small: the output is still 8.
- It changes the inputs instead of the weights.
> The new output is \(1.4 \times 2 + 2.6 \times 3 = 10.6\). The error was 2 and the update was too big, so the output went past the target instead of settling on it.
:::

:::checklist What you can now do
- [ ] I can define machine learning and deep learning and explain how they relate to AI.
- [ ] I can state the reasons for using machine learning, deep learning and reinforcement learning.
- [ ] I can distinguish supervised, unsupervised and reinforcement learning and name the type for a scenario.
- [ ] I can describe the structure of an artificial neural network: input, hidden and output layers, nodes, weights and activation functions.
- [ ] I can calculate the output of a node from its inputs, weights, bias and activation function.
- [ ] I can explain how neural networks have helped machine learning.
- [ ] I can describe how a network is trained using back propagation of errors, including the forward pass, the error, the backward pass and the weight update.
- [ ] I can explain what regression is, why it is supervised, and how it differs from classification.
- [ ] I can describe the limits of machine learning: data quality, bias and explainability.
:::

:::recap
- AI is the wide field, machine learning is learning from data inside it, and deep learning is machine learning with neural networks of many hidden layers.
- Supervised learning uses labelled data (classification predicts a category, regression predicts a number); unsupervised learning finds structure in unlabelled data; reinforcement learning learns by trial and error from rewards.
- An artificial neural network has an input layer, hidden layers and an output layer. A node adds its weighted inputs and bias, then applies an activation function (step or ReLU).
- Training: random weights, forward pass, error, back propagation of the error (not the data), small weight adjustments set by the learning rate, repeated over many epochs.
- Weight update for a plain node: \(w_{\text{new}} = w + \text{rate} \times \text{error} \times x\).
- Deep learning learns features in layers and suits large, complex data such as images and speech, but needs much data and computing power and is hard to explain.
- Linear regression fits \(y = mx + c\) by least squares. Limits of machine learning: data quality, bias, explainability, cost and privacy.
:::

:::links
- practise: [AI: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/18-artificial-intelligence-ai-/artificial-intelligence-ai/exam-questions/) · Save My Exams · 9618-style questions with mark schemes [paid]
- watch: [But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk) · 3Blue1Brown · a clear picture of layers, weights and learning
- read: [Neural networks lessons](https://www.3blue1brown.com/lessons/neural-networks) · 3Blue1Brown · the whole series, including back propagation
- explore: [TensorFlow Playground](https://playground.tensorflow.org/) · TensorFlow Playground · train a small neural network in the browser and watch the weights change
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos by university computer scientists on machine learning

Links checked 13 November 2026.
:::

Next: [Searching, sorting and Big O](#cs.algorithms2)
