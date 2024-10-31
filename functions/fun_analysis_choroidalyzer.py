#Import libraries
import matplotlib.pyplot as plt 


#Import tool
# from choroidalyze import Choroidalyzer



def analysis_choroidalyzer(choroidalyzer, file):
    '''
    Ejecuta análisis sobre file. Sobreescribe file
    show = True: Muestra el plot
    '''
    if type(file) == list:
        #Aplico iterativamente analysis_choroidalyzer
        files, metrics = [], []
        for f in file:
            f, metric = analysis_choroidalyzer(choroidalyzer, f)
            files.append(f)
            metrics.append(metric)
        return files, metrics
    
    else:

        # choroidalyzer = Choroidalyzer()

        # basic useage: get the metrics
        print(file)
        metrics = choroidalyzer.analyze(file) #, scale=(11.49, 3.87)
        print(metrics)

        # choroidalyzer also has a basic plotting function to inspect segmentation outputs
        fig = choroidalyzer.predict_and_plot(file)
        #Elimino la imagen del output
        plt.close(fig)        

        #Save plot shown
        fig.savefig(file)

        return file, metrics