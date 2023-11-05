#AUTHOR: ARTUR GĘSIARZ
"""
For the tests to work properly, you must place the 'graphs-lab1' folder and the file dimacs.py. in the local folder where the script is located.
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

def gen_tests():
    test_path=f'{getcwd()}/graphs-lab1' #finds current path
    count_files(test_path)
    files=listdir(test_path) #reads all files in the graphs-lab1 folder
    graphs=[]
    solutions=[]
    for file in files:
        if not file.startswith('.'): #want to avoid hidden files
            test_file=test_path+f"/{file}" #changing the path to my file
            V,L,sol=loadWeightedGraph(test_file)
            graph=[[] for _ in range(V)]
            for (x,y,c) in L: #I'm browsing through all the edges - remembering that I'm numbering from 1 in the file, but I'll change it for the solution -> I also remember that I'm dealing with an undirected graph
                graph[x-1].append((y-1,c))
                graph[y-1].append((x-1,c))
            graphs.append(graph)
            solutions.append(sol)
    return graphs,solutions

def check(solutions,act_test,sol_recive,test_time):
    global TEST_PASSED
    print(f"Result received {sol_recive}, expected result {solutions[act_test]}")
    print(f"Time: {test_time}s")
    if solutions[act_test]==sol_recive:
        print("TEST PASSED")
        TEST_PASSED+=1
    else:
        print("TEST FAILED!")



def sum_up(all_test): #function summarizing how many tests I have passed
    global TEST_PASSED,ALL_TEST,TOTAL_TIME
    if all_test:
        print(f"Passed tests: {TEST_PASSED}/{ALL_TEST}")
        print(f"Total time: {round(TOTAL_TIME, 4)}s")
        if TEST_PASSED==ALL_TEST:
            print("Congratulations! All tests passed")
    else:
        print(f"Passed tests: {TEST_PASSED}/{BASIC_TEST}")
        print(f"Total time: {round(TOTAL_TIME, 4)}s")
        if TEST_PASSED==BASIC_TEST:
            print("Congratulations! All tests passed")

def testing(f,all_test):
    global TOTAL_TIME
    graphs,solutions=gen_tests()
    if all_test:
        for act_test in range(ALL_TEST):
            print(f"TEST {act_test}:")
            start_time=datetime.datetime.now()
            sol_recive=f(graphs[act_test],0,1)
            end_time=datetime.datetime.now()
            test_time = round((end_time - start_time).total_seconds(),4)
            TOTAL_TIME+=test_time
            check(solutions,act_test,sol_recive,test_time)
    else:
        for act_test in range(BASIC_TEST):
            print(f"TEST {act_test}:")
            start_time = datetime.datetime.now()
            sol_recive=f(graphs[act_test],0,1)
            end_time = datetime.datetime.now()
            test_time = round((end_time - start_time).total_seconds(),4)
            TOTAL_TIME += test_time
            check(solutions,act_test,sol_recive,test_time)
    sum_up(all_test)
