#ARTUR GĘSIARZ
"""
    Aby testy dzialaly poprawnie nalezy w lokalnym folderze gdzie znajduje sie owy skrypt umiescic folder 'graphs-lab3', oraz plik
    dimacs.py.
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
    test_path=f'{getcwd()}/graphs-lab3' #znajduje aktualne
    count_files(test_path)
    files=listdir(test_path) #zczytuje wszystkie pliki w folderze graphs-lab1
    graphs=[]
    solutions=[]
    for file in files:
        if not file.startswith('.'): #chce uniknac ukrytych plikow
            test_file=test_path+f"/{file}" #zmieniam sciezkie do mojego pliku
            V,L,sol=loadDirectedWeightedGraph(test_file)
            graph=[[] for _ in range(V)]
            for (x,y,c) in L: #przegladam wszystkie krawedzie - pamietajac o tym ze numeruje od 1 w pliku ale na potrzeby rozwiazania bede to zmienial -> pamietam tez ze mam doczynienia z grafem nieskierowanym
                graph[x-1].append((y-1,c)) #zabezpieczenie przed tym, ze chodzi mi tylko o graf skierowany
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
    print('\n')


def sum_up(all_test): #funkcja podsumuwajaca ile testow zaliczylem
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

def testing(f,all_test):
    global TOTAL_TIME
    graphs, solutions = gen_tests()
    if all_test:
        for act_test in range(ALL_TEST):
            edges_amount=len(graphs[act_test])-1
            print(f"TEST {act_test}, S={0}, T={edges_amount}")
            start_time=datetime.datetime.now()
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
            sol_recive = f(graphs[act_test])
            end_time = datetime.datetime.now()
            test_time = round((end_time - start_time).total_seconds(),3)
            TOTAL_TIME += test_time
            check(solutions,act_test,sol_recive,test_time)
    sum_up(all_test)