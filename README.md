# ProfilingViz
## Learning Project
Automated profiling and Exploratory Data Analysis of a .csv dataset using Python libraries.

## Table of Contents
- [Run Locally](#run-locally)
- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Roadmap](#roadmap)
- [Acknowledgements](#acknowledgements)
- [Future Development](#future-development)
- [License](#license)
    
## Run Locally
Clone the project

```bash
  git clone https://github.com/josezg/ProfilingViz
```

Go to the project directory

```bash
  cd ProfilingViz
```

### The suggestion is to work in an environment
Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run app.py
```

## Features
- Upload a dataset in .xlsx or .csv format
- Analyze the dataset with y-profiling, sweetviz, and klib
- Calculate the time spent analyzing the dataset
- Visualize the analysis results
- Basic interaction with the results

## Project Structure
File and project structure
```
├── reports
├── src
│   ├── config.py
│   ├── data_utils.py
│   ├── profiling.py
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

## Tech Stack
- Python, pandas, numpy, ydata-profiling, sweetviz, klib, and streamlit.

## Roadmap
* To do
  - Refactor all code for better readability and performance
  - Implement robust exception handling
  - Complete and test the Dockerfile for containerization
* Next features
  - Integrate **Lux** library for advanced data exploration
  - Enhance user interaction with more visualizations and filtering options

## Future Development
This project aims to continuously improve and expand its capabilities, as a learning project. Some potential future developments include:

- Integration of additional data profiling libraries for a more comprehensive analysis
- Support for more file formats and data sources
- Advanced data visualization options for better insights
- Deployment on cloud platforms for scalability and accessibility

## License
[MIT](https://choosealicense.com/licenses/mit/)