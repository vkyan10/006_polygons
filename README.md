# 006_polygons
Alter 3d shapes to be based on triangles, to create a wire-frame model / polygon mesh:
- Create new functions to add a polygon to a matrix, and go through the matrix 3 points at a time to draw triangles
- A new triangle matrix for 3d shapes, and the edge matrix now only used for 2d shapes
- Relevant parser commands (apply, clear, display, save) modify/use the triangle matrix as well
- Modify add box, add sphere and add torus to add triangles to the new triangle matrix instead of points

Implement back-face culling
- Surfaces that face away are not drawn
