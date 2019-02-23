class Battery {
  constructor(nb_Floors, nb_elevators) {
    this.nb_Floors = nb_Floors;
    this.nb_elevators = nb_elevators;
    this.column = new Column(nb_floors, nb_elevators);
  }
  // take request of elevator with number of request floor and direction
  Request_Elevator(requested_nb_floor, direction) {
    console.log("Elevator requested at floor number", requested_floor_number);
    sleep(2000);
    console.log(
      "Elevator",
      this.column.elevator_list[0].elevator_number,
      "is currently at floor number",
      this.column.elevator_list[0].current_floor
    );
    sleep(2000);
    console.log(
      "Elevator",
      this.column.elevator_list[1].elevator_number,
      "is currently at floor number",
      this.column.elevator_list[1].current_floor
    );
    sleep(2000);
    // find elevator with the nearest one
    var nearest_elevator = this.FindElevator(requested_nb_floor, direction);
    console.log("Returning Elevator", nearest_elevator.elevator_number);
    sleep(2000);
    console.log(
      "Elevator",
      nearest_elevator.elevator_number,
      "is going",
      direction
    );
    nearest_elevator.addFloorToList(requested_nb_floor);
    nearest_elevator.move_next();
  }
  // take a request of number of floor with activate button
  Request_floor(elevator, requested_nb_floor) {
    console.log("Floor", requested_nb_floor, "is requested");
    elevator.activate_inside_button(requested_nb_floor);
    elevator.addFloorToList(requested_nb_floor);
    elevator.moveNext();
  }
  // method too find the best elevator
  FindElevator(requested_nb_floor, direction) {
    let best_difference = 10;
    let best_elevator = null;
    for (var i = 0; i < this.column.elevator_list.length; i++) {
      var difference_floor = Math.abs(
        requested_nb_floor - this.column.elevatorList[i].current_floor
      );
      if (difference_floor < best_difference) {
        best_difference = difference_floor;
        best_elevator = i;
      }
    }
    return this.column.elevatorList[bestElevator];
  }
}
//========================================================== COLUMN =======================================================

