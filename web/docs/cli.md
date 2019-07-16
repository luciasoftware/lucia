# The cli utilities
Lucia contains varius CLI utilities, that can aid you in creating games quicker. Below follows an explenation of the varius CLI utilities found in lucia.
The CLI utilities are automatically installed along lucia, so no extra setup is required to use them.
All of the CLI utilities can be localed in the "lucia-cli" package.
Note: Many CLI utilities provides help by just typing their name without any arguments.

### The Packer Utility
The packer util, located in "lucia-cli.packer" is an util that takes care of packing all your game resources into a compressed and encrypted pack file, that you will then be able to load with lucia in your game.

#### Create a pack file:
To use the packer util, do the following:

* Go into your resource folder (containing audio / map data or anything else really)
`cd resources/`
* invoke the packer.
`python3 -m lucia-cli.packer name key`
Where:
* name is the name of the pack file, fx: resources.dat
* key is the encryption key to use (you will need it later, when loading your packfile into Lucia).


#### Load the created pack file into lucia:
To load your created pack file into lucia, so you and the audio backends can use the data within it, can be done the following way:
Note: This asumes that you have copied the newly created pack file from where you created into the same folder, where your game source is located.

```python
# This should take place after lucia.initialize has been called.
ress = lucia.ResourceFile(key="THE_ENCRYPTION_KEY_YOU_USED_BEFORe") # this key needs to match the one you used before, or else the decryption will fail.
ress.load("resources.dat") # "resources.dat" is the name of your pack file, here we tell lucia, that it can be found in the same folder, and that it's called resources.dat.
lucia.set_global_resources_file(ress) # This tells lucia to use the above resource file as the global resource file. What this does is, telling the audio backends to search for audio data in the above pack file before trying anything else.
```


### API Source:
[lucia](#)
[lucia.ResourceFile](#)
