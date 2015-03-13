import numpy
def closest_points(a, b, ncp=10):
    '''Returns the closest points from "b" for each line in "a"
    a is the array representing the points for which the closest have to be
    found
      - has the format: (x,y,z) or (id,x,y,z)
    b is the array containing all the points, among which some will be chosen as
      closest
      - has the format: (x,y,z) or (id,x,y,z)

    The Algorithm goes as follows:
        - classify b in groups using the resultant r = x1**2 + x2**2 + x3**2
        - store the groups in a dictionary that can be easily tracked
          later
        - for each point in a identify its resultant "r" and find the
          group above and below
        - using the groups from above and from below build a distance
          matrix
        - extract the closest points according to the "ncp" parameter
    '''
    def get_std( s ):
        if len(s.shape) == 1:
            s_ids = range(s.shape[0])
            s = s
        else: # assuming shape = (:,4)
            s_ids = s[:,0]
            s = s[:,1:]
        return s_ids, s
    a_ids, a = get_std(a)
    b_ids, b = get_std(b)
    r_b = b[:,0]**2 + b[:,1]**2 + b[:,2]**2
    r_b_argsort = r_b.argsort()
    r_b_sorted = r_b[r_b_argsort]
    num_groups_b = 1000
    group_r_vals = numpy.linspace(r_b_sorted[0],r_b_sorted[-1],num_groups_b)
    groups_b = {} # stored group_r_val:[pos,pt]
    group_i = 0
    for i, r_b in enumerate(r_b_sorted):
        if group_b_vals[i]
    # for the measured_imp routines there is not need to keep track of
    # ids... so this can be much simplified... we have to go along only
    # with the coordinates





