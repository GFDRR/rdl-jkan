---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: U.S. Census Bureau
  url: https://data.humdata.org/dataset/the-bahamas-gridded-population-dataset
creator:
  affiliation: null
  email: null
  name: U.S. Census Bureau
  url: https://data.humdata.org/dataset/the-bahamas-gridded-population-dataset
dataset_id: rdls_exp-bhs_uscensus_bahamasgriddedpopulationd
description: 'The geodatabase contains gridded population rasters which can be used
  to identify the population for a custom area.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/the-bahamas-gridded-population-dataset]'
details: null
exposure:
- asset_type:
    description: Gridded population distribution derived from disaggregated subnational
      census data using dasymetric mapping
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
  description: Subnational census data for The Bahamas were disaggregated using a
    random forest model trained on human and physical geography datasets to generate
    a population weighting layer, which was then applied via dasymetric mapping to
    create gridded population rasters at fine spatial resolution.
  sources:
  - id: source_1
    license: null
    name: U.S. Census Bureau
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/the-bahamas-gridded-population-dataset
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
  description: The geodatabase contains six rasters representing density, people per
    hectare, and people per pixel, for the census year (2010) and 2021.
  download_url: https://data.humdata.org/dataset/561608bb-e211-4bca-8794-c82f1cd841eb/resource/1a8d65c0-e229-48d9-9468-8af53592b60c/download/demobasethebahamas.gdb.zip
  format: Geodatabase
  id: resource_1a8d65c0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DemobaseTheBahamas.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bhs_uscensus_bahamasgriddedpopulationd
spatial:
  bbox: null
  centroid: null
  countries:
  - BHS
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: The Bahamas Gridded Population Dataset
version: null
vulnerability: null
---
