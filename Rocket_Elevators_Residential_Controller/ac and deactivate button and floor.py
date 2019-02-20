
    def deactivate_floor_request_button(self, direction, floor): #returning button
        self.deactivate_floor_request_button = deactivate_floor_request_button
        self.direction = direction
        self.floor = floor
        
            
# SEQUENCE DeactivateFloorRequestButton USING Elevator AND Floor
#     CALL FindButton WITH Direction AND Floor RETURNING Button
#     SET Button Inactive 
# END SEQUENCE

    def activate_floor_request_button(self, elevator, floor):
        self.activate_floor_request_button = activate_floor_request_button
        self.elevator = elevator
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
