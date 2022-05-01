from csv import DictReader
from distutils.ccompiler import gen_preprocess_options
from functools import _make_key
from json.encoder import INFINITY
import puzzle as p
import treenode as tn
from queue import PriorityQueue
import copy

# Uniform Cost Search (Tree Search)
def uniform_cost(problem : p.Puzzle) -> int:
    found_solution = 0
    num_nodes_expanded = 0 # stores the number of nodes expanded
    max_queue_size = 1 # stores the maximum size of the frontier queue
    root = tn.TreeNode(problem.initial_state, problem.blank_row, problem.blank_col)
    frontier = PriorityQueue()
    offset = 1
    frontier.put((0, offset, root))
    offset += 1
    while frontier.not_empty:
        temp = frontier.get() # get lowest-cost node from frontier
        cost = temp[0]
        current_node = temp[2]
        if problem.goal_test(current_node): # apply goal test
            found_solution = 1
            return found_solution, num_nodes_expanded, max_queue_size, cost # solution found, return relevant info
        # if the current node is not a solution, expand it
        num_nodes_expanded += 1
        #temp1 = temp2 = temp3 = temp4 = copy.deepcopy(current_node)
        temp1 = copy.deepcopy(current_node)
        temp2 = copy.deepcopy(temp1)
        temp3 = copy.deepcopy(temp2)
        temp4 = copy.deepcopy(temp3)
        if problem.check_blank_left(temp1) == True:
            temp1 = problem.move_blank_left(temp1)
            #print(temp1.state)
            frontier.put((cost + 1, offset, temp1))
            offset += 1
        if problem.check_blank_right(temp2) == True:
            temp2 = problem.move_blank_right(temp2)
            #print(temp2.state)
            frontier.put((cost + 1, offset, temp2))
            offset += 1
        if problem.check_blank_up(temp3) == True:
            temp3 = problem.move_blank_up(temp3)
            #print(temp3.state)
            frontier.put((cost + 1, offset, temp3))
            offset += 1
        if problem.check_blank_down(temp4) == True:
            temp4 = problem.move_blank_down(temp4)
            #print(temp4.state)
            frontier.put((cost + 1, offset, temp4))
            offset += 1
        # update max queue size if needed
        if frontier.qsize() > max_queue_size:
            max_queue_size = frontier.qsize()

    # if no solution found, return with found_solution to 0
    return found_solution, num_nodes_expanded, max_queue_size, cost


def astar_misplace_tile(problem : p.Puzzle) -> int:
    found_solution = 0
    num_nodes_expanded = 0 # stores the number of nodes expanded
    max_queue_size = 1 # stores the maximum size of the frontier queue
    root = tn.TreeNode(problem.initial_state, problem.blank_row, problem.blank_col)
    frontier = PriorityQueue()
    offset = 1
    initial_cost = problem.find_misplaced_tile(root)
    frontier.put((initial_cost, offset, 0, root))
    root_key = problem.make_key(root)
    explored = { root_key : 'found' }
    offset += 1
    while frontier.not_empty:
        temp = frontier.get() # get lowest-cost node from frontier
        g_cost = temp[2]
        current_node = temp[3]
        if problem.goal_test(current_node): # apply goal test
            found_solution = 1
            return found_solution, num_nodes_expanded, max_queue_size, g_cost
        
        # add current node to explored
        current_node_key = problem.make_key(current_node)
        explored[current_node_key] = 'found'

        # if the current node is not solution, expand it
        num_nodes_expanded += 1
        temp1 = copy.deepcopy(current_node)
        temp2 = copy.deepcopy(temp1)
        temp3 = copy.deepcopy(temp2)
        temp4 = copy.deepcopy(temp3)
        g_cost += 1
        if problem.check_blank_left(temp1) == True:
            temp1 = problem.move_blank_left(temp1)
            temp1_key = problem.make_key(temp1)
            if not temp1_key in explored:
                h_cost1 = problem.find_misplaced_tile(temp1)
                frontier.put((g_cost + h_cost1, offset, g_cost, temp1))
                offset += 1
        if problem.check_blank_right(temp2) == True:
            temp2 = problem.move_blank_right(temp2)
            temp2_key = problem.make_key(temp2)
            if not temp2_key in explored:
                h_cost2 = problem.find_misplaced_tile(temp2)
                frontier.put((g_cost + h_cost2, offset, g_cost, temp2))
                offset += 1
        if problem.check_blank_up(temp3) == True:
            temp3 = problem.move_blank_up(temp3)
            temp3_key = problem.make_key(temp3)
            if not temp3_key in explored:
                h_cost3 = problem.find_misplaced_tile(temp3)
                frontier.put((g_cost + h_cost3, offset, g_cost, temp3))
                offset += 1
        if problem.check_blank_down((temp4)) == True:
            temp4 = problem.move_blank_down(temp4)
            temp4_key = problem.make_key(temp4)
            if not temp4_key in explored:
                h_cost4 = problem.find_misplaced_tile(temp4)
                frontier.put((g_cost + h_cost4, offset, g_cost, temp4))
                offset += 1
        # update max queue size if needed
        if frontier.qsize() > max_queue_size:
            max_queue_size = frontier.qsize()

    # if no solution found, return with found_solution to 0
    return found_solution, num_nodes_expanded, max_queue_size, g_cost


