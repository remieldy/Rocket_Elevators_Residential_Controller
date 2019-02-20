class Column(object):  
    def __init__(self, status, nb_elevator, nb_floor, direction):
        self.status = status
        self.nb_elevator = nb_elevator
        self.nb_floor = nb_floor
        self.direction = direction
        self.elevator_list = []
        self.generate_button = generate_button
        self.call_button = call_button

        # inside button
    def generate_button(self):
        for x in range(self.nb_floor):
            if x!=(self.nb_floor -1):
                self.call_buttons.append(call_button("UP", x+1))
            if x!=0:
                self.call_buttons.append(call_button("DOWN", x+1))

#outside button
        for x in range(self.nb_elevator):
            	self.elevators_list.append(elevator("elevator"+str(x+1), 'idle', "none", 0, 0, "close", [], []))


class elevator(object):   
    def __init__(self, name, status, direction, origin, nb_floor, doors, activate_call_button, floor_list):
        self.name = name
        self.status = status
        self.direction = direction
        self.origin = origin
        self.nb_floor = nb_floor
        self.doors = doors
        self.activate_call_button = activate_call_button
        self.floor_list = floor_list


    def inside_light_elevator(self, status):
        self.inside_light_elevator = inside_light_elevator
        self.status = status
        self.open_inside_light_elevator = open_inside_light_elevator
        self.closed_inside_light_elevator = closed_inside_light_elevator
        

    def Doors(self,status):
        self.doors = doors
        self.status = status
        self.open_doors = open_doors
        self.closed_doors = closed_doors

        open_doors.status is stopped
    open_doors():
        deactivate_call_button(elevator.direction and elevator.current_floor):
        deactivate_floor_request_button(elevator, elevator_current_floor):
    closed_door(elevator):


    def open_door_button_pushed(self):
        self.open_door_button_pushed = open_door_button_pused
    open_door(elevator):


        
    def find_call_button(direction, floor):
        for button in call_button
            if floor == button.floor and direction == button.direction
                return button

    def find_elevator(self, direction, floor):  #returning elevator 
        self.find_elevator = find_elevator
        self.direction = direction.up
        self.floor = floor

    
class find_best_elevator():
    def __init__(self, direction, requested_floor):
        self.find_best_elevator = find_best_elevator
        self.direction = direction
        self.requeted_floor = requested_floor

    for elevator in elevators
        if requested_floor == elevator_current_floor 
        if status.stopped and elevator.direction is direction
            return elevator


        elif status is "idle"
            return


        elif requested_floor > elevator_current_floor 
            is status.moving and elevator.direction is move_up and direction is elevator.direction
                return elevator


        elif status.stopped and elevator.direction is move_up and direction is elevator.direction
                return elevator


        elif requested_floor < elevator_current_floor
                status.moving and elevator.direction is move_down and direction is elevator.direction
                    return elevator


        elif status.stopped and elevator.direction is move_down and direction is elevator.direction
                return elevator
#                ELSE IF Status IS Stopped AND ElevatorDirection IS GoingDown AND Direction IS ElevatorDirection
#                    RETURN Elevator
#                END IF

        elif elevator_current_floor is nearest_elevator and elevator.floor_list is <
                return elevator

        else: status.idle 
                return elevator



    def find_floor_request_button(self, status, elevator, floor):

        for button in floor_requst_buttons
            if floor is button.floor and button.direction
                return button
            

        self.status = status
        self.find_floor_request_button = find_floor_request_button
        self.elevator = elevator
        self.floor = floor

        
    def move_up(self, status, up, idle):
        self.move_up = move_up
        self.status = status
        self.up = up
        self.idle = idle


    def move_down(self, status, down, idle):
        self.move_down = move_down
        self.status = status
        self.down = down
        self.idle = idle

    def request_elevator(self, elevator, requested_floor):
        
        self.request_elevator = request_elevator
        self.elevator = elevator
        self.requested_floor = requested_floor
        self.elevator_floor_list = elevator_floor_list

        
def request_floor(self, elevator, requested_floor):
    self.request_floor = request_floor
    self.elevator = elevator
    self.requested_floor = requested_floor
    
activate_floor_request_button(elevator, requested_floor)
    if requested_floop > elevator_current_floor == elevator.direction == move_up
requested_floor(elevator, requested_floor):

    elif requested_floor < elevator and 
    else (open_doors) #with elevator



                
        
        


