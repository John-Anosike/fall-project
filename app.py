import gradio as gr
import random

steps = []


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
        merged = m_merge(m_sort(m_list[:len(m_list)//2]), m_sort(m_list[len(m_list)//2:]))
        steps.append(merged)
        return merged


# generates list of random integers from 1-100 of user-defined length
def generate_list(length, list_to_clear):
    g_list = []
    list_to_clear.clear()
    steps.clear()
    try:
        if 0 <= int(length) <= 100000:
            for n in range(int(length)):
                g_list.append(random.randint(1, int(length)))
        else:
            return g_list, gr.update(maximum=1), gr.update(value=1), "List length must fall in between the range 0 <= n <= 100,000"
        return g_list, gr.update(maximum=len(g_list) - 2), gr.update(value=0), length
    except ValueError:
        return g_list, gr.update(maximum=1), gr.update(value=1), "ERROR: List length must be an integer!"


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
            inp = gr.Textbox(placeholder="Enter a positive number for the length of the list",
                             label='Enter an integer between 0 and 100,000 for the list length. Then press "Create List" to create a randomized list of said length. Finally, press "Sort List" to sort the list')
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
        step_slider = gr.Slider(minimum=0,
                                maximum=1,
                                step=1,
                                label='Adjust the slider to view any step in the process. Then press "View Step" to view what happens at that point.')
        steps_btn = gr.Button("View Step")
    step = gr.Label(label="This is a demonstration of the merge at each step. The list is broken down into partitions, which are repeatedly sorted and merged together until one sorted list is created.", visible=False)

    create_btn.click(fn=generate_list,
                     inputs=[inp, out_list],
                     outputs=[out_list,
                              step_slider,
                              step_slider,
                              inp])
    sort_btn.click(fn=m_sort,
                   inputs=out_list,
                   outputs=sorted_list)
    steps_btn.click(fn=view_steps,
                    inputs=step_slider,
                    outputs=[step, step])

# gr.themes.builder()
instance.launch(theme=gr.themes.Citrus())
