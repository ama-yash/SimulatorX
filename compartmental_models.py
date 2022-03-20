from activity_network import generate_activity_network
from selector.selector import seed_graph, infect, recover
from count import count_compartament_data, count_attributes, count_data
import networkx as nx

# constants
SEEDS = 1 # percentage of seeds, by default 1%
TIME = 100 # by default simulate for 100 timesteps
NEIGHBOURS_TO_INFECT = 2 # default number of nodes to infect

def check_graph(G, is_activity_network, infection_rate):
    if is_activity_network and G.number_of_edges() > 0:
        raise Exception("Activity network requires a graph without any edges. Please use G = nx.empty_graph(N) instead!")

    if not nx.get_node_attributes(G, "age") and not nx.get_node_attributes(G, "gender") and not nx.get_node_attributes(G, "ethnicity") and not infection_rate:
        raise Exception('Age, gender and ethnicity have not been set in the graph. Please specify infection_rate!')

def si(G, infection_rate=None, is_activity_network=False, seeds=SEEDS, time=TIME, neighbours_to_infect=NEIGHBOURS_TO_INFECT):
    # network logic
    check_graph(G, is_activity_network, infection_rate)

    nx.set_node_attributes(G, 'S', 'status')
    N = G.number_of_nodes()
    seed_graph(G, seeds) # seed the graph based on inital number of infection within the given population

    sus = []
    inf = []
    model_data = None

    if is_activity_network:
        data = count_attributes(G)
        model_data = {k: [] for k in list(data.keys())}

    for t in range(time):
        if is_activity_network:
            G, active_nodes = generate_activity_network(G, N, neighbours_to_infect)
        else:
            # if we are not using activity driven network all nodes are considered active
            active_nodes = list(G.nodes)

        # run the SI model
        infect(active_nodes, G, infection_rate)
        status_count = count_compartament_data(G)
        sus.append(status_count.get("S", 0))
        inf.append(status_count.get("I", 0))
        if is_activity_network:
            data = count_attributes(G)
            model_data = count_data(model_data, data)

    # if the model doesn't have any data return just the susceptible and infected lists
    return model_data or sus, inf


def sis(G, infection_rate=None, recovery_rate=None, is_activity_network=False, seeds=SEEDS, time=TIME, neighbours_to_infect=NEIGHBOURS_TO_INFECT):
    # network logic
    check_graph(G, is_activity_network, infection_rate)

    nx.set_node_attributes(G, 'S', 'status')
    N = G.number_of_nodes()
    seed_graph(G, seeds)  # seed the graph based on inital number of infection within the given population

    sus = []
    inf = []
    model_data = None

    if is_activity_network:
        data = count_attributes(G)
        model_data = {k: [] for k in list(data.keys())}

    for t in range(time):
        if is_activity_network:
            G, active_nodes = generate_activity_network(G, N, neighbours_to_infect)
        else:
            # if we are not using activity driven network all nodes are considered active
            active_nodes = list(G.nodes)

        # run the SI model
        infect(active_nodes, G, infection_rate)
        recover(active_nodes, G, recovery_rate)
        status_count = count_compartament_data(G)
        sus.append(status_count.get("S", 0))
        inf.append(status_count.get("I", 0))
        if is_activity_network:
            data = count_attributes(G)
            model_data = count_data(model_data, data)

    # if the model doesn't have any data return just the susceptible and infected lists
    return model_data or sus, inf


def sir(G, infection_rate=None, recovery_rate=None, is_activity_network=False, seeds=SEEDS, time=TIME, neighbours_to_infect=NEIGHBOURS_TO_INFECT):
    # network logic
    check_graph(G, is_activity_network, infection_rate)

    nx.set_node_attributes(G, 'S', 'status')
    N = G.number_of_nodes()
    seed_graph(G, seeds)  # seed the graph based on inital number of infection within the given population

    sus = []
    inf = []
    rec = []
    model_data = None

    if is_activity_network:
        data = count_attributes(G)
        model_data = {k: [] for k in list(data.keys())}

    for t in range(time):
        if is_activity_network:
            G, active_nodes = generate_activity_network(G, N, neighbours_to_infect)
        else:
            # if we are not using activity driven network all nodes are considered active
            active_nodes = list(G.nodes)

        # run the SI model
        infect(active_nodes, G, infection_rate)
        recover(active_nodes, G, recovery_rate, permanent_recovery=True)
        status_count = count_compartament_data(G)
        sus.append(status_count.get("S", 0))
        inf.append(status_count.get("I", 0))
        rec.append(status_count.get("R", 0))
        if is_activity_network:
            data = count_attributes(G)
            model_data = count_data(model_data, data)

    # if the model doesn't have any data return just the susceptible and infected lists
    return model_data or sus, inf, rec