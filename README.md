# snowflake
DIY alternative to the very cool Flipper Zero project.  You can read more about
that project on their GitHub page or Kickstarter:
https://github.com/Flipper-Zero

The purpose of this Snowflake project is to consolidate some of the
functionality of various project in a single DIY project.  The primary goal
of this project is a beginer to mid-level project using off the shelf parts and
standard home shop tools (e.g. screwdrivers, soldering iron, 3d printer) The 
plans and "how to" for the hardward will also be linked here once I finish
writing up those instructions.

This goal has driven the choice to use Python for the majority of the front end.
My hope is that the framework I have built for the menu system encourages experiments
and tinkering from the end user.  The hardware has also been optimized for ease
of construction and cost, instead of being super slick.  That said, I will also 
be releasing the Eagle files for a custom board if you want to take it to that
next step.

This work is primarily a frontend to the P4wnP1 project that builds 
upon a minimal Kali Linux distribution and adds a nice Web interface and 
scripting language.  Check out that project here: 
https://github.com/RoganDawes/P4wnP1_aloa

This repo contains a user interface for a screen attached directly
to the Raspberry Pi Zero W giving you control over most of the key functions.
It works in conjunction with the A.L.O.A user interface (see paragraph above), and
of course you can always just ssh into a pretty standard Kali envirnoment, and
run things from there.

FAQ:
1. Why did you use Python? It is slow.

The goal here was something friendly to tinkering.  I may do a C port later if 
there is enough interest.  Or maybe you want to and contribute it back....

2. Why is this code so crappy?

First, mean.  Second, yeah it's not great.  This started as a quick one day project
and grew in scope a little.  It is actually my first Python project that isn't just
a temporary script.  I am normally a Java guy. Please do make improvements and
submit pull requests.  I will accept anything that keeps with the primary goal
of DIY.

3. Flipper is much better, it can do ....

Yup, you are correct.  It is a great product and I also preordered one.  You will
spend more time, money, and energy on this project and get worse results.  The 
goal was just to encourage people to get their hands dirty and demystify prototype
hardware development

4. Can I buy one?

No.  It's free, that's the whole point.

5. Where did the name come from?

It's fictional dolphins all the way down.

6. This project is dumb.

That's really more of a statement...



TODO: Link to hardward BOM

TODO: Link to assembly video

TODO: upload an image for the sd card
