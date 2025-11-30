import gradio as gr
import random

# merges two lists together, out-of-place
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


# recursive portion of the mergesort function
# TO-DO: Create some visual demonstration of the list being split and sorted
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

# basic gradio interface, just for testing purposes
interface = gr.Interface(
    fn = m_sort,  # interface works off of our mergesort function
    inputs=[
        gr.List(datatype="number", 
                label="Unsorted List", 
                value=random_list(10, 100)) # TO-DO: change the value to a customizable list, input by the user
    ],
    outputs=[gr.List(datatype="number", label="Sorted List")],
)

interface.launch()
