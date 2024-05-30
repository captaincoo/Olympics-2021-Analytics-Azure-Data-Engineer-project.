# Olympic Data Analysis with Azure

<img width="1156" alt="Screenshot 2024-05-30 at 1 02 44 PM" src="https://github.com/captaincoo/Olympics-2021-Analytics-Azure-Data-Engineer-project./assets/49879935/a8732654-711b-4e21-9f6f-fef5bd119146">
Welcome to the Olympic Data Analysis with Azure project! This project showcases an end-to-end data engineering pipeline that collects, transforms, and analyzes Olympic data using various Azure services. Whether you're interested in understanding the process, replicating it, or contributing to its development, this README will guide you through the project.

## Project Overview

The primary objective of this project is to demonstrate the capabilities of Azure services in handling a real-world data engineering scenario. We will take you through the following steps:

### Step 1: Data Collection from Kaggle and GitHub

- **Data Sources:** We start by acquiring Olympic data from Kaggle, an excellent source for datasets. This data will serve as the foundation of our analysis.
- **GitHub Repository:** To ensure version control and facilitate collaboration, we created a dedicated GitHub repository for this project. The Olympic data is uploaded here.

### Step 2: Creating Azure Data Factory (ADF)

- **Azure Data Factory:** In this step, we set up an Azure Data Factory instance within your Azure account. This is where the magic begins as we define a pipeline for data movement and transformation.
- **Pipeline Definition:** Within ADF, we create a pipeline that orchestrates the data flow, ensuring that the data reaches its destination correctly.
- **Linked Services:** To establish a connection between ADF and our GitHub repository, we configure linked services.

### Step 3: Data Extraction and Storage in Azure Data Lake Storage Gen 2 (ADLS)

- **GitHub Data Extraction:** Using ADF, we extract the Olympic data from our GitHub repository.
- **ADLS Gen 2:** The extracted data is then transferred and stored in Azure Data Lake Storage Gen 2 (ADLS). Here, we also pay attention to structuring the data for ease of access.

### Step 4: Data Transformation using Azure Databricks

- **Databricks Setup:** We set up an Azure Databricks cluster to handle data transformation. Databricks provides a powerful environment for data processing.
- **Data Ingestion:** In this phase, we ingest the data from ADLS into Databricks for further processing.
- **Data Transformation:** Using Databricks notebooks, we perform data transformations, including data cleansing and enrichment. Advanced analytics, such as aggregations and statistical analyses, are also executed.

### Step 5: Storing Transformed Data Back to ADLS

- **Data Storage:** Once the data is transformed and enriched, it is stored back into Azure Data Lake Storage Gen 2.
- **Data Organization:** We ensure that the transformed data is organized and labeled appropriately, making it easy to retrieve and use.

### Step 6: Utilizing Azure Synapse Analytics (formerly SQL Data Warehouse)

- **Azure Synapse Analytics:** Here, we create an Azure Synapse Analytics instance. It's a powerful tool for data analysis.
- **Schema Design:** We design the schema and tables to accommodate the transformed data.
- **Data Loading:** The data is loaded from ADLS into Synapse Analytics, preparing it for analysis.

### Step 7: Data Exploration and Analysis

- **SQL Queries:** We develop complex SQL queries within Azure Synapse Analytics to explore valuable insights from the Olympic data.
- **Analysis:** This is where the fun begins! We perform historical analysis, identify patterns, and extract meaningful information from the Olympic data.

## Getting Started

To get started with this project, follow the high-level steps outlined above. For detailed instructions, consult the documentation provided within each step's directory in this repository.

## Prerequisites

Before you begin, make sure you have the following prerequisites in place:

- An Azure Account with appropriate subscriptions.
- Azure Data Factory, Databricks, and Synapse Analytics instances set up.
- A GitHub account for version control and data storage.

Now you're ready to dive into the world of Olympic data analysis with Azure! If you have any questions or need assistance, don't hesitate to reach out.

Enjoy exploring the fascinating world of data engineering and analytics! 🏅📊🚀
