# Rocket football

<img width="545" height="392" alt="image" src="https://github.com/user-attachments/assets/09485f3c-a7a9-4a50-8903-8338de3c725f" />


View the demo video at https://www.youtube.com/shorts/yagwG0tLJ1o?is=GJSgdv2bLIIDCHmR.


# What is Rocket Football
Rocket football is a game which based on the popular video game Rocket League, Rocket League is a video game where you drive cars around into balls and the objective is to basically play football with the cars. Rocket football is the in real life version of rocket league where we custom made 2 rovers which use 2 N20 geared motors each to drive around each cart. The motors are controlled with a H bridge motor driver which recieves power from out NRF Super mini which is controlled by the nRF52840. The controllers which are used to drive the cars also use the same nRF52840 devboard and are connected to 4 cherry MX switches, these switches when pressed use the nRF42840's onboard bluetooth functionality to to send commands to the car and drive the ball forward.

# How did we built rocket football
 We built Rocket football as a part of a hackathon which I attended. The theme for this hackathon was to make an interactive project for open sauce 2026, While our original idea was too make a claw machine we realised that we didn't have all the necessary equipment in order for us to make one. In the end we settled on this project as we had everything we needed to make it and we believed we could do it

# Day 1
 We started off this project on the first day of the hackathon by CAD modelling the case for the cars and controllers and then figured out what components we would need to make this project work. We ended up with a final components list of the components we needed to make the project as well as a fully CAD modelled car and controller

# Day 2
 We used a breadboard to make a working prototype of the car and finalise the firmware we needed for the car and controller to work
 We then tried to transfer everything to protoboard however this took a long time as at first our project wouldn't work and we had to debug the code to get it too work. There was also some extensive problems with the hardware caused by a broken H bridge

 I also designed and made the pitch this game would be played on.

# Day 3
 We finally made the car work near the end of the hackathon and we also made the controller work, we very quickly made a duplicate of the car where both will be used to play the game. We also made and uploaded everything to github and made the BOM for all the components this project uses.

# BOM
* 4x nRF52840's - used in the cars and controllers
* 2x H-bridge drivers - used to drive the motors in the car
* 4x Motors - N20 geared motors which were driven by the H-bridge and were used to make the car drive
* 8x Cherry MX keys - used in the controller
* 4x batteries - powers the controllers and cars
* 2x cardboard boxes - used to make the pitch
* 4x 3d printed parts - enclosure of the controllers and the cars
* 1x sheet of foam - used to make the 2nd pitch

WE GOT ALL OF THESE PARTS AT THE HARDWARE STATION AT Outpost hackathon or elsewhere around the hackathon venue
