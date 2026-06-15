---
attributions:
- entity:
    affiliation: null
    email: null
    name: Pacific Community Statistics for Development Division (SDD)
    url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-tonga
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-tonga
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-tonga
dataset_id: rdls_exp-ton_spc_coastalproximitypopulatio_20190930
description: 'Spatial datasets utilized to conduct the spatial analysis and additional
  information from the research article: Coastal proximity of populations in 22 Pacific
  Island Countries and Territories. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
  https://sdd.spc.int/mapping-coastal Access this dataset from the Pacific Data Hub.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-tonga]'
details: null
exposure:
- asset_type:
    description: Gridded population distribution at 1km resolution derived from 2016
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
  description: Census population data from Tonga's 2016 census was spatially gridded
    at 1km resolution and intersected with coastal buffer zones (1km inland from shoreline)
    to quantify populations in coastal proximity. Administrative block boundaries
    and household counts were used to distribute population across spatial units for
    coastal vulnerability assessment.
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
- href: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-tonga
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
    Territories - Dataset - Tonga (TON Block Boundaries)
  download_url: https://pacificdata.org/data/dataset/b6eee133-8dbe-4bdd-b237-282c64845212/resource/287ed261-1f01-487b-83d4-9f52cc961a2d/download/blk_ton_4326.geojson
  format: null
  id: resource_91a794e5
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TON Block Boundaries
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Tonga (TON 1km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/b6eee133-8dbe-4bdd-b237-282c64845212/resource/201d8dcf-21b7-462c-b827-7fcc6d6f235f/download/ton1kmbuff_4326.geojson
  format: null
  id: resource_6f6e1fb3
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TON 1km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This spatial 1km resolution grid contains population data generated
    from 2016 Tonga PHC. For more information about this dataset please check on https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
    https://sdd.spc.int/mapping-coastal
  download_url: https://pacificdata.org/data/dataset/b6eee133-8dbe-4bdd-b237-282c64845212/resource/591b8596-345b-4071-b2b7-21f4d5376ddc/download/gpspop2016.zip
  format: zipped tif
  id: resource_d5c1a9b9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TON 2016 PopGrid
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ton_spc_coastalproximitypopulatio_20190930
spatial:
  bbox: null
  centroid: null
  countries:
  - TON
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
  - Dataset - Tonga
version: null
vulnerability: null
---
