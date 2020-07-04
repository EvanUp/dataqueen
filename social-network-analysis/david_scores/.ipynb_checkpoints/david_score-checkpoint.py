# This function calculates David's Scores for a weighted, directed networkx Graph
# PDF of paper: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.490.7556&rep=rep1&type=pdf
# tags: david scores, david's scores, davids scores, bonobos, dominance hierarchies

def davids_score(G):
    """
    Calculates David's Scores for a directed, weighted NetworkX Graph object.
    See: "Measuring and testing the steepness of dominance hierarchies" for more details. PDF linked above.
    
    Returns a matrix of David's Scores that with indices corresponding to G.nodes()
    """
    
    adj = nx.adjacency_matrix(G)
    # convert to a dense matrix
    X = (adj.todense())
    # networkX's adjacency matrix needs to be transposed in order to be read correctly
    tmat = X.T+1
    # create a symmetrical matrix
    sym = X + tmat
    
    # Create a weighted proportion Matrix
    Dij = np.divide(tmat, sym) - (((np.divide(tmat, sym) - 0.5)/(sym+1)))
    
    # get row and col sums of proportion matrix
    w1 = np.sum(Dij, axis = 0)
    w2 = np.dot(w1, Dij)
    
    # get row and col sums weighted by the proportion matrix
    l1 = np.sum(Dij, axis = 1)
    l2 = l1.T * Dij
    
    # Get David's Scores for each node
    DS = w1 + w2 - l1.T - l2
    
    return DS



