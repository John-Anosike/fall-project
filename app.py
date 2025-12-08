import gradio as gr
import random

steps = []

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
        merged = m_merge(m_sort(m_list[:len(m_list)//2]), m_sort(m_list[len(m_list)//2:]))
        steps.append(merged)
        return merged


# generates list of random integers from 1-100 of user-defined length
def generate_list(length):
    g_list = []
    steps.clear()
    if int(length) < 0:
        return "ERROR: List length cannot be negative!"
    else:
        for n in range(int(length)):
            g_list.append(random.randint(1, 100))
        return g_list, gr.update(maximum=len(g_list))


def view_steps(val):
    output = str(steps[val])
    output = output.replace("[", "")
    output = output.replace("]", "")
    return output, gr.update(visible=True)


# gradio blocks interface
with gr.Blocks(title="MergeSort Demonstration") as instance:
    # section for creating random list and sorting said list
    with gr.Row():
        with gr.Column():
            inp = gr.Textbox(placeholder="Enter a positive number for the length of the list", label="List Length")
        with gr.Column():
            create_btn = gr.Button("Create List")
            sort_btn = gr.Button("Sort List")

    with gr.Row():
        with gr.Column():
            out_list = gr.List(headers=["Generated List"])
        with gr.Column():
            sorted_list = gr.List(headers=["Sorted List"])

    # section for viewing steps
    with gr.Row():
        # all defaulted to False; they get enabled after the list is sorted and after a step is viewed
        step_slider = gr.Slider(minimum=0, maximum=1, step=1, label="Current Step")
        steps_btn = gr.Button("View Step")
    step = gr.Label(label="Recursive Step: merge the partitions and sort them from least to greatest", visible=False)

    create_btn.click(fn=generate_list, inputs=inp, outputs=[out_list, step_slider])
    sort_btn.click(fn=m_sort, inputs=out_list, outputs=sorted_list)
    steps_btn.click(fn=view_steps,
                    inputs=step_slider,
                    outputs=[step, step])

# gr.themes.builder()
instance.launch(theme=gr.themes.Citrus())

