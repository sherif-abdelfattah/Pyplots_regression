import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tick

def reformat_large_tick_values(tick_val, pos):
   """
   Turns large tick values (in the billions, millions and thousands) such as 4500 into 4.5K and also appropriately turns 4000 into 4K (no zero after the decimal).
   """
   if tick_val >= 1000000000:
       val = round(tick_val/1000000000, 1)
       new_tick_format = '{:}G'.format(val)
   elif tick_val >= 1000000:
       val = round(tick_val/1000000, 1)
       new_tick_format = '{:}M'.format(val)
   elif tick_val >= 1000:
       val = round(tick_val/1000, 1)
       new_tick_format = '{:}K'.format(val)
   elif tick_val < 1000:
       new_tick_format = round(tick_val, 1)
   else:
       new_tick_format = tick_val

   # make new_tick_format into a string value
   new_tick_format = str(new_tick_format)

   # code below will keep 4.5M as is but change values such as 4.0M to 4M since that zero after the decimal isn't needed
   index_of_decimal = new_tick_format.find(".")

   if index_of_decimal != -1:
       value_after_decimal = new_tick_format[index_of_decimal+1]
       if value_after_decimal == "0":
           # remove the 0 after the decimal point since it's not needed
           new_tick_format = new_tick_format[0:index_of_decimal] + new_tick_format[index_of_decimal+2:]

   return new_tick_format

#points = np.array([(1, 1), (2, 4), (3, 1), (4,8), (9, 3), (5,25), (6,36), (7,28), (8,16), (10,3), (11,0), (12,5)])
# data array, obtained from Postgres.
points = np.array([
(7,16106127360),
(8,2147483648),
(8,2147483648),
(85,6291456000),
(85,2147483648),
(85,4294967296),
(89,5368709120),
(98,2147483648),
(98,1623195648),
(101,8589934592),
(102,12884901888),
(102,8589934592),
(102,12884901888),
(103,5368709120),
(105,6442450944),
(105,8589934592),
(110,4294967296),
(112,15032385536),
(124,2147483648),
(134,6442450944),
(137,3221225472),
(145,10737418240),
(145,10737418240),
(145,10737418240),
(145,8589934592),
(149,8589934592),
(150,5368709120),
(152,4294967296),
(153,5368709120),
(156,12884901888),
(160,4294967296),
(163,6442450944),
(164,2147483648),
(169,8589934592),
(169,8589934592),
(171,4294967296),
(172,8908701696),
(175,10737418240),
(175,4294967296),
(175,3221225472),
(175,10737418240),
(175,10737418240),
(194,8589934592),
(196,4294967296),
(202,2147483648),
(208,8589934592),
(209,4294967296),
(209,4294967296),
(211,5368709120),
(217,3221225472),
(217,3221225472),
(228,8589934592),
(246,4294967296),
(247,2147483648),
(247,8589934592),
(255,8589934592),
(267,4294967296),
(273,805306368),
(289,4294967296),
(290,2147483648),
(291,2147483648),
(295,8589934592),
(310,11534336000),
(310,11534336000),
(354,10737418240),
(354,4269801472),
(355,10737418240),
(360,33285996544),
(377,2147483648),
(389,3221225472),
(427,14751367168),
(427,14751367168),
(440,8589934592),
(445,12884901888),
(445,12884901888),
(476,4294967296),
(483,4294967296),
(483,4294967296),
(509,6442450944),
(512,6868172800),
(530,25769803776),
(546,25769803776),
(566,8388608000),
(571,20971520000),
(597,16106127360),
(597,16106127360),
(597,16106127360),
(600,8589934592),
(600,8589934592),
(600,8589934592),
(600,8589934592),
(616,12834570240),
(635,9663676416),
(641,6442450944),
(674,10737418240),
(718,42949672960),
(722,33285996544),
(729,33285996544),
(739,33285996544),
(741,8589934592),
(741,8589934592),
(745,4294967296),
(745,4294967296),
(772,21474836480),
(807,12884901888),
(807,12884901888),
(807,12884901888),
(809,7516192768),
(835,17179869184),
(918,17179869184),
(921,17179869184),
(932,25971130368),
(943,6442450944),
(949,17179869184),
(953,30064771072),
(957,17179869184),
(990,17179869184),
(1007,16106127360),
(1025,21474836480),
(1256,10737418240),
(1256,10737418240),
(1554,17179869184),
(1727,33285996544),
(1734,26214400000),
(1743,26214400000),
(1775,26214400000),
(1989,8665432064),
(3089,16106127360)
])
# get x and y vectors
x = points[:,0]
y = points[:,1]

# calculate polynomial try 3rd order polynomial
z = np.polyfit(x, y, 3)
f = np.poly1d(z)
# calculate polynomial try 1st order polynomial (linear regression)
z1 = np.polyfit(x, y, 1)
f1 = np.poly1d(z1)

# calculate new x and y values
x_new = np.linspace(x[0], x[-1], 800)
y_new = f(x_new)
y1_new = f1(x_new)

#y01,y02 = np.split(y_new,2)
#y11,y12 = np.split(y1_new,2)
#ytemp = (y01 + y11)/2
#y2_new = np.append(ytemp,y12)

# Calculate y2_new as a weighted average of 1 y_new + 2 y1new, this is to get a closer fit on the data we have
y2_new = (y_new + 2* y1_new)/3

#Plot work
plt.plot(x,y,'o', x_new, y_new)
plt.plot(x_new,y1_new)
# Make y2_new more bold
plt.plot(x_new,y2_new,linewidth=3)
plt.xlim([x[0]-1, x[-1] + 1 ])
# Add labels
plt.xlabel("Data Objects",size=20)
plt.ylabel("Heap",size=20)
# Add the tick, so that we have more readable heap size values
ay = plt.gca()
ay.yaxis.set_major_formatter(tick.FuncFormatter(reformat_large_tick_values));

plt.title("Data Objects vs Heap",size=30)
plt.grid(True)
plt.show()
