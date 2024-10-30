
#Import tool
from choroidalyze import Choroidalyzer


def analysis_choroidalyzer(file):
    '''
    Ejecuta análisis sobre file. Sobreescribe file
    '''
    if type(file) == list:
        #Aplico iterativamente analysis_choroidalyzer
        files, metrics = [], []
        for f in file:
            f, metric = analysis_choroidalyzer(f)
            files.append(f)
            metrics.append(metric)

        return files, metrics
    else:

        # This initialises choroidalyzer. 
        # It will try to automatically download the model weights from github the first time you run it. 
        choroidalyzer = Choroidalyzer()

        # basic useage: get the metrics
        metrics = choroidalyzer.analyze(file) #, scale=(11.49, 3.87)

        # choroidalyzer also has a basic plotting function to inspect segmentation outputs
        fig = choroidalyzer.predict_and_plot(file)

        #Save plot shown
        fig.savefig(file)

        return file, metrics