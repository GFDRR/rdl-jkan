---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: U.S. Census Bureau
  url: https://data.humdata.org/dataset/dominica-gridded-population-dataset
creator:
  affiliation: null
  email: null
  name: U.S. Census Bureau
  url: https://data.humdata.org/dataset/dominica-gridded-population-dataset
dataset_id: rdls_exp-dma_uscensus_dominicagriddedpopulation
description: 'The geodatabase contains gridded population rasters which can be used
  to identify the population for a custom area.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/dominica-gridded-population-dataset]'
details: null
exposure:
- asset_type:
    description: Gridded population distribution derived from census data disaggregated
      using dasymetric mapping and random forest weighting
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
  description: Subnational census population data were disaggregated into a gridded
    raster using a random forest model trained on human and physical geography datasets
    as inputs, with dasymetric mapping applied to create a spatially explicit population
    distribution dataset for Dominica.
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
- href: https://data.humdata.org/dataset/dominica-gridded-population-dataset
  rel: source
loss: null
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
    hectare, and people per pixel, for the census year (2011) and 2021.
  download_url: https://data.humdata.org/dataset/0a3aff95-e37e-48f4-844b-a105cd2325e8/resource/10a8a289-0fb4-4f39-8909-eb1369c03d96/download/demobasedominica.gdb.zip
  format: Geodatabase
  id: resource_10a8a289
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DemobaseDominica.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-dma_uscensus_dominicagriddedpopulation
spatial:
  bbox: null
  centroid: null
  countries:
  - DMA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Dominica Gridded Population Dataset
version: null
vulnerability: null
---
