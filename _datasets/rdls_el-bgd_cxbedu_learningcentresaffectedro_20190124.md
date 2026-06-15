---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Cox's Bazar Education Sector
  url: https://data.humdata.org/dataset/learning-centres-affected-by-road-closures
creator:
  affiliation: null
  email: null
  name: Cox's Bazar Education Sector
  url: https://data.humdata.org/dataset/learning-centres-affected-by-road-closures
dataset_id: rdls_el-bgd_cxbedu_learningcentresaffectedro_20190124
description: 'Pcodes and information on road closures and affected learning centres.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/learning-centres-affected-by-road-closures]'
details: THIS DOCUMENT IS DEVELOPED FOR SITE MANAGEMENT SECTOR, COX'S BAZAR STAKEHOLDERS
  ONLY. IT PRESENTS INFRASTRUCTURE INCIDENTS IN THE KUTUPALONG-BALUKHALI EXPANSION
  (KBE) AND TEKNAF EXPANSION SITES USING INFORMATION AVAILABLE AT THE TIME OF PUBLICATION.
  DATA IS COLLECTED DAILY THROUGH DIRECT SURV EYS AND REPORTED INFORMATION. IT HAS
  BEEN CREATED W ITH THE HIGHEST DEGREE OF ACCURACY POSSIBLE HOWEV ER, SM SECTOR CANNOT
  BE HELD RESPONSIBLE FOR ANY DAM AGES DU E TO ERRORS OR OMISSIONS IN THIS PRODUCT.
  DEPICTION OF BOUNDARIES IS NOT AUTHORATIVE.
exposure:
- asset_type:
    description: Road network infrastructure with closure status and affected segments
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Learning centres (schools) with spatial location and accessibility
      status
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Direct observational data collected by Cox's Bazar Education Sector
    documenting road closures and their impact on learning centre accessibility. Data
    compiled from field observations and anecdotal reports to identify which schools
    are affected by road disruptions, enabling assessment of indirect disaster impacts
    on education service delivery.
  sources:
  - id: source_1
    license: null
    name: Cox's Bazar Education Sector
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/learning-centres-affected-by-road-closures
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Road closures affecting accessibility and service disruption
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Learning centres affected by road closures and reduced accessibility
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
        modelling: observed
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bangladesh - Learning Centres Affected by Road Closures (LC affected
    by Road_20190214.xlsx)
  download_url: https://data.humdata.org/dataset/29e43086-15a8-40ce-8c9d-24298e62db3c/resource/dd18a448-6942-4e47-99aa-306463d0fd19/download/lc-affected-by-road_20190214.xlsx
  format: null
  id: resource_dd18a448
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LC affected by Road_20190214.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bangladesh - Learning Centres Affected by Road Closures (image of affected
    roads)
  download_url: https://data.humdata.org/dataset/29e43086-15a8-40ce-8c9d-24298e62db3c/resource/da4098c5-3143-49bc-9918-807c93efcf16/download/190124-road_adb_packages_ktp1.pdf
  format: null
  id: resource_da4098c5
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 190124 Road_ADB_Packages_KTP(1).pdf
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-bgd_cxbedu_learningcentresaffectedro_20190124
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-01-24'
temporal_resolution: null
title: Bangladesh - Learning Centres Affected by Road Closures
version: null
vulnerability: null
---
