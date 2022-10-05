# <center>![page](https://github.com/matiassingers/awesome-readme/blob/master/icon.png?raw=true)


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

# AARON, I STOPPED HERE

## <center>How to Use (plus Examples)
The user of *hsh* will be able to utilize it in an interactive or non-interactive mode as desired. Running *./hsh* in terminal will open up a prompt that the user can call functions from. For example:

    ./hsh
    ($) cat "file"
    [prints contents of "file" to stdout]
    ($) exit
    

Either piping in commands or executing them with *./hsh* will executes the commands without opening the prompt and keeps you in your linux terminal. For example:

Both

    cat "file" | ./hsh

and

   `./hsh cat "file"` 

Will display the contents of "file" to stdout. 

## Contributors
This project exists because of the following contributors:<br />
<a href="https://github.com/mdallen5393"><img src="https://avatars.githubusercontent.com/u/92639333?v=4"></a> <a href="https://github.com/AaronManuel15"><img src="https://avatars.githubusercontent.com/u/100643249?v=4"></a> <a href="https://github.com/AnActualBanana"><img src="https://avatars.githubusercontent.com/u/92802843?v=4"></a> 


