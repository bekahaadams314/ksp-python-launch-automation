# KSP: Python Launch Automation & Orbital Mechanics
A project that utilizes Python to automate launch sequences and navigate orbital mechanics within Kerbal Space Program (KSP), a spaceflight simulator and sandbox game where you can create rockets and launch them! This repository bridges the gap between theoretical physics and applied systems engineering by programmatically controlling spacecraft to achieve stable orbits.

The primary goal is to move beyond manual piloting and utilize mathematical modeling, continuous mathematics, and automation logic to optimize ascent trajectories, manage staging, and execute precise gravity turns. What once started as a simple project to enhance the gaming experience became something bigger. 

## Methodology
- **Language & Interface:** Python, integrating with the [kRPC mod](https://krpc.github.io/krpc/index.html) for KSP to enable remote procedure calls and telemetry streaming.
- **Mathematical Approach:** Applying ordinary differential equations (ODEs) and kinematic principles to model the flight path, adjusting thrust and pitch dynamically to counteract atmospheric drag and gravity.
- **Control Systems:** Utilizing feedback loops to maintain optimal thrust-to-weight ratios and precise attitude control during atmospheric ascent.

## Future Directions
While the current script reliably achieves Low Kerbal Orbit (LKO), future iterations will expand the complexity of the automated systems:
- **PID Controller Integration:** Implementing proportional-integral-derivative (PID) controllers for smoother and more robust throttle and steering management.
- **Interplanetary Trajectories:** Expanding the scope to include automated Hohmann transfer orbits and planetary rendezvous calculations.

I am also open to other suggestions as to what I should try! This is just a fun project I love coming back to when I have time.
