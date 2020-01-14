"""
Program to check if water tank overflows when n solid balls are dipped in the water tank

Given the dimensions of cylindrical water tank, spherical solid balls and the amount of water present
in the tank check if water tank will overflow when balls are dipped in the water tank.


Examples :

input : H = 10, r =  5
        h = 5
        N = 2, R = 2
output : Not in overflow state
Explanation :
water tank capacity = 3.14 * r * r * H
                    = 3.14 * 5 * 5 * 10
                    = 785

volume of water in tank = 3.14 * r * r * h
                        = 3.14 * 5 * 5 * 5
                        = 392.5

Volume of balls = N * (4/3) * 3.14 * R * R * R
                = 2 * (4/3) * 3.14 * 2 * 2 * 2
                = 67.02
Total volume of water + dip balls = 392.5 + 67.02
                                  = 459.52

Total volume (459.02) < tank capacity (785)
So, there is no overflow in tank

input : H = 5, r = 3
        h = 3
        N = 3, R = 2
output : Overflow
Explanation:
water tank capacity = 3.14 * r * r * H
                    = 3.14 * 3 * 3 * 5
                    = 141.3

volume of water in tank = 3.14 * r * r * h
                        = 3.14 * 3 * 3 * 3
                        = 84.78

volume of balls = N * (4/3) * 3.14 * R * R * R
                = 3 * (4/3) * 3.14 * 2 * 2 * 2
                = 100.48

Total volume of water + dip balls = 84.78 + 100.48
                                  = 185.26

Total volume (185.26) > tank capacity (141.3)
So, tank will overflow

Reference: https://www.geeksforgeeks.org/program-check-water-tank-overflows-n-solid-balls-dipped-water-tank/
"""
def overflow( H, r, h, N, R ):

	# cylinder capacity
	tank_cap = 3.14 * r * r * H

	# volume of water in tank
	water_vol = 3.14 * r * r * h

	# volume of n balls
	balls_vol = N * (4 / 3) * 3.14 * R * R * R

	# total volume of water
	# and n dipped balls
	vol = water_vol + balls_vol

	# condition to check if tank is in
	# overflow state or not
	if vol > tank_cap:
		print("Overflow")
	else:
		print("Not in overflow state")


if __name__ == "__main__":
	# giving dimensions
	H = 10
	r = 5
	h = 5
	N = 2
	R = 2
	overflow (H, r, h, N, R)