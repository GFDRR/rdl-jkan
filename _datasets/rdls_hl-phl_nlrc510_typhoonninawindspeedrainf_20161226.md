---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine government
    url: https://data.humdata.org/dataset/typhoon-nina-windspeed-rainfall-and-priority-index
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/typhoon-nina-windspeed-rainfall-and-priority-index
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/typhoon-nina-windspeed-rainfall-and-priority-index
dataset_id: rdls_hl-phl_nlrc510_typhoonninawindspeedrainf_20161226
description: 'This dataset contains: windspeeds of Typhoon Nina rainfall of Typhoon
  Nina Priority Index of Typhoon Nina The predicted priority index of Typhoon Nina
  is produced by a machine learning algorithm that was trained on five past typhoons:
  Haiyan, Melor, Hagupit and Rammasun and Haima, It uses base line data for the whole
  country, combined with impact data of windspeeds and rains, and trained on counts
  by the Philippine government on houses damaged and completely destroyed. The output
  is a weighted index between partially damaged and completely damaged, where partially
  damaged is counted as 25% of the completely damaged. This has proven to give he
  highest accuracy. The absolute number of houses damaged / people affected is insufficiently
  validated at the moment, and should just be used for further trainng and ground-truthing.
  Scoring The model has an best r2 score of 0.794933727 and an accuracy of 0.699470899
  Data sources: Administrative boundaries (P_Codes) - Philippines Government; Published
  by GADM and UN OCHA (HDX) Census 2015 (population) - Philippine Statistics Authority;
  received from UN OCHA (HDX) Avg. wind speed (mph) - University College London Typhoon
  path - University College London Houses damaged - NDRRMC Rainfall - GPM Poverty
  - Pantawid pamilyang pilipino program (aggregated) Roof and wall materials New geographical
  features All the columns with feat_ indicates the importance of that feature, if
  not present that feature was not used. learn_matrix name of the learning matrix
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/typhoon-nina-windspeed-rainfall-and-priority-index]'
details: See https://data.humdata.org/dataset/philippines-typhoon-haima-priority-index
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
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
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: Observed windspeed and rainfall data from Typhoon Nina were combined
    with baseline country-wide exposure data and historical damage counts from five
    past typhoons to train a machine learning algorithm that produces a weighted priority
    index indicating the degree of building damage (partial to complete destruction)
    at sub-national locations.
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
    name: Netherlands Red Cross - 510
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/typhoon-nina-windspeed-rainfall-and-priority-index
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage (partial and complete destruction) from Typhoon
      Nina
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
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://data.humdata.org/dataset/philippines-typhoon-haima-priority-index
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Typhoon Nina - windspeed, rainfall and priority index
    (Windspeed data provided by Mark Saunders, University College London)
  download_url: https://data.humdata.org/dataset/5d75ef75-e57a-45a3-8992-84af62db0b3c/resource/0e11586a-5549-4df3-a999-7cd9df7f8848/download/typhoon-nina-windspeed.zip
  format: null
  id: resource_0e11586a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Typhoon Nina Windspeed.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Typhoon Nina - windspeed, rainfall and priority index
    (Rainfall between december 24-26th 2016 in the Philippines)
  download_url: https://data.humdata.org/dataset/5d75ef75-e57a-45a3-8992-84af62db0b3c/resource/1bb5fd80-997d-4143-ae3b-bb04ef9a9085/download/typhoon-nina-rainfall.csv
  format: null
  id: resource_1bb5fd80
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Typhoon Nina - rainfall.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - Typhoon Nina - windspeed, rainfall and priority index
    (GradientBoosting best algorithm outcome)
  download_url: https://data.humdata.org/dataset/5d75ef75-e57a-45a3-8992-84af62db0b3c/resource/fb8817df-6b9d-4b15-a540-f15ee6310118/download/typhoon-nina-priority-index.csv
  format: null
  id: resource_fb8817df
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Typhoon Nina - Priority Index.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: SitRep No.13 re Preparedness Measures and Effects of TY NINA (NOCK-TEN)
    as of 09 January 2017, 8:00 AM
  download_url: https://data.humdata.org/dataset/5d75ef75-e57a-45a3-8992-84af62db0b3c/resource/6189c788-ea52-4366-a290-614e4e252c80/download/nock-ten-damage-data.xlsx
  format: null
  id: resource_6189c788
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nock-Ten damage data.xlsx
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-phl_nlrc510_typhoonninawindspeedrainf_20161226
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
  start: '2016-12-26'
temporal_resolution: null
title: Philippines - Typhoon Nina - windspeed, rainfall and priority index
version: null
vulnerability: null
---
