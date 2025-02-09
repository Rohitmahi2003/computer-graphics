# Computer Graphics Using Python

## Introduction

This repository contains computer graphics programs implemented in Python using OpenGL libraries: GLUT, GLU, and GL. These programs demonstrate fundamental graphics concepts such as rendering shapes, transformations, and animations.

## Requirements

To run these programs, you need the following:

- Python (3.x recommended)
- PyOpenGL (`PyOpenGL` and `PyOpenGL-accelerate`)
- GLUT (via `freeglut` or `pygame` for Windows/Linux/Mac)

## Installation

### Windows:

1. Install Python from [Python.org](https://www.python.org/downloads/).
2. Install PyOpenGL and related packages:
   ```
   pip install PyOpenGL PyOpenGL-accelerate
   ```
3. Install FreeGLUT (e.g., using `choco install freeglut` for Chocolatey users).

### Linux/Mac:

1. Install Python and dependencies:
   ```
   sudo apt install freeglut3 freeglut3-dev  # Ubuntu/Debian
   brew install freeglut                      # macOS
   pip install PyOpenGL PyOpenGL-accelerate
   ```

## Running the Programs

To run any program, execute the Python script:

```sh
python filename.py
```

## Program List

- `basic_shapes.py`: Draws basic geometric shapes.
- `2d_transformations.py`: Demonstrates translation, rotation, and scaling.
- `3d_cube.py`: Renders a rotating 3D cube.
- `animation.py`: Implements basic animation using OpenGL.

## Libraries Used

- **GLUT (GL Utility Toolkit)**: Manages window creation, input handling, and event loops.
- **GLU (GL Utility Library)**: Provides higher-level drawing functions.
- **GL (OpenGL)**: Core graphics rendering functions.

## References

- [OpenGL Documentation](https://www.opengl.org/documentation/)
- [PyOpenGL Documentation](http://pyopengl.sourceforge.net/)

## Author

[Your Name]

## License

This project is licensed under the MIT License - see the LICENSE file for details.

