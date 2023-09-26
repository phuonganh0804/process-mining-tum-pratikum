import graphviz
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt

class AlphaAlgorithm:

    def __init__(self, file):
        self.file = file
        self.tL = []
        self.tI = []
        self.tO = []
        self.xL = []
        self.yL = []
        self.pL = []
        self.fL = [] 
        self.parallel = []
        self.eventLog = []
        self.min = []
        self.max = []
        self.event = {}

    def step_1(self):
        # check all traces in event log:
        file = open(self.file, 'r')
        text = file.read()
        file.close()
        traces = text.split('<trace>')
        traces.pop(0)
        for i in traces:
            events = i.split('<event>')
            events.pop(0)
            trace = []
            for event in events:
                indexN = event.find('name')
                n = 13
                name = ''
                while event[indexN+n] != '"':
                    name = name + event[indexN+n]
                    n += 1
                indexT = event.find('transition')
                if indexT != -1:
                    m = 19
                    transition = ''
                    while (m <= 26):
                        transition = transition + event[indexT+m]
                        m += 1
                    if transition == 'complete':
                        trace.append(name)
                else:
                    trace.append(name)
                # check frequency of each event: 
                if name not in self.event:
                    self.event[name] = 1
                else:
                    self.event[name] += self.event[name]
                # check all transitions:
                if self.tL.count(name) == 0:
                    self.tL.append(name)
            if self.eventLog.count(trace) == 0:
                self.eventLog.append(trace)
        self.tL.sort()
        return self.tL 
    
    def step_2(self):
        for trace in self.eventLog:
            if self.tI.count(trace[0]) == 0:
                self.tI.append(trace[0])
        self.tI.sort()
        return self.tI 
    
    def step_3(self):
        for trace in self.eventLog:
            if self.tO.count(trace[len(trace)-1]) == 0:
                self.tO.append(trace[len(trace)-1])
        self.tO.sort()
        return self.tO
    
    def test_independent(self, tmp):
        for i in range(len(tmp)): 
            for j in range(i, len(tmp)):
                if self.parallel.count((tmp[i], tmp[j]))!= 0 or self.parallel.count((tmp[j], tmp[j]))!= 0 :
                    return False
        return True 
    
    def step_4(self):
        # check causally related pairs: 
        basic = []
        for trace in self.eventLog:
            trace_length = len(trace)
            for i in range(trace_length):
                if i < trace_length - 1:
                    tmp = ([trace[i]], [trace[i+1]])
                    reversedTmp = ([trace[i+1]],[trace[i]])
                    if [trace[i]] == [trace[i+1]]:
                        if self.parallel.count((trace[i], trace[i+1])) == 0:
                            self.parallel.append((trace[i], trace[i+1]))
                    else:
                        if basic.count(tmp) == 0:
                            if basic.count(reversedTmp) == 0:
                                if self.parallel.count((trace[i], trace[i+1])) == 0:
                                    basic.append(tmp)
                            else:
                                basic.remove(reversedTmp)
                                self.parallel.append((trace[i], trace[i+1]))
                                self.parallel.append((trace[i+1], trace[i]))
        # check independent pairs:
        tmp = []
        tmp.extend(basic)
        for current in tmp:
            if self.test_independent(current[0]) == False or self.test_independent(current[1]) == False:
                basic.remove(current)
        tmp.clear()
        basic.sort()
        self.xL.extend(basic)
        self.min.extend(basic)
        #check maximum pairs
        while (len(basic) != 0):
            current = basic.pop(0)
            for next in basic:  
                if current[0] == next[0]:
                    tmpL = []
                    tmpL.extend(current[1])
                    for k in next[1]:
                        if tmpL.count(k) == 0:
                            tmpL.append(k)
                    tmpL.sort()
                    if self.test_independent(tmpL) == True:
                        if basic.count((current[0], tmpL)) == 0:
                            basic.append((current[0], tmpL))
                        # remove merged pair from minimum list:
                        if self.min.count((current)) != 0:
                            self.min.remove((current))
                        if self.min.count((next)) != 0:
                            self.min.remove((next))
                        # add the unioned pair to maximum list if not present:
                        if self.max.count((current[0], tmpL)) == 0:
                            self.max.append((current[0], tmpL))
                            if self.max.count((current)) != 0:
                                self.max.remove((current))
                            if self.max.count((next)) != 0:
                                self.max.remove((next)) 
                        else:
                            if (current[0], tmpL) != current and self.max.count((current)) != 0 :
                                self.max.remove((current))
                            if (current[0], tmpL) != next and self.max.count((next)) != 0:
                                self.max.remove((next)) 
                       
                elif current[1] == next[1]:
                    tmpF = []
                    tmpF.extend(current[0])
                    for k in next[0]:
                        if tmpF.count(k) == 0:
                            tmpF.append(k)
                    tmpF.sort()
                    if self.test_independent(tmpF) == True:
                        if basic.count((tmpF, current[1])) == 0:
                            basic.append((tmpF, current[1]))
                        if self.min.count((current)) != 0:
                            self.min.remove((current))
                        if self.min.count((next)) != 0:
                            self.min.remove((next))
                        if self.max.count((tmpF, current[1])) == 0:
                            self.max.append((tmpF, current[1]))
                            if self.max.count((current)) != 0:
                                self.max.remove((current))
                            if self.max.count((next)) != 0:
                                self.max.remove((next)) 
                        else:
                            if (tmpF, current[1]) != current and self.max.count((current)) != 0:
                                self.max.remove((current))
                            if (tmpF, current[1]) != next and self.max.count((next)) != 0:
                                self.max.remove((next)) 
                            
        self.xL.extend(self.max)                    
        return self.xL
    
    def step_5(self):
        self.yL.extend(self.min)
        self.yL.extend(self.max)
        return self.yL
    
    def step_6(self):
        #convert to string:
        for place in self.yL:
            tmp = self.convert_to_string(place)
            self.pL.append(tmp)
        self.pL.sort()
        self.pL.append('iL')
        self.pL.append('oL')
        return self.pL
    
    def convert_to_string(self, place):
        tmp = 'p('
        for current in place :
            string = '{' + ",".join(current) + '}'
            tmp = tmp + string
            if place.index(current) < len(place) - 1:
                tmp = tmp +', '
        tmp = tmp + ')'
        return tmp
    
    def step_7(self):
        for i in self.tI:
            self.fL.append(('iL', i))
        for place in self.yL:
            tmp = self.convert_to_string(place)
            for current in place:
                if place.index(current) == 0:
                    for i in current:
                        self.fL.append((i, tmp))
                else:
                    for i in current:
                        self.fL.append((tmp,i))
        for i in self.tO:
            self.fL.append((i, 'oL'))
        return self.fL
    
    def step_8(self):
        table = PrettyTable()
        table.field_names = ["Place", " "]
        dot = graphviz.Digraph('petrinet', format='png', graph_attr={'rankdir':  'LR', 'nodesep': '1' })
        dot.graph_attr['ranksep'] = '1'
        with dot.subgraph(name="places", node_attr={'shape': 'circle'}) as places:
            n = 1
            for current in self.pL:
                if current == "iL" or current == "oL":
                    places.node(current, xlabel = current, label=" ")
                else:
                    index = "p" + str(n)
                    n += 1
                    places.node(current, xlabel = index, label=" ")
                    table.add_row([index, current])
        table_format: str = "html"
        html_string = table.get_formatted_string(table_format)
        html_string = html_string.replace("<thead>", "").replace("</thead>", "").replace("<tbody>","").replace("</tbody>", "").replace("<th>", "<td>").replace("</th>", "</td>")
        html_string = "<" + html_string + ">"
        with dot.subgraph(name = 'places') as places:
            places.node("net",shape = "plaintext", label = html_string)
        with dot.subgraph(name="transitions", node_attr={'shape': 'square'}) as transitions:
            for current in self.tL:
                transitions.node(current)
        edges = {}
        visited =[]
        tmp = []
        tmp.extend(self.fL)
        for current in self.fL:
            if visited.count(current[0]) == 1 and visited.count(current[1]) == 1:
                dot.edge(current[0], current[1])
            if visited.count(current[0]) == 0 :
                visited.append(current[0])
                dot.edge(current[0], current[1])
                edges[current] = 1     
            if visited.count(current[1]) == 0:
                visited.append(current[1])
                if current not in edges.keys():
                    dot.edge(current[0], current[1])
                    edges[current] = 1   

        return dot.render()

    def get_petri_net(self):
        self.step_1()
        self.step_2()
        self.step_3()
        self.step_4()
        self.step_5()
        self.step_6()
        self.step_7()
        return self.step_8()
    
    def frequency(self):
        data = []
        label = []
        sorted_by_value = sorted(self.event.items(), key=lambda x:x[1], reverse=True)
        sorted_event = dict(sorted_by_value)
        for key in sorted_event:
            label.append(key)
            data.append(sorted_event[key])
        plt.xticks(range(len(data)), label)
        plt.xlabel('Activities')
        plt.ylabel('Frequency')
        plt.bar(range(len(data)), data) 
        plt.savefig('frequency.png')


            






      
    


    






        


    































