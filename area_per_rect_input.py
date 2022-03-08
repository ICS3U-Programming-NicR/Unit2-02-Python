#!/usr/bin/env python3

# Created By: Nicolas Riscalas

# Date: 02-28-2022

# Calculates the area and perimeter of a rectangle


import math

PI = math.pi


def main():
    side = list(
        map(
            int,
            input("What is the length and the width of your rectangle?\n")
            .strip()
            .split(),
        )
    )
    perimeter = 2 * side[0] + 2 * side[1]
    area = side[0] * side[1]
    print("Area of the rectangle = %.2f" % area)
    print("Perimeter of the rectangle = %.2f" % perimeter)


if __name__ == "__main__":
    main()
