最多需要的会议室数量

给出会议时间安排，把每段会议时间看作一个线段
转换为求线段最大的重合数
----
     ------
        -----
                ----
          --------

从图像中可以看出需要安排3个会议室

不妨把每段会议时间起始位置标记为1，结束位置标记为-1
按会议起始时间对会议进行排序
则会形成 
1       -1
            1        -1
                           1   -1
               1              -1
对上述排列从前往后进行累加，得到的最大值即为需要安排的会议室数量；