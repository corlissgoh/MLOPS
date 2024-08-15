# MLOps Project Repository

Welcome to the MLOps project repository! This repository contains multiple machine learning applications. Depending on which application you want to deploy on Render, you should configure the settings to point to the correct folder.

## Repository Structure

The repository is organized as follows:

```
/mushroom_classification_app
    ├── conf/
    ├── data/
    ├── logs/
    ├── models/
    ├── notebooks/
    ├── src/
    ├── Procfile.txt
    ├── pyproject.toml
    ├── README.md
    └── poetry.lock

/house_pricing_app
    ├── conf/
    ├── data/
    ├── logs/
    ├── models/
    ├── notebooks/
    ├── src/
    ├── Procfile.txt
    ├── pyproject.toml
    ├── README.md
    └── poetry.lock

```

- **mushroom_classification_app**: Contains the code and resources for the Mushroom Classification application.
- **house_pricing_app**: Contains the code and resources for the House Price Prediction application.

## Deploying on Render

To deploy an application on Render, follow these steps:

1. **Choose the Application**: Decide whether you want to deploy the `mushroom_classification_app` or the `house_pricing_app`.

2. **Set the Repository and Branch Settings**: In the Render dashboard, under the "Build & Deploy" settings, specify these items:
   - Repository: `https://github.com/corlissgoh/mlops`
   - Branch: `main`

3. **Set the Root Directory**: In the Render dashboard, under the "Build & Deploy" setting, specify the folder of the application you wish to deploy:
   - For Mushroom Classification: `mushroom_classification_app`
   - For House Price Prediction: `house_pricing_app`

4. **Set the Build Command**: Specify the command to be `poetry install`. There is no need for a requirements.txt since Poetry is used in this project.

5. **Set the Start Command**: Specify the command to be `streamlit run src/app.py --server.enableCORS false`. Render will look for the `Procfile` in the specified root directory.

6. **Build and Deploy**: After configuring the settings, you can trigger a deploy. Render will build and deploy the application according to the specified directory's `Procfile` and other configurations.

## Running Locally

If you want to run an application locally:

### Prerequisites

Before you can clone the repository, ensure you have Git installed and configured on your local machine.

1. **Install Git**:
   - [Download Git](https://git-scm.com/downloads) and follow the installation instructions for your operating system.

2. **Configure Git**: Open your Terminal (macOS) or Anaconda Prompt (Windows) and run the following commands, replacing `"Your Name"` and `"your.email@example.com"` with your
   actual Github name and email address.
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

After these steps, you can proceed with the cloning and other instructions for running the applications locally.

### Next Steps

1. **In your Terminal (macOS) or Anaconda (Windows), navigate to the directory where you want the app files & folders to be in**:
   - For Mushroom Classification:
     ```bash
     cd Desktop/webapp/mushroom_classification_app # just an example directory structure
     ```
   - For House Price Prediction:
     ```bash
     cd Downloads/house_pricing_app # just an example directory structure
     ```

2. **Clone this Repository**:
   - Replace 'your-username' with your actual GitHub username:
     ```bash
     git clone https://github.com/your-username/https://github.com/corlissgoh/mlops
     ```
     
3. **Install Dependencies**: Ensure you have [Poetry](https://python-poetry.org/) installed, then run:
   ```bash
   poetry install
   ```

4. **Run the Application**:
   - For a Streamlit app, you would typically run:
     ```bash
     streamlit run src/app.py
     ```
