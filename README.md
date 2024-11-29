# Zhongjie_AssProject_Emlyon
This is my Final_Project for Machine Learning Practice in Emlyon

###Project Overview

This is a Data Analysis for Human Development Index (HDI)

#What is Human Development Index(HDI) ⬇

The Human Development Index (HDI) is a summary measure of average achievement in key dimensions of human development: a long and healthy life, being knowledgeable and have a decent standard of living. The HDI is the geometric mean of normalized indices for each of the three dimensions. The health dimension is assessed by life expectancy at birth, the education dimension is measured by mean of years of schooling for adults aged 25 years and more and expected years of schooling for children of school entering age. The standard of living dimension is measured by gross national income per capita. The HDI uses the logarithm of income, to reflect the diminishing importance of income with increasing GNI. The scores for the three HDI dimension indices are then aggregated into a composite index using geometric mean. Refer to Technical notes for more details. The HDI can be used to question national policy choices, asking how two countries with the same level of GNI per capita can end up with different human development outcomes. These contrasts can stimulate debate about government policy priorities. The HDI simplifies and captures only part of what human development entails. It does not reflect on inequalities, poverty, human security, empowerment, etc. The HDRO provides other composite indices as a broader proxy on some of the key issues of human development, inequality, gender disparity, and poverty. A fuller picture of a country's level of human development requires analysis of other indicators and information presented in the HDR statistical annex.

## Installation process
This project uses python `3.11` as core interpreter, and poetry `1.8.3` as dependency manager.
1) Create a new conda environment with
```
conda env create -f environment.yml
```

2) Activate the environment with
```
conda activate ecl-course-2024-t4
```

3) Move to the project directory, and install the project dependencies with
```
poetry install
```

4) Launch a jupyter server with
```
jupyter notebook
```

5) Remove the environment with
```
conda remove -n ecl-course-2024-t4 --all
```

## Collect data
For this Machine Learning Course the dataset we consider is the [bluebook for bulldozers 
competition](https://www.kaggle.com/c/bluebook-for-bulldozers/overview). 
You can download the Train.zip data file [here](https://www.kaggle.com/c/bluebook-for-bulldozers/data), 
and move unzip your file in the subfolder  `data/bulldozers`


## How to use it
run the streamlit app
```shell
streamlit run demo.py
```
