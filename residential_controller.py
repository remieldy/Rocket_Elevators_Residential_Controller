import time
import math


# this  is the initial system for start the system for columns and elevator when is status is operational all system turn it on
print("Initial Battery Is Now Operational")
class Battery(object):
    def __init__(self, nb_column, nb_elevator):
        self.status = "OPERATIONAL"
        self.nb_column = nb_column
        self.column_list = []
        self.generate_columns(nb_column, nb_elevator)


  
                           
#generate_column and add in a column list
    def generate_columns(self, nb_column, nb_elevator):
        for x in range(self.nb_column):
            self.column_list.append(Column("Column"+str(x+1), 2, 10))

print("Starting Column System: ")
class Column(object):
    def __init__(self, column_name, nb_elevator, nb_floor):
        self.name = column_name
        self.status = "Operational"
        self.nb_elevator = nb_elevator
        self.nb_floor = nb_floor
        self.elevator_list = []
        self.generate_elevator()
        self.call_buttons = []
        self.generate_button()
        self.column_list = []
        print(column_name, "In Direction")
    


    def find_call_button(self, requested_floor, direction):
        best_elevator = None
        for button in self.elevator_list:
            if button.requested_floor == requested_floor and button.direction == direction:
                best_elevator = button
                print("FOUND BUTTON HAVE BEEN PRESSEND"+str(requested_floor))
                break
        return best_elevator


    def RequestElevator(self, requested_floor, direction):
        best_elevator = None
        nearest_elevator = self.nearestElevator(requested_floor)
        print("Nearest Elevator Is: " + str(nearest_elevator.name))
        for elevator in self.elevator_list:

            if requested_floor == elevator.current_floor:
                best_elevator = elevator
                print("The Best Elevator Is Choice:")
                # elevator.elevator_Doors()
              
            elif elevator == nearest_elevator:
                best_elevator = elevator 
                print("Second Nearest Elevator is Choice:")
                # elevator.elevator_Doors()
        
            elif elevator.status == "Stopped" and elevator.current_floor == requested_floor:
                best_elevator = elevator
                print("Third Nearest Elevator Is Choice:")
                # elevator.elevator_Doors()

            elif elevator.status == "Idle" and elevator.current_floor == requested_floor:
                best_elevator = elevator
                print("fourth Nearest Elevator Is Choice:")
                # elevator.elevator_Doors()

            elif elevator.status == "STOPPED" and direction == "GoingUp" and elevator.current_floor == requested_floor:
                best_elevator = elevator
                print("Fift Nearest Elevator Is Choice:")
                # elevator.elevator_Doors()

            elif elevator.status == "STOPPED" and direction == "GoingDown" and elevator.current_floor == requested_floor:
               best_elevator = elevator
               print("sixth Nearest Elevator Is Choice:")
        print("The Nearest Elevator: " + str(best_elevator.name)+str(requested_floor))
        best_elevator.floor_list.append(requested_floor)
        return best_elevator
    print("CalCulating The Nearest Elevator: ")
                
        
# reference_gap = difference between reference gap and gap between 
# each elevator Reference_gap is Elevator is looking for a distance then it goes around and finds the nearest   
    def nearestElevator(self, requested_floor):
        reference_gap = self.elevator_list[0].current_floor - requested_floor
        for elevator in self.elevator_list:
            gap = elevator.current_floor - requested_floor
            if gap <= reference_gap:
                reference_gap = gap
                nearest_elevator = elevator
        return nearest_elevator

# how elevator gonna move with alls parameter and return it 
    def moveElevator(self, elevator, requested_floor, direction, current_floor): 
        while requested_floor > elevator.current_floor:
            elevator.status == "moving"
            if elevator.status == "moving" and elevator.direction == "GoingUp" and direction == elevator.direction:
                if elevator.status == "moving" and elevator.direction == "GoingUp" and direction == elevator.direction:
                    return elevator
    #                 IF Status IS Stopped AND ElevatorDirection IS GoingUp AND Direction IS ElevatorDirection THEN
    #                    RETURN Elevator
        while requested_floor < elevator.current_floor:
            elevator.status == "moving"
            if elevator.status == "moving" and elevator.direction == "GoingDown" and direction == elevator.direction:
                if elevator.status == "STOPPED" and elevator.direction == "GoingDown" and direction == elevator.direction:
                    return elevator
    #                 IF Status IS Stopped AND ElevatorDirection IS GoingDown AND Direction IS ElevatorDirection
            if elevator.current_floor == elevator.best_elevator and elevator.floor_list < elevator.current_floor:
                return elevator
            else:
                return elevator

  
    def request_floor(self, elevator, requested_floor):
        # print activate_floor_request_button(Elevator, requested_floor)
        elevator.floor_list.append(requested_floor)
        
