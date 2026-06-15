---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNOSAT
    url: https://data.humdata.org/dataset/cox-s-bazar-refugee-settlement-roads-and-footpaths
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/cox-s-bazar-refugee-settlement-roads-and-footpaths
creator:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/cox-s-bazar-refugee-settlement-roads-and-footpaths
dataset_id: rdls_exp-bgd_reach_coxsbazarrefugeesettlemen_20171026
description: 'Satellite and UAV imagery derived roads and footpaths of Rohingya refugee
  settlements in Cox''s Bazar District, Bangladesh. Based on best available imagery
  acquired in October 2017.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cox-s-bazar-refugee-settlement-roads-and-footpaths]'
details: This is a rapid analysis which has not yet been validated in the field. It
  is important to consider the characteristics of the source imagery used in the analyses
  when interpreting results. Users with specific questions or concerns should contact
  reach.mapping@impact-initiatives.org to seek clarification.
exposure:
- asset_type:
    description: Road and footpath network in Rohingya refugee settlement with geometry
      and classification by type
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
  description: Road and footpath network was extracted through manual digitization
    of satellite imagery (October 2017) and UAV imagery by REACH/UNOSAT analysts.
    Multiple imagery sources were compared to identify and classify transportation
    infrastructure within the Kutupalong refugee settlement. The resulting vector
    dataset contains linear features classified by type (roads vs. footpaths) with
    source attribution.
  sources:
  - id: source_1
    license: null
    name: REACH Initiative
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: UNOSAT
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cox-s-bazar-refugee-settlement-roads-and-footpaths
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
  description: Zipped shapefile of Kutupalong Expansion Site road and footpath centerlines,
    digitized from a combination of UAV imagery from 1 October 2017 and satellite
    imagery from 26 October 2017.
  download_url: https://data.humdata.org/dataset/7aafa9b3-b51d-4edd-a1ed-3dcf8b66970f/resource/504b85b5-eacf-4e19-9829-fb8e180a293e/download/reach_bgd_kutupalong_roads_footpaths_v1.zip
  format: null
  id: resource_504b85b5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reach_bgd_kutupalong_roads_footpaths_v1.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bgd_reach_coxsbazarrefugeesettlemen_20171026
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-10-26'
temporal_resolution: null
title: Bangladesh - Cox's Bazar Refugee Settlement Roads and Footpaths
version: null
vulnerability: null
---
