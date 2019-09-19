from spongebot import SpongeBot
import time


def my_callback_function(file_name):
    print('Hey Patrick! Look at this new file I found! ' + file_name)

# Create the SpongeBot
sb = SpongeBot('./my_directory/', my_callback_function)

# Start it. It will now monitor the './my_directory/' directory.
sb.start()

# Create a few files inside of './my_directory/' to test the SpongeBot.
time.sleep(2.0)
open('./my_directory/new_file_%d.txt' % time.time(), 'a').close()
time.sleep(1.0)
open('./my_directory/new_file_%d.txt' % time.time(), 'a').close()

# Wait fot the bot to detect the last file.
time.sleep(2.1)

# Stop the SpongeBot. Since this is the only SpongeBot that is currently
# running, our python script will automatically exit.
sb.stop()