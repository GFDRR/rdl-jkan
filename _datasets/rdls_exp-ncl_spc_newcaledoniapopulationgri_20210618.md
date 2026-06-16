---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook High-Resolution Population Density Maps
    url: https://data.humdata.org/dataset/pdh-new_caledonia_population_grid_2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: New Caledonia 2011 Census
    url: https://data.humdata.org/dataset/pdh-new_caledonia_population_grid_2020
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-new_caledonia_population_grid_2020
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-new_caledonia_population_grid_2020
dataset_id: rdls_exp-ncl_spc_newcaledoniapopulationgri_20210618
description: 'Population Raster New Caledonia 2020 Data Input: Settlement footprint
  from Facebook''s High-Resolution Population Density Maps https://data.humdata.org/dataset/new-caledonia-high-resolution-population-density-maps-demographic-estimates
  Population allocated proportionally using 2011 census population counts at enumeration
  area (districts de recensement) level. Year Population Growth Rate of 0.2% (0.001957)
  has been applied to update population up to 2020 The human settlement footprint
  with census population allocated has been converted into a 100 m resolution raster.
  Access this dataset from the Pacific Data Hub. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/pdh-new_caledonia_population_grid_2020]'
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
license: CC-BY-4.0
lineage:
  description: Settlement footprints from Facebook's High-Resolution Population Density
    Maps were intersected with 2011 census population counts at enumeration area level.
    Population was proportionally allocated to settlement areas and updated to 2020
    using a 0.2% annual growth rate. The resulting population distribution was converted
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
    name: New Caledonia 2011 Census
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pdh-new_caledonia_population_grid_2020
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
  description: 'Population Raster New Caledonia 2020 Data Input: Settlement footprint
    from Facebook''s High-Resolution Population Density Maps https://data.humdata.org/dataset/new-caledonia-high-resolution-population-density-maps-demographic-estimates
    Population allocated proportionally using 2011 census population counts at enumeration
    area (districts de recensement) level. Year Population Growth Rate of 0.2% (0.001957)
    has been applied to update population up to 2020 The human settlement footprint
    with census population allocated has been converted into a 100 m resolution raster.
    This is a demo version, SDD is still evaluating the methodology but given the
    COVID outbreak the dataset has been early released.'
  download_url: https://pacificdata.org/data/dataset/f3abaff7-0d7d-48f2-bd3b-265d1b1e5732/resource/65791c86-0bc3-4de3-8cdf-6cd3518ca733/download/ncl_pop_grid_2020.tif
  format: null
  id: resource_7bfbf06b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NCL_Pop_Grid_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Caledonia - New_Caledonia_Population_Grid_2020
  download_url: https://pacificdata.org/data/dataset/f3abaff7-0d7d-48f2-bd3b-265d1b1e5732/resource/133abe4f-5fd9-4eaa-952f-8e0993a855f5/download/ncl_pop_grid_2020_readme.txt
  format: null
  id: resource_04da6384
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NCL_Pop_Grid_2020_README.txt
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Caledonia - New_Caledonia_Population_Grid_2020 (Static maps of
    the New Caledonia Population Grid 2020)
  download_url: https://pacificdata.org/data/dataset/f3abaff7-0d7d-48f2-bd3b-265d1b1e5732/resource/5f5986f0-ac2e-42d5-ba0b-32d5fbf2b115/download/ncl_pop_grid_atlas.zip
  format: zipped jpeg
  id: resource_f42a15b3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NCL_Pop_Grid_ATLAS
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ncl_spc_newcaledoniapopulationgri_20210618
spatial:
  bbox: null
  centroid: null
  countries:
  - NCL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-06-18'
temporal_resolution: null
title: New Caledonia - New_Caledonia_Population_Grid_2020
version: null
vulnerability: null
---
