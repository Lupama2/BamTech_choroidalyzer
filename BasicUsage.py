from choroidalyze import Choroidalyzer

# initialise choroidalyzer
choroidalyzer = Choroidalyzer()

# replace with the path to your image
metrics = choroidalyzer.analyze('example_data/image4.png')
print(metrics)
# prints: {'thickness': 183.0, 'area': 1.356311, 'vascular_index': 0.46774, 'vessel_area': 0.634401, 'raw_thickness': array([174, 263, 112])}
choroidalyzer.predict_and_plot('example_data/image4.png')