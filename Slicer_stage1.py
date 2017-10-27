#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:54:33 2017

@author: pravda
"""
class LaplacianTrial:
    
    def _init_(self, parent):
        parent.title = "Laplacian Trial"
        parent.categories = ["Examples"]
        parent.dependencies = []
        parent.contributors = ["Pravda Ray"]
        parent.helpText = """
        Slicer programming initial stage for laplacian implementation"""
        parent.acknowledgementText = """ This is done with the help of different tuitorials along with the implementation details from slicer programming tuitorila by Sonia Pujol"""
        self.parent = parent
        
        
    def toggle():
      n = slicer.util.getNode('liver-orig001')
      a = slicer.util.array('liver-orig001')
      a[:] = a.max()/2. - a
      n.GetImageData().Modified()
      print "toggled"
    
    toggle()
    
    
    def onApply(self):
        laplacian = vtk.vtkImageLaplacian()
        laplacian.SetInputData(inputVolume.GetImagedata())
        laplacian.setDimensionality(3)
        laplacian.Update()
    
    def laplace_test(self):
        #collapsible button slicer
        self.laplaceCollapsibleButton = ctk.ctkCollapsibleButton()
        self.laplaceCollapsibleButton.text = "Laplace Operator"
        self.layout.addWidget(self.laplaceCollapsibeButton)
        
        #layout within the laplacian operator button
        
        self.laplaceFormLayout = qt.QformLayout(laplaceCollapsibleButton)
        
        # Volume selectors
        
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
        
        
        self.outputFrame = qt.QFrame(self.laplaceCollapsibleButton)
        self.outputFrame.setlayout(qt.QHBoxlayout())
        self.laplaceFormLayout.addWidget(self.outputFrame)
        self.outputSelector = qt.QLabel("Output Volume:" , self.outputFrame)
        self.outputFrame.Layout().addWidget(self.outputSelector)
        self.outputSelector = slicer.qMRMLNodeComboBox(self.outputFrame) 
        self.outputSelector.nodeTypes = (("vtkMRMLScalarVolumeNode), "")
        self.outputSelector.setMRMLScene(slicer.mrmlScene) 
        self.outputFrame.layout().addWidget(self.outputSelector) 
        
        #Apply laplace button
        
        laplaceButton = qt.QPushButton("Apply laplace")
        laplace.Button.toolTip = "Execute Lapalce Operator"
        self.laplaceFormLayout.addWidget(laplaceButton)
        laplaceButton.connect('clicked()', self.onApply)
    
    