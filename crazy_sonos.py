from soco import SoCo
from soco.snapshot import Snapshot
from settings import sonos_ip_address, max_time_to_run, sleep_time_before_start, boom_volume, min_random_volume, max_random_volume
import random
import time

def check_playing_status():
  try:
   status = str(speaker.get_current_transport_info()['current_transport_state'])
   if(status!='PLAYING'):
    print("Status is not PLAYING. Restarting play...")
    speaker.play()
  except:
   # Restore status to starting one
   print("Exception caught while trying to restart play. Restoring snapshot...")
   snap.restore(fade=True)
   
def check_time_to_run(max_time_to_run):
  if(max_time_to_run<=0):
   print("MAX TIME TO RUN EXCEEDED! Stopping the speaker and exiting...")
   speaker.stop()
   exit()

def set_random_volume_for_random_time(max_time_to_run):
  random_sleep = random.randint(5,15)
  random_volume = random.randint(min_random_volume, max_random_volume)
  print("Putting volume to " + str(random_volume) + " for " + str(random_sleep) + " seconds")
  speaker.volume = random_volume
  time.sleep(random_sleep)
  return max_time_to_run-random_sleep
  
def set_BOOM_volume_for_random_time(max_time_to_run, boom_volume):
  random_BOOM_decision = random.randint(0,1)
  if(random_BOOM_decision==1):
    random_sleep = random.randint(2,5)
    print("BOOOOOOM! Putting volume to " + str(boom_volume) + " for " + str(random_sleep) + " seconds")
    speaker.volume = boom_volume
    time.sleep(random_sleep)
    return max_time_to_run-random_sleep
  return max_time_to_run

def take_snapshot():
  print("Taking snapshot for backup purposes...")
  snap = Snapshot(speaker)
  return snap.snapshot()

def check_initial_status():
  print("Checking if there is already something playing...")
  status = str(speaker.get_current_transport_info()['current_transport_state'])
  if(status!='PLAYING'):
    print("Nothing is playing, putting up radio...")
    # something to play on a Sonos player to start (a radio station)
    start_uri = "http://topweek.stream.ouifm.fr/ouifmtopweek.mp3"
    print("Playing a radio station")
    speaker.volume=20
    speaker.play_uri(start_uri, title="test radio station")

speaker = SoCo(sonos_ip_address)

print("Operating on speaker with name " + speaker.player_name)
print("The current volume of the speaker is " + str(speaker.volume))

print("Sleeping for " + str(sleep_time_before_start) + "s, Zzz...")
time.sleep(sleep_time_before_start)
check_initial_status()
snap = take_snapshot()
print("I will run for " + str(max_time_to_run) + "s")

while True:
  check_playing_status()
  check_time_to_run(max_time_to_run)
  max_time_to_run=set_random_volume_for_random_time(max_time_to_run)
  max_time_to_run=set_BOOM_volume_for_random_time(max_time_to_run, boom_volume)
  check_time_to_run(max_time_to_run)
  print("Time remaining: " + str(max_time_to_run) + "s")