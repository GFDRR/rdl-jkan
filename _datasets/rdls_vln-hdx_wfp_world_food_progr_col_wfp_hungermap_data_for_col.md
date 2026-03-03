---
catalog: Humanitarian Data Exchange
contact_point:
  email: null
  id: attribution_contact
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/9a8b705d-1679-4554-95de-9fc6343e57c8
creator:
  email: null
  id: attribution_creator
  name: WFP HungerMap
  url: https://data.humdata.org/dataset/9a8b705d-1679-4554-95de-9fc6343e57c8
dataset_id: rdls_vln-hdx_wfp_world_food_progr_col_wfp_hungermap_data_for_col
description: 'HungerMapLIVE is the World Food Programme (WFP)''s global hunger monitoring
  system. It combines key metrics from various data sources - such as food security
  information, weather, population size, conflict, hazards, nutrition information
  and macro-economic data - to help assess, monitor and predict the magnitude and
  severity of hunger in near real-time. The resulting analysis is displayed on an
  interactive map that helps WFP staff, key decision makers and the broader humanitarian
  community to make more informed and timely decisions relating to food security.
  The platform covers 94 countries, including countries where WFP has operations as
  well as most lower and lower-middle income countries (as classified by the World
  Bank). [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX) at https://data.humdata.org] [Original dataset: https://data.humdata.org/dataset/9a8b705d-1679-4554-95de-9fc6343e57c8]'
details: "Methodology: WFP's Hunger Monitoring Unit in the Research, Assessment and\
  \ Monitoring Division conducts real-time food security monitoring to track the latest\
  \ food security trends. In areas where limited or no data is available, we use machine\
  \ learning-based predictive models to estimate the food security situation. WFP\
  \ conducts continuous food security monitoring via computer assisted telephone interviewing\
  \ (CATI) through call centers. Data is collected on a rolling basis, spread evenly\
  \ over a past 28/30 calendar days or over a three-month period. The main advantage\
  \ of this approach is that data is available more frequently and processed daily\
  \ through automated statistical engines. Daily updates are then produced showing\
  \ a snapshot of the current food security situation (with a slight time lag of 2-4\
  \ days to ensure data quality) over the past 28/30 calendar days. Call interviews\
  \ aim to cover all mobile service providers, and telephone numbers are randomly\
  \ selected from a database of phone numbers or generated using random-digit dialling\
  \ (RDD) method. To ensure a more representative sample, WFP uses various types of\
  \ pre/post-stratification and sampling methods, including by weighting results by\
  \ population at the first or second administrative level and by a demographic variable\
  \ such as the level of education or water sources which could impact food security,\
  \ in order to account for the fact that households with more phones are more likely\
  \ to be selected (e.g. younger, somewhat better-off households who live in urban\
  \ areas). In order to compensate for non-response and attrition, key challenges\
  \ for high frequency mobile phone surveys, new observations are added in each administrative\
  \ area following the sample design specific for each of the country. The questionnaire\
  \ includes questions on household demographics, households' food consumption, coping\
  \ strategies used (food-based and livelihood-based), access to food, market and\
  \ health services, and other country-specific livelihood-related questions. In addition,\
  \ at the end of the survey, respondents are given the opportunity to share additional\
  \ information on the food situation in their communities. For first-level administrative\
  \ areas where daily updated survey data is not available, the prevalence of people\
  \ with poor or borderline food consumption (FCS) and the prevalence of people with\
  \ reduced coping strategy index (rCSI) \xE2\u2030\xA519 is estimated with a predictive\
  \ model. Predictive model design: Training data: The models were trained using FCS\
  \ and rCSI data spanning over 70 countries across, aggregated at the level of first-order\
  \ administrative divisions. The input variables used to make the predictions were\
  \ built using information about population density, rainfall, vegetation status,\
  \ conflict, market prices, macroeconomic indicators, and undernourishment. For areas\
  \ where past FCS/rCSI measurements are available, the last available data point\
  \ is also included as input variable. Data sources: Beyond the data sources already\
  \ credited in the Glossary, additional sources used only for the model but not for\
  \ display purposes are: Gridded Population of the World, Version 4 (GPWv4): Population\
  \ Count, Revision 11 WFP's Alert for Price Spikes (ALPS) indicator Algorithm: XGBoost\
  \ - a machine learning technique producing predictive models in the of an ensemble\
  \ of regression trees. The model parameters were optimized by a cross-validated\
  \ grid-search. Model evaluation: The accuracy of the model was evaluated on a test\
  \ set comprising 20% of the historical data, having trained 100 models on subsamples\
  \ (with replacement) of the remaining 80% of the historical data. Predictions: The\
  \ model produces current estimates of the prevalence of people with poor or borderline\
  \ FCS and rCSI for areas where no food security data is available; we call this\
  \ nowcasting. For each first-level administrative boundary we report the median\
  \ and 95% confidence intervals of a distribution of predictions obtained from 100-bootstrap\
  \ models trained on subsamples (with replacement) of the training data. | Temporal\
  \ coverage: [2024-03-11T00:00:00 TO 2024-10-02T23:59:59] | Update frequency: As\
  \ needed | Last modified: 2025-03-11"
exposure:
- category: agriculture
  dimension: structure
  quantity_kind: area
  taxonomy: null
extra_attributions: []
hazard:
  calculation_method: observed
  disaster_identifiers: ''
  hazard_analysis_type: empirical
  hazard_type: earthquake
  intensity: PGA:g
  occurrence_range: ''
  processes: ground_motion
  seasonality: ''
license: CC-BY-SA-4.0
loss: null
project: null
publisher:
  email: null
  id: attribution_publisher
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/9a8b705d-1679-4554-95de-9fc6343e57c8
purpose: null
resources:
- coordinate_system: null
  description: Dataset-level metadata exported from HDX.
  download_url: https://data.humdata.org/dataset/9a8b705d-1679-4554-95de-9fc6343e57c8/download_metadata?format=json
  format: JSON (json)
  id: hdx_dataset_metadata_json
  media_type: null
  spatial_resolution: null
  temporal: null
  title: HDX dataset metadata (JSON)
- coordinate_system: null
  description: Colombia - HungerMap data
  download_url: https://data.humdata.org/dataset/9a8b705d-1679-4554-95de-9fc6343e57c8/resource/2213956f-b8da-4e18-900e-243aaf790d63/download/wfp-hungermap-data-for-col.csv
  format: CSV (csv)
  id: hdx_res_2213956f
  media_type: null
  spatial_resolution: null
  temporal: null
  title: wfp-hungermap-data-for-col.csv
- coordinate_system: null
  description: Colombia - HungerMap data long format
  download_url: https://data.humdata.org/dataset/9a8b705d-1679-4554-95de-9fc6343e57c8/resource/4a935f8f-aa84-45ae-b5ba-0e926fbe0633/download/wfp-hungermap-data-for-col-long.csv
  format: CSV (csv)
  id: hdx_res_4a935f8f
  media_type: null
  spatial_resolution: null
  temporal: null
  title: wfp-hungermap-data-for-col-long.csv
risk_data_type:
- hazard
- exposure
- vulnerability
schema: rdl-03
slug: rdls_vln-hdx_wfp_world_food_progr_col_wfp_hungermap_data_for_col
spatial:
  countries:
  - COL
  scale: national
title: Colombia - HungerMap data
version: null
vulnerability:
  approach: ''
  base_data_type: ''
  category: ''
  dimension: ''
  function_type: ''
  hazard_analysis_type: ''
  hazard_primary: ''
  hazard_process_primary: ''
  hazard_process_secondary: ''
  hazard_secondary: ''
  intensity: ''
  metric: ''
  relationship: ''
  taxonomy: ''
  unit: ''
---
