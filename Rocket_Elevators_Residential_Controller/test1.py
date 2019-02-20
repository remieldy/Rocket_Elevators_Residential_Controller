class Column(object):  
    def __init__(self, status, nb_elevator, nb_floor, direction):
        self.status = status
        self.nb_elevator = nb_elevator
        self.nb_floor = nb_floor
        self.direction = direction
        self.nb_elevator_list = []
        self.generate_button = generate_button
        self.call_button = call_button

    	self.call_buttons = call_buttons


# inside elevator button
    def generate_button(self):
        for x in range(self.nb_floor):
            if x!=(self.nb_floor -1):
                self.call_buttons.append(call_button("UP", x+1))
            if x!=0:
                self.call_buttons.append(call_button("DOWN", x+1))

#outside button
        for x in range(self.nb_elevator):
            	self.nb_elevators_list.append(elevator(x+1, 'idle', "none", 1, 1, "close", [], []))

print("column")
                #        elevator def __init__(self, name, status, direction, origin, nb_floor, doors, activate_call_button, floor_list ):


class callButton(object):
    def __init__(self, floor, direction):
        self.floor = floor
        self.direction = direction
        self.activate_floor_request_button = activate_floor_request_button
        self.deactivate_floor_request_button = deactivate_floor_request_button
        self.activate_call_button = activate_call_button
        self.deactivate_call_button = deactivate_call_button

    
# SEQUENCE DeactivateFloorRequestButton USING Elevator AND Floor
#     CALL FindButton WITH Direction AND Floor RETURNING Button
#     SET Button Inactive 
# END SEQUENCE

    def activate_floor_request_button(self, elevator, floor):
        self.activate_floor_request_button = activate_floor_request_button
        self.elevator = elevator
        self.floor = floor

    def deactivate_floor_request_button(self, direction, floor): #returning button
        self.deactivate_floor_request_button = deactivate_floor_request_button
        self.direction = direction
        self.floor = floor
        
# SEQUENCE ActivateFloorRequestButton USING Elevator AND Floor
#     CALL FindButton WITH Direction AND Floor RETURNING Button
#     SET Button Active
# END SEQUENCE
# ---------------------------------------------------------------------------------------------
    def activate_call_button(self, direction, floor):
        self.activate_call_button = activate_call_buton
        self.direction = direction
        self.floor = floor

# SEQUENCE ActivateCallButton USING Direction AND Floor
#     CALL FindButton WITH Direction AND Floor RETURNING Button
#     SET Button Active
# END SEQUENCe
# --------------------------------------------------------------------
    def deactivate_call_button(self, direction, floor):
        self deacivate_call_button = deactivate_call_button
        self.direction = direction
        self.floor = floor
   
# SEQUENCE DeactivateCallButton USING Direction AND Floor
#     CALL FindButton WITH Direction AND Floor RETURNING Button
#     SET Button Inactive 
# END SEQUENCE

                