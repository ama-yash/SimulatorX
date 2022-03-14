import random
from count import count_all_si,count_all_sir
from covid_19_selectors import infect as cov_inf, sis_recover as cov_sis_recover, sir_recover as cov_sir_recover
from gen_simulation_tools import infect as gen_inf, recover_sir as gen_sir_recover, recover_sis as gen_sis_recover
from gen_simulation_tools import init_si_counts, update_si_counts, init_sir_counts, update_sir_counts
from genNode import generateNodes
from selector.selector import (activate_graph, load_susceptibility_matrix,
                               power_law, seed_graph)

class Models():
    #initialise parameters, generate network, and preparing for simulation
    def __init__(self, mode, parameters):
        self.mode = mode
        self.N = int(parameters["pop_size"])
        ethn = {
            "white": parameters["white"],
            "black": parameters["black"],
            "asian": parameters["asian"],
            "other": parameters["other"],
        }
        gen = {"male": parameters["male"], "female": parameters["female"]}
        ag = {
            "child": parameters["child"],
            "adult": parameters["adult"],
            "senior": parameters["senior"],
        }
        self.seeds = float(parameters["seeds"])
        self.time = int(parameters["time"])
        self.graph_code = int(parameters["graph_code"])
        self.m = int(parameters["m"])
        self.G = generateNodes(self.N, ethn, gen, ag, self.graph_code, self.m)
        if self.graph_code == 0:
            epsilon = 0.001
            gamma = -2.1
            self.act = power_law(epsilon, 1, gamma, self.N)
        if mode == 'manual':
            self.infection_parameters = {
                    "white": float(parameters["white_inf"]),
                    "black": float(parameters["black_inf"]),
                    "asian": float(parameters["asian_inf"]),
                    "other": float(parameters["other_inf"]),
                    "male": float(parameters["male_inf"]),
                    "female": float(parameters["female_inf"]),
                    "child": float(parameters["child_inf"]),
                    "adult": float(parameters["adult_inf"]),
                    "senior": float(parameters["senior_inf"]),
                }
            if parameters["model"] != 0:
                self.recovery_parameters = {
                    "white": float(parameters["white_rec"]),
                    "black": float(parameters["black_rec"]),
                    "asian": float(parameters["asian_rec"]),
                    "other": float(parameters["other_rec"]),
                    "male": float(parameters["male_rec"]),
                    "female": float(parameters["female_rec"]),
                    "child": float(parameters["child_rec"]),
                    "adult": float(parameters["adult_rec"]),
                    "senior": float(parameters["senior_rec"]),
                }
        else:
            self.dataframe = load_susceptibility_matrix()
    
    #perform SI compartment model
    def si(self):
        count_dicts = init_si_counts()
        seed_graph(self.G, self.seeds)     
        if self.mode == 'manual':
            for i in range(self.time):
                if self.graph_code == 0:
                    active_nodes = activate_graph(self.act, self.N)
                    for i in active_nodes:
                        count = 0
                        while count < self.m:
                            target = random.randint(0, self.N - 1)
                            if target != i and target not in self.G.neighbors(i):
                                self.G.add_edge(i, target)
                                count += 1
                else:
                    active_nodes = self.G.nodes()
                gen_inf(active_nodes, self.G, self.infection_parameters)
                data = count_all_si(self.G)
                count_dicts = update_si_counts(count_dicts, data)
            return count_dicts
        elif self.mode == 'covid':
            for t in range(self.time):
                active_nodes = activate_graph(self.act, self.N)
                for i in active_nodes:
                    count = 0
                    while count < self.m:
                        target = random.randint(0, self.N - 1)
                        if target != i and target not in self.G.neighbors(i):
                            self.G.add_edge(i, target)
                            count += 1
                cov_inf(active_nodes, self.G, self.dataframe)
                data = count_all_si(self.G)
                count_dicts = update_si_counts(count_dicts, data)
            return count_dicts
    
    #perform SIS compartment model
    def sis(self):
        count_dicts = init_si_counts()
        seed_graph(self.G, self.seeds)         
        if self.mode == 'manual':
            for i in range(self.time):
                if self.graph_code == 0:
                    active_nodes = activate_graph(self.act, self.N)
                    for i in active_nodes:
                        count = 0
                        while count < self.m:
                            target = random.randint(0, self.N - 1)
                            if target != i and target not in self.G.neighbors(i):
                                self.G.add_edge(i, target)
                                count += 1
                else:
                    active_nodes = self.G.nodes()
                gen_inf(active_nodes, self.G, self.infection_parameters)
                gen_sis_recover(active_nodes,self.G,self.recovery_parameters)
                data = count_all_si(self.G)
                count_dicts = update_si_counts(count_dicts, data)
            return count_dicts
        elif self.mode == 'covid':
            for t in range(self.time):
                active_nodes = activate_graph(self.act, self.N)
                for i in active_nodes:
                    count = 0
                    while count < self.m:
                        target = random.randint(0, self.N - 1)
                        if target != i and target not in self.G.neighbors(i):
                            self.G.add_edge(i, target)
                            count += 1
                cov_inf(active_nodes, self.G, self.dataframe)
                cov_sis_recover(active_nodes,self.G)
                data = count_all_si(self.G)
                count_dicts = update_si_counts(count_dicts, data)
            return count_dicts
    
    #perform SIR compartment model
    def sir(self):
        count_dicts = init_sir_counts()
        seed_graph(self.G, self.seeds) 
        if self.mode == 'manual':
            for i in range(self.time):
                if self.graph_code == 0:
                    active_nodes = activate_graph(self.act, self.N)
                    for i in active_nodes:
                        count = 0
                        while count < self.m:
                            target = random.randint(0, self.N - 1)
                            if target != i and target not in self.G.neighbors(i):
                                self.G.add_edge(i, target)
                                count += 1
                else:
                    active_nodes = self.G.nodes()
                gen_inf(active_nodes, self.G, self.infection_parameters)
                gen_sir_recover(active_nodes,self.G,self.recovery_parameters)
                data = count_all_sir(self.G)
                count_dicts = update_sir_counts(count_dicts, data)
            return count_dicts
        elif self.mode == 'covid':
            for t in range(self.time):
                active_nodes = activate_graph(self.act, self.N)
                for i in active_nodes:
                    count = 0
                    while count < self.m:
                        target = random.randint(0, self.N - 1)
                        if target != i and target not in self.G.neighbors(i):
                            self.G.add_edge(i, target)
                            count += 1
                cov_inf(active_nodes, self.G, self.dataframe)
                cov_sir_recover(active_nodes,self.G)
                data = count_all_sir(self.G)
                count_dicts = update_sir_counts(count_dicts, data)
            return count_dicts
        
    #define additional models below
