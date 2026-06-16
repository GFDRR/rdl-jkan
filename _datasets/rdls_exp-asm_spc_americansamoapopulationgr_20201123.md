---
attributions:
- entity:
    affiliation: null
    email: null
    name: Facebook High-Resolution Population Density Maps
    url: https://data.humdata.org/dataset/pdh-american_samoa_population_grid_2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: 2011 Census Population Counts (American Samoa)
    url: https://data.humdata.org/dataset/pdh-american_samoa_population_grid_2020
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-american_samoa_population_grid_2020
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-american_samoa_population_grid_2020
dataset_id: rdls_exp-asm_spc_americansamoapopulationgr_20201123
description: 'Population Raster American Samoa 2020 Data Input: Settlement footprint
  from Facebook''s High-Resolution Population Density Maps (https://data.humdata.org/dataset/american-samoa-high-resolution-population-density-maps-demographic-estimates)
  Population allocated proportionally using 2011 census population counts at enumeration
  area level. Year Population Growth Rate of 0.23% has been applied to update population
  up to 2020 Access this dataset from the Pacific Data Hub. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/pdh-american_samoa_population_grid_2020]'
details: null
exposure:
- asset_type:
    description: Gridded population distribution for American Samoa in 2020, derived
      from settlement footprints and census data with growth rate adjustment
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
  description: Settlement footprints from Facebook's high-resolution population density
    maps were intersected with 2011 census population counts at enumeration area level
    and allocated proportionally across grid cells. A 0.23% annual population growth
    rate was applied to project the 2011 baseline to 2020, producing a gridded population
    raster for disaster risk assessment.
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
    name: 2011 Census Population Counts (American Samoa)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pdh-american_samoa_population_grid_2020
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
  description: 'Population Raster American Samoa 2020 Data Input: Settlement footprint
    from Facebook''s High-Resolution Population Density Maps (https://data.humdata.org/dataset/american-samoa-high-resolution-population-density-maps-demographic-estimates)
    Population allocated proportionally using 2011 census population counts at enumeration
    area level. Year Population Growth Rate of 0.23% has been applied to update population
    up to 2020 The human settlement footprint with census population allocated has
    been converted into a 100 m resolution raster. This is a demo version, SDD is
    still evaluating the methodology but given the COVID outbreak the dataset has
    been early released.'
  download_url: https://pacificdata.org/data/dataset/88eb6392-c134-4736-b204-6de34a775166/resource/f03ee67f-8d8a-4cb6-a05b-f0f09b898577/download/asm_pop_grid_2020.tif
  format: null
  id: resource_91eba695
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ASM_Pop_Grid_2020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: American Samoa - American_Samoa_Population_Grid_2020
  download_url: https://pacificdata.org/data/dataset/88eb6392-c134-4736-b204-6de34a775166/resource/63081e26-bc81-44d4-b8a6-6c3c1df9a41f/download/asm_pop_grid_2020_readme.txt
  format: null
  id: resource_d1c72acf
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ASM_Pop_Grid_2020_README
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: American Samoa - American_Samoa_Population_Grid_2020 (Static maps of
    the American Samoa Population Grid 2020)
  download_url: https://pacificdata.org/data/dataset/88eb6392-c134-4736-b204-6de34a775166/resource/d231b639-8259-427f-8ae4-d7705dafba9c/download/asm_popgrid_2020_atlas.zip
  format: zipped jpeg
  id: resource_dfa5bca9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ASM_Pop_Grid_ATLAS
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-asm_spc_americansamoapopulationgr_20201123
spatial:
  bbox: null
  centroid: null
  countries:
  - ASM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-23'
temporal_resolution: null
title: American Samoa - American_Samoa_Population_Grid_2020
version: null
vulnerability: null
---
