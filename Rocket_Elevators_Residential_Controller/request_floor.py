
def request_floor(self, elevator, requested_floor):
    self.request_floor = request_floor
    self.elevator = elevator
    self.requested_floor = requested_floor


#         SEQUENCE RequestFloor USING Elevator AND RequestedFloor 
#     CALL ActivateFloorRequestButton WITH Elevator AND RequestedFloor
#     IF  RequestedFloor IS GREATER THAN Elevator CurrentFloor AND Elevator Direction IS GoingUp THEN 
#         CALL RequestElevator WITH Elevator AND RequestedFloor
#     ELSE IF RequestedFloor IS SMALLER THAN Elevator CurrentFloor AND Elevator Direction IS GoingUp THEN
#         CALL RequestElevator WITH Elevator AND RequestedFloor
#     ELSE
#         CALL OpenDoor WITH Elevator
# END SEQUENCE
