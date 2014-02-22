'''
Created on Feb 21, 2012

@author: peekgv
'''

#===============================================================================
# >>> number_of_quarters = 4 (future option)?
#
# >>> from collections import deque
# >>> d = deque()
# >>> d.extend([Clock(),Clock(),'half',Clock(),Clock(),'end'])
# >>> while d:
#     ct = d.popleft()
#     try:
#         while ct.time_remaining:
#             t = ct.run_clock()
#             str(t)[2:7]
#     except:
#         print 'end of half processing'
# 
# Example:
# >>> c = Clock()
# >>> while c.time_remaining:
#     t = c.run_clock()
#     str(t)[2:7]
#===============================================================================


from datetime import timedelta

class Clock(object):
    "Basic Clock"
    def __init__(self, quarter_length=15):
        self.time_remaining = timedelta(seconds=(quarter_length*60))

    def run_clock(self):
        self.time_remaining -= timedelta(seconds=30)
    
        return self.time_remaining