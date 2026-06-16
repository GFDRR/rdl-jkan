---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook High-Resolution Population Density Maps
    url: https://data.humdata.org/dataset/pdh-guam_population_grid_2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: 2011 Census Population Counts
    url: https://data.humdata.org/dataset/pdh-guam_population_grid_2020
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-guam_population_grid_2020
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-guam_population_grid_2020
dataset_id: rdls_exp-gum_spc_guampopulationgrid2020_20211202
description: 'Population Raster Guam 2020 Data Input: Settlement footprint from Facebook''s
  High-Resolution Population Density Maps https://data.humdata.org/dataset/guam-high-resolution-population-density-maps-demographic-estimates
  Population allocated proportionally using 2011 census population counts at district
  level. Year Population Growth Rate of 1.64% has been applied to update population
  up to 2020 The human settlement footprint with census population allocated has been
  converted into a 100 m resolution raster. Access this dataset from the Pacific Data
  Hub. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-guam_population_grid_2020]'
details: null
exposure:
- asset_type:
    description: Gridded population distribution at 100m resolution derived from settlement
      footprints and census data
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
  description: Settlement footprints from Facebook's High-Resolution Population Density
    Maps were combined with 2011 census population counts at district level, with
    a 1.64% annual growth rate applied to project population to 2020, then converted
    to a 100m resolution raster grid.
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
    name: 2011 Census Population Counts
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pdh-guam_population_grid_2020
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
  description: Guam_Population_Grid_2020 (Population raster Guam 2020)
  download_url: https://pacificdata.org/data/dataset/e8f78001-4585-49e7-b4d7-04e549fa9e35/resource/bd2407f0-1813-49c4-8977-507009a7769c/download/gum_pop_grid_2020.tif
  format: null
  id: resource_54de7db7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GUM_Pop_Grid_2020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Guam_Population_Grid_2020 (Text)
  download_url: https://pacificdata.org/data/dataset/e8f78001-4585-49e7-b4d7-04e549fa9e35/resource/03710e76-2ef4-4167-8600-2f94b692a105/download/gum_pop_grid_2020_readme.txt
  format: null
  id: resource_d5ffaa68
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GUM_Pop_Grid_2020_README
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-gum_spc_guampopulationgrid2020_20211202
spatial:
  bbox: null
  centroid: null
  countries:
  - GUM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-12-02'
temporal_resolution: null
title: Guam_Population_Grid_2020
version: null
vulnerability: null
---
