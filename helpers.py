from collections import namedtuple

make_episode = namedtuple('Episode', 
                          field_names=['states', 
                                       'actions', 
                                       'rewards', 
                                       'total_return', 
                                       'length'])