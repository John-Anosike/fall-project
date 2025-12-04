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


# generates list of random integers from 1-100 of user-defined length
def generate_list(length):
    g_list = []
    if int(length) < 0:
        return "ERROR: List length cannot be negative!"
    else:
        for n in range(int(length)):
            g_list.append(random.randint(1, 100))
        return g_list
    

# gradio blocks interface
with gr.Blocks() as instance:
    # section for creating random list
    with gr.Column():
        inp = gr.Textbox(placeholder="Enter a positive number for the length of the list", label="List Length")
        create_btn = gr.Button("Create List")
    
    # section for sorting list
    with gr.Row():
        with gr.Column():
            out_list = gr.List(label="Generated List")
            create_btn.click(fn=generate_list, inputs=inp, outputs=out_list)
        with gr.Column():
            sort_btn = gr.Button("Sort List")
            sorted_list = gr.Textbox(label="Sorted List")
            sort_btn.click(fn=m_sort, inputs=out_list, outputs=sorted_list)

instance.launch()

