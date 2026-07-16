# Rocket Football

![Rocket Football](https://github.com/user-attachments/assets/09485f3c-a7a9-4a50-8903-8338de3c725f)

**Demo Video:** https://www.youtube.com/shorts/yagwG0tLJ1o?is=GJSgdv2bLIIDCHmR

---

# What is Rocket Football?

Rocket Football is a real-world version of the popular video game **Rocket League**. In Rocket League, players drive cars into a giant ball and compete to score goals in a soccer-style game.

For Rocket Football, we built two custom RC cars that allow players to recreate that experience in real life. Each car is powered by two N20 geared motors controlled by an H-bridge motor driver. An nRF52840-based SuperMini development board handles the motor control and communicates over Bluetooth.

The handheld controllers also use nRF52840 development boards. Each controller has four Cherry MX switches that send movement commands over Bluetooth to the corresponding car, allowing players to drive around the field and push the ball toward the goal.

---

# How We Built Rocket Football

We built Rocket Football during the Outpost hackathon. The challenge was to create an interactive project for Open Sauce 2026.

Our original idea was to build a claw machine, but we quickly realized we did not have the equipment or time required to complete it. Instead, we chose to build Rocket Football because we already had access to the necessary parts and believed we could finish it before the end of the event.

---

# Day 1

On the first day, we designed the CAD models for both the cars and the controllers. We also planned the electronics and created a complete bill of materials for the project.

By the end of the day, we had:

* v1 of CAD models for the cars and controllers
* Finalized BOM
* Wiring diagram

---

# Day 2

We built a working prototype of the car on a breadboard and finalized the firmware for both the cars and controllers.

After confirming the prototype worked, we transferred the electronics to protoboard. This process took much longer than expected because the project initially stopped working. We spent a significant amount of time debugging both the firmware and the hardware before discovering that one of the H-bridge motor drivers was faulty.

During this time, I also designed and built the playing field for the game.

---

# Day 3

Near the end of the hackathon, we successfully completed the first car and controller. We then quickly assembled a second identical car so that two players could compete against each other.

We also:

* Published the project on GitHub
* Created the bill of materials (BOM)
* Finished the remaining assembly and testing

---

# Bill of Materials (BOM)

* **4× nRF52840 development boards**
* **2× H-bridge motor drivers**
* **4× N20 geared motors**
* **8× Cherry MX switches**
* **4× LiPo batteries**
* **2× Cardboard boxes**
* **4× 3D-printed parts**
* **1× Foam board sheet**

---

# Parts

All of the components used in this project were sourced from the hardware station at the Outpost Hackathon or from other supplies available around the hackathon venue.
