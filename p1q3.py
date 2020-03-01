# Name: <TODO: replace with your name>
# Section: <TODO: replace with your section>

# p1q3

# All statements should only be in functions. Do not include statements outside functions in this file.
# You may insert additional helper functions into this file if desired.

# We need to max V, How do we max V???
# Each user has a V ranking, rank each users in terms of V.
# Then we tabulate how much value can 1 user get,
# Using cost, to find the average,
# of course we pick the top average ones, starting from the top,
# Need to optimise that also
# We need to make sure that c remains below budget

def select_advertisers(budget, followers, c, v):
    value_each_advertiser_bring = []
    for i in followers:
        k = 0
        for g in range(len(i)):
            k += v[i[g]]
        value_each_advertiser_bring.append(k)
        k = 0
    print(value_each_advertiser_bring)
    ac = [value_each_advertiser_bring/c for value_each_advertiser_bring, c in zip(value_each_advertiser_bring, c)]
    final_list = []
    costing = 0
    while costing < budget:
         final_list.append(ac.index(max(ac)))
         costing += c[(ac.index(max(ac)))]
         if costing< budget:
             ac[ac.index(max(ac))] = 0
         else:
             final_list.remove(ac.index(max(ac)))
             return final_list
