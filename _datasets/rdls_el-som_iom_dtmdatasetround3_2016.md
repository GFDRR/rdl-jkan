---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/somalia-iom-dtm-dataset-round-3
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/somalia-iom-dtm-dataset-round-3
dataset_id: rdls_el-som_iom_dtmdatasetround3_2016
description: 'Round III of DTM captured information on variables about the population
  of concern, disaggregated at the settlement level in Somalia. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/somalia-iom-dtm-dataset-round-3]'
details: null
exposure:
- asset_type:
    description: Internally displaced persons, returnees, and baseline population
      disaggregated at settlement level in Somalia
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
license: CC-BY-4.0
lineage:
  description: IOM DTM Round 3 collected settlement-level registry data on displaced
    persons, returnees, and baseline populations in Somalia through direct field enumeration
    and community informant networks. Data was disaggregated by population group and
    geographic settlement to provide a snapshot of displacement and migration patterns
    in response to drought and conflict-related hazards.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-iom-dtm-dataset-round-3
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and returnee populations affected by
      drought and conflict-related displacement
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - IOM DTM Dataset - Round 3 (DTM Round 3 Dataset.xlsx)
  download_url: https://data.humdata.org/dataset/305c976b-6b41-4d0b-aee9-6bcbb46538dd/resource/b52ba891-4ef4-42d6-834e-36bfc795a347/download/dtm-round-3-dataset.xlsx
  format: null
  id: resource_b52ba891
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Round 3 Dataset.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-som_iom_dtmdatasetround3_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-12-31'
  start: '2016-10-01'
temporal_resolution: null
title: Somalia - IOM DTM Dataset - Round 3
version: null
vulnerability: null
---