def astar_euclidean_distance(problem : p.Puzzle) -> int:
    found_solution = 0
    num_nodes_expanded = 0 # stores the number of nodes expanded
    max_queue_size = 1 # stores the maximum size of the frontier queue
    root = tn.TreeNode(problem.initial_state, problem.blank_row, problem.blank_col)
    frontier = PriorityQueue()
    offset = 1
    initial_cost = problem.find_euclidean_distance(root)
    frontier.put((initial_cost, offset, 0 , root))
    offset += 1
    root_key = problem.make_key(root)
    explored = { root_key : 'found' }
    while frontier.not_empty:
        temp = frontier.get() # get lowest-cost node from frontier
        g_cost = temp[2]
        current_node = temp[3]
        if problem.goal_test(current_node): # apply goal test
            found_solution = 1
            return found_solution, num_nodes_expanded, max_queue_size, g_cost

        # add current node to explored
        current_node_key = problem.make_key(current_node)
        explored[current_node_key] = 'found'

        # if the current node is not solution, expand it
        num_nodes_expanded += 1
        temp1 = copy.deepcopy(current_node)
        temp2 = copy.deepcopy(temp1)
        temp3 = copy.deepcopy(temp2)
        temp4 = copy.deepcopy(temp3)
        g_cost += 1
        if problem.check_blank_left(temp1) == True:
            temp1 = problem.move_blank_left(temp1)
            temp1_key = problem.make_key(temp1)
            if not temp1_key in explored:
                h_cost1 = problem.find_euclidean_distance(temp1)
                frontier.put((g_cost+ h_cost1, offset, g_cost, temp1))
                offset += 1
        if problem.check_blank_right(temp2) == True:
            temp2 = problem.move_blank_right(temp2)
            temp2_key = problem.make_key(temp2)
            if not temp2_key in explored:
                h_cost2 = problem.find_euclidean_distance(temp2)
                frontier.put((g_cost + h_cost2, offset, g_cost, temp2))
                offset += 1
        if problem.check_blank_up(temp3) == True:
            temp3 = problem.move_blank_up(temp3)
            temp3_key = problem.make_key(temp3)
            if not temp3_key in explored:
                h_cost3 = problem.find_euclidean_distance(temp3)
                frontier.put((g_cost + h_cost3, offset, g_cost, temp3))
                offset += 1
        if problem.check_blank_down((temp4)) == True:
            temp4 = problem.move_blank_down(temp4)
            temp4_key = problem.make_key(temp4)
            if not temp4_key in explored:
                h_cost4 = problem.find_euclidean_distance(temp4)
                frontier.put((g_cost + h_cost4, offset, g_cost, temp4))
                offset += 1
        # update max queue size if needed
        if frontier.qsize() > max_queue_size:
            max_queue_size = frontier.qsize()

    # if no solution found, return with found_solution to 0
    return found_solution, num_nodes_expanded, max_queue_size, g_cost