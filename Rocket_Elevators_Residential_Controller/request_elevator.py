
def request_elevator(self, elevator, requested_floor):
    self.request_elevator = request_elevator
    self.elevator = elevator
    self.requested_floor = requested_floor

    self.elevator_floor_list = elevator_floor_list

        
    
#         COMPUTE Sort WITH Elevator FloorList AND Elevator Direction RETURNING SortedFloorList
#         SET Elevator FloorList TO SortedFloorList
# END SEQUENCE

# SEQUENCE RequestElevator USING Elevator AND RequestedFloor
#         ADD RequestedFloor TO Elevator FloorList
#         COMPUTE Sort WITH Elevator FloorList AND Elevator Direction RETURNING SortedFloorList
#         SET Elevator FloorList TO SortedFloorList
# END SEQUENCE