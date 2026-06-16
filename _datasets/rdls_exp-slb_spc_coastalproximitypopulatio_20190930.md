---
attributions:
- entity:
    affiliation: null
    email: null
    name: Pacific Community Statistics for Development Division (SDD)
    url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-solomon-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-solomon-
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-solomon-
dataset_id: rdls_exp-slb_spc_coastalproximitypopulatio_20190930
description: 'Spatial datasets utilized to conduct the spatial analysis and additional
  information from the research article: Coastal proximity of populations in 22 Pacific
  Island Countries and Territories. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
  https://sdd.spc.int/mapping-coastal Access this dataset from the Pacific Data Hub.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-solomon-]'
details: null
exposure:
- asset_type:
    description: Census-based population counts in enumeration areas with coastal
      proximity analysis at 1km, 5km, and 10km buffer zones
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
  description: Population counts from Solomon Islands census data were spatially aggregated
    by enumeration area and intersected with coastal buffer zones (1km, 5km, 10km)
    to quantify populations at varying distances from the coast. A 1km gridded population
    raster was derived from these enumeration area-level counts to support spatial
    analysis of coastal population exposure.
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
- href: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-solomon-
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
    Territories - Dataset - Solomon Islands (SLB EA boundaries)
  download_url: https://pacificdata.org/data/dataset/14645f67-bd3f-4b72-9918-4f0dc8e88dee/resource/30d713a3-32bd-4315-8274-40e4b18289f3/download/eaid_4326_totpop.geojson
  format: null
  id: resource_23cab2c3
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB EA boundaries
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Solomon Islands (SLB 1km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/14645f67-bd3f-4b72-9918-4f0dc8e88dee/resource/72398e19-a752-4380-8797-7b63fc0b35a5/download/slb1kmbuff_4326.geojson
  format: null
  id: resource_2c35fb4a
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB 1km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Solomon Islands (SLB 5km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/14645f67-bd3f-4b72-9918-4f0dc8e88dee/resource/2e115edc-d439-4dbf-b614-689430f5dd78/download/slb5kmbuff_4326.geojson
  format: null
  id: resource_65a3cc48
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB 5km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Solomon Islands (SLB 10km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/14645f67-bd3f-4b72-9918-4f0dc8e88dee/resource/97fb1dea-4281-4b21-8481-a24c06e29967/download/slb10kmbuff_4326.geojson
  format: null
  id: resource_811473d8
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB 10km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This spatial 1km resolution grid contains population data generated
    from 2009 Solomon Islands PHC. For more information about this dataset please
    check on https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
    https://sdd.spc.int/mapping-coastal
  download_url: https://pacificdata.org/data/dataset/14645f67-bd3f-4b72-9918-4f0dc8e88dee/resource/ceaf2f36-0f1d-4f12-bb92-30ab74ecc427/download/rmgps_popgrid.zip
  format: zipped tif
  id: resource_e7132a1d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SLB PopGrid
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-slb_spc_coastalproximitypopulatio_20190930
spatial:
  bbox: null
  centroid: null
  countries:
  - SLB
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
  - Dataset - Solomon Islands
version: null
vulnerability: null
---
