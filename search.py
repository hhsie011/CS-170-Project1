from json.encoder import INFINITY
from logging import root
import puzzle as p
import treenode as tn
from queue import PriorityQueue

# Uniform Cost Search (Tree Search)
def uniform_cost(problem : p.Puzzle) -> int:
    found_solution = 0
    num_nodes_expanded = 0 # stores the number of nodes expanded
    max_queue_size = 1 # stores the maximum size of the frontier queue
    root = tn.TreeNode(problem.initial_state, problem.blank_row, problem.blank_col)
    frontier = PriorityQueue()
    frontier.put((0 , root))
    while frontier.not_empty:
        temp = frontier.get() # get lowest-cost node from frontier
        cost = temp[0]
        current_node = temp[1]
        if current_node.state == problem.goal_state: # apply goal test
            found_solution = 1
            return found_solution, num_nodes_expanded, max_queue_size, cost # solution found, return relevant info
        # if the current node is not solution, expand it
        num_nodes_expanded += 1
        temp1 = temp2 = temp3 = temp4 = current_node
        if problem.move_blank_left(temp1) == True:
            frontier.put((cost + 1, temp1))
        if problem.move_blank_right(temp2) == True:
            frontier.put((cost + 1, temp2))
        if problem.move_blank_up(temp3) == True:
            frontier.put((cost + 1, temp3))
        if problem.move_blank_down((temp4)) == True:
            frontier.put((cost + 1, temp4))
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
    frontier.put((0 , root))
    min_cost = INFINITY
    while frontier.not_empty:
        temp = frontier.get() # get lowest-cost node from frontier
        cost = temp[0]
        current_node = temp[1]
        if current_node.state == problem.goal_state: # apply goal test
            if cost < min_cost:
                min_cost = cost
            found_solution = 1
            
        # if the current node is not solution, expand it
        num_nodes_expanded += 1
        temp1 = temp2 = temp3 = temp4 = current_node
        if problem.move_blank_left(temp1) == True:
            h_cost = problem.find_misplaced_tile(temp1)
            frontier.put((cost + 1 + h_cost, temp1))
        if problem.move_blank_right(temp2) == True:
            h_cost = problem.find_misplaced_tile(temp2)
            frontier.put((cost + 1 + h_cost, temp2))
        if problem.move_blank_up(temp3) == True:
            h_cost = problem.find_misplaced_tile(temp3)
            frontier.put((cost + 1 + h_cost, temp3))
        if problem.move_blank_down((temp4)) == True:
            h_cost = problem.find_misplaced_tile(temp4)
            frontier.put((cost + 1 + h_cost, temp4))
        # update max queue size if needed
        if frontier.qsize() > max_queue_size:
            max_queue_size = frontier.qsize()

    # if no solution found, return with found_solution to 0
    return found_solution, num_nodes_expanded, max_queue_size, min_cost


def astar_euclidean_distance(problem : p.Puzzle) -> int:
    found_solution = 0
    num_nodes_expanded = 0 # stores the number of nodes expanded
    max_queue_size = 1 # stores the maximum size of the frontier queue
    root = tn.TreeNode(problem.initial_state, problem.blank_row, problem.blank_col)
    frontier = PriorityQueue()
    frontier.put((0 , root))
    min_cost = INFINITY
    while frontier.not_empty:
        temp = frontier.get() # get lowest-cost node from frontier
        cost = temp[0]
        current_node = temp[1]
        if current_node.state == problem.goal_state: # apply goal test
            if cost < min_cost:
                min_cost = cost
            found_solution = 1

        # if the current node is not solution, expand it
        num_nodes_expanded += 1
        temp1 = temp2 = temp3 = temp4 = current_node
        if problem.move_blank_left(temp1) == True:
            h_cost = problem.find_misplaced_tile(temp1)
            frontier.put((cost + 1 + h_cost, temp1))
        if problem.move_blank_right(temp2) == True:
            h_cost = problem.find_misplaced_tile(temp2)
            frontier.put((cost + 1 + h_cost, temp2))
        if problem.move_blank_up(temp3) == True:
            h_cost = problem.find_misplaced_tile(temp3)
            frontier.put((cost + 1 + h_cost, temp3))
        if problem.move_blank_down((temp4)) == True:
            h_cost = problem.find_misplaced_tile(temp4)
            frontier.put((cost + 1 + h_cost, temp4))
        # update max queue size if needed
        if frontier.qsize() > max_queue_size:
            max_queue_size = frontier.qsize()

    # if no solution found, return with found_solution to 0
    return found_solution, num_nodes_expanded, max_queue_size, min_cost