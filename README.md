# Zhongjie_AssProject_Emlyon
This is my Final_Project for Machine Learning Practice

### Project Overview

This is a Data Analysis for Brewery Operations and Market Analysis Dataset

## How is this dataset about

This dataset presents an extensive collection of data from a craft beer brewery, spanning from January 2020 to January 2024. It encapsulates a rich blend of brewing parameters, sales data, and quality assessments, providing a holistic view of the brewing process and its market implications.

## Installation process
This project uses python `3.11` as core interpreter, and poetry `1.8.3` as dependency manager.
1) Create a new conda environment with
```
conda env create -f environment.yml
```

2) Activate the environment with
```
conda activate EM-Assproject-2024-Zhongjie
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
conda remove -n EM-Assproject-2024-Zhongjie --all
```

## Collect data
I collect data from kaggle [Brewery Operations and Market Analysis Dataset](https://www.kaggle.com/datasets/ankurnapa/brewery-operations-and-market-analysis-dataset/data)

and we should first to transformed data.


## How to use it
run the streamlit app
```shell
streamlit run demo.py
```
