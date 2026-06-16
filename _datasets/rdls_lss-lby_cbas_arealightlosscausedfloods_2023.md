---
attributions:
- entity:
    affiliation: null
    email: null
    name: SDGSAT-1
    url: https://data.humdata.org/dataset/the-area-of-light-loss-caused-by-floods-in-libya
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Research Center of Big Data for Sustainable Development Goals
    (CBAS)
  url: https://data.humdata.org/dataset/the-area-of-light-loss-caused-by-floods-in-libya
creator:
  affiliation: null
  email: null
  name: International Research Center of Big Data for Sustainable Development Goals
    (CBAS)
  url: https://data.humdata.org/dataset/the-area-of-light-loss-caused-by-floods-in-libya
dataset_id: rdls_lss-lby_cbas_arealightlosscausedfloods_2023
description: 'This dataset is showing the Gap Light Index (GLI) difference in Albayda
  and Derna. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/the-area-of-light-loss-caused-by-floods-in-libya]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Gap Light Index (GLI) difference calculated from SDGSAT-1 satellite
    nighttime light imagery comparing pre- and post-flood conditions in Albayda and
    Derna, Libya to quantify infrastructure disruption and damage extent.
  sources:
  - id: source_1
    license: null
    name: SDGSAT-1
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/the-area-of-light-loss-caused-by-floods-in-libya
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Nighttime light loss as proxy for infrastructure damage and disruption
      from flooding in Albayda and Derna
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
        metric: loss
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
  description: The area of light lost by flood in Derna and Albayda, Libya, is based
    on SDGSAT-1 GLI images taken on 17 September 2023 and 4 April 2023.
  download_url: https://data.humdata.org/dataset/10f2f308-cb0b-47d7-9223-f420dcca5c5e/resource/c92c9ec5-014d-47e8-b3c3-d44bc441d69a/download/libyaflood_light_lossorup.gdb.zip
  format: Geodatabase
  id: resource_c92c9ec5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LibyaFlood_Light_lossOrUp.gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-lby_cbas_arealightlosscausedfloods_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - LBY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-09-17'
  start: '2023-04-04'
temporal_resolution: null
title: 'Libya: The Area of Light Loss Caused by Floods'
version: null
vulnerability: null
---
