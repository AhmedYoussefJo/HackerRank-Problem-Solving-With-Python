#https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
import math

ab = int(input())
bc = int(input())

angle_rad = math.atan2(ab, bc)
angle_deg = math.degrees(angle_rad)

print(str(round(angle_deg)) + chr(176)) # ° = ascii of 176