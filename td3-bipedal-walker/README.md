# TD3 on BipedalWalker

Reinforcement learning coursework: a Twin Delayed DDPG (TD3) agent trained to
walk in OpenAI Gym's `BipedalWalker-v3`, with `BipedalWalkerHardcore-v3` as the
harder variant.

Written in Google Colab, which is where the GPU and the video rendering came
from, so it is a notebook rather than a package.

## What is in it

- `Actor` and `Critic` networks, and a `TD3` class implementing the three ideas
  the algorithm is named for: twin critics with the minimum taken to damp
  overestimation, a delayed policy update (`policy_delay = 2`), and smoothing
  noise on the target action (`policy_noise = 0.2`, clipped at `0.5`).
- `ReplayBuffer`, a fixed-size circular buffer sampled uniformly.
- A decaying exploration-noise schedule. This was the part I actually
  experimented with: `noise_eq` shapes the noise as a cosine over the episode
  count rather than holding it constant, to reach a score of 300 in fewer
  episodes. A commented-out variant of the equation is left in the cell beside
  the one that worked best.
- Soft target updates with `polyak = 0.995`, and a reward plot with a shaded
  variance band.

The seed is fixed at 42, which was the seed requested for marking.

## Running it

Open it in Colab. The first cell pins an old toolchain —
`gym[box2d]==0.20.0`, `pyglet==1.5.27`, `setuptools==65.5.0` — and installs
`xvfb` so the environment can be rendered headlessly to capture videos. Those
pins matter: the Box2D environments and the virtual display do not work with
current versions without changes.

`max_episodes` is set to 10 in the committed version, which trains nothing
useful; raise it to see the agent learn.

## Credit

The TD3 implementation draws on the paper (Fujimoto et al.,
[arXiv:1802.09477](https://arxiv.org/abs/1802.09477)) and on several reference
implementations, listed in the notebook's first cell and in the report:
[nikhilbarhate99/TD3-PyTorch-BipedalWalker-v2](https://github.com/nikhilbarhate99/TD3-PyTorch-BipedalWalker-v2),
[sfujim/TD3](https://github.com/sfujim/TD3) and OpenAI Spinning Up. The
environment setup and video-capture scaffolding came from the module's starter
notebook and were left as provided.

Outputs were stripped before committing, so the saved videos and reward plots
are not here.
