---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNFPA Indonesia
    url: https://data.humdata.org/dataset/building-damaged-west-sulawesi-earthquake
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNFPA Indonesia (inactive)
  url: https://data.humdata.org/dataset/building-damaged-west-sulawesi-earthquake
creator:
  affiliation: null
  email: null
  name: UNFPA Indonesia (inactive)
  url: https://data.humdata.org/dataset/building-damaged-west-sulawesi-earthquake
dataset_id: rdls_el-idn_unfpaidn_buildingdamagedwestsulawe_20210122
description: 'Building Damaged West Sulawesi Earthquake. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/building-damaged-west-sulawesi-earthquake]'
details: null
exposure:
- asset_type:
    description: Building stock inventory with damage classification from the West
      Sulawesi earthquake
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC0-1.0
lineage:
  description: Building damage data collected through direct field observation and
    anecdotal reports by UNFPA Indonesia following the West Sulawesi earthquake event,
    compiled into a spatial geodataset (shapefile) documenting damaged infrastructure
    locations and damage status.
  sources:
  - id: source_1
    license: null
    name: UNFPA Indonesia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/building-damaged-west-sulawesi-earthquake
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from the West Sulawesi earthquake
      event
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Indonesia - Building Damaged West Sulawesi Earthquake (Shapefile)
  download_url: https://drive.google.com/file/d/1I5ZVeth3bBSQo41TrgIHtOSz0Lvg_BPd/view?usp=drive_web
  format: null
  id: resource_e7e6c993
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: infras.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-idn_unfpaidn_buildingdamagedwestsulawe_20210122
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-01-22'
temporal_resolution: null
title: Indonesia - Building Damaged West Sulawesi Earthquake
version: null
vulnerability: null
---
