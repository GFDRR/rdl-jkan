---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Imagery and Mapping Agency (NIMA) Vmap L1
    url: https://data.humdata.org/dataset/liberia-roads
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: United Nations Mission in Liberia (UNMIL) Irish team survey
    url: https://data.humdata.org/dataset/liberia-roads
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Landsat imagery
    url: https://data.humdata.org/dataset/liberia-roads
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: United Nations Development Programme (UNDP)
    url: https://data.humdata.org/dataset/liberia-roads
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Liberia (inactive)
  url: https://data.humdata.org/dataset/liberia-roads
creator:
  affiliation: null
  email: null
  name: OCHA Liberia (inactive)
  url: https://data.humdata.org/dataset/liberia-roads
dataset_id: rdls_exp-lbr_ochalb_roads_20070101
description: 'Road network of Liberia This dataset represents roads network within
  Liberia. These data are part of the government-derived shape files provided by UNDP
  in January 2007. This dataset was derived from NIMA Vmap L1 and a survey by UNMIL
  Irish team, then anaylised and updated by UNMIL GIS Unit using Landsat imagery.
  New roads were digitized from the Landsat and non-existing roads were deleted from
  the source datasets. The attributes include category, names, description and assessment
  roads planning.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/liberia-roads]'
details: '**Most Recent Changes:** (2014-11-19) metadata updated **Languages:** EN'
exposure:
- asset_type:
    description: Road network infrastructure with classification by category and condition
      assessment
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
license: CC-BY-4.0
lineage:
  description: Road network data derived from NIMA Vmap L1 baseline and UNMIL field
    survey, then analyzed and updated by UNMIL GIS Unit using Landsat satellite imagery
    to digitize new roads and remove non-existent features, resulting in a validated
    national road infrastructure inventory with category and condition attributes.
  sources:
  - id: source_1
    license: null
    name: National Imagery and Mapping Agency (NIMA) Vmap L1
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: United Nations Mission in Liberia (UNMIL) Irish team survey
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: Landsat imagery
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_4
    license: null
    name: United Nations Development Programme (UNDP)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/liberia-roads
  rel: source
loss: null
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
  description: Liberia - Roads (Shapefile)
  download_url: https://data.humdata.org/dataset/ee904c54-a82a-41f5-9bef-bbd6dc72c874/resource/1e66f5de-4c31-42d0-a7f6-52efac59dcaa/download/lbr_rdsl_unmil.zip
  format: null
  id: resource_1e66f5de
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lbr_rdsl_unmil.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-lbr_ochalb_roads_20070101
spatial:
  bbox: null
  centroid: null
  countries:
  - LBR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2007-01-01'
temporal_resolution: null
title: Liberia - Roads
version: null
vulnerability: null
---
