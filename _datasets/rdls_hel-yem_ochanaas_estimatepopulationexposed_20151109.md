---
attributions:
- entity:
    affiliation: null
    email: null
    name: Global Assessment Report on Disaster Risk Reduction 2015
    url: https://data.humdata.org/dataset/estimate-of-population-exposed-to-flood-risk-from-cyclone-megh
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Coordinated Assessment and Support Section (CASS)
    url: https://data.humdata.org/dataset/estimate-of-population-exposed-to-flood-risk-from-cyclone-megh
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/estimate-of-population-exposed-to-flood-risk-from-cyclone-megh
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNISDR
    url: https://data.humdata.org/dataset/estimate-of-population-exposed-to-flood-risk-from-cyclone-megh
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: JRC
    url: https://data.humdata.org/dataset/estimate-of-population-exposed-to-flood-risk-from-cyclone-megh
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Needs Assessment and Analysis Section (NAAS) (inactive)
  url: https://data.humdata.org/dataset/estimate-of-population-exposed-to-flood-risk-from-cyclone-megh
creator:
  affiliation: null
  email: null
  name: OCHA Needs Assessment and Analysis Section (NAAS) (inactive)
  url: https://data.humdata.org/dataset/estimate-of-population-exposed-to-flood-risk-from-cyclone-megh
dataset_id: rdls_hel-yem_ochanaas_estimatepopulationexposed_20151109
description: 'Population exposure estimates for 11 governorates based on the past
  25 years flood hazard data for Yemen. Our source of data is Global Assessment Report
  on Disaster Risk Reduction 2015.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/estimate-of-population-exposed-to-flood-risk-from-cyclone-megh]'
details: null
exposure:
- asset_type:
    description: Population exposed to cyclone-induced flooding and wind hazards across
      11 governorates in Yemen
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: simulated
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
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: "Population exposure estimates were calculated by overlaying tropical\
    \ cyclone Megh's projected rainfall (\xE2\u2030\xA52 inches for 9-11 November)\
    \ and wind speed forecasts with gridded population data from WorldPop and historical\
    \ 25-year flood hazard data from the Global Assessment Report 2015. OCHA CASS\
    \ integrated these datasets to estimate affected populations across 11 Yemeni\
    \ governorates at administrative levels 1 and 2."
  sources:
  - id: source_1
    license: null
    name: Global Assessment Report on Disaster Risk Reduction 2015
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: OCHA Coordinated Assessment and Support Section (CASS)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_4
    license: null
    name: UNISDR
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_5
    license: null
    name: JRC
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/estimate-of-population-exposed-to-flood-risk-from-cyclone-megh
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposure estimates to tropical cyclone Megh wind speeds
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
        metric: exposure
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population exposure estimates to cyclone-induced rainfall and flood
      hazards based on 25-year historical flood data
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Based on the Tropical Cyclone Megh projected path on Monday 9 November,
    Coordinated Assessment and Support Section (CASS) calculated estimated population
    exposure to 2 inch or more accumulated rainfall, forecast for 9 - 11 November
    (please see 'Final Result-Governorate level' worksheet). Based on the analysis
    17 governorates were highlighted, with estimated 7.6 million population living
    in the rainfall zone.
  download_url: https://data.humdata.org/dataset/4abeb724-ec79-441a-ac7f-34bb6a90b33a/resource/5085b0aa-b5a3-43ee-bd9a-9cfe31a525dc/download/tc_megh_pop_exp_admin12_5_days_rainfall9-11nov_2inch_yemen_v0.2_9nov2015.xlsx
  format: null
  id: resource_5085b0aa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC_Megh_PoP_Exp_Admin1&2_5_days_Rainfall(9-11Nov)_2inch_YEMEN_v0.2_9Nov2015.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Yemen - Estimate of Population Exposed to Flood Risk from Cyclone Megh
    (PDF)
  download_url: https://data.humdata.org/dataset/4abeb724-ec79-441a-ac7f-34bb6a90b33a/resource/cec1451f-d8dc-42e2-8493-0fd4c7160f59/download/yem_tc_9nov_megh_v5.pdf
  format: null
  id: resource_cec1451f
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: YEM_TC_9Nov_MEGH_v5.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Based on the Tropical Cyclone Megh projected path on Monday 9 November,
    Coordinated Assessment and Support Section (CASS) calculated estimated population
    exposure to 2 inch or more accumulated rainfall, forecast for 9 - 11 November
    (please see ''TC_Megh_PoP_Exp_Admin1&2_5_days_Rainfall(9-11Nov)_2inch_YEMEN_v0.2_9Nov2015.xlsx''
    worksheet). Based on the analysis 17 governorates were highlighted, with estimated
    7.6 million population potentially exposed. CASS further refined the estimated
    population figures for 15 out of the 19 governorates (please see ''Final Result-15
    Governorates'' and ''Final Result-District level''worksheets), by calculating
    population exposure based on 25 years (RP) flood hazard data. Estimated population
    figure: 667, 245'
  download_url: https://data.humdata.org/dataset/4abeb724-ec79-441a-ac7f-34bb6a90b33a/resource/69c103d0-5890-4f1a-af00-2da06341390b/download/tc_megh_pop_exp_admin12_floods_25year_yemen_v0.2_9nov2015.xlsx
  format: null
  id: resource_69c103d0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC_Megh_PoP_Exp_Admin1&2_Floods_25Year_YEMEN_v0.2_9Nov2015.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Based on the Tropical Cyclone Megh projected path on Monday 9 November,
    Coordinated Assessment and Support Section (CASS) calculated estimated population
    exposure to high wind speed zones (60km/h, 90km/h and 120km/h). Based on the analysis
    11 governorates were highlighted, with estimated 359,072 population living in
    the 120km/h wind speed zone.
  download_url: https://data.humdata.org/dataset/4abeb724-ec79-441a-ac7f-34bb6a90b33a/resource/e4404e59-384e-4f1e-bf2c-06d307affef5/download/tc_megh_pop_exp_admin12_windspeed_9-11-novyemen_v0.2-9nov2015.xlsx
  format: null
  id: resource_e4404e59
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC_Megh_PoP_Exp_Admin1&2_WindSpeed_(9-11 Nov)YEMEN_v0.2-9Nov2015.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-yem_ochanaas_estimatepopulationexposed_20151109
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-11-09'
temporal_resolution: null
title: Yemen - Estimate of Population Exposed to Flood Risk from Cyclone Megh
version: null
vulnerability: null
---
