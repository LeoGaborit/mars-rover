### This project will be only in ENGLISH
# R3.04 : Mars Rover

## Your Task
You're part of the team that explores Mars by sending remotely controlled vehicles to the surface of the planet.

Develop an API that translates the commands sent from Earth to instructions that are understood by the rover. This API helps to move a rover around on a grid.

## Requirements
- You are given the initial starting point `(x, y)` of a rover and the direction `(N, S, E, W)` it is facing.
- The rover receives a character array of commands.
- Implement commands that move the rover forward/backward (`f`, `b`).
- Implement commands that turn the rover left/right (`l`, `r`).
- Implement wrapping from one edge of the grid to another (planets are spheres, after all).
- Implement obstacle detection before each move to a new square.
  - If a given sequence of commands encounters an obstacle, the rover moves up to the last possible point, aborts the sequence, and reports the obstacle.
- You will need to amend your code to take in an array of obstacles.

---

## Example
A robot situated at `(0, 0)` and facing North on a 100x100 grid will end up at `(2, 2)` and face East if it is given the commands `"ffrff"`.

---

## Additional Information
- This project must be completed in pairs to implement the best practices of **pair programming**.

![Image of Spirit Rover](https://upload.wikimedia.org/wikipedia/commons/f/f8/KSC-03PD-0786.jpg)
