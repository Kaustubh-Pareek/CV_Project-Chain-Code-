import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def chain_code(img_path, connectivity=8):
    if connectivity == 4:
        directions = [(0,1), (1,0), (0,-1), (-1,0)] # E, S, W, N
                    #  0      1       2       3
    else:
        directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]  # E, SE, S, SW, W, NW, N, NE
                   #   0     1        2      3       4       5       6        7

    # makin the copy of the org img
    org_img = cv.imread(img_path)
    if org_img is None:
        return "Invalid path"
    img_cpy = org_img.copy()

    # convert the copied image to grayscale
    grey_scaled_img = cv.cvtColor(img_cpy, cv.COLOR_BGR2GRAY)

    _, bin_img = cv.threshold(grey_scaled_img, 127, 255, cv.THRESH_BINARY)

    # making the border around the image-> makes it easy for finding the boundary
    bodered_img = cv.copyMakeBorder(bin_img, 1, 1, 1, 1, cv.BORDER_CONSTANT, value=0)

     # finding the first white pixel
    start_pixel = None
    for row in range(bodered_img.shape[0]):
        for col in range(bodered_img.shape[1]):
            if bodered_img[row, col] == 255:
                start_pixel = (row, col)
                break
        if start_pixel:
            break

    # no white pixel found
    if not start_pixel:
        return "No white pixel"
    
    # border_pints and cc initialization
    border_points = [start_pixel]
    cc = []
    curr_pixel = start_pixel

    if connectivity == 8:
        curr_direction = 7 
    else:
        curr_direction = 3   # Start from NE or N


    # start boundary tracing
    while True:
        pixel_found = False   #set up a flag

        # Try each direction in a clockwise manner
        for i in range(len(directions)):
            direction_index = (curr_direction + i) % len(directions) # % for circular movement
            row, col = directions[direction_index]
            neighbor_pixel_row = curr_pixel[0] + row
            neighbor_pixel_col = curr_pixel[1] + col

            # add the neighbour pixel if it is white i.e. part of the boundary
            if bodered_img[neighbor_pixel_row, neighbor_pixel_col] == 255:
                curr_pixel = (neighbor_pixel_row, neighbor_pixel_col)
                border_points.append(curr_pixel)

                # Updating the direction - 2 steps backward.
                curr_direction = (direction_index + len(directions) - 2) % len(directions)

                # Adding to the chain code 
                if len(cc) == 0 or cc[-1] != direction_index:
                    cc.append(direction_index)

                pixel_found = True
                break  # break the for loop when next boundary pixel is found

        # breaking thw while loop if no new white pixel is found or we reach at the start ppixel again.
        if not pixel_found or curr_pixel == start_pixel:
            break

    # Draw the traced boundary on a color version of the original image
    processed_img = cv.cvtColor(bin_img, cv.COLOR_GRAY2BGR)
    for point in border_points:
        x = point[1] - 1  # column
        y = point[0] - 1  # row   -1 for converting the value of the pixel back to the to original value
        cv.circle(processed_img, (x, y), 1, (0, 0, 255), -1) #making the red point on the boundary/border pixel

    return cc, processed_img, None






