# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:39:05 2020

@author: gouna
"""


def next_states(s):
    l = []
    if s[-1] == "I":
        if s+"U" not in l:
            l.append(s + "U")
    if s[0] == ("M"):
        if s+s[1:] not in l:
            l.append(s + s[1:])
    if "III" in s:
        for i in range(len(s)):
            index = s.find("III", i, i + 3)
            if index != -1:
                if s[:index] + "U" + s[(index + 3):] not in l:
                    l.append(s[:index] + "U" + s[(index + 3):])
    if "UU" in s:
        temp = s.replace("UU", "")
        if temp not in l:
            l.append(s.replace("UU", ""))
    return l

def extendPath(p):
    arr = []
    list = []
    l = next_states(p[-1])
    for i in l:
        for x in p:
            arr.append(x)
        arr.append(i)
        list.append(arr)
        arr = []
    return list

def breadthFirstSearch(goalString):
    agenda = [["MI"]]
    limit = 1000
    count = 0
    max = 0
    
    while len(agenda) > 0:
        if count <= limit:
            if max < len(agenda):
                max = len(agenda)
            current = agenda.pop(0)
            if current[-1] == goalString:
                print ("path size:", len(current), "| extendPath() was called", count, "times | the max size of agenda was", max)
                return current
            else:
                next = extendPath(current)
                count = count + 1
                agenda = agenda + next
        else:
            print(count)
            return []

def depthlimited_dfs(goalString, lenlimit):
    agenda = [["MI"]]
    count = 0
    max = 0
    
    while len(agenda) > 0:
        if max < len(agenda):
            max = len(agenda)
        current = agenda.pop(0)
        if current[-1] == goalString:
            print ("path size:", len(current), "| extendPath() was called", count, "times | the max size of agenda was", max)
            return current
        elif len(current) < lenlimit:
            next = extendPath(current)
            count = count + 1
            agenda = next + agenda
    
    return []

def dfs_iter (goalString):
    limit = 2
    path = depthlimited_dfs(goalString, limit)
    while path == []:
        limit = limit + 1
        path = depthlimited_dfs(goalString, limit)
    return path

def bfsDict(goalString):
    agenda = ["MI"]
    dictionary = {}
    limit = 1000
    count = 0
    max = 0
    
    while len(agenda) > 0:
        if count <= limit:
            if max < len(agenda):
                max = len(agenda)
            current = agenda.pop(0)
            if current == goalString:
                dictCount = 1
                path = current
                found = False
                while found == False:
                    current = dictionary[current]
                    path = current + ", " + path
                    dictCount += 1
                    if current == "MI":
                        found = True
                print ("path size:", dictCount, "|  next_states() was called", count, "times | the max size of agenda was", max)
                return path
            else:
                next = next_states(current)
                for x in next:
                    dictionary[x] = current
                    agenda.append(x)
                    
                count = count + 1
        else:
            print(count)
            return []
    
def estimateSteps(current, goal):
    if(current == goal):
        return 0
    else:
        return 1
    
def astarSearch(goalString):
    agenda = ["MI"]
    visited = []
    dictionary = {}
    limit = 1000
    count = 0
    max = 0
    while len(agenda) > 0:
        if count < limit:
            if max < len(agenda):
                max = len(agenda)
            minimum = pathSoFar("MI", agenda[0], dictionary) + estimateSteps(agenda[0], goalString)
            minimumElement = 0
            
            for index, item in enumerate(agenda):
                if (pathSoFar("MI", item, dictionary) + estimateSteps(item, goalString)) < minimum:
                    minimumElement = index
            current = agenda.pop(minimumElement)
            
            if current == goalString:
                dictCount = 1
                path = current
                found = False
                while found == False:
                    current = dictionary[current]
                    path = current + ", " + path
                    dictCount += 1
                    if current == "MI":
                        found = True
                print ("path size:", dictCount, "| next_states() was called", count, "times | the max size of agenda was", max)
                return path
            
            else:
                next = next_states(current)
                for x in next:
                    if x not in visited:
                        dictionary[x] = current
                        agenda.append(x)
                visited.append(current)
                count = count + 1
        else:
            print("limit reached", count)
            return []
            
def pathSoFar(initial, current, dictionary):
    if current == "MI":
        return 0
    dictCount = 0
    
    found = False
    while found == False:
        current = dictionary[current]
        dictCount += 1
        if current == "MI":
            found = True
    return dictCount