# it generate a request of outside elevator up and down and add it too call_button_list
    def generate_button(self):
        for x in range(self.nb_floor):
            if x!=(self.nb_floor -1):
                self.call_buttons.append(("UP", x+1))
            if x!=0:
                self.call_buttons.append(("DOWN", x+1))

# it generate elevator and add it too elevator list with them attribute
#outside button 
    def generate_elevator(self):
        for x in range(self.nb_elevator):
            self.elevator_list.append(Elevator("elevator"+str(x+1), 0, 0))


    def OperateElevator(self):
        for elevator in self.elevator_list:
            while len(elevator.floor_list) > 0:
                if elevator.current_floor == elevator.floor_list[0]:
                    elevator.status = "Stopped"
                    elevator.floor_list.pop(0)
                    elevator.elevator_doors()
                elif elevator.current_floor > elevator.floor_list[0]:
                    elevator.status = "Moving"
                    elevator.Direction = "GoingDown"
                    elevator.move_down(elevator.floor_list[0])
                    elevator.elevator_doors()
                elif elevator.current_floor < elevator.floor_list[0]:
                    elevator.status = "Moving"
                    elevator.Direction = "GoingUp"
                    elevator.move_up(elevator.floor_list[0])
                    elevator.elevator_doors()
            elevator.status = "Idle"
            elevator.Direction = "GoingNoWhere"
    print("Elevator Is Moving: ")

class Elevator(object):   
    def __init__(self, name, origin, nb_floor):
        self.name = name
        self.status = "idle"
        self.direction = "none"
        self.origin = origin
        self.nb_floor = nb_floor
        self.doors = "close"
        self.call_button = []
        self.floor_list = []
        self.current_floor = 1
        self.request_floor_list = []
        self.inside_light_elevator = "OFF"

          
# inside light with turn "off" and "on" 
    def turn_light(self, status, elevator):
        if elevator.inside_light_elevator == "OFF":
            print("light OFF")
        else:
            print("light ON")
            
            
#  making doors open of elevator with a timer of 5 secondes   and closed it after 5 secondes      
    def elevator_doors(self):
            elevator.doors = "Open"
            time.sleep(3)
            print("open_doors")
            elevator.doors = "Closed"
            time.sleep(5)
            print("elevator_doors" == "Closed")


#  create a sequence that moves Elevator up with the Elevator and Elevator position,
#  then it categorizes all the Elevator and if Elevator are bigger and it increases by 1 each time,
#  and repeats until it finds the good stages
    def move_up(self, floor):
        while self.current_floor < floor:
            self.current_floor +=1
            print(" #" + str(self.name) + " is at floor number: " + str(self.current_floor))

#  create a sequence that moves Elevator down with the Elevator and Elevator position,
#  then it categorizes all the Elevator and if Elevator are smaller and it decreases by 1 each time,

    def move_down(self, floor):
        while self.current_floor > floor:
            self.current_floor -=1
            print("#" + str(self.name) + " is at floor number: " + str(self.current_floor))


#   def __init__(self, name, origin, nb_floor):
# elevatorsss = Elevator("coucou", 0, 10,)
# print("first.elevatorsss.status =" + elevatorsss.status)

# print("Debut test de base remi*****************************")
# column = Column("column_name", 2, 10)
# print("first column status = " + column.status)

# for elevator in column.elevator_list:
#     print(elevator)
#     print(elevator.name)
# print("FIN test de base remi*****************************")

# for elevator in column.call_buttons:
#     print("call_buttons")


# print("Debut remi test scenario 1 exigence*****************************")
# column_test_scenario_1 = Column("column_name", 2, 10)



# /////////////////// TEST /////////////////

battery1 = Battery(1, 2)

battery1.column_list[0].elevator_list[0].current_floor = 10
battery1.column_list[0].elevator_list[1].current_floor = 9

elevator = battery1.column_list[0].RequestElevator(6, "UP")
battery1.column_list[0].OperateElevator()

battery1.column_list[0].request_floor(elevator, 8)
battery1.column_list[0].OperateElevator()



