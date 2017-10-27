#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:54:33 2017

@author: pravda
"""

from __main__ import vtk, qt, ctk, slicer

class LaplaceTest:
  def __init__(self, parent):
    parent.title = "Laplacian Trial"
    parent.categories = ["Examples"]
    parent.dependencies = []
    parent.contributors = ["Pravda Ray"]
    parent.helpText = """
            Slicer programming initial stage for laplacian implementation"""
    parent.acknowledgementText = """ This is done with the help of different tuitorials along with the implementation details from slicer programming tuitorila by Sonia Pujol"""
    self.parent = parent
        

class LaplaceWidget:
  def __init__(self, parent = None):
    if not parent:
      self.parent = slicer.qMRMLWidget()
      self.parent.setLayout(qt.QVBoxLayour())
      self.parent.setMRMLScene(slicer.mrmlScene)
    else:
      self.parent =- parent
    self.layout = self.parent.layout()
    if not parent:
      self.laplace_test()
      self.parent.show()
            

        
  def laplace_test(self):
        #collapsible button slicer
    self.laplaceCollapsibleButton = ctk.ctkCollapsibleButton()
    self.laplaceCollapsibleButton.text = "Laplace Operator"
    self.layout.addWidget(self.laplaceCollapsibeButton)
        
        #layout within the laplacian operator button
        
    self.laplaceFormLayout = qt.QformLayout(laplaceCollapsibleButton)
        
        # Volume selectors
        
        #input volume selector
        
    self.inputFrame = qt.QFrame(self.laplaceCollapsibleButton)
    self.inputFrame.setlayout(qt.QHBoxlayout())
    self.laplaceFormLayout.addWidget(self.inputFrame)
    self.inputSelector = qt.QLabel("Input Volume:" , self.inputFrame)
    self.inputFrame.Layout().addWidget(self.inputSelector)
    self.inputSelector = slicer.qMRMLNodeComboBox(self.inputFrame)
    self.inputSelector.nodeTypes = (("vtkMRMLScalarVolumeNode"), "")
    self.inputSelector.addEnabled = False 
    self.inputSelector.removeEnabled = False 
    self.inputSelector.setMRMLScene(slicer.mrmlScene) 
    self.inputFrame.layout().addWidget(self.inputSelector) 
        
        #output volume selector
        
    self.outputFrame = qt.QFrame(self.laplaceCollapsibleButton)
    self.outputFrame.setlayout(qt.QHBoxlayout())
    self.laplaceFormLayout.addWidget(self.outputFrame)
    self.outputSelector = qt.QLabel("Output Volume:" , self.outputFrame)
    self.outputFrame.Layout().addWidget(self.outputSelector)
    self.outputSelector = slicer.qMRMLNodeComboBox(self.outputFrame) 
    self.outputSelector.nodeTypes = (("vtkMRMLScalarVolumeNode"), "")
    self.outputSelector.setMRMLScene(slicer.mrmlScene) 
    self.outputFrame.layout().addWidget(self.outputSelector) 
        
        #Apply laplace button
        
    laplaceButton = qt.QPushButton("Apply laplace")
    laplace.Button.toolTip = "Execute Lapalce Operator"
    self.laplaceFormLayout.addWidget(laplaceButton)
    laplaceButton.connect('clicked(bool)', self.onApply)
        
        # Add vertical space
        
    self.layout.addStretch(1)
        
        #Local variable set as instance attribute
        
    self.laplaceButton = laplaceButton
        
  def onApply(self):
    inputVolume = self.inputSelector.currentNode()
    outputVolume = self.outputSelector.currentNode()
    if not (inputVolume and outputVolume):
      qt.QMessageBox.information(slicer.util.mainWindow(), 'Laplace', 'Input and output volumes required for laplacian')
      return
    laplacian = vtk.vtkImageLaplacian()
    laplacian.SetInputData(inputVolume.GetImagedata())
    laplacian.setDimensionality(3)
    laplacian.Update()
        
    ijkToRAS = vtk.vtkMatrix4x4()
    inputVolume.GetIJKToRASMatrix(ijkToRAS)
    outputVolume.SetIJKToRASMatrix(ijkToRAS)
    outputvolume.SetAndObserveImageData(laplacian.GetOutput())
        
        #make the volume appear in all the slice views
        
    selectionNode = slicer.app.applicationLogic().GetSelectionNode()
    selectionNode.setReferenceActiveVolumeID(outputVolume.GetID())
    slicer.app.applicationLogic().PropagateVolumeSelection(0) 
    