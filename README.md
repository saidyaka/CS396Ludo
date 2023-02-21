ASSIGNMENT 7

>to run simply pull and run main.py 
----------------------------------------------------------------------------------------------------------------------------------------------
>I changed the body in solutions.py to generate randomly at first it generates a random number, according to that number we get a rectangle of random shapes. Next we pick a random axis (X,Y,Z) and then we do a "coinflip" to see if the new body part will have a sensor or not making the rectangles blue or green, we do this for each shape till we hit our random number. 

>For positioning we start at 0,0,1 and go on from the relative positions for example if the random piece we generated goes to the 'Z' axis we will position it (0, 0 , random_length_generated/2) we divide by 2 because we want the cubes to have joints not from their middles but from their edges.

> first rectangle doesn't have an axis it just places it at position [0,0,1] and it also doesn't have a joint as its alone, but when the next one is generated its put relative of the first rectangle and the joint is put relative to the length/width/height of the previous rectangle so they don't intersect
>

Heres a diagram to better explain it


(https://user-images.githubusercontent.com/19967483/220274532-39298956-5e41-42e1-b9e5-9ea2927eee1c.png)
