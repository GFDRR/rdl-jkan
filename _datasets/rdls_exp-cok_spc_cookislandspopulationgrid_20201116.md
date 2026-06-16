---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook High-Resolution Population Density Maps
    url: https://data.humdata.org/dataset/pdh-cook_islands_population_grid_2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: 2011 Census Population Counts (Cook Islands)
    url: https://data.humdata.org/dataset/pdh-cook_islands_population_grid_2020
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-cook_islands_population_grid_2020
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-cook_islands_population_grid_2020
dataset_id: rdls_exp-cok_spc_cookislandspopulationgrid_20201116
description: 'Population Raster Cook Islands 2020 Data Input: Settlement footprint
  from Facebook''s High-Resolution Population Density Maps https://data.humdata.org/dataset/cook-islands-high-resolution-population-density-maps-demographic-estimates
  Population allocated proportionally using 2011 census population counts at enumeration
  area level. Year Population Growth Rate of 0.23% has been applied to update population
  up to 2020 The human settlement footprint with census population allocated has been
  converted into a 100 m resolution raster. Access this dataset from the Pacific Data
  Hub. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-cook_islands_population_grid_2020]'
details: null
exposure:
- asset_type:
    description: Gridded population distribution at 100m resolution derived from settlement
      footprints and 2011 census enumeration area data, updated to 2020 using growth
      rates
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
  description: Settlement footprints from Facebook's High-Resolution Population Density
    Maps were intersected with 2011 census population counts at enumeration area level
    and population was allocated proportionally. A 0.23% annual growth rate was applied
    to update the 2011 baseline to 2020. The resulting population distribution was
    converted to a 100m resolution raster grid.
  sources:
  - id: source_1
    license: null
    name: Facebook High-Resolution Population Density Maps
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: 2011 Census Population Counts (Cook Islands)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pdh-cook_islands_population_grid_2020
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
  description: Cook Islands - Cook_Islands_Population_Grid_2020 (Population Raster
    Cook Islands 2020)
  download_url: https://pacificdata.org/data/dataset/313e08cc-aa54-48d1-b40b-e2d165c6f1c8/resource/663491e3-4e32-4e62-a4b4-c4f71660103e/download/cok_pop_grid_2020.tif
  format: null
  id: resource_c964ba3d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: COK_Pop_Grid_2020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cook Islands - Cook_Islands_Population_Grid_2020
  download_url: https://pacificdata.org/data/dataset/313e08cc-aa54-48d1-b40b-e2d165c6f1c8/resource/339aceaa-9f47-4a72-b199-718aa76c2ed1/download/cok_pop_grid_2020_readme.txt
  format: null
  id: resource_29da29fa
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: COK_Pop_Grid_2020_README
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cook Islands - Cook_Islands_Population_Grid_2020 (Static maps of the
    Cook Islands Population Grid 2020)
  download_url: https://pacificdata.org/data/dataset/313e08cc-aa54-48d1-b40b-e2d165c6f1c8/resource/55a3930c-5800-4dea-bbe1-9452bfc915b6/download/cok_popgrid_2020_atlas.zip
  format: zipped jpeg
  id: resource_e1ead111
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: COK_PopGrid_2020_ATLAS
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-cok_spc_cookislandspopulationgrid_20201116
spatial:
  bbox: null
  centroid: null
  countries:
  - COK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-16'
temporal_resolution: null
title: Cook Islands - Cook_Islands_Population_Grid_2020
version: null
vulnerability: null
---
