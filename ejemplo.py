

from choroidalyze import Choroidalyzer

# This initialises choroidalyzer. 
# It will try to automatically download the model weights from github the first time you run it. 
choroidalyzer = Choroidalyzer()

# basic useage: get the metrics
metrics = choroidalyzer.analyze('example_data/image1.png')
print(metrics)