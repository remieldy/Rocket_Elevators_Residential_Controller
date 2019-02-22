import time
import math


#  Check all elevators and clear all request list that the initiation system for all 
class battery(object):
    def __init__(self, nb_column, nb_elevator):
        self.status = "OPERATIONAL"
        self.nb_column = nb_column
        self.column_list = []
        self.generate_columns(nb_column, nb_elevator)



    #     while battery.status == "OPERATIONAL":
    #         for elevator in column_elevators:
    #             while floor_list == "NOT EMPTY":
    #                 if elevator_current_floor == floor:
    #                     if elevator.status == "STOPPED":
    #                         open_doors(elevator)
    #                 elif elevator_current_floor > floor:
    #                     if elevator.status == "MOVING":
    #                         if elevator.direction == move_down:
    #                             move_down(elevator, floor)
    #                 elif elevator_current_floor < floor:
    #                     if elevator.status == "MOVING":
    #                         if elevator.direction == "move_up":
    #                             move_up(elevator, floor)
    #                             if elevator.status == "IDLE":
    #                                 if elevator.direction == "GoingNoWhere":
    #                                     pass
#generate_column
    def generate_columns(self, nb_column, nb_elevator):
        for x in range(self.nb_column):
            self.column_list.append(Column("Column"+str(x+1), "Operational", 2, 10))

class call_button(object):
    def __init__(self, floor, direction):
        self.floor = floor
        self.direction = direction


class Column(object):  
    def __init__(self, column_name, status, nb_elevator, nb_floor):
        self.name = column_name
        self.status = "Operational"
        self.nb_elevator = nb_elevator
        self.nb_floor = nb_floor
        self.elevator_list = []
        self.generate_elevator()
        self.call_buttons = []
        self.generate_button()

        self.column_list = []


# inside button
    def generate_button(self):
        for x in range(self.nb_floor):
            if x!=(self.nb_floor -1):
                self.call_buttons.append(call_button("UP", x+1))
        if x!=0:
            self.call_buttons.append(call_button("DOWN", x+1))


#outside button 
    def generate_elevator(self):
        for x in range(self.nb_elevator):
            self.elevator_list.append(Elevator("elevator"+str(x+1), 'idle', "none", 0, 0, "close"))

class Elevator(object):   
    def __init__(self, name, status, direction, origin, nb_floor, doors):
        self.name = name
        self.status = status
        self.direction = direction
        self.origin = origin
        self.nb_floor = nb_floor
        self.doors = doors
        self.call_button = []
        self.floor_list = []
        self.current_floor = 1
        

    def activate_floor_request_button(self, elevator, floor, direction):
        print("activate_floor_request_button")

        #button = find_button(direction, floor)
        #return button
        #button.active is true


    def deactivate_floor_request_button(self, direction, floor): #returning button
        print("deactivate_floor_request_button")
        #find_button(direction, floor)
# return button
# button.inactive is true


def find_elevator(self, direction, floor):  #returning elevator 
        self.find_elevator = find_elevator
        self.direction = direction.up
        self.floor = floor

        
def move_up(self, status, up, idle):
        self.status = status
        self.up = up
        self.idle = idle


def move_down(self, status, down, idle):
        self.move_down = move_down
        self.status = status
        self.down = down
        self.idle = idle



# class elevator_doors(object):
#     def __init__(Self, status, elevator):
#         self.elevator_doors = elevator_doors
#         self.status = status
#     def open_doors(self, Open):
#         if elevator.status == "Stopped":
#             if elevator_doors == "Open":
#                 import time 
#             time.sleep(5)
#             if elevator_doors == "Close":

#                 def close_doors(self, elevator):
#                     if elevator.doors == "Close":
#                         while elevator.doors == "close":
#                             if elevator.doors == "Obstructed":
#                                 break


    #     # if light == "OFF":
    #     #     break
    # def turn_light_on(self):
    #     if light == "ON":
    #         break
    # def turn_light_off(self):
    #     if light == "OFF":
    #        break


#     def find_call_button(direction, floor):
#         for button in call_button:
#             if floor == button.floor and direction == button.direction:
#                 return button

#     def open_doors_button_pushed(self):
#         self.open_door_button_pushed = open_door_button_pused

 
def request_floor(self, elevator, requested_floor):

    #self.current_floor = current_floor
      
    if ((requested_floor > elevator.current_floor) and (elevator.direction == "GoingUp")):          
        requested_floor(elevator.requested_floor)         
    elif ((requested_floor < elevator.current_floor) and (elevator.direction == "GoingUP")):       
        print("request_elevator")
        #request_elevator(elevator, requested_floor)       
    
    elevator.open_doors()
                
        

def activate_floor_request_button(self, floor, direction):
    print("activate_floor_request_button")


    #self.activate_floor_request_button = activate_floor_request_button
    #self.floor = floor
    #self.direction = direction
  #  button = find_call_Button(floor, direction)
      #  return button
  #  button.active = true
       # break


    # def __init__(self, name, status, direction, origin, nb_floor, doors, activate_call_button, floor_list):
elevatorsss = Elevator("coucou", "idle", "up", 0, 10, "close")
print("first.elevatorsss.status =" + elevatorsss.status)

print("Debut test de base remi*****************************")
column = Column("column_name", "Idle", 2, 10)
print("first column status = " + column.status)

for elevator in column.elevator_list:
    print(elevator)
    print(elevator.name)
print("FIN test de base remi*****************************")

for elevator in column.call_buttons:
    print("call_buttons")


# print("Debut remi test scenario 1 exigence*****************************")
# column_test_scenario_1 = Column("Idle", 2, 10)





# Etape 1: Creer une battery
# Etape 2 Creer une column
# Etape 3: Creer des ascenseurs
# Etape 4: Gerer les Call buttons
# Etape 5: Liste de requetes des ascenseurs
# Etape 6: Gerer le bon choix d'ascenseur
# Etape 7: Gerer les deplacements des ascenseurs

# /////////////////// TEST /////////////////
#battery1 = Battery(1, 2)

# request_floor(battery1.column_list[0].elevator_list[0], 8)



