# MLOps Project Repository

Welcome to the MLOps project repository! This repository contains multiple machine learning applications. Depending on which application you want to deploy on Render, you should configure the settings to point to the correct folder.

## Repository Structure

The repository is organized as follows:

```
/mushroom_classification_app
    ├── conf/
    ├── data/
    ├── models/
    ├── notebooks/
    ├── src/
    ├── Procfile
    ├── README.md
    └── config.yaml

/house_price_app
    ├── conf/
    ├── data/
    ├── models/
    ├── notebooks/
    ├── src/
    ├── Procfile
    ├── README.md
    └── config.yaml

...
other files and folders
```

- **mushroom_classification_app**: Contains the code and resources for the Mushroom Classification application.
- **house_price_app**: Contains the code and resources for the House Price Prediction application.

## Deploying on Render

To deploy an application on Render, follow these steps:

1. **Choose the Application**: Decide whether you want to deploy the `mushroom_classification_app` or the `house_price_app`.

2. **Set the Root Directory**: In the Render dashboard, under the "Root Directory" setting, specify the folder of the application you wish to deploy:
   - For Mushroom Classification: `mushroom_classification_app`
   - For House Price Prediction: `house_price_app`

3. **Set the Start Command**: Ensure that the start command in your Procfile is correctly configured. Render will look for the `Procfile` in the specified root directory.

4. **Build and Deploy**: After configuring the settings, you can trigger a deploy. Render will build and deploy the application according to the specified directory's `Procfile` and other configurations.

## Running Locally

If you want to run an application locally:

1. **Navigate to the Application Directory**:
   - For Mushroom Classification:
     ```bash
     cd mushroom_classification_app
     ```
   - For House Price Prediction:
     ```bash
     cd house_price_app
     ```

2. **Install Dependencies**: Ensure you have [Poetry](https://python-poetry.org/) installed, then run:
   ```bash
   poetry install
   ```

3. **Run the Application**:
   - For a Streamlit app, you would typically run:
     ```bash
     streamlit run src/app.py
     ```
