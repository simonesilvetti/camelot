class Observer:
    def update(self, state):
        print(state.get_node().get_name())