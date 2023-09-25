# def mystery(l):
#     if l == []:
#         return(l)
#     else:
#         return(mystery(l[1:])+l[:1])

# print(mystery([22,14,19,65,82,55]))


# pairs = [ (x,y) for x in range(4,1,-1) for y in range(5,1,-1) if (x+y)%3 == 0 ]
# print(pairs)


# wickets = {"Tests":{"Bumrah":[3,5,2,3],"Shami":[4,4,1,0],"Ashwin":[2,1,7,4]},"ODI":{"Bumrah":[2,0],"Shami":[1,2]}}
# wickets["ODI"]["Ashwin"][0:] = [4,4]
# wickets["ODI"]["Ashwin"].extend([4,4])
# wickets["ODI"]["Ashwin"] = [4,4]
# wickets["ODI"]["Ashwin"] = wickets["ODI"]["Ashwin"] + [4,4]


# hundreds = {}
# hundreds[["Tendulkar","international"]] = 100

# hundreds["Tendulkar, international"] = 100
# hundreds["Tendulkar"] = {"international":100}
# hundreds[("Tendulkar","international")] = 100
# hundreds[["Tendulkar","international"]] = 100

# Write a Python function frequency(l) that takes as input a list of integers and returns a pair of the form (minfreqlist,maxfreqlist) where

# minfreqlist is a list of numbers with minimum frequency in l, sorted in ascending order
# maxfreqlist is a list of numbers with maximum frequency in l, sorted in ascending order
# Here are some examples of how your function should work.
# >>> frequency([13,12,11,13,14,13,7,11,13,14,12])
# ([7], [13])

# >>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14])
# ([7], [13, 14])

# >>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7])
# ([7, 11, 12], [13, 14])


# def frequency(listita):
#     (A,B) = ([],[])
#     dict = {}
#     for x in listita: 
#         if x in dict:
#             dict[x] = dict[x]+1
#         else:
#             dict[x]=1

#     A.append(list(dict.keys())[0])
#     B.append(list(dict.keys())[0])

#     for x in dict.keys():
#         if dict[A[0]] == dict[x]:
#             if x not in A:
#                 A.append(x)
#         elif dict[A[0]] < dict[x]:
#             A = []
#             A.append(x)

#         if dict[B[0]] == dict[x]:
#             if x not in B:
#                 B.append(x)
#         elif dict[B[0]] > dict[x]:
#             B = []
#             B.append(x)
        
#     B.sort()
#     A.sort()

#     return (B,A)

# print(frequency([13,12,11,13,14,13,7,11,13,14,12]))
# # # ([7], [13])

# print(frequency([13,12,11,13,14,13,7,11,13,14,12,14,14]))
# # ([7], [13, 14])

# print(frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7]))
# # # ([7, 11, 12], [13, 14])



# An airline has assigned each city that it serves a unique numeric code. 
# It has collected information about all the direct flights it operates, 
# represented as a list of pairs of the form (i,j), 
# where i is the code of the starting city and j is the code of the destination.

# It now wants to compute all pairs of cities 
# connected by one intermediate hope — city i is connected to city j by one intermediate hop 
# if there are direct flights of the form (i,k) and (k,j) for some other city k. 
# The airline is only interested in one hop flights between different cities — pairs of the form (i,i) are not useful.

# Write a Python function onehop(l) that takes as input a list of pairs representing direct flights, 
# as described above, and returns a list of all pairs (i,j), where i != j, 
# such that i and j are connected by one hop. 
# Note that it may already be the case that there is a direct flight from i to j. 
# So long as there is an intermediate k with a flight from i to k and from k to j, 
# the list returned by the function should include (i,j). The input list may be in any order. 
# The pairs in the output list should be in lexicographic (dictionary) order. Each pair should be listed exactly once.

# Here are some examples of how your function should work.




# def onehop(listita):
#     result = []
#     Cities = []
#     for x in listita:
#         if x[0] not in Cities:
#             Cities.append(x[0])
#         if x[1] not in Cities:
#             Cities.append(x[1])
#     Cities.sort()

#     for c in Cities:
#         for x in listita:
#             if c == x[0]:
#                 for y in listita:
#                     if x[1] == y[0]:
#                         if c != y[1]:
#                             if (c,y[1]) not in result:
#                                 result.append((c,y[1]))
#     result.sort()
#     return result


 
# print(onehop([(2,3),(1,2)]))
# # [(1, 3)]

# print(onehop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)]))
# # [(1, 2), (1, 3), (1, 4), (2, 1), (3, 2), (3, 4), (4, 2), (4, 3)]

# print(onehop([(1,2),(3,4),(5,6)]))
# # []



def frequency(listita):
    (A,B) = ([],[])
    dict = {}
    for x in listita: 
        if x in dict:
            dict[x] = dict[x]+1
        else:
            dict[x]=1

    A.append(list(dict.keys())[0])
    B.append(list(dict.keys())[0])

    for x in dict.keys():
        if dict[A[0]] == dict[x]:
            if x not in A:
                A.append(x)
        elif dict[A[0]] < dict[x]:
            A = []
            A.append(x)

        if dict[B[0]] == dict[x]:
            if x not in B:
                B.append(x)
        elif dict[B[0]] > dict[x]:
            B = []
            B.append(x)
        
    B.sort()
    A.sort()

    return (B,A)




def onehop(listita):
    result = []
    Cities = []
    for x in listita:
        if x[0] not in Cities:
            Cities.append(x[0])
        if x[1] not in Cities:
            Cities.append(x[1])
    Cities.sort()

    for c in Cities:
        for x in listita:
            if c == x[0]:
                for y in listita:
                    if x[1] == y[0]:
                        if c != y[1]:
                            if (c,y[1]) not in result:
                                result.append((c,y[1]))
    result.sort()
    return result




print(onehop([(2,3),(1,2)]))
# [(1, 3)]

print(onehop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)]))
# [(1, 2), (1, 3), (1, 4), (2, 1), (3, 2), (3, 4), (4, 2), (4, 3)]

print(onehop([(1,2),(3,4),(5,6)]))
# []