"""
Common Functions
"""

from qgis.gui import QgsMessageBar
from qgis.PyQt.QtWidgets import *
from qgis.core import QgsVectorLayer, QgsProject
from qgis.utils import iface
import sys

def import_validate_vector_layer(layer_path, layer_name):
    layer = QgsVectorLayer(layer_path, layer_name)
    if layer.isValid():
        print("Validation for " + layer_name + " completed successfully")
        return layer
    else:
        # Display warning bar
        iface.messageBar().pushMessage("File Uploaded into " + layer_name + " is Either Invalid or Missing", "Please Try Again", level = 1)

        # Display Error Box
        close_dialog = QMessageBox()
        close_dialog.setWindowTitle("Error with Validation")
        close_dialog.setText("The file uploaded into the " + layer_name + " field was incorrect or missing. Please try a different file.")
        close_dialog.setIcon(QMessageBox.Critical)
        close_dialog.exec_()
        print("invalid layer, Please try a different file.")
        return "Invalid Layer"

def display_vector_layer(layer, name = None):
    displayed_layer = QgsProject.instance().addMapLayer(layer)
    if name:
        displayed_layer.setName(name)

def zoom_to_layer(layer):
    canvas = iface.mapCanvas()
    extent = layer.extent()
    canvas.setExtent(extent)
    canvas.refresh()

def count_features(name, layer):
    if name != 'Land File':
        feature_count = layer.featureCount()
        dialog = QMessageBox()
        dialog.setWindowTitle(name + " Feature Count")
        print(name + " contains " + str(feature_count) + " features")
        dialog.setText("Please select 'Show Details...' if you would like to feature count for the " + name + " file.")
        dialog.setDetailedText("The amount of features in " + name + " is: " + str(feature_count))
        dialog.exec_()

def display_distance_popup(distance):
    if distance > 0:
        distance_dialog = QMessageBox()
        distance_dialog.setWindowTitle("Distance Report")
        distance_dialog.setText(
            "The distaance between the features your selected is: " + str(distance))
        distance_dialog.setIcon(QMessageBox.Information)
        distance_dialog.exec_()
    else:
        false_distance_dialog = QMessageBox()
        false_distance_dialog.setWindowTitle("Out of Bounds")
        false_distance_dialog.setText(
            "One of the ID Numbers you selected was out of bounds! Please try again.")
        false_distance_dialog.setIcon(QMessageBox.Critical)
        false_distance_dialog.exec_()