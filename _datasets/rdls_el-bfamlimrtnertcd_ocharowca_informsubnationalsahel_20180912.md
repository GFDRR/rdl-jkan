---
attributions:
- entity:
    affiliation: null
    email: null
    name: Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/2016-sahel-inform
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/2016-sahel-inform
creator:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/2016-sahel-inform
dataset_id: rdls_el-bfamlimrtnertcd_ocharowca_informsubnationalsahel_20180912
description: 'The Index for Risk Management INFORM is a composite indicator developed
  by JRC as a tool for understanding the risk of humanitarian crisis and disasters..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/2016-sahel-inform]'
details: null
exposure:
- asset_type:
    description: Population exposed to humanitarian crisis and disaster risk in Sahel
      subnational areas
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
  description: INFORM aggregates approximately 50 indicators from multiple sources
    into a composite risk index across three dimensions (hazards, exposure, vulnerability)
    to measure humanitarian crisis and disaster risk at subnational level in the Sahel
    region. The index synthesizes data from various organizations to produce annual
    risk assessments for 2016-2018.
  sources:
  - id: source_1
    license: null
    name: Joint Research Centre (JRC)
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/2016-sahel-inform
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Humanitarian crisis risk combining hazard exposure and vulnerability
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
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: http://www.inform-index.org/InDepth
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Subnational Sahel (Data as of 30 September 2016)
  download_url: https://data.humdata.org/dataset/fe348e48-9c1f-4138-a368-b45a10e5fde7/resource/f3458c96-0c72-4401-9fa0-18b6c3f21143/download/inform_sahel-2016_v330_final-as300916.xlsx
  format: null
  id: resource_f3458c96
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM_SAHEL 2016_v330_Final (as300916).xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Subnational Sahel (Data as of 01 June 2017)
  download_url: https://data.humdata.org/dataset/fe348e48-9c1f-4138-a368-b45a10e5fde7/resource/646e8391-97d2-4f61-a17f-35478b0ffdea/download/inform_sahel-2017_v102.xlsx
  format: null
  id: resource_646e8391
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM_SAHEL 2017_v102.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Subnational Sahel (INFORM_SAHEL 2018_v100.xlsx)
  download_url: https://data.humdata.org/dataset/fe348e48-9c1f-4138-a368-b45a10e5fde7/resource/4781670c-444b-4ca7-b70d-07692d125750/download/inform_sahel-2018_v100.xlsx
  format: null
  id: resource_4781670c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM_SAHEL 2018_v100.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-bfamlimrtnertcd_ocharowca_informsubnationalsahel_20180912
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  - BFA
  - NER
  - TCD
  - MRT
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-09-12'
temporal_resolution: null
title: INFORM Subnational Sahel
version: null
vulnerability: null
---
