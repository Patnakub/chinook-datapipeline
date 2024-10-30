# Databricks notebook source
import pandas as pd
import math

# file path
inputPath = "/Workspace/Users/sorawit.ther@kmutt.ac.th/DevOps/track_small.csv"
outputPath = "/Workspace/Users/sorawit.ther@kmutt.ac.th/DevOps/output_small.csv"

# Extract
tracks = pd.read_csv(inputPath)

# Transform
tracks['UnitPrice'] = tracks['UnitPrice'].apply(lambda x: math.ceil(x))

# Load
tracks.to_csv(outputPath, index=False)

# COMMAND ----------


