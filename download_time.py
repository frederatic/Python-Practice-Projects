# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).


# converts seconds into hours, minutes, seconds
def convert_seconds(s):
    basemin = int(s/60)
    hr = int(s/3600)
    min = int(s/60-hr*60)
    sec = int(s-basemin*60)
    hours = str(hr) + " hours"
    minutes = str(min) + " minutes"
    seconds = str(sec) + " seconds"
    if hr == 1:
        hours = str(hr) + " hour"
    if min == 1:
        minutes = str(min) + " minute"
    if sec == 1:
        seconds = str(sec) + " second"
    return hours, minutes, seconds
    
# number of bits in units
kb = 2**10
kB = 2**10*8
Mb = 2**20
MB = 2**20*8
Gb = 2**30
GB = 2**30*8
Tb = 2**40
TB = 2**40*8

def download_time(filesize, size_unit, bandwidth, bw_unit):
    # download time = filesize/bandwidth
    seconds = (filesize*size_unit)/(bandwidth*bw_unit) # download time in seconds for bandwidth in seconds
    time = convert_seconds(seconds) # call convert seconds function to convert time
    return time
    


print download_time(1024, kB, 1, MB)
#>>> 0 hours, 0 minutes, 1 second

print download_time(13, GB, 5.6, MB)
#>>> 0 hours, 39 minutes, 37 seconds

print download_time(10, MB, 2, kb)
#>>> 11 hours, 22 minutes, 40 seconds


