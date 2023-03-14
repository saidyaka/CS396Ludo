# CS 339 Artificial Life Final Project 

>TLDR/Just want to run?: 
>> if you want to see the first and the best robot run 'python3 main.py show'
>> 
>>if you want to evolve your own robots run (takes 30+ mins 500 generations at 10 parents) 'python3 main.py evolve'
----------------------------------------------------------------------------------------------------------------------------------------------
## GIF

![gif](pics/theGif.gif)

## What does my project do?
Basically we are trying to create a robot that RUNS REALLY FAST! This code creates randomly generated robots that have random movement and bodies, like most completely randomly generated things at first it's AWFUL and barely working, but after big and sometimes small tweaks to both the body and the brain we are able to create robots that RUN REALLY FAST, maybe as fast as Sonic and the Flash! (and maybe even faster if we had more time and a better PC). Now all of this might sound like impossible to do so lets start from the beginning!
## What is Evolution ? 
Evolution is the process by which living things change over time to better survive in their environments. Imagine a group of animals living in the wild, like a herd of deer. Some of the deer might have traits that make them better at running or finding food, like longer legs or a better sense of smell. These traits give those deer an advantage over the others, so they are more likely to survive and have babies with those same helpful traits. Over time, the traits that are helpful become more common in the population, and the animals become better adapted to their environment. This is how evolution works - it's like a long, slow process of trial and error, where the animals that are best suited to their environment are the ones that survive and pass on their traits to the next generation.
## What is the goal of my evolution ? 
My robots try to evolve to try and create robots that get as far from the starting position as possible. Just like many animals who migrate my robots that aren't capable of going far away from the starting point will "die out". The first randomly generated bodies are usually very bad at this but they can improve, and with small improvements over a long period of time we can get very capable robots
## How does body generation work ?
I already talked about "Generating Bodies" but seriously what does that even mean? See in the ludobots library we work with cubes to create virtual robots,if we were to randomize the size of these cubes and put them together and randomly pick if they are a cube with a sensor or not (blue or green) we could create a robot totally randomly. And A lot of the time the first robot we create will just be awful :(

![pic](pics/generation.png)

>I changed the body in solutions.py to generate randomly at first it generates a random number, according to that number we get a rectangle of random shapes. Next we pick a random axis (X,Y,Z) and then we do a "coinflip" to see if the new body part will have a sensor or not making the rectangles blue or green, we do this for each shape till we hit our random number. For the future generations it only changes the body when the fitness function is low and if its increasing it changes the brain
>if the absolute value of fitness is less than 2 after 5 evolutions we assume the body is unfit for movement and create a new body and a brain, if the fitness is greater than 2 we create a new brain ONLY. WE use absolute value because we assume if a robot can move in the positive direction it could technically move backwards as well with reverse weights


Sources: 

reddit.com/ludobots
https://amandaghassaei.com
https://infoscience.epfl.ch/record/184991
