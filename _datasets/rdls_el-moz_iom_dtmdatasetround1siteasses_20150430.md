---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) DTM
    url: https://data.humdata.org/dataset/iom-dtm-mozambique-datset-round-1
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/iom-dtm-mozambique-datset-round-1
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/iom-dtm-mozambique-datset-round-1
dataset_id: rdls_el-moz_iom_dtmdatasetround1siteasses_20150430
description: 'This data is about the site assessments conducted in Zambezia Province
  (April 2015). [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/iom-dtm-mozambique-datset-round-1]'
details: DTM Round I
exposure:
- asset_type:
    description: Internally displaced persons enumerated through site assessments
      in displacement sites
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM conducted direct observational site assessments in Zambezia
    Province in April 2015 to enumerate internally displaced persons and document
    displacement site characteristics. The data captures post-event displacement impacts
    from flooding through field-based enumeration and anecdotal reporting.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) DTM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/iom-dtm-mozambique-datset-round-1
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced population from flooding in Zambezia Province
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
        metric: displaced
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
  description: IOM DTM Mozambique Dataset Round 1 - Site assessment data (04_IOM DTM
    Mozambique_Dataset_Round 1 Report_20150424.xlsx)
  download_url: https://data.humdata.org/dataset/fb0e16af-f9bb-4aa2-b275-4801bcdf40a3/resource/3ae3f0fe-6fbc-4a51-8650-b142c9227c1f/download/04-iom-dtm-mozambique-dataset-round-1-report-20150424.xlsx
  format: null
  id: resource_3ae3f0fe
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 04_IOM DTM Mozambique_Dataset_Round 1 Report_20150424.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-moz_iom_dtmdatasetround1siteasses_20150430
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-04-30'
temporal_resolution: null
title: IOM DTM Mozambique Dataset Round 1 - Site assessment data
version: null
vulnerability: null
---
