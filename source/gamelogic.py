import random

def random_state(rows, columns):
    x = []
    for i in range(rows):
        x.append([])
        for j in range(columns):
            x[i].append(random.choices([0,1], weights=[0.7,0.3], k=1)[0])
    return x

def dummy_state(rows, columns):
    x = []
    for i in range(rows):
        x.append([])
        for j in range(columns):
            x[i].append(0)
    return x

def neighbors_count(state):
    # create dummy state
    row = len(state)
    column = len(state[0])
    x = dummy_state(row, column)

    for i_state in range(len(state)):
        for j_state in range(len(state[0])):

            #last-row + 1 = 0
            if i_state == len(state)-1:
                i_new = -1
            else:
                i_new = i_state
            #last-column + 1 = 0
            if j_state == len(state[0])-1:
                j_new = -1
            else:
                j_new = j_state

            #top-neighbors
            if state[i_new-1][j_new]:
                x[i_new][j_new] += 1
            if state[i_new-1][j_new-1]:
                x[i_new][j_new] += 1
            if state[i_state-1][j_new+1]:
                x[i_new][j_new] += 1
            
            #bottom-neighbors
            if state[i_new+1][j_new]:
                x[i_new][j_new] += 1
            if state[i_new+1][j_new-1]:
                x[i_new][j_new] += 1
            if state[i_new+1][j_new+1]:
                x[i_new][j_new] += 1

            #left-right
            if state[i_new][j_new+1]:
                x[i_new][j_new] += 1
            if state[i_new][j_new-1]:
                x[i_new][j_new] += 1    
    return x

def count_alive(state):
    count = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 1:
                count+=1
    return count

def next_state(state):
    # create dummy state
    row = len(state)
    column = len(state[0])
    x = dummy_state(row, column)

    n = neighbors_count(state)

    for i in range(row):
        for j in range(column):
            if n[i][j] < 2:
                x[i][j] = 0
            elif n[i][j] == 3:
                x[i][j] = 1
            elif n[i][j] > 3:
                x[i][j] = 0
            else:
                x[i][j] = state[i][j]
    return x