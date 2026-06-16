---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Food Programme (WFP)
    url: https://data.humdata.org/dataset/south-sudan-road-network_hdx
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap (OSM)
    url: https://data.humdata.org/dataset/south-sudan-road-network_hdx
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA South Sudan
  url: https://data.humdata.org/dataset/south-sudan-road-network_hdx
creator:
  affiliation: null
  email: null
  name: OCHA South Sudan
  url: https://data.humdata.org/dataset/south-sudan-road-network_hdx
dataset_id: rdls_exp-ssd_ochassd_roadnetwork_20220215
description: 'The data coming from MapAction South Sudan Pilot Integrated Humanitarian
  Data Package. The data coming from a compilation of WFP and OSM datasets. The South
  Sudan pilot Integrated Humanitarian Data Package (IHDP) is a package of cleaned,
  checked and enriched data. For more information, please visit: https://maps.mapaction.org/dataset/south-sudan-pilot-integrated-humanitarian-data-package.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/south-sudan-road-network_hdx]'
details: null
exposure:
- asset_type:
    description: Road network with geometry, classification by type, surface, status,
      and capacity
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
  description: Road network data compiled from WFP and OpenStreetMap sources, cleaned
    and enriched as part of the South Sudan Integrated Humanitarian Data Package.
    The dataset contains road geometry with attributes including surface type, status,
    capacity, and speed characteristics for logistics and infrastructure planning.
  sources:
  - id: source_1
    license: null
    name: World Food Programme (WFP)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: OpenStreetMap (OSM)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/south-sudan-road-network_hdx
  rel: source
loss: null
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
  description: The data coming from a compilation of WFP and OSM datasets that has
    been cleaned, checked and enriched.
  download_url: https://data.humdata.org/dataset/b2fabd55-947b-416d-87d5-8178d96d72c8/resource/f67431a1-355c-4980-8f85-36214d8fe762/download/ssd_road_network.zip
  format: null
  id: resource_f67431a1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SSD_road_network.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ssd_ochassd_roadnetwork_20220215
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-02-15'
temporal_resolution: null
title: 'South Sudan: Road Network'
version: null
vulnerability: null
---
