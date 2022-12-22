Maximize
  1 x1,1 + 4 x2,2 + 3 x3,1 + 8 x4,2 

Subject To
GUB1: x1,1 + x1,2 <= 1
GUB2: x2,1 + x2,2 <= 1
GUB3: x3,1 + x3,2 <= 1
GUB4: x4,1 + x4,2 <= 1
(1,3)-SEP_#1_c1: x1,1 + x3,1 - x2,1 - x4,1 <= 1
(1,3)-SEP_#1_c2: x1,2 + x3,2 - x2,2 - x4,2 <= 1
(2,4)-SEP_#1_c1: x2,1 + x4,1 - x1,1 - x3,1 <= 1
(2,4)-SEP_#1_c2: x2,2 + x4,2 - x1,2 - x3,2 <= 1

Bounds

Binaries
 x1,1  x1,2  x2,1  x2,2  x3,1  x3,2  x4,1  x4,2 

End
