---
attributions:
- entity:
    affiliation: null
    email: null
    name: Open Street Map
    url: https://data.humdata.org/dataset/papua-new-guinea-roads
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Papua New Guinea National Mapping Bureau (NMB)
    url: https://data.humdata.org/dataset/papua-new-guinea-roads
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/papua-new-guinea-roads
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/papua-new-guinea-roads
dataset_id: rdls_exp-png_ocharoap_roads_20150224
description: 'These spatial datasets provide the delimitation of primary, secondary
  and tertiary roads and tracks in Papua New Guinea. The OSM dataset includes attribute
  information includes OSM id and road names in English where known and comprehensive
  track network for the mainland. This dataset can be complemented by the National
  Mapping Bureau (NMB) (2000) dataset. The NMB dataset includes comprehensive road
  network in both mainland and non-mainland districts and road surface attributes..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/papua-new-guinea-roads]'
details: '**Languages:** EN'
exposure:
- asset_type:
    description: Road network including primary, secondary, tertiary roads and tracks
      with surface attributes and geometry
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
  description: 'Road network data compiled from two sources: Open Street Map (OSM)
    providing mainland road geometry and attributes, and Papua New Guinea National
    Mapping Bureau (NMB) 2000 dataset providing comprehensive coverage including non-mainland
    districts and road surface characteristics. The datasets are integrated to create
    a complete national road infrastructure inventory.'
  sources:
  - id: source_1
    license: null
    name: Open Street Map
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Papua New Guinea National Mapping Bureau (NMB)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/papua-new-guinea-roads
  rel: source
loss:
  losses: []
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
  description: Papua New Guinea - Roads (Shapefile)
  download_url: https://data.humdata.org/dataset/81cb8373-0105-4c4d-b2aa-a67ec3c1415b/resource/639ae014-e057-4b1a-bd25-b9e67f0ec4d0/download/png_rdsl_2014_osm.zip
  format: null
  id: resource_639ae014
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_rdsl_2014_osm.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Papua New Guinea - Roads (Shapefile)
  download_url: https://data.humdata.org/dataset/81cb8373-0105-4c4d-b2aa-a67ec3c1415b/resource/c35212ad-8975-4ed0-9cf7-d99704f77b51/download/png_rdsl_2000_nmb.zip
  format: null
  id: resource_c35212ad
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_rdsl_2000_nmb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-png_ocharoap_roads_20150224
spatial:
  bbox: null
  centroid: null
  countries:
  - PNG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-02-24'
temporal_resolution: null
title: Papua New Guinea - Roads
version: null
vulnerability: null
---
