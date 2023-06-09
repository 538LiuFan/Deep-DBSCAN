from Utils.Feature_extractor import Feature_extractor
from Utils.Clusterer import Clusterer

dataset              = "mnist"
cnn_architecture     = "resnet"
layer 				 = "fc2"
clustering_algorithm = "dbscan"
metric				 = "both"

fe = Feature_extractor(dataset, cnn_architecture, layer)
fe.extract_and_save_features()
cl = Clusterer(dataset, cnn_architecture, layer, clustering_algorithm)
cl.cluster()
predicted_labels = cl.predicted_labels
print("Shape predicted labels: %s" % str(predicted_labels.shape))
cl.evaluate(metric)