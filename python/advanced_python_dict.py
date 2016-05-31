import collections
profile_sorted = collections.OrderedDict(sorted(profile.items(), key = lambda x: x[1]))
profile_sorted = dict(profile_sorted)
