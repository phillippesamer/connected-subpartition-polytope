Maximize
  1 x1,1 + 4 x2,2 + 9 x3,3 + 4 x4,1 

Subject To
GUB1: x1,1 + x1,2 + x1,3 <= 1
GUB2: x2,1 + x2,2 + x2,3 <= 1
GUB3: x3,1 + x3,2 + x3,3 <= 1
GUB4: x4,1 + x4,2 + x4,3 <= 1
(1,2)-SEP_#1_c1: x1,1 + x2,1 - x3,1 <= 1
(1,2)-SEP_#1_c2: x1,2 + x2,2 - x3,2 <= 1
(1,2)-SEP_#1_c3: x1,3 + x2,3 - x3,3 <= 1
(1,4)-SEP_#1_c1: x1,1 + x4,1 - x3,1 <= 1
(1,4)-SEP_#1_c2: x1,2 + x4,2 - x3,2 <= 1
(1,4)-SEP_#1_c3: x1,3 + x4,3 - x3,3 <= 1
(2,4)-SEP_#1_c1: x2,1 + x4,1 - x3,1 <= 1
(2,4)-SEP_#1_c2: x2,2 + x4,2 - x3,2 <= 1
(2,4)-SEP_#1_c3: x2,3 + x4,3 - x3,3 <= 1

Bounds

Binaries
 x1,1  x1,2  x1,3  x2,1  x2,2  x2,3  x3,1  x3,2  x3,3  x4,1  x4,2  x4,3 

End
