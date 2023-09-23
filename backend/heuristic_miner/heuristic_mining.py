import graphviz
from prettytable import PrettyTable

class HeuristicMiner:

    def __init__(self, file, dependency_threshold, and_threshold):
        self.file = file
        self.dependency_threshold = dependency_threshold
        self.and_threshold = and_threshold
        self.loops_two = {}
        self.frequency = {}
        self.dependency = {}
        self.input = {}
        self.output = {}
        self.eventLog = []
        self.activities = []

    def step_1(self):
        #read file:
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
            self.eventLog.append(trace)
        # check all activities:
        for trace in self.eventLog:
            traceLength = len(trace)
            for i in range(traceLength):
                if self.activities.count(trace[i]) == 0:
                    self.activities.append(trace[i])
        self.activities.sort()
        # check frequency of all pairs:
        for trace in self.eventLog:
            trace_length = len(trace)
            for i in range(trace_length):
                if i < trace_length - 1:
                    tmp = (trace[i], trace[i+1])
                    reversed_tmp = (trace[i+1], trace[i])
                    # not loops of length two:
                    if tmp not in self.frequency:
                        self.frequency[tmp] = 1 
                    else:
                        self.frequency[tmp] = self.frequency[tmp] + 1 
                    # check frequency of a loop of length two : ACDCDCDCDB, ACDCDB, ACDCDB
                    if i < trace_length - 3:
                        next = (trace[i+2], trace[i+3])
                        if tmp == next:
                            if tmp in self.frequency:
                                del self.frequency[tmp]
                            if tmp not in self.loops_two:
                                self.loops_two[tmp] = 1
                            else:
                                self.loops_two[tmp] = self.loops_two[tmp] + 1
                    if i < trace_length - 2:
                        if tmp in self.loops_two or reversed_tmp in self.loops_two:
                            if trace[i+2] == trace[i]:  
                                    self.loops_two[tmp] = self.loops_two[tmp] + 1
        # mining the dependency:
        for i in self.frequency:
            reverse = (i[1], i[0])
            if i[0] == i[1]: # loop of length one
                self.dependency[i] = self.frequency[i] / (self.frequency[i] + 1)
            else: 
                if reverse in self.frequency: # causal in both directions
                    self.dependency[i] = (self.frequency[i] - self.frequency[reverse]) / (self.frequency[i] + self.frequency[reverse] + 1)
                else: # causal in one direction
                    self.dependency[i] = self.frequency[i] / (self.frequency[i] + 1)
            self.dependency[i] = round(self.dependency[i], 3)
        for i in self.loops_two:
            reverse = (i[1], i[0]) 
            self.dependency[i] = (self.loops_two[i] + self.loops_two[reverse]) / (self.loops_two[i] + self.loops_two[reverse] + 1)
            self.dependency[i] = round(self.dependency[i], 3)
        sorted(self.dependency)
        return self.dependency  
        
    def step_2(self):
        for pair in self.dependency:
            if self.dependency[pair] >= self.dependency_threshold:
                first = pair[0].split(',')
                for current in first:
                    if current in self.output and pair[1] not in self.output[current]:
                        self.output[current].append(pair[1])
                    else:
                        self.output[current] = [pair[1]]
                last = pair[1].split(',')
                for current in last:
                    if current in self.input and pair[0] not in self.input[current]:
                        self.input[current].append(pair[0])
                    else:
                        self.input[current] = [pair[0]]
        # check start activities:
        start = []
        for trace in self.eventLog:
            if start.count(trace[0]) == 0:
                start.append(trace[0])
        start.sort()
        for current in start:
            if current in self.output:
                self.input[current] = ['0']
        # check end activities:
        end = []
        for trace in self.eventLog:
            if end.count(trace[len(trace)-1]) == 0:
                end.append(trace[len(trace)-1])
        end.sort()
        for current in end:
            if current in self.input:
                self.output[current] = ['0']
        # check xor relation in output:
        for key in self.output:
            if self.output[key] == ['0']:
                continue 
            xor = []
            value = []
            value.extend(self.output[key])
            while (len(value) != 0):
                current = value.pop(0)
                for next in value:
                    tmp = (current, next)
                    reversed_tmp = (next, current)
                    tmp_frequency = 0
                    if tmp in self.frequency:
                        tmp_frequency = self.frequency[tmp]
                    reversed_tmp_frequency = 0
                    if reversed_tmp in self.frequency:
                        reversed_tmp_frequency = self.frequency[reversed_tmp]
                    key_tmp = (key, current)
                    key_reversed_tmp = (key, next)
                    key_tmp_frequency = 0
                    if key_tmp in self.frequency:
                        key_tmp_frequency = self.frequency[key_tmp]
                    key_reversed_tmp_frequency = 0
                    if key_reversed_tmp in self.frequency:
                        key_reversed_tmp_frequency = self.frequency[key_reversed_tmp]
                    test_xor = (tmp_frequency + reversed_tmp_frequency) / (key_tmp_frequency + key_reversed_tmp_frequency + 1)
                    if test_xor < self.and_threshold:
                        xor.append(tmp)  
            temp = []
            temp.extend(self.output[key])
            for current in self.output[key]:
                for tmp in xor:
                    if current in tmp and current in temp:
                        temp.remove(current)                         
            self.output[key] = temp
            for tmp in xor:
                self.output[key].append(tmp)
        # sort output after key:
        myKeys = list(self.output.keys())
        myKeys.sort()
        sorted_dict = {i: self.output[i] for i in myKeys}
        self.output = sorted_dict
        # check xor relation in input:
        for key in self.input:
            if self.input[key] == ['0']:
                continue 
            xor = []
            value = []
            value.extend(self.input[key])
            while (len(value) != 0):
                current = value.pop(0)
                for next in value:
                    tmp = (current, next)
                    reversed_tmp = (next, current)
                    tmp_frequency = 0
                    if tmp in self.frequency:
                        tmp_frequency = self.frequency[tmp]
                    reversed_tmp_frequency = 0
                    if reversed_tmp in self.frequency:
                        reversed_tmp_frequency = self.frequency[reversed_tmp]
                    key_tmp = (current, key)
                    key_reversed_tmp = (next, key)
                    key_tmp_frequency = 0
                    if key_tmp in self.frequency:
                        key_tmp_frequency = self.frequency[key_tmp]
                    key_reversed_tmp_frequency = 0
                    if key_reversed_tmp in self.frequency:
                        key_reversed_tmp_frequency = self.frequency[key_reversed_tmp]
                    test_xor = (tmp_frequency + reversed_tmp_frequency) / (key_tmp_frequency + key_reversed_tmp_frequency + 1)
                    if test_xor < self.and_threshold:
                        xor.append(tmp)
            temp = []
            temp.extend(self.input[key])
            for current in self.input[key]:
                for tmp in xor:
                    if current in tmp and current in temp:
                        temp.remove(current)         
            self.input[key] = temp
            for tmp in xor:
                self.input[key].append(tmp)
        # sort input after key:
        myKeys = list(self.input.keys())
        myKeys.sort()
        sorted_dict = {i: self.input[i] for i in myKeys}
        self.input = sorted_dict

    def find_column(self, dict):
        column = []
        for current in dict:                                
            str = ""
            for value in dict[current]:
                if len(value) > 1:
                    if isinstance(value, tuple) == True:
                        str = str + "("             
                        for i in value:
                            str = str + i 
                            if value.index(i) < len(value) - 1:
                                str = str + " ∨ "
                            else:
                                str = str + ")"
                    else:
                       str = str + value 
                else:
                    str = str + value
                if dict[current].index(value) < len(dict[current])-1:
                    str = str + " ∧ """
            column.append(str)
        return column

    def step_3(self):
        if len(self.input) == 0 or len(self.output) == 0:
            dot = graphviz.Digraph('heuristic', format='pdf')
            with dot.subgraph(name="heuristic net", node_attr={'shape': 'square'}, graph_attr={'rankdir':  'LR', 'nodesep': '1' }) as net:
                net.graph_attr['ranksep'] = '1'
                net.node_attr['shape'] = 'square'
                dot.node("no relations detected")
            return dot.view()
        dot = graphviz.Digraph('heuristic', format='pdf')
        with dot.subgraph(name="heuristic net", node_attr={'shape': 'square'}, graph_attr={'rankdir':  'LR', 'nodesep': '1' }) as net:
            net.graph_attr['ranksep'] = '1'
            net.node_attr['shape'] = 'square'
            for key in self.output:
                dot.node(key)
                visited = []
                for value in self.output[key]:
                    if isinstance(value, tuple) == True:
                        for i in value:
                            if visited.count(i) == 0:
                                visited.append(i)
                                dot.node(i)
                                if i != '0':
                                    tmp = self.dependency[(key,i)]
                                    dot.edge(key, i, label = str(tmp))
                                else:
                                    dot.edge(key, i)
                    else:
                        if visited.count(value) == 0:
                            visited.append(value)
                            if value != '0':
                                tmp = self.dependency[(key,value)]
                                dot.edge(key, value, label = str(tmp))
                            else:
                                dot.edge(key, value)
        with dot.subgraph(name = 'causal matrix') as causal_matrix:
            html_string = self.causal_matrix()
            causal_matrix.node("net",shape = "plaintext", label = html_string)
        return dot.view()

    def causal_matrix(self):
        if len(self.input) == 0 or len(self.output) == 0:
            return 0
        activity = []
        for current in self.activities:
            activity.append(current)
        input = self.find_column(self.input)
        output = self.find_column(self.output)
        table = PrettyTable()
        table.add_column("ACTIVITY", activity)
        table.add_column("INPUT", input)
        table.add_column("OUTPUT", output)
        table_format: str = "html"
        html_string = table.get_formatted_string(table_format)
        html_string = html_string.replace("<thead>", "").replace("</thead>", "").replace("<tbody>","").replace("</tbody>", "").replace("<th>", "<td>").replace("</th>", "</td>")
        html_string = "<" + html_string + ">"
        return html_string

    def heuristic_net(self):
        self.step_1()
        self.step_2()
        return self.step_3()


        
        

    




                



        






        
                    


