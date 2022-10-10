# <center>![page](https://camo.githubusercontent.com/a8cd2eef2325c425519095dc2501111e630a77eddb454938c527cb82ea9c3aeb/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)


# <center>Holberton AirBnB Clone - The Console

## <center> Purpose

This project was assigned to us by Holberton School Tulsa. It is a simple command interpreter to manage the objects used in the AirBnB clone project by:
- Allowing for the creation of new objects.
- Allows retrieval of an object from a file, a database, etc.
- Allows operations to be performed on objects
- Allows object attributes to be updated.
- Allows objects to be destroyed.

The project contains:
- A parent class (called `BaseModel`) used for initialization, serialization, and deserialization of instances.
- Creates a simple flow of serialization/deserialization, as follows: Instance <-> Dictionary <-> JSON string <-> file
- Creation of all subclasses (`User`, `State`, `City`, `Amenity`, `Place`, `Review`)
- Creation of a the first abstracted storage engine of the project: File storage.
- Unittests to validate all classes as well as the storage engine.


## <center>How to Use (with examples)
The user of the console will be able to utilize it in an interactive or non-interactive mode as desired. Running `./console.py` in terminal will open up a prompt that the user can call functions from. For example:

    ./console.py
    (hbtn) help
    Documented commands (type help <topic>):
    ========================================
    EOF  all  create  destroy  help  quit  show  update

Commands may be executed non-interactively by piping them into the console. For example:

Both

    echo "create BaseModel" | ./console.py

and

    ./console.py
    (hbtn) create BaseModel

will create an instance of the BaseModel class and print its id. 

The `EOF` command is used to terminate the console.  Alternatively, Ctrl+D may be used.

## Contributors
This project exists because of the following contributors:<br />

Matthew Allen<br />
<a href="https://github.com/mdallen5393"><img src="https://avatars.githubusercontent.com/u/92639333?v=4"></a>

Aaron Manuel<br />
<a href="https://github.com/AaronManuel15"><img src="https://avatars.githubusercontent.com/u/100643249?v=4"></a>

Logan Mcclain<br />
<a href="https://github.com/AnActualBanana"><img src="https://avatars.githubusercontent.com/u/92802843?v=4"></a>


