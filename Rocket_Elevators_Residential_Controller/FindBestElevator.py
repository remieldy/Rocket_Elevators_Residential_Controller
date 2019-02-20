
class find_best_elevator():
    def __init__(self, direction, requested_floor):
        self.find_best_elevator = find_best_elevator
        self.direction = direction
        self.requeted_floor = requested_floor


# SEQUENCE FindBestElevator USING Direction AND RequestedFloor
#    WHILE Elevator IS NOT Found
#        FOR EACH Elevator in Elevators
#            IF RequestedFloor = Elevator CurrentFloor THEN
#               IF Status IS Stopped AND ElevatorDirection IS Direction THEN
#                    RETURN Elevator
#               ELSE IF Status IS Idle THEN
#                    RETURN 
#               END IF
#            ELSE IF RequestedFloor > Elevator CurrentFloor THEN
#                IF Status IS Moving AND ElevatorDirection IS GoingUp AND Direction IS ElevatorDirection THEN
#                    RETURN Elevator
#                ELSE IF Status IS Stopped AND ElevatorDirection IS GoingUp AND Direction IS ElevatorDirection THEN
#                    RETURN Elevator
#                END IF 
#             ELSE IF RequestedFloor < Elevator CurrentFloor THEN
#                IF Status IS Moving AND ElevatorDirection IS GoingDown AND Direction IS ElevatorDirection THEN
#                    RETURN Elevator
#                ELSE IF Status IS Stopped AND ElevatorDirection IS GoingDown AND Direction IS ElevatorDirection
#                    RETURN Elevator
#                END IF
#             ELSE 
#                 IF DETERMINE Elevator CurrentFloor IS Nearest Elevator AND Elevator FloorList IS Shortest THEN
#                     RETURN Elevator
#                 ELSE IF Status IS Idle THEN
#                     RETURN Elevator
#                 END IF
#            END IF
#        END FOR
#   END WHILE
# END SEQUENCE