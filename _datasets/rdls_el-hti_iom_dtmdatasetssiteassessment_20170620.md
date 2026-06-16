---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Haiti
    url: https://data.humdata.org/dataset/haiti-iom-dtm-datasets-site-assessment-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/haiti-iom-dtm-datasets-site-assessment-data
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/haiti-iom-dtm-datasets-site-assessment-data
dataset_id: rdls_el-hti_iom_dtmdatasetssiteassessment_20170620
description: 'HAITI - IOM DTM DATASET Round 25. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/haiti-iom-dtm-datasets-site-assessment-data]'
details: null
exposure:
- asset_type:
    description: Displaced and affected populations assessed at displacement sites
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
- asset_type:
    description: Shelter facilities and site infrastructure at displacement locations
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
  description: IOM DTM Round 25 collected direct observational data through site assessments
    of displacement locations across Haiti, documenting affected populations and shelter
    conditions resulting from gang violence and insecurity-driven displacement events.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Haiti
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/haiti-iom-dtm-datasets-site-assessment-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displaced population from gang violence and insecurity events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Affected shelter sites and displacement locations
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: HAITI - IOM DTM DATASETS - SITE ASSESSMENT DATA (Excel)
  download_url: https://data.humdata.org/dataset/6064c16a-8bf4-4e94-bbab-3aafda4a4ef2/resource/3a4df419-b521-4b38-a129-e2e6cd85892d/download/dtm_master_list_round25.xlsx
  format: null
  id: resource_3a4df419
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM_Master_List_Round25.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-hti_iom_dtmdatasetssiteassessment_20170620
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-06-20'
temporal_resolution: null
title: HAITI - IOM DTM DATASETS - SITE ASSESSMENT DATA
version: null
vulnerability: null
---
