2D Gravity Simulation (Python + Pygame)

This project is an object-oriented 2D gravity simulator built using Python, Pygame, and Euler’s method for numerical integration.
It provides two simulation modes:

Fixed-object environment:
Large, stationary bodies act as gravitational sources while smaller particles move based on Newtonian physics.

Interactive mass placement:
Allows users to place large mass objects dynamically on the screen and observe how they influence smaller bodies.

The project is designed as an educational tool for understanding classical mechanics, numerical integration, and basic physics simulation in Python.

✨ Features
🔹 Realistic Newtonian Gravity

Simulates gravitational attraction between bodies

Supports both stationary and dynamic mass objects

Configurable mass, initial velocity, and particle behavior

🔹 Euler Integration

Uses forward Euler’s method to update position and velocity

Simple and efficient for real-time visualization

Demonstrates limitations and characteristics of basic integrators

🔹 Two Simulation Modes
1. Fixed Mass Simulation

Large fixed objects act as gravity wells

Smaller particles orbit, fall, or scatter depending on initial conditions

Great for visualizing multi-body attraction

2. Interactive Placement Mode

Click to add large mass objects

Real-time interaction with the gravitational field

Experiment with custom setups and dynamic systems

🔹 Object-Oriented Design

Body class for planets/masses

Particle class for small moving bodies

Simulation engine manages updates, rendering, and physics

Clean separation between physics logic and rendering

🛠️ Technologies Used

Python 3.x

Pygame for rendering & event handling

OOP architecture for modular, maintainable code

Euler’s Method for numerical integration

▶️ Running the Simulation
1. Install dependencies
pip install pygame

2. Run one of the simulation modes
Fixed objects + particles:
python fixed_simulation.py

Interactive mass placement:
python interactive_simulation.py

Rendering

Particles are drawn as small points or circles

Large masses are rendered at fixed or clicked positions

Trails or fading effects can optionally be added

📈 Future Improvements (Optional)

Improved integrator (RK4, Verlet)

Collision detection & merging masses

Orbital trails

Adjustable gravity constant, time-step, and particle count

UI for real-time parameter tuning
