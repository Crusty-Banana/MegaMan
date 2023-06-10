gym retro version: 0.21.0

```
python -m venv .venv
pip install gym==0.21.0
python -m retro.import .
```

Todo:
1. Define what is in a state
2. Define action space
3. Define reward 
4. Established learning rate $\alpha$
5. Established discounting factor $\gamma$ 
6. Established initial policy $\pi$ 
7. Established exploration strategy

<h2> I. Definition of a State</h2>

- Health: How much health Mega Man have left $[0, 24]$  
- Lives: How many death can Mega Man have before Game Over $[0, 3]$
- Progress: How much progress have he make, his x coordinate on the map $[0, +\infty]$ and his y coordinate on the map.
- Position of character on the screen.
- Checkpoint
- (y_pos, x_pos, checkpoint, health)
<h2> II. Action space</h2>

- Move left, right.
<!-- - Climb up, down at ladder -->
- shoot
- jump (how high?)

<h2> III. Reward</h2>

learning rate: $\alpha = $
discounting factor: $\gamma = $
exploring constant: $k = $
formula: $Q(s, a) = \alpha[R(s, a, s') + \gamma$ $\underset{a'}{max} (Q(s', a') + k / N(s', a'))]$
$R(s, a, s') = x_1(progress[s'] - progress[s]) + x_2(checkpoint[s'] - checkpoint[s]) + x_3(health[s'] - health[s])$
$N(s, a) += 1$

<h2> IV. Initial policy </h2>

- move right
- shoot and jump periodically

<h2> VIII. Exploration strategy </h2>

Epsilon Greedy

<h2> Data storage <h2> 

Python matrix pickle

