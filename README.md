ASSIGNMENT 8

>to run simply pull and run main.py 

This code works by creating a random body with a random amount of sensors and motors and generating a new brain each time for the body to find the best fitness after 40 generations with a population size of 5
----------------------------------------------------------------------------------------------------------------------------------------------
>I changed the body in solutions.py to generate randomly at first it generates a random number, according to that number we get a rectangle of random shapes. Next we pick a random axis (X,Y,Z) and then we do a "coinflip" to see if the new body part will have a sensor or not making the rectangles blue or green, we do this for each shape till we hit our random number. For the future generations it only changes the body when the fitness function is low and if its increasing it changes the brain
>if the absolute value of fitness is less than 2 after 5 evolutions we assume the body is unfit for movement and create a new body and a brain, if the fitness is greater than 2 we create a new brain ONLY. WE use absolute value because we assume if a robot can move in the positive direction it could technically move backwards as well with reverse weights

>> https://user-images.githubusercontent.com/19967483/220274532-39298956-5e41-42e1-b9e5-9ea2927eee1c.png

>>Diagram explaining more
>>https://user-images.githubusercontent.com/19967483/221935626-5358eb44-349f-40fb-864f-c0d15d902a09.png

> Each body after passing a fitness of abs(2) will have 5*40 = 120 different brains made to optimize the fitness function, optimizing meaning to make it the most negative. 
> My random robots at first will have very bad fitness functions ranging from - 2 - + 10 but in the end I was able to hit as low as -31 meaning it moved very far away


Here are fitness functions from 5 different runs with 40 generations


https://user-images.githubusercontent.com/19967483/221930351-27ef52d5-cc3b-4d2d-b5b4-efc9e1b56e83.png

https://user-images.githubusercontent.com/19967483/221930420-7e31b9ef-d958-40ec-bf97-21f4d9ed1fa0.png

https://user-images.githubusercontent.com/19967483/221930531-c300ddef-88b6-40b7-8251-9e9a66ec98f6.png

https://user-images.githubusercontent.com/19967483/221930902-4f238037-cf5f-4deb-b626-d366e52f1f49.png

Sources: 

reddit.com/ludobots
https://amandaghassaei.com
https://infoscience.epfl.ch/record/184991
