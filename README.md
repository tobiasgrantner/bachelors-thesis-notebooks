# Enabling the Scalability of DBRepo - Evaluation Notebooks

This repository contains the notebooks used to produce the data, figures, and tables included in the evaluation of the bachelor's thesis "Enabling the Scalability of DBRepo" by Tobias Grantner.


## Getting Started

The notebooks contain code written in Python for which an environment with the necessary dependencies is required. The environment is managed using [Poetry](https://python-poetry.org/), which first needs to be [installed on your system](https://python-poetry.org/docs/#installation). After installing Poetry, the environment can be set up by running the following command:

```bash
poetry install
```


## Repository Structure

The repository is split into three main directories containing the notebooks for the three experiments conducted in the thesis, a directory containing the source code of the Python package used to conduct the experiments, and a directory containing the [Docker compose](https://docs.docker.com/compose/) files used to set up the environments for the experiments:

- [`code-duplication`](code-duplication/): Contains the notebooks for the code duplication evaluation and the artifacts produced by it.
    - [`data/`](code-duplication/data/): Contains the data produced by [`1_measurement.ipynb`](code-duplication/1_code_duplication.ipynb) as CSV files.
    - [`tables/`](code-duplication/tables/): Contains the tables produced by [`2_visualization.ipynb`](code-duplication/2_visualization.ipynb) as LaTeX files.
    - [`1_measurement.ipynb`](code-duplication/1_measurement.ipynb): Notebook to conduct the code duplication evaluation.
    - [`2_visualization.ipynb`](code-duplication/2_visualization.ipynb): Notebook to visualize the results of the code duplication evaluation.
- [`compose/`](compose/): Contains the Docker compose files augmented with image digests used to set up the environments for the experiments.
    - [`environment-independence/`](compose/environment-independence/):
        - [`before/`](compose/environment-independence/before/): Contains the Docker compose file and other necessary files to deploy the environment for the environment independence evaluation before the changes.
        - [`after/`](compose/environment-independence/after/): Contains the Docker compose file and other necessary files to deploy the environment for the environment independence evaluation after the changes.
    - [`service-merge/`](compose/service-merge/):
        - [`before/`](compose/service-merge/before/): Contains the Docker compose file and other necessary files to deploy the environment for the service merge evaluation before the changes.
        - [`after/`](compose/service-merge/after/): Contains the Docker compose file and other necessary files to deploy the environment for the service merge evaluation after the changes.
- [`memory-usage`](memory-usage/): Contains the notebooks for the memory usage evaluation and the artifacts produced by it.
    - [`data/`](memory-usage/data/): Contains the data produced by [`1_measurement.ipynb`](memory-usage/1_memory_usage.ipynb) as CSV files.
    - [`figures/`](memory-usage/figures/): Contains the figures produced by [`2_visualization.ipynb`](memory-usage/2_visualization.ipynb) as PDF files.
    - [`tables/`](memory-usage/tables/): Contains the tables produced by [`2_visualization.ipynb`](memory-usage/2_visualization.ipynb) as LaTeX files.
    - [`1_measurement.ipynb`](memory-usage/1_measurement.ipynb): Notebook to conduct the memory usage evaluation.
    - [`2_visualization.ipynb`](memory-usage/2_visualization.ipynb): Notebook to visualize the results of the memory usage evaluation.
- [`runtime`](runtime/): Contains the notebooks for the runtime evaluation and the artifacts produced by it.
    - [`data/`](runtime/data/): Contains the data produced by [`1_measurement.ipynb`](runtime/1_measurement.ipynb) as CSV files.
    - [`figures/`](runtime/figures/): Contains the figures produced by [`2_visualization.ipynb`](runtime/2_visualization.ipynb) as PDF files.
    - [`1_measurement.ipynb`](runtime/1_measurement.ipynb): Notebook to conduct the runtime evaluation.
    - [`2_visualization.ipynb`](runtime/2_visualization.ipynb): Notebook to visualize the results of the runtime evaluation.
- [`src/`](src/): Contains the source code of the Python package used to conduct the experiments.
- [`README.md`](README.md): This file you are currently reading.
- [`STATES.md`](STATES.md): Contains a description of the states of the system before and after the environment independence and service merge changes.