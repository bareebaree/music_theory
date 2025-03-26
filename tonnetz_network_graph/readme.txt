# This project uses network graphs to interactively explore chord changes using neo-Riemannian theory tonnetz

This method to explore chord changes utilises smooth voice leading determined by similarity to adjacent chords by sharing notes. This does not currently account for chord changes that work due to functional harmony/cadence, nor does it account for notes close to others, it functions by homology between any two chords.

Chords are linked by a level of difference, given as a parameter, and transitionary pathways between them defined by level of difference are highlighted.

Initial proof of concept is a non interactive graph that demonstrates network transitions between chords.

Future iterations will utilise an interactive, rotatable plot that highlights paths and nodes from any given chord, and filters by chord, making it far easier to read what is an a complex network.
