---
attributions:
- entity:
    affiliation: null
    email: null
    name: Food Security Information Network (FSIN)
    url: https://data.humdata.org/dataset/regional-report-on-food-security-and-nutrition-in-west-africa-and-the-sahel-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Permanent Interstate Committee for Drought Control in the Sahel (CILSS)
    url: https://data.humdata.org/dataset/regional-report-on-food-security-and-nutrition-in-west-africa-and-the-sahel-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Food Security Information Network
  url: https://data.humdata.org/dataset/regional-report-on-food-security-and-nutrition-in-west-africa-and-the-sahel-2024
creator:
  affiliation: null
  email: null
  name: Food Security Information Network
  url: https://data.humdata.org/dataset/regional-report-on-food-security-and-nutrition-in-west-africa-and-the-sahel-2024
dataset_id: rdls_lss-fsin_regionalreportnutritionwe_2014
description: "The Regional Report on Food Security and Nutrition in West Africa and\
  \ the Sahel 2024 (RRSAN) provides timely and reliable data needed to address the\
  \ region's increasing food security and nutrition challenges. It presents data and\
  \ analyses from the latest March 2024 Cadre Harmonis\xE9 (CH) cycle and includes\
  \ expanded technical analyses by the Permanent Interstate Committee for Drought\
  \ Control in the Sahel (CILSS) and its partners on the 2023-2024 agricultural campaign..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/regional-report-on-food-security-and-nutrition-in-west-africa-and-the-sahel-2024]"
details: https://www.fsinplatform.org/regional-report-food-security-and-nutrition-west-africa-and-sahel-2024
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: "The dataset aggregates March 2024 Cadre Harmonis\xE9 (CH) cycle data\
    \ from FSIN and CILSS partners, classifying populations across five food insecurity\
    \ phases based on standardized vulnerability assessments. Population counts are\
    \ disaggregated by country, geographical area, and analysis period to quantify\
    \ food security impacts driven primarily by drought and agricultural stress in\
    \ West Africa and the Sahel."
  sources:
  - id: source_1
    license: null
    name: Food Security Information Network (FSIN)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Permanent Interstate Committee for Drought Control in the Sahel (CILSS)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/regional-report-on-food-security-and-nutrition-in-west-africa-and-the-sahel-2024
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population in food insecurity phases (3-5) due to drought and food
      crisis in West Africa and Sahel
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
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data from the Regional Report on Food Security and Nutrition in West
    Africa and the Sahel 2024.
  download_url: https://data.humdata.org/dataset/160b1bb3-450d-413e-8a83-2dda2486a951/resource/94d8ef18-b802-448e-9c92-afa6245cb36b/download/cilss-master.xlsx
  format: null
  id: resource_94d8ef18
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FSIN-CILSS_RRSAN.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-fsin_regionalreportnutritionwe_2014
spatial:
  bbox: null
  centroid: null
  countries:
  - CPV
  - BEN
  - BFA
  - CIV
  - GMB
  - GHA
  - GIN
  - GNB
  - LBR
  - MLI
  - MRT
  - NER
  - SEN
  - SLE
  - TGO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2014-01-01'
temporal_resolution: null
title: Regional Report on Food Security and Nutrition in West Africa and the Sahel
  2024
version: null
vulnerability: null
---
