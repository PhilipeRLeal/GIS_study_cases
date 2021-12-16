# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:17:33 2018

@author: Philipe Leal
"""

import numpy as np
def floodFill(c, r, mask):
	"""
	Crawls a mask array containing
	only 1 and 0 values from the
	starting point (c=column,
	r=row - a.k.a. x, y) and returns
	an array with all 1 values
	connected to the starting cell.
	This algorithm performs a 4-way
	check non-recursively.
	"""
	# cells already filled
	filled = set()
	# cells to fill
	fill = set()
	fill.add((c, r))
	width = mask.shape[1]-1
	height = mask.shape[0]-1
	# Our output inundation array
	flood = np.zeros_like(mask, dtype=np.int8)
	# Loop through and modify the cells which
	# need to be checked.
	while fill:
	# Grab a cell
		x, y = fill.pop()
	
	if y == height or x == width or x < 0 or y < 0:
		# Don't fill
		pass
    
	if mask[y][x] == 1:
		# Do fill
		flood[y][x] = 1
	
	filled.add((x, y))
	# Check neighbors for 1 values
	west = (x-1, y)
	east = (x+1, y)
	north = (x, y-1)
	south = (x, y+1)

	if west not in filled:
		fill.add(west)
	if east not in filled:
		fill.add(east)
	if north not in filled:
		fill.add(north)
	if south not in filled:
		fill.add(south)
		
	return flood