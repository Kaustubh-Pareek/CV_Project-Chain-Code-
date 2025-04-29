# Chain Code Boundary Tracing

This project implements a boundary tracing algorithm using Chain Codes. Given a binary image, the algorithm traces the boundary of the white region (foreground) using a specified connectivity (4-connectivity or 8-connectivity). The traced boundary is visualized by drawing red dots along the boundary and generating a Chain Code that represents the boundary's movement.

## Features

- Boundary tracing of a binary image using Chain Code.
- Supports both 4-connectivity and 8-connectivity.
- Visualize the boundary on the original image.
- Outputs the Chain Code and processed image.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Matplotlib

### Install dependencies:

```bash
pip install opencv-python numpy matplotlib



