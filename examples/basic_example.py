from spongebot import SpongeBot


def my_callback_function(file_name):
    print('A new file was added to the directory!')

sb = SpongeBot('./my_directory', my_callback_function)
sb.start()