# Classes basic definition

## Game
Represents the "game". It can keep track of global scores and players accross multiple maps loading. 

When defining an object, you can define the different modules to use.
 
## Module
Represents a functional part of the engine. Graphics, Physics, Audio, Network, ... 

Each Module can decide to follow a specific Interface or be completely custom.

Each Module is associated to a context. Some contexts force to follow a specific interface to be able to plug a Module.

Standard defined interfaces are GraphicsModuleInterface, AudioModuleInterface, NetworkModuleInterface, PhysicsModuleInterface, and ControllerInputInterface.
 Each Module can define when it should be called to process data.

Proposed flags are: 

 - "for each actor in the update loop" : when looping to process update for each Actor, call the module if a State for its context is present 
 - "once before update loop" : call once before processing Actors update 
 - "once after update loop" : call once after processing Actors update
 - "only when called" : call only when some code asks for it
 - "alone for each actor before update loop" : run a complete separated loop over all Actors and call this Module on them before the Actor update process
 - "alone for each actor after update loop" : run a complete separated loop over all Actors and call this Module on them after the Actor update process

 Several options could be defined for threading options.

## Scene
Represents the "map". It can be loaded from a file, saved, ...

It contains the Actors. Runs the Actors update loop.
 
## Actor
Something in the Scene. It can be anything. Can be serialized and deserialized.

It has a set of States associated to a context.
 
## State
The State is a "pack of values" associated with a context. For instance, a State associated with the "audio" context contains values for this context. The context name is what other part of the engine use to process a specific part of the Actor (render sound, graphics, ...).
 Usual contexts:

 - "graphics" : data needed for visual representation. Sprites, for instance.
 - "audio" : data needed for audio representation. Sound references from the ResourceManager, the state of the sounds, ...
 - "network" : data needed for network replication management. Who is the owner? Server? Client? Replication logic.
 - "physics" : data needed for physics management. The physics body and simulation values.
 - "logic" : data needed for object behavior management. Custom for every game.
 
The State contents are directly linked to the engine part used. If the physics engine is swapped, the physics states of the actors might contain different informations because they might use it differently. Although they might respect specific interfaces for loose coupling purposes.

# Precise Interfaces

## Module Interfaces

### ModuleInterface

#### Description
Define the minimal interface a Module should always respect. This is mainly defined so the engine can use it.

#### Methods:

##### getUseOptions()
Returns an enum flag about when this module should be called during the update loop.

##### process(Actor actor, State state)
Called for each actor 

### AudioModuleInterface
TBD.

### ControllerModuleInterface
TBD.

### NetworkModuleInterface
TBD.

### PhysicsModuleInterface
TBD.

### GraphicsModuleInterface
TBD.


