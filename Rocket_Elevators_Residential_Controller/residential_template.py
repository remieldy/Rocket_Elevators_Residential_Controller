Reference Alorithm for an Elevator System servicing a Residential Building
Definitions:


Battery: All the elevator sections operating for a given Building
Column: All the elevators operating a specific number of landings servicing a section of the Building
Floor: One of the destinations serviced by a given elevator
Elevator: One route going up and down
CallButton: Buttons located on each floors designed to call for an elevator to go up or down
FloorRequestButton: Buttons located inside an elevator to request a destination floor that the elevator will take the passenger to
Doors: The doors open and close to let passengers in or out of the elevator
OpenDoorButton: Button located inside an elevator to force the door to remain open
CloseDoorButton: Button located inside an elevator to request the closing of the door whenever possible


---------------------------------------------------------------------------------------------------------------------------

# SEQUENCE CallElevator USING Direction AND Floor 
#     CALL ActivateCallButton WITH Direction AND Floor 
#     CALL FindElevator WITH Direction AND Floor RETURNING Elevator 
#     CALL RequestElevator WITH Elevator AND Floor
# END SEQUENCE

----------------------------------------------------------------------------------------------------------------------------
# SEQUENCE RequestFloor USING Elevator AND RequestedFloor 
#     CALL ActivateFloorRequestButton WITH Elevator AND RequestedFloor
#     IF  RequestedFloor IS GREATER THAN Elevator CurrentFloor AND Elevator Direction IS GoingUp THEN 
#         CALL RequestElevator WITH Elevator AND RequestedFloor
#     ELSE IF RequestedFloor IS SMALLER THAN Elevator CurrentFloor AND Elevator Direction IS GoingUp THEN
#         CALL RequestElevator WITH Elevator AND RequestedFloor
#     ELSE
#         CALL OpenDoor WITH Elevator
# END SEQUENCE
----------------------------------------------------------------------------------------------------------------------

# SEQUENCE ActivateCallButton USING Direction AND Floor
#     CALL FindButton WITH Direction AND Floor RETURNING Button
#     SET Button Active
# END SEQUENCE
# ----------------------------------------------------------------------------------------------------------------------

# SEQUENCE DeactivateCallButton USING Direction AND Floor
#     CALL FindButton WITH Direction AND Floor RETURNING Button
#     SET Button Inactive 
# END SEQUENCE

----------------------------------------------------------------------------------------------------------------------
# SEQUENCE FindCallButton USING Direction AND Floor 
#     FOR EACH Button IN CallButtons 
#         IF Floor = Button Floor AND Direction = Button Direction THEN
#             RETURN Button 
#     END FOR 
# END SEQUENCE
----------------------------------------------------------------------------------------------------------------------

# SEQUENCE ActivateFloorRequestButton USING Elevator AND Floor
#     CALL FindButton WITH Direction AND Floor RETURNING Button
#     SET Button Active
# END SEQUENCE
# ---------------------------------------------------------------------------------------------------------------------

# SEQUENCE DeactivateFloorRequestButton USING Elevator AND Floor
#     CALL FindButton WITH Direction AND Floor RETURNING Button
#     SET Button Inactive 
# END SEQUENCE

--------------------------------------------------------------------------------------------------------------------
# SEQUENCE FindFloorRequestButton USING Elevator AND Floor 
#     FOR EACH Button IN FloorRequestButtons 
#         IF Floor = Button Floor AND Direction = Button Direction THEN
#             RETURN Button 
#     END FOR 
# END SEQUENCE

----------------------------------------------------------------------------------------------------------------------
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
---------------------------------------------------------------------------------------------------------------------------

# SEQUENCE RequestElevator USING Elevator AND RequestedFloor
#         ADD RequestedFloor TO Elevator FloorList
#         COMPUTE Sort WITH Elevator FloorList AND Elevator Direction RETURNING SortedFloorList
#         SET Elevator FloorList TO SortedFloorList
# END SEQUENCE
--------------------------------------------------------------------------------------------------------------------------

SEQUENCE OperateBattery
    WHILE Battery Status IS Operational
        FOR EACH Column IN Battery Columns
            FOR EACH Elevator IN Column Elevators 
                WHILE(FloorList IS NOT EMPTY)        
                    READ NextFloor FROM FloorList
                    IF CurrentFloor IS Floor THEN
                        SET Elevator Status TO Stopped 
                        CALL OpenDoor (Elevator)
                    IF CurrentFloor > Floor THEN
                        SET Elevator Status TO Moving
                        SET Elevator Direction TO GoingDown
                        CALL MoveDown (Elevator, Floor)
                    IF CurrentFloor < Floor THEN
                        SET Elevator Status TO Moving
                        SET Elevator Direction TO GoingUp
                        CALL MoveUp (Elevator, Floor)
                    END IF
                END WHILE
                SET Status TO Idle
                SET Direction to GoingNoWhere
            END FOR
        END FOR
    END WHILE
END SEQUENCE 

---------------------------------------------------------------------------------------------------------------------
SEQUENCE OpenDoor FOR Elevator
    IF Status IS NOT Moving THEN
        Open Elevator Doors
        SET Doors Timer TO 5 Seconds
        CALL DeactivateCallButton WITH Elevator Direction AND Elevator CurrentFloor
        CALL DeactivateFloorRequestButton WITH Elevator AND Elevator CurrentFloor
    END IF
    CALL CloseDoor WITH Elevator
END SEQUENCE
-----------------------------------------------------------------------------------------------------------------

SEQUENCE CloseDoor FOR Elevator
    WHILE Elevator Doors Timer IS GREATER THAN 0 Seconds
        IF Elevator Doors IS Obstructed THEN
            ADD 2 Seconds TO Elevator Doors Timer
    END WHILE
    Close Elevator Doors
    
    WHILE Doors IS Closing
        IF Elevator Doors IS Obstructed THEN
            CALL OpenDoor WITH Elevator
    END WHILE
END SEQUENCE
-----------------------------------------------------------------------------------------------------------

SEQUENCE MoveDown USING Elevator AND RequestedFloor 
    WHILE Elevator CurrentFloor IS GREATER THAN RequestedFloor
        Move Elevator Down 
        DECREMENT Elevator CurrentFloor BY 1
    END WHILE
END SEQUENCE
----------------------------------------------------------------------------------------------------

SEQUENCE MoveUp USING Elevator AND RequestedFloor 
    WHILE Elevator CurrentFloor IS SMALLER THAN RequestedFloor
        Move Elevator Up 
        INCREMENT Elevator CurrentFloor BY 1
    END WHILE
END SEQUENCE
-----------------------------------------------------------------------------------------------------

SEQUENCE OpenDoorButtonPushed FOR Elevator
    CALL OpenDoor With Elevator
END SEQUENCE
=---------------------------------------------------------------------------------------------------------

SEQUENCE CloseDoorButtonPushed FOR Elevator
    SET Elevator Doors Timer TO 0
    CALL CloseDoor WITH Elevator
END SEQUENCE