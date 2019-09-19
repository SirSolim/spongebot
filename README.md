# SpongeBot
*Monitor a directory for new files*

 When instantiating a new SpongeBot, you need to provide it with a path to a directory and a callback function. The callback function is called each time a new file is added to the directory, passsing the name of the new file as the first parameter.
 SpongeBot will run as a thread, making it possible to run multiple SpongeBots simultaneously.
 
 A typical usecase for SpongeBot would look like this:
 
	from spongebot import SpongeBot
  
	def my_callback_function(file_name):
		print('A new file was added to the directory!')
   
	 sb = SpongeBot('./my_directory', my_callback_function)
	 sb.start()
	
The following parameters can be passed to SpongeBot:

- **path**: The path to the directory that needs to be monitored
- **callback**: A callable that takes a filepath as the first parameter
- **interval**: The interval length in seconds that determines how frequently SpongeBot checks for new files. Defaults to 10 seconds.
- **static_args**: A list that will be unpacked and passed to the callback function
- **static_kwargs**: A dictionary that will be unpacked and passed to the callback function
- **snapshot_file**: A file that can be used by SpongeBot to keep track of the files tht are already in the directory. This is used to make SpongeBot more robust in the case of  system crashes. Defaults to "./.spongeBot_snapshot.txt".