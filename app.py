import gradio as gr
import random


def m_merge(list_a, list_b):
    i, j = 0, 0
    new_list = []
    # compare values from each list and add the smaller value first
    while i < len(list_a) and j < len(list_b):
        if list_a[i] <= list_b[j]:
            new_list.append(list_a[i])
            i += 1
        else:
            new_list.append(list_b[j])
            j += 1
    # once all comparison has been done, add the rest
    while i < len(list_a):
        new_list.append(list_a[i])
        i += 1
    while j < len(list_b):
        new_list.append(list_b[j])
        j += 1
    return new_list


def m_sort(m_list):
    # if the list can no longer be split in two, return it
    # otherwise, recursively return the merge between two sorted lists
    if len(m_list) < 2:
        return m_list
    else:
        return m_merge(m_sort(m_list[:len(m_list)//2]), m_sort(m_list[len(m_list)//2:]))


# create a randomized list of any length
def random_list(length, limit):
    new_list = []
    for n in range(length):
        new_list.append(random.randint(1, limit))
    return new_list


print("Creating list...")
temp_list = random_list(20, 10)
print(f"List successfully created! Now sorting {temp_list}")
print(m_sort(temp_list))