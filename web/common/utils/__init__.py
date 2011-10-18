import sys

def update_sorted_dict_order(d, *keys):
    "Update the sortedDict d to have order defined by keys."

    oldKeys = d.keyOrder[:]
    newOrder = list(*keys)

    for key in oldKeys:
        if key not in newOrder:
            newOrder.append(key)

    d.keyOrder = newOrder
