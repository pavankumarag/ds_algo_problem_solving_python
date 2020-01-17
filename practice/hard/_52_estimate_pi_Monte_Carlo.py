"""
simulate random (x, y) points in a 2-D plane with domain as a square of side 1 unit.
Imagine a circle inside the same domain with same diameter and inscribed into the square.
We then calculate the ratio of number points that lied inside the circle and total number of generated points


The Algorithm
1. Initialize circle_points, square_points and interval to 0.
2. Generate random point x.
3. Generate random point y.
4. Calculate d = x*x + y*y.
5. If d <= 1, increment circle_points.
6. Increment square_points.
7. Increment interval.
8. If increment < NO_OF_ITERATIONS, repeat from 2.
9. Calculate pi = 4*(circle_points/square_points).
10. Terminate.
"""
import random
INTERVAL = 1000


def monte_carlo_pi():
	global INTERVAL
	circle_points = square_points = pi = 0
	for i in range(INTERVAL*INTERVAL):
		rand_x = (random.uniform(1, 1000) % (INTERVAL+1))/INTERVAL
		rand_y = (random.uniform(1, 1000) % (INTERVAL+1))/INTERVAL
		original_dist = rand_x * rand_x + rand_y * rand_y
		if original_dist <= 1:
			circle_points += 1
		square_points += 1
		pi = (4.0 * circle_points)/square_points
	return pi


if __name__ == "__main__":
	print monte_carlo_pi()