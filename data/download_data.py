import json
from subprocess import call

def download_data(url, file):
    print "Downloading original data set..."
    call(["curl", "--output", file, url])

download_data("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data", "adult.data")
download_data("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names", "adult.names")
download_data("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test", "adult.test")
print "Done."
