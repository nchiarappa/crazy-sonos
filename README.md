# Crazy Sonos
Want to make someone go crazy with their Sonos player? This repo will help you to make it look possessed!

## Things you can do

### set_random_volume_for_random_time()
Set the volume of the Sonos speaker to a random value for a random amount of time

### set_BOOM_volume_randomly()
Set the volume of the Sonos speaker to the max volume you choose for a shorter random amount of time

There are also ```check_playing_status``` that checks if the speaker is reproducing something (if not it restarts the reproduction), ```check_time_to_run``` that allows you to set the maximum script execution time, ```check_initial_status``` that checks if there is reproducing something as soon as the code is run (if not it puts a radio on), and ```take_snapshot``` that is useful to restore a previous backup reproducing session (if someone stops the reproduction while the script is running, see ```check_playing_status``` that uses this).

## To run

1. Clone this repository
2. Install the requirements: ```pip3 install -r requirements.txt```
3. Modify settings.py file adding the ```sonos_ip_address``` (optionally you can configure the other parameters)
4. Run script.py: ```python3 crazy_sonos.py```. Right now the script is set to sleep first for 5 minutes then it will start to put a radio if something is not playing and then change the sonos speaker volume randomly according to the settings.
5. ???
6. Profit!
