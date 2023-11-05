#AUTHOR: ARTUR GĘSIARZ
"""
For the tests to work properly, you must place the 'flow' folder and the 'connectivity' and script 'dimacs.py' in the local folder where this script is located.
"""
from dimacs import *
from os import listdir,getcwd
import datetime

TEST_PASSED=0
ALL_TEST=0
BASIC_TEST=0
TOTAL_TIME=0

def count_files(path):
    global ALL_TEST,BASIC_TEST
    files = listdir(path)
    for file in files:
        if not file.startswith('.'): ALL_TEST+=1
    BASIC_TEST=ALL_TEST//2

def gen_tests(exercise):
    if exercise==1:
        test_path=f'{getcwd()}/flow' 
    elif exercise==2:
        test_path = f'{getcwd()}/connectivity' 
    else: exit()
    count_files(test_path)
    files=listdir(test_path) 
    graphs=[]
    solutions=[]
    for file in files:
        if not file.startswith('.'): #want to avoid hidden files
            test_file=test_path+f"/{file}" #changing the path to my file
            V,L,sol=loadDirectedWeightedGraph(test_file)
            graph=[[] for _ in range(V)]
            for (x,y,c) in L: #I'm browsing through all the edges - remembering that I'm numbering from 1 in the file, but I'll change it for the solution -> I also remember that I'm dealing with an undirected graph
                graph[x-1].append((y-1,c)) #protection against the fact that I'm only talking about a directed graph
                if exercise==2:
                    graph[y-1].append((x-1,c))
            graphs.append(graph)
            solutions.append(sol)
    return graphs,solutions

def check(solutions,act_test,sol_recive,test_time):
    global TEST_PASSED
    print(f"Result received {sol_recive}, expected result {solutions[act_test]}")
    print(f"Time: {test_time}s")
    if solutions[act_test]==sol_recive:
        print("TEST CORRECT!")
        TEST_PASSED+=1
    else:
        print("TEST FILED!")


def sum_up(all_test):
    global TEST_PASSED,ALL_TEST,TOTAL_TIME
    if all_test:
        print(f"Result received: {TEST_PASSED}/{ALL_TEST}")
        print(f"All time: {round(TOTAL_TIME, 4)}s")
        if TEST_PASSED==ALL_TEST:
            print("Congratulations! All tests passed")
    else:
        print(f"Passed tests: {TEST_PASSED}/{BASIC_TEST}")
        print(f"Total time: {round(TOTAL_TIME, 4)}s")
        if TEST_PASSED==BASIC_TEST:
            print("Congratulations! All tests passed")

def testing(f,exercise,all_test):
    global TOTAL_TIME
    graphs, solutions = gen_tests(exercise)
    if all_test:
        for act_test in range(ALL_TEST):
            edges_amount=len(graphs[act_test])-1
            print(f"TEST {act_test}, S={0}, T={edges_amount}")
            start_time=datetime.datetime.now()
            if exercise==1:
                sol_recive=f(graphs[act_test],0,edges_amount)
            else:
                sol_recive=f(graphs[act_test])
            end_time=datetime.datetime.now()
            test_time = round((end_time - start_time).total_seconds(),3)
            TOTAL_TIME+=test_time
            check(solutions,act_test,sol_recive,test_time)
    else:
        for act_test in range(BASIC_TEST):
            edges_amount = len(graphs[act_test]) - 1
            print(f"TEST {act_test}, S={0}, T={edges_amount}")
            start_time = datetime.datetime.now()
            if exercise == 1:
                sol_recive = f(graphs[act_test], 0, edges_amount)
            else:
                sol_recive = f(graphs[act_test])
            end_time = datetime.datetime.now()
            test_time = round((end_time - start_time).total_seconds(),3)
            TOTAL_TIME += test_time
            check(solutions,act_test,sol_recive,test_time)
    sum_up(all_test)
