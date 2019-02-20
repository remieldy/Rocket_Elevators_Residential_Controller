

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

# inside button
    def generate_button(self):
        for x in range(self.nb_floor):
            if x!=(self.nb_floor -1):
                self.call_buttons.append(call_button("UP", x+1))
            if x!=0:
                self.call_buttons.append(call_button("DOWN", x+1))

#outside button
        for x in range(self.nb_elevator):
            	self.nb_elevators_list.append(elevator(x+1, 'idle', "none", 1, 1, "close", [], []))


                       
class call_elevator():
    def __init__(self, direction, floor, activate_call_button):
        self.call_elevator = call_elevator
        self.direction = direction
        self.floor = floor
        self.activate_call_button = activate_call_button
       


# ----------------------------------------------------------------------------------------------------
#i define how find elevator with direction up and down and the floor of the building are
class find_elevator():
    def __init__(self, direction, floor):  #returning elevator 
        self.find_elevator = find_elevator
        self.direction = direction
        self.floor = floor


# --------------------------------------------------------------------------------------------------
 # i define a doors Class with priority (itself, open and closed)
# i define my class doors with each attributes
class doors():
    def __init__(self, open, closed):
        self.doors = door
        self.doors = doors_open
        self.doors = doors_closed

# i define a class for the light inside elevator and i put priority ( itself, open, closed)
# i define a class with each attributes)
class inside_light_elevator():
    def __init__(self, open, closed):
        self.inside_light_elevator = inside_light_elevator
        self.open = open
        self.closed = closed
        # -------------------------------------------------------------------------------------------------------------

class request_floor():
    def __init__(self, elevator, requested_floor):
        self.request_floor = request_floor
        self.elevator = elevator
        self.requested_floor = requested_floor


"""
        SEQUENCE RequestFloor USING Elevator AND RequestedFloor 
    CALL ActivateFloorRequestButton WITH Elevator AND RequestedFloor
    IF  RequestedFloor IS GREATER THAN Elevator CurrentFloor AND Elevator Direction IS GoingUp THEN 
        CALL RequestElevator WITH Elevator AND RequestedFloor
    ELSE IF RequestedFloor IS SMALLER THAN Elevator CurrentFloor AND Elevator Direction IS GoingUp THEN
        CALL RequestElevator WITH Elevator AND RequestedFloor
    ELSE
        CALL OpenDoor WITH Elevator
END SEQUENCE
"""
# --------------------------------------------------------------------------------------------------------------------------

class find_floor_request_button():
    def __init__(self, elevator, floor):
        self.find_floor_request_button = find_floor_request_button
        self.elevator = elevator
        self.floor = floor

"""
        SEQUENCE FindFloorRequestButton USING Elevator AND Floor 
    FOR EACH Button IN FloorRequestButtons 
        IF Floor = Button Floor AND Direction = Button Direction THEN
            RETURN Button 
    END FOR 
END SEQUENCE
"""
# --------------------------------------------------------------------------------------------------------------
#i defie how find elevator with direction up and down and the floor of the building are
class find_elevator():
    def __init__(self, direction, floor):  #returning elevator 
        self.find_elevator = find_elevator
        self.direction = direction
        self.floor = floor
   

    #  -----------------------------------------------------------------------------------------------------------
#  class find call button  with a "for loop"using direction and floor after
class find_call_button():
    def __init__(self, direction, floor):
        self.find_call_button = find_call_button
        self.direction = direction
        self.floor = floor

        # for i in range(0,n) :

#  SEQUENCE FindCallButton USING Direction AND Floor 
#     FOR EACH Button IN CallButtons 
#         IF Floor = Button Floor AND Direction = Button Direction THEN
#             RETURN Button 
#     END FOR 
# END SEQUENCE

# --------------------------------------------------------------------------------------------------------------------
#i define a class with elevtor and floor proprety 
#the button gonna active when customer pressed it for request his elevator
class activate_floor_request_button():
    def __init__(self, elevator, floor):
        self.activate_floor_request_button = activate_floor_request_button
        self.elevator = elevator
        self.floor = floor

"""
SEQUENCE ActivateFloorRequestButton USING Elevator AND Floor
    CALL FindButton WITH Direction AND Floor RETURNING Button
    SET Button Active
END SEQUENCE
"""
# ---------------------------------------------------------------------------------------------------------------------------
# class with button  when customer pressed it it send tou a elevator

class activate_call_button():
    def __init__(self, direction, floor):
        self.activate_call_button = activate_call_button
        self.direction = direction
        self.floor = floor
        
       
#             CALL FindButton WITH Direction AND Floor RETURNING Button
#     SET Button Active
# END SEQUENCE

# -----------------------------------------------------------------------------------------------

class open_door_button_pushed():
    def __init__(self):
        self.open_door_button_pushed = open_door_button_pused

        self.open_door_button_pushed =  elevator


# SEQUENCE OpenDoorButtonPushed FOR Elevator
#     CALL OpenDoor With Elevator
# END SEQUENCE
