---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop Unconstrained Individual Countries
    url: https://data.humdata.org/dataset/global-subnational-population-humanitarian
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: United Nations World Population Prospects
    url: https://data.humdata.org/dataset/global-subnational-population-humanitarian
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Global Edge-Matched Subnational Boundaries - Humanitarian
    url: https://data.humdata.org/dataset/global-subnational-population-humanitarian
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FieldMaps
  url: https://data.humdata.org/dataset/global-subnational-population-humanitarian
creator:
  affiliation: null
  email: null
  name: FieldMaps
  url: https://data.humdata.org/dataset/global-subnational-population-humanitarian
dataset_id: rdls_exp-fieldmaps_globalsubnationalpopulati_20250729
description: 'Original site: https://fieldmaps.io/data/population Population statistics
  using data from WorldPop Unconstrained Individual Countries to create a complete
  global coverage population raster. Results are aggregated to humanitarian edge-matched
  boundaries , adjusted so that ADM0 totals match those of the 2024 projections in
  the United Nations World Population Prospects .. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/global-subnational-population-humanitarian]'
details: null
exposure:
- asset_type:
    description: Subnational population counts aggregated to humanitarian administrative
      boundaries, adjusted to UN World Population Prospects 2024 projections
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
  description: WorldPop gridded population raster data was aggregated to humanitarian
    edge-matched subnational administrative boundaries (ADM0-ADM4) and calibrated
    using UN World Population Prospects 2024 projections to ensure consistency with
    official national population estimates.
  sources:
  - id: source_1
    license: null
    name: WorldPop Unconstrained Individual Countries
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: United Nations World Population Prospects
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: Global Edge-Matched Subnational Boundaries - Humanitarian
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/global-subnational-population-humanitarian
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
  description: Global Subnational Population - Humanitarian (Excel)
  download_url: https://data.fieldmaps.io/population/humanitarian/intl/worldpop/adm4_population.xlsx
  format: null
  id: resource_1556653b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: adm4_population.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Subnational Population - Humanitarian (ZIP archive)
  download_url: https://data.fieldmaps.io/population/humanitarian/intl/worldpop/adm4_population.csv.zip
  format: null
  id: resource_378f983a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: adm4_population.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Subnational Population - Humanitarian (Excel)
  download_url: https://data.fieldmaps.io/population/humanitarian/intl/worldpop/adm3_population.xlsx
  format: null
  id: resource_5740e9cf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: adm3_population.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Subnational Population - Humanitarian (ZIP archive)
  download_url: https://data.fieldmaps.io/population/humanitarian/intl/worldpop/adm3_population.csv.zip
  format: null
  id: resource_23f84759
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: adm3_population.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Subnational Population - Humanitarian (Excel)
  download_url: https://data.fieldmaps.io/population/humanitarian/intl/worldpop/adm2_population.xlsx
  format: null
  id: resource_2b8e8e50
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: adm2_population.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Subnational Population - Humanitarian (ZIP archive)
  download_url: https://data.fieldmaps.io/population/humanitarian/intl/worldpop/adm2_population.csv.zip
  format: null
  id: resource_daa82fe2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: adm2_population.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Subnational Population - Humanitarian (Excel)
  download_url: https://data.fieldmaps.io/population/humanitarian/intl/worldpop/adm1_population.xlsx
  format: null
  id: resource_60d9cd20
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: adm1_population.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Subnational Population - Humanitarian (ZIP archive)
  download_url: https://data.fieldmaps.io/population/humanitarian/intl/worldpop/adm1_population.csv.zip
  format: null
  id: resource_928b88f4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: adm1_population.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Subnational Population - Humanitarian (Excel)
  download_url: https://data.fieldmaps.io/population/humanitarian/intl/worldpop/adm0_population.xlsx
  format: null
  id: resource_e68cb9f3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: adm0_population.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Subnational Population - Humanitarian (ZIP archive)
  download_url: https://data.fieldmaps.io/population/humanitarian/intl/worldpop/adm0_population.csv.zip
  format: null
  id: resource_8467c9e3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: adm0_population.csv
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-fieldmaps_globalsubnationalpopulati_20250729
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-07-29'
temporal_resolution: null
title: Global Subnational Population - Humanitarian
version: null
vulnerability: null
---