class Column {
  constructor(nbFloors, nbElevators) {
    this.nb_floors = nbFloors;
    this.nb_elevators = nbElevators;
    this.elevator_list = [];
    this.call_elevator_list = [];
    this.outside_call_buttons_list = [];
    this.create_elevators();
    this.create_outside_buttons();
  }
  // create elevator and put it in the elevator list
  create_elevators() {
    for (let i = 0; i < this.nb_elevators; i++) {
      let elevator = new Elevator(i + 1, this.nb_floors);
      this.elevator_list.push(elevator);
    }
  }
  // create outside button  and add it too call_button_list
  create_outside_buttons() {
    for (let i = 0; i < this.nb_floors; i++) {
      if (i != this.nb_floors - 1) {
        this.outside_call_buttons_list.push(new Outside_button(i, "Up"));
      }
      if (i != 0) {
        this.outside_call_buttons_list.push(new Outside_button(i, "Down"));
      }
    }
  }
  // it call elevator list with number of requested
  //and send you elevator 
  addToCallElevatorList(requested_nb_floor) {
    this.call_elevator_list.push(requested_nb_floor);
    if (this.direction == "Up") {
      this.call_elevator_list.sort();
    } else if (this.direction == "Down") {
      this.call_elevator_list.sort().reverse();
    }
  }
}
class Outside_button {
  constructor(requFloor, direction) {
    this.requFloor = requFloor;
    this.direction = direction;
    this.activateButton = false;
  }
}
//========================================================== ELEVATOR ==========================================================================
// class elevator for all initial parameter 
class Elevator {
  constructor(elevator_number, nb_floors) {
    this.elevator_number = elevator_number;
    this.nb_floors = nbFloors;
    this.direction = "Stop";
    this.status = "Idle";
    this.request_floor_list = [];
    this.inside_request_button_list = [];
    this.current_floor = 0;
    this.create_inside_buttons();
  }
// create inside button and add it too a list 
  create_inside_buttons() {
    for (var i = 0; i < this.nbFloors; i++) {
      this.inside_request_button_list.push(new Inside_button(i));
    }
  }
  // create method for send the best elevator
  moveNext() {
    let requested_nb_floor = this.request_floor_list.shift();
    if (this.current_floor === requested_nb_floor) {
      this.OpenDoor();
    } else {
      while (this.current_floor != requested_nb_floor) {
        if (this.current_floor > requested_nb_floor) {
          this.moveDown();
          console.log(this.current_floor, "Going Down");
          sleep(2000);
        } else if (this.current_floor < requested_nb_floor) {
          this.moveUp();
          console.log(this.current_floor, "Going up");
          sleep(2000);
        }
      }
    }
    console.log(
      "Elevator",
      this.elevator_number,
      "arrived at floor number",
      this.current_floor
    );
    // open door and closed it aftert 2 sec
    this.OpenDoor();
    sleep(2000);
    this.CloseDoor();
  }
  moveDown() {
    this.direction = "Down";
    this.status = "Moving";
    this.current_floor = this.current_floor - 1;
    sleep(2000);
  }
  moveUp() {
    this.direction = "Up";
    this.status = "Moving";
    this.current_floor = this.current_floor + 1;
    sleep(2000);
  }
  // create request floor list 
  addFloorToList(requestedFloorNumber) {
    this.request_floor_list.push(requested_nb_floor);
    if (this.direction == "Up") {
      this.request_floor_list.sort();
    } else if (this.direction == "Down") {
      this.request_floor_list.sort().reverse();
    }
  }
  activateInsideButton(requested_nb_floor) {
    console.log(
      "In Elevator",
      this.elevator_number,
      ", which is at floor",
      this.current_floor,
      ",",
      "floor number",
      requested_nb_floor,
      "is requested"
    );
    if (this.requFloor == this.request_floor_list) {
      this.activate_inside_button = false;
    }
    if (this.requFloor < this.request_floor_list) {
      this.moveUp();
    } else if (this.requFloor > this.request_floor_list) {
      this.moveDown();
    }
  }
  OpenDoor() {
    console.log("Opening doors at floor number", this.current_floor);
    //this.status = "openDoor";
  }
  CloseDoor() {
    console.log("Closing doors");
    //this.status = "closeDoor";
  }
}
//=================================================================== REQUEST BUTTON ==================================================================
class inside_button {
  constructor(floor) {
    this.floor = floor;
    this.status = "desactivated";
  }
}
// function for add time 
function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if (new Date().getTime() - start > milliseconds) {
      break;
    }
  }
}
//=====================================================================================================================================================
const battery = new Battery(10, 2);
////==================================TEST 1========================////
battery.column.elevator_list[0].current_floor = 1;
battery.column.elevator_list[1].current_floor = 1;
battery.Request_elevator(4, "UP");
battery.Request_floor(battery.column.elevator_list[1], 7);
////=========================TEST 2====================================////
// battery.column.elevator_list[0].current_floor = 10;
// battery.column.elevator_list[1].current_floor = 3;
// battery.Request_elevator(1, "Up");
// battery.Request_floor(battery.column.elevator_list[], 6);
// battery.Request_elevator(3, "Up");
// battery.Request_floor(battery.column.elevator_list[], 5);
// battery.Request_elevator(9, "Down");
// battery.Request_floor(battery.column.elevator_list[], 2);
////========================TEST 3========================================////
// battery.column.elevator_list[0].current_floor = 10;
// battery.column.elevator_list[1].current_floor = 3;
// battery.Request_elevator(10, "Down");
// battery.Request_floor(battery.column.elevator_list[], 3);
// battery.Request_elevator(3, "Down");
// battery.Request_floor(battery.column.elevator_list[], 2);