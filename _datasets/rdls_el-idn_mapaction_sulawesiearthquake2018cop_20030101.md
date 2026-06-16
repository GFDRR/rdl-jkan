---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus
    url: https://data.humdata.org/dataset/ma-sulawesi-earthquake-2018-copernicus-building-damage-classfcn
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: MapAction
  url: https://data.humdata.org/dataset/ma-sulawesi-earthquake-2018-copernicus-building-damage-classfcn
creator:
  affiliation: null
  email: null
  name: MapAction
  url: https://data.humdata.org/dataset/ma-sulawesi-earthquake-2018-copernicus-building-damage-classfcn
dataset_id: rdls_el-idn_mapaction_sulawesiearthquake2018cop_20030101
description: 'This point dataset aggregrates Copernicus building damage data derived
  from post-event satellite imagery into a single dataset. Within the areas analysed,
  individual buildings are classified as damage/destroyed/none/possibly damaged. Separate
  datasets show the footprint of the areas analysed, and a hex grid analysis of building
  counts.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ma-sulawesi-earthquake-2018-copernicus-building-damage-classfcn]'
details: null
exposure:
- asset_type:
    description: Individual building footprints classified by damage state from post-event
      satellite imagery
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
license: CC-BY-4.0
lineage:
  description: Copernicus derived building damage classifications from post-event
    satellite imagery of the 2018 Sulawesi earthquake. Individual buildings were classified
    into damage states and aggregated into point and hex grid summary formats to quantify
    direct structural impacts across the affected region.
  sources:
  - id: source_1
    license: null
    name: Copernicus
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ma-sulawesi-earthquake-2018-copernicus-building-damage-classfcn
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from 2018 Sulawesi earthquake derived
      from Copernicus satellite imagery
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Indonesia - Sulawesi Earthquake 2018, Copernicus Building Damage Classification
    (Sulawesi earthquake 2018 Copernicus building damage classification)
  download_url: https://maps.mapaction.org/dataset/0de28aa8-cd7f-41f9-87bb-0db0aad7c20d/resource/67a7fa66-a398-49f3-8f41-14d52815af03/download/sulaffdbldgpts1copernicusdamagedbuilding.zip
  format: null
  id: resource_d8b87b54
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sulawesi earthquake 2018 Copernicus building damage classification
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sulawesi earthquake 2018, hex grid summary of Copernicus damaged/destroyed
    buildings
  download_url: https://maps.mapaction.org/dataset/0de28aa8-cd7f-41f9-87bb-0db0aad7c20d/resource/c90f48a2-4632-4faa-bb0f-0baacda9f3b2/download/sulaffdbldgpys1copernicusdamageddestroyedhexgrid.zip
  format: null
  id: resource_d4b90253
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sulawesi earthquake 2018, hex grid summary of Copernicus damaged/destroyed
    buildings
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-idn_mapaction_sulawesiearthquake2018cop_20030101
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
  start: '2003-01-01'
temporal_resolution: null
title: Indonesia - Sulawesi Earthquake 2018, Copernicus Building Damage Classification
version: null
vulnerability: null
---
