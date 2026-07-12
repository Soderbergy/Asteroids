# Asteroids

A clone of the classic arcade game **Asteroids**, built in Python with
[Pygame](https://www.pygame.org/). Fly a ship, blast asteroids into smaller
pieces, and don't get hit.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.6-green?style=flat)

## Gameplay

- Asteroids spawn from the screen edges and drift across the field.
- Shooting a large asteroid **splits it** into two smaller ones; the smallest
  are destroyed outright.
- Colliding with any asteroid ends the game.

## Controls

| Key | Action |
| --- | --- |
| `W` / `S` | Move forward / backward |
| `A` / `D` | Rotate left / right |
| `Space` | Shoot (with a cooldown) |

## Run it

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Play
python3 main.py
```

## How it works

The game is built around a small object-oriented design. `CircleShape` is a base
`pygame.sprite.Sprite` that gives every object a position, velocity, radius, and
circle-based collision test. Everything else inherits from it:

```
main.py            game loop: spawn, update, collide, draw
constants.py       tunable values (speeds, sizes, spawn rate)
circleshape.py     base sprite with position + collision
player.py          the ship — movement, rotation, shooting
shot.py            bullets fired by the player
asteroid.py        an asteroid, including its split() behavior
asteroidfield.py   spawns asteroids over time from the edges
```

Pygame sprite groups drive the update/draw loop, so adding a new entity is just a
matter of subclassing `CircleShape` and assigning it to the right groups.

---

Built as a project while learning game development and OOP in Python.
