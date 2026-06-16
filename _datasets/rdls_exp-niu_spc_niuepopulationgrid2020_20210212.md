---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian OpenStreetMap Team (HOT) Niue Building Footprint
    url: https://data.humdata.org/dataset/pdh-niue_population_grid_2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: 2011 Census Population Counts (Enumeration Area Level)
    url: https://data.humdata.org/dataset/pdh-niue_population_grid_2020
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-niue_population_grid_2020
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-niue_population_grid_2020
dataset_id: rdls_exp-niu_spc_niuepopulationgrid2020_20210212
description: 'Population Raster Niue 2020 Data Input: Household locations from Open
  Street Maps - HOSM Niue Building footprint. https://data.humdata.org/dataset/hotosm_niu_buildings
  Population allocated proportionally using 2011 census population counts at enumeration
  area level. Year Population Growth Rate of 0.76% has been applied to update population
  up to 2020 The human settlement footprint with census population allocated has been
  converted into a 100 m resolution raster. Access this dataset from the Pacific Data
  Hub. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-niue_population_grid_2020]'
details: null
exposure:
- asset_type:
    description: Gridded population distribution at 100m resolution derived from census
      enumeration areas and building footprints
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
license: CC-BY-4.0
lineage:
  description: Building footprints from HOT/OpenStreetMap were intersected with 2011
    census population counts at enumeration area level. Population was allocated proportionally
    to building locations, then grown to 2020 using a 0.76% annual growth rate. The
    resulting human settlement footprint with allocated population was converted to
    a 100m resolution raster.
  sources:
  - id: source_1
    license: null
    name: Humanitarian OpenStreetMap Team (HOT) Niue Building Footprint
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: 2011 Census Population Counts (Enumeration Area Level)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pdh-niue_population_grid_2020
  rel: source
loss: null
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
  description: Niue_Population_Grid_2020 (Population Raster Niue 2020)
  download_url: https://pacificdata.org/data/dataset/f0ae6b16-af3d-40d4-b8f2-a04b2744f9e5/resource/85b5e76d-0f83-4cde-899b-0c2df1a8137f/download/niu_pop_grid_2020.tif.tif
  format: null
  id: resource_b1eccc6b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NIU_Pop_Grid_2020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue_Population_Grid_2020 (Text)
  download_url: https://pacificdata.org/data/dataset/f0ae6b16-af3d-40d4-b8f2-a04b2744f9e5/resource/d60bc776-25f7-47f8-86ee-85268dece672/download/niu_pop_grid_2020_readme.txt
  format: null
  id: resource_8104b89b
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NIU_Pop_Grid_2020_README
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue_Population_Grid_2020 (Static maps of the Niue Population Grid
    2020)
  download_url: https://pacificdata.org/data/dataset/f0ae6b16-af3d-40d4-b8f2-a04b2744f9e5/resource/0dc1eba9-75a0-4c78-862b-cb00c1709ef0/download/niue.jpg
  format: JPEG
  id: resource_15ad2009
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NIU_PopGrid_2020_ATLAS
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-niu_spc_niuepopulationgrid2020_20210212
spatial:
  bbox: null
  centroid: null
  countries:
  - NIU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-02-12'
temporal_resolution: null
title: Niue_Population_Grid_2020
version: null
vulnerability: null
---
