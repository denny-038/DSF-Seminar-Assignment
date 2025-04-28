# Does Environmental Disclosure Matter?  
*Evidence from Textual Analysis of 10-K Filings*

## Overview

This project studies whether environmental language in 10-K filings helps explain U.S. stock returns beyond standard risk factors. Using ClimateBERT models, we construct:  
- **ENV Score**: share of environmental content  
- **ENV Sentiment**: tone of environmental language  

We apply these variables to Fama-French three- and five-factor models across 70 S&P 500 firms from 2018–2023.

## Repository Structure

- **10%_Portfolio**:  
Contains the scripts used for the additional findings section, comparing portfolios formed from the top 10% and bottom 10% of both ENV Score and ENV Sentiment, using both the Fama-French three-factor and five-factor models.

- **Climate-Bert**:  
  Applies ClimateBERT models to the processed 10-K filings to generate ENV sentiment scores.

- **Data**:  
  Contains datasets used in this project, including:  
  - A list of all S&P 500 companies,  
  - Links to all 10-K filings for these companies,  
  - Extracted and processed items from the filings, and  
  - ClimateBERT scores for the intersecting S&P 500 companies from 2018 to 2023.  

  *Note:* The full extracted item data from the 10-K filings is **not** included in this folder because the file sizes exceed GitHub’s maximum upload limit.

- **Data_Processing**:  
  Contains all scripts used to prepare the dataset, including:  
  - Constructing the list of all S&P 500 companies from 2018 to 2024 and identifying their 10-K filings,  
  - Extracting the required sections (Items 1, 1A, 7, and 8) from the 10-K filings,  
  - Checking which items are still missing after the initial extraction, and  
  - Cleaning and processing the extracted items for analysis.

- **FF3 FF5**:  
Contains the code and datasets used for the analysis. It includes the Fama-French three- and five-factor regressions based on standard factors, the extended models incorporating firm-specific environmental variables (ENV Score and ENV Sentiment), and the trend analysis of these variables over time.
  
- **Robustness**/**5Factor**:  
  Contains the script used to generate the tables for the Fama-French five-factor model extension.
  
- **Robustness**/**ESG Robustness**:  
  Contains the scripts used to run the regressions testing the predictive power of our text-based variables, as well as summary tables and Fama-French three-factor model comparison results. The folder also contains:
  - Input: all the datasets needed to run the code,
  - Output: all the tables produced by the code.

- **Robustness**/**Train_Test_Split**:


## Setup

To install all required Python packages, simply run:

```bash
pip install -r requirements.txt
```

## Authors

- Ohaness Alokpa  
- Andrea Zoccarato  
- Ching-Wei Su  
- Safa Berber  
- Purev-Ochir Byambajav  

Master in Data Science for Finance — EUR 2024–2025

