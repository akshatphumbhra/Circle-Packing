# Circle-Packing

Generates a certain number of circles every frame and starts expanding them till they hit another circle or the edge of the canvas. The number of circles generated every frame affects how big the final circles are. This can be adjusted using the `resolution` parameter in `variables.py`. 

The color of each circle is determined by the pixel at the coordinate of the circle center on some target image. Setting the `fill` parameter in `variables.py` allows for the circles to either be filled in or just be outlined.


This is the Wikipedia page for Circle Packing - https://en.wikipedia.org/wiki/Circle_packing

This is an artist named Julien Leonard that has done some really cool generative art with this - https://julienleonard.com/tutorials.html

Adapted from https://thecodingtrain.com/CodingChallenges/050.1-circlepackinganimated.html. 