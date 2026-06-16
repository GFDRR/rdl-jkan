---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine government
    url: https://data.humdata.org/dataset/philippines-typhoon-haima-priority-index
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Baseline country data
    url: https://data.humdata.org/dataset/philippines-typhoon-haima-priority-index
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/philippines-typhoon-haima-priority-index
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/philippines-typhoon-haima-priority-index
dataset_id: rdls_hel-phl_nlrc510_typhoonhaimapriorityindex_20161122
description: 'Blog post about this prediction can be found here: http://bit.ly/2fWF2jq
  The predicted priority index of Typhoon Haima is produced by a machine learning
  algorithm that was trained on four past typhoons: Haiyan, Melor, Hagupit and Rammasun.
  It uses base line data for the whole country, combined with impact data of windspeeds
  and rains, and trained on counts by the Philippine government on people affected
  and houses damaged. First run The Priority Index is a 1-5 classification that can
  be used to identify the worst hit areas: those that need to be visited for further
  assessments or support first. Second run The model now predicts two things: a weighted
  index between partially damaged and completely damaged, where partially damaged
  is counted as 25% of the completely damaged. This has proven to give he highest
  accuracy. the precentage of total damage (damaged houses versus all houses) The
  absolute number of houses damaged / people affected is insufficiently validated
  at the moment, and should just be used for further trainng and ground-truthing.
  Data sources: Administrative boundaries (P_Codes) - Philippines Government; Published
  by GADM and UN OCHA (HDX) Census 2015 (population) - Philippine Statistics Authority;
  received from UN OCHA (HDX) Avg. wind speed (km/h) - University College London Typhoon
  path - University College London Houses damaged - NDRRMC Rainfall - GPM Poverty
  - Pantawid pamilyang pilipino program (aggregated) For the second run of the algorithm
  we also included: Roof and wall materials New geographical features The result of
  different models can be found in the file ''Typhoon Haima - performance of different
  models - second run.csv'' A note on how to interpret this. date running date alg_date
  same alg_model name of the algorithm used alg_predict_on name of the learning variable
  alg_use_log i s the learning variable transformed in log code_version version of
  the learn.py code All the columns with feat_ indicates the importance of that feature,
  if not present that feature was not used. learn_matrix name of the learning matrix
  with the 5 typhoons run_name unique run name (pickle files and csv files have this
  name for this model) typhoon_to_predict name of a new typhoon to predict val_accuracy
  accuracy based on 10 categories of damage 0% 10% 20% ... val_perc_down perc of underpredicted
  categories val_perc_up perc of overpredicted categories Val_best_score best r2 score
  Val_stdev_best_score error on best score based on the CV Val_score_test r2 score
  on the test set (this should be around +- 5% of the previus number to not overfit
  Val_mean_error_num_houses average error on the number of houses val_median_error_num_houses
  median val_std_error_num_houses std deviation of the errors (lower is better) Algorithm
  developed by 510.global the data innovation initiative of the Netherlands Red Cross..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/philippines-typhoon-haima-priority-index]'
details: 'Accuracy: NDRRMC publishes official data; they can only publish the official
  data when it is validated by their local counterparts (LGU or regional officials).'
exposure:
- asset_type:
    description: Building stock across the Philippines classified by vulnerability
      to typhoon damage
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Population distribution across the Philippines with poverty classification
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Windspeed, rainfall, population, and poverty baseline data for the
    Philippines were integrated with historical impact records (people affected and
    houses damaged) from four past typhoons. A machine learning algorithm was trained
    on these combined datasets to predict a priority index (1-5 classification) and
    house damage counts for Typhoon Haima, enabling identification of worst-hit areas
    requiring assessment.
  sources:
  - id: source_1
    license: null
    name: Philippine government
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Baseline country data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-typhoon-haima-priority-index
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Predicted house damage counts from Typhoon Haima based on machine
      learning model trained on historical typhoon impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Predicted people affected by Typhoon Haima based on priority index
      classification
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Typhoon Haima - Priority Index (Importance of features
    of the 1st run of the model)
  download_url: https://data.humdata.org/dataset/76bf7791-6c77-4a6f-81af-f2a28df17f68/resource/b29e6261-8b72-4cdb-95e2-c1ce23fd6f84/download/importancefeatures.xlsx
  format: null
  id: resource_b29e6261
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Typhoon Haima - importance - first run.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Typhoon Haima - Priority Index (First run of the algorithm
    (october 18th))
  download_url: https://data.humdata.org/dataset/76bf7791-6c77-4a6f-81af-f2a28df17f68/resource/d3c55dc6-ea2a-41cb-935b-21b650feaed9/download/typhoon-haima-house-damage-predictions-version-1.csv
  format: null
  id: resource_d3c55dc6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Typhoon Haima - house damage predictions (Version 1).csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Typhoon Haima - Priority Index (Second run of the algorithm,
    including new datasets (november 21st))
  download_url: https://data.humdata.org/dataset/76bf7791-6c77-4a6f-81af-f2a28df17f68/resource/b7ce9c4a-92d0-489d-8fc8-b0d7ef298f45/download/typhoon-haima-house-damage-predictions-version-2.csv
  format: null
  id: resource_b7ce9c4a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Typhoon Haima - house damage predictions (Version 2).csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Importance of features for second run of the algorithm, including new
    datasets (november 21st)
  download_url: https://data.humdata.org/dataset/76bf7791-6c77-4a6f-81af-f2a28df17f68/resource/89e50950-6787-4e3c-aa96-03d844983837/download/typhoon-haima-best-run.xlsx
  format: null
  id: resource_89e50950
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Typhoon Haima - importance - second run.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Typhoon Haima - Priority Index (Log file of different
    models tried during the second run of the model)
  download_url: https://data.humdata.org/dataset/76bf7791-6c77-4a6f-81af-f2a28df17f68/resource/a5da1f6d-c560-4f35-bb4f-ddee7750f6fa/download/typhoon-haima-performance-of-different-models-second-run.csv
  format: null
  id: resource_a5da1f6d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Typhoon Haima - performance of different models - second run.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-phl_nlrc510_typhoonhaimapriorityindex_20161122
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-11-22'
temporal_resolution: null
title: Philippines - Typhoon Haima - Priority Index
version: null
vulnerability: null
---
