portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    if len(ports) == 0:
        print(' '.join([portnames[i] for i in route]))
    else:
        # Write your recursive code here
        for i in range(len(ports)):
            permutations(route + [ports[i]], ports[:i]+ports[i+1:])
    # Print the port names in route when the recursion terminates
    # print(' '.join([portnames[i] for i in route]))


# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))