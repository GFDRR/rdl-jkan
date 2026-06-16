---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: British Red Cross Maps Team
  url: https://data.humdata.org/dataset/cyclone-pam-poverty-priority-index
creator:
  affiliation: null
  email: null
  name: British Red Cross Maps Team
  url: https://data.humdata.org/dataset/cyclone-pam-poverty-priority-index
dataset_id: rdls_el-vut_brc_cyclonepampovertypriority_20150319
description: 'An index to target those in poverty and affected by cyclone Pam. Methodology
  and contact available on tab in spreadsheet.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/cyclone-pam-poverty-priority-index]'
details: null
exposure:
- asset_type:
    description: Population in poverty classified by vulnerability to cyclone Pam
      impacts
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
      quantity_kind: index
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: The dataset combines poverty indicators with cyclone Pam impact data
    to create a priority index for targeting vulnerable populations. The methodology
    integrates socioeconomic vulnerability with cyclone exposure to identify populations
    requiring humanitarian assistance.
  sources:
  - id: source_1
    license: null
    name: British Red Cross Maps Team
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cyclone-pam-poverty-priority-index
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by cyclone Pam prioritized by poverty status
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Vanuatu - Cyclone Pam Poverty Priority Index (Excel)
  download_url: https://data.humdata.org/dataset/c05f1fe5-f49b-40d7-89bf-da0d3ddbf25d/resource/337cfeaa-11e6-4c2a-aad6-20d839ebc1eb/download/cyclone-pan-priority-index.xlsx
  format: null
  id: resource_337cfeaa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cyclone_pan_priority_index.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Vanuatu - Cyclone Pam Poverty Priority Index (Shapefile)
  download_url: https://data.humdata.org/dataset/c05f1fe5-f49b-40d7-89bf-da0d3ddbf25d/resource/66f63888-e830-42ca-99c1-043bb5ee0caf/download/cyclone-pam-area-council-priority-index.zip
  format: null
  id: resource_66f63888
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cyclone_pam_area_council_priority_index.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-vut_brc_cyclonepampovertypriority_20150319
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-03-19'
temporal_resolution: null
title: Vanuatu - Cyclone Pam Poverty Priority Index
version: null
vulnerability: null
---
