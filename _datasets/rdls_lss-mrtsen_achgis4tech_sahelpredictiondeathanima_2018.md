---
attributions:
- entity:
    affiliation: null
    email: null
    name: PREDISAN (Food and Nutrition Security Monitoring and Prediction System in
      the Sahel)
    url: https://data.humdata.org/dataset/sahel-prediction-dead-animals-by-ach-gis4tech
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/sahel-prediction-dead-animals-by-ach-gis4tech
creator:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/sahel-prediction-dead-animals-by-ach-gis4tech
dataset_id: rdls_lss-mrtsen_achgis4tech_sahelpredictiondeathanima_2018
description: "The model trains with the actual data of the variables to be predicted\
  \ and uses their correlation with agroclimatic indicators, biomass, and violence\
  \ to predict said variable where there is no actual data, at the level of Commune/Municipality\
  \ for all of Senegal and Mauritania. This information belongs to the Food and Nutrition\
  \ Security Monitoring and Prediction System in the Sahel (PREDISAN) Project, funded\
  \ by the Agencia Andaluza de Cooperaci\xF3n Internacional para el Desarrollo (AACID)\
  \ and the University of Granada (UGR). The PREDISAN AI-SAHEL Project focuses on\
  \ the Monitoring and Prediction System for Humanitarian Vulnerability of Pastoral\
  \ and Agro-pastoral Populations in the Western Sahel, based on GIS Analysis and\
  \ Artificial Intelligence. For more information, contact GIS4Tech at info@gis4tech.com\
  \ or visit the PREDISAN platform at https://predisan.gis4tech.com/sahel.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/sahel-prediction-dead-animals-by-ach-gis4tech]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The model integrates historical livestock mortality data with agroclimatic
    indicators, biomass measurements, and violence records to train a predictive algorithm
    that estimates dead animals at commune/municipality spatial resolution. Predictions
    are generated for areas lacking direct observational data, producing probabilistic
    outputs (prob_dead_animals_0, prob_dead_animals_1) alongside point estimates.
  sources:
  - id: source_1
    license: null
    name: PREDISAN (Food and Nutrition Security Monitoring and Prediction System in
      the Sahel)
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sahel-prediction-dead-animals-by-ach-gis4tech
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Predicted livestock mortality (dead animals) from drought conditions
      in Sahel region
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: Sahel prediction Death Animals
  download_url: https://data.humdata.org/dataset/2ee5806a-848b-4a87-9fb8-e5b68d8a9a45/resource/74dd04cf-cb51-4aa1-b63e-7745e91cbe45/download/sahel-prediction-death-animals-by-ach-gis4tech.csv
  format: null
  id: resource_74dd04cf
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sahel-prediction-death-animals-by-ACH-GIS4Tech.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mrtsen_achgis4tech_sahelpredictiondeathanima_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - SEN
  - MRT
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-02-28'
  start: '2018-01-01'
temporal_resolution: null
title: Sahel Prediction Death Animals
version: null
vulnerability: null
---
