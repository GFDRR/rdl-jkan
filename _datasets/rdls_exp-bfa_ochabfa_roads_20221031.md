---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/burkina-faso-roads
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Government of Burkina Faso maps
    url: https://data.humdata.org/dataset/burkina-faso-roads
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Burkina Faso
  url: https://data.humdata.org/dataset/burkina-faso-roads
creator:
  affiliation: null
  email: null
  name: OCHA Burkina Faso
  url: https://data.humdata.org/dataset/burkina-faso-roads
dataset_id: rdls_exp-bfa_ochabfa_roads_20221031
description: 'This dataset contains roads data from OpenStreetMap for which attributes
  and classifications have been enhanced using maps from the government. The new classifications
  added based on the government maps are using the attribute igb_class: Igb_class
  = 2: for Major roads Igb_class = 1 or 3 : for Minor roads. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/burkina-faso-roads]'
details: This data was processed and validated by the humanitarian partners.
exposure:
- asset_type:
    description: Road network with geometric and classification attributes including
      surface type, condition, and administrative classification
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
      quantity_kind: length
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Road network geometry and attributes were sourced from OpenStreetMap
    contributors and enhanced with government-derived road classifications (igb_class)
    to distinguish major and minor roads. The dataset provides a comprehensive infrastructure
    inventory with attributes including surface type, condition, number of lanes,
    and administrative classification for disaster risk assessment purposes.
  sources:
  - id: source_1
    license: null
    name: OpenStreetMap contributors
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Government of Burkina Faso maps
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/burkina-faso-roads
  rel: source
loss:
  losses: []
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
  description: 'Burkina Faso: Roads (Burkina Faso road data)'
  download_url: https://data.humdata.org/dataset/cb636d8a-2e44-46e3-8f7e-c97d76de70d5/resource/d579b75d-58d5-46f9-af8f-4211b49cac5f/download/bfa_trs_roads_osm-hdx.zip
  format: null
  id: resource_d579b75d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bfa_roads.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bfa_ochabfa_roads_20221031
spatial:
  bbox: null
  centroid: null
  countries:
  - BFA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-10-31'
temporal_resolution: null
title: 'Burkina Faso: Roads'
version: null
vulnerability: null
---
