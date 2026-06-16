---
attributions:
- entity:
    affiliation: null
    email: null
    name: Pacific Community Statistics for Development Division (SDD)
    url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-western-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-western-
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-western-
dataset_id: rdls_exp-wsm_spc_coastalproximitypopulatio_20190930
description: 'Spatial datasets utilized to conduct the spatial analysis and additional
  information from the research article: Coastal proximity of populations in 22 Pacific
  Island Countries and Territories. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
  https://sdd.spc.int/mapping-coastal Access this dataset from the Pacific Data Hub.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-western-]'
details: null
exposure:
- asset_type:
    description: Gridded population distribution at 1km resolution derived from 2011
      census data
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Population distribution data from the 2011 census was gridded at 1km
    resolution and intersected with coastal buffer zones (1km, 5km, 10km) to quantify
    populations in coastal proximity. Enumeration area boundaries and household counts
    were spatially linked to coastal buffer geometries to enable analysis of coastal
    population exposure.
  sources:
  - id: source_1
    license: null
    name: Pacific Community Statistics for Development Division (SDD)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-western-
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Western Samoa (WSM EA boundaries)
  download_url: https://pacificdata.org/data/dataset/0e332c97-9c6c-4c02-87d1-0b84aaaf35b5/resource/b4efc7e0-f2f4-47ee-828f-f592668dd048/download/samoa_eas_4326.geojson
  format: null
  id: resource_10d64cfb
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM EA boundaries
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Western Samoa (WSM 1km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/0e332c97-9c6c-4c02-87d1-0b84aaaf35b5/resource/7992c220-a8af-4325-aaa6-b5d889a396b2/download/wsm1kmbuff_4326.geojson
  format: null
  id: resource_647896bd
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM 1km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Western Samoa (WSM 5km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/0e332c97-9c6c-4c02-87d1-0b84aaaf35b5/resource/17dbeff1-640c-4840-a7b2-d21bf075a808/download/wsm5kmbuff_4326.geojson
  format: null
  id: resource_9d7214d9
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM 5km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Western Samoa (WSM 10km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/0e332c97-9c6c-4c02-87d1-0b84aaaf35b5/resource/5cb323ea-03ca-40ee-90c2-286b9cbf7cce/download/wsm10kmbuff_4326.geojson
  format: null
  id: resource_76cfd5e0
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM 10km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Western Samoa (WSM 2011 PopGrid)
  download_url: https://pacificdata.org/data/dataset/0e332c97-9c6c-4c02-87d1-0b84aaaf35b5/resource/32dc79f1-3e36-4a7e-a1ac-487b1582dfd6/download/gpsgrid.zip
  format: zipped tif
  id: resource_3cb698f3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WSM 2011 PopGrid
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-wsm_spc_coastalproximitypopulatio_20190930
spatial:
  bbox: null
  centroid: null
  countries:
  - WSM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-09-30'
temporal_resolution: null
title: Coastal proximity of populations in 22 Pacific Island Countries and Territories
  - Dataset - Western Samoa
version: null
vulnerability: null
---
