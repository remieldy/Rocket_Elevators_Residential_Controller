
#    battery,call_button,column,elevator, inside button

class call_elevator(object):   
    def __init__(self, name, status, direction, origin, nb_floor, doors, activate_call_button, floor_list):
        self.call_elevator = call_elevator
        self.name = name
        self.status = status
        self.direction = direction
        self.origin = origin
        self.nb_floor = nb_floor
        self.doors = doors
        self.activate_call_button = activate_call_button
        self.floor_list = floor_list

        

        # SEQUENCE CallElevator USING Direction AND Floor 
#     CALL ActivateCallButton WITH Direction AND Floor 
#     CALL FindElevator WITH Direction AND Floor RETURNING Elevator 
#     CALL RequestElevator WITH Elevator AND Floor
# END SEQUENCE


#----------------------------------------------------------------------------------------------------
#i define how find elevator with direction up and down and the floor of the building are

    def find_elevator(self, direction, floor):  #returning elevator 
        self.find_elevator = find_elevator
        self.direction = direction
        self.floor = floor
#----------------------------------------------------------------------------------------------------------------

    def activate_call_button(self, direction, floor):
        self.activate_call_button = activate_call_button
        self.direction = direction
        self.floor = floor
        
        
#             CALL FindButton WITH Direction AND Floor RETURNING Button
#     SET Button Active
# END SEQUENCE

#-----------------------------------------------------------------------------------------------------------------------

    def request_elevator(self, elevator, requested_floor):
        self.request_elevator = request_elevator
        self.elevator = elevator
        self.requested_floor = requested_floor
    

# SEQUENCE RequestElevator USING Elevator AND RequestedFloor
#         ADD RequestedFloor TO Elevator FloorList
#         COMPUTE Sort WITH Elevator FloorList AND Elevator Direction RETURNING SortedFloorList
#         SET Elevator FloorList TO SortedFloorList
# END SEQUENCE

#----------------------------------------------------------------------------------------------------------




