# AI_Level_Jobs

**AI_Level_Jobs** is a Python application built with **Streamlit** for visualizing the risk of job automation across different industries and cities. The dashboard allows users to filter and explore data on automation risks and trends based on location and sector, offering insights into the impact of AI automation.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Docker Setup](#docker-setup)

---

## Requirements

To run **AI_Level_Jobs**, you need the following:

- **Python**: >= 3.9 (avoid version 3.9.7 due to compatibility issues)
- **Streamlit**: >= 1.18.0
- **Docker** (Optional, for containerization)

The dependencies are specified in the `requirements.txt` file:

```txt
streamlit>=1.18.0
pandas==1.3.3
numpy==1.21.2
altair==4.1.0
vega_datasets==0.9.0
plotly==5.10.0

---

## Installation

### Step 1: Clone the Repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/samlekalai/AI_Level_Jobs
cd AI_Level_Jobs
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

It’s best practice to use a virtual environment for managing dependencies:

```bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
```

### Step 3: Install Dependencies

Once inside your virtual environment (if you’re using one), install the necessary dependencies using pip:

```bash
pip install -r requirements.txt
```

### Running the App

To run the application locally using Streamlit, use the following command:

```bash
streamlit run AI_Level_Jobs.py
```
## Docker Setup
We put a Dockerfile inside this repo in order to config docker. Thanks to that, you can run the app while dockerising it.
First build the image:

```bash
docker build -t AI_Level_Jobs . 
```

And then create the conntainer:
```bash
docker run -dp 8501:8501 AI_Level_Jobs
```

Now you can type this url in your browser:
http://localhost:8501/