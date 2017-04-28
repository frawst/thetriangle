# thetriangle
generate serpinski triangles using cool maths

Created by Justyn Chaykowski, github.com/frawst
git:github.com/frawst/thetriangle
    
Contributors:
frawst
EclectickMedia
    
## TODO    
- [ ] generating a random start point inside the triangle
- [x] Fucking comment and organize shit, jezus damn.
- [ ] Impliment parameter naming
- [ ] Impliment paramater image sizing
- [ ] Impliment parameter dot-count

## Project Overview

Python Serpinski Triangle Generator utilizing randomly incrimented point placement within a pre-defined triangle determined by randomly selecting a vertex then translating half way towards that vertex from the current point. Begin with a 'random' point inside the triangle

## Functionality
### genPoint()
Utilizes a list of graphics.py points to generate pseudo-random points within a beginning triangle

### dfc(pointx, pointy, originX, originY)
finds the distance between two points

### rgbMap(val, limiter)
given a value ('val'), and the maximum for that value ('limiter'), will anchor/map that value to an RGB value (0-255)
