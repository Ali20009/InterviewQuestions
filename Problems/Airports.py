'''
We should write a function where gets 3 inputs 
first one is all of our airports
second one is list of lists with length 2 which representes oneway connected airports
third is an specific airport

we need to return minimum new routers needed to have access to all other airports initilizing from given airport(3th input)

'''

class Min_flights:
    def calculator(self, airports: list[str], connections : list[list[str]], startingAirport : str ):

        con = dict()
        con[startingAirport] = self.routers(i , connections)

        # Base Case
        if not con[startingAirport]:
            return 
        
        for i in con[startingAirport]:
            self.calculator(airports , connections, i)

    def routers(self, airport, connections):
        con = {airport : []}
        for i in range(len(connections)):
            if connections[i][0] == airport:
                con[airport].append(connections[i][1])
        return con[airport]

    


ariport = Min_flights()
connections = [['teh', 'mash'], ['shi' , 'tab'], ['tab', 'esf']]

print(ariport.calculator(['teh', 'mash', 'shi' , 'tab', 'esf', 'ras'], connections , 'teh'))

