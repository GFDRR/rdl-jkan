---
attributions:
- entity:
    affiliation: null
    email: null
    name: Palau Bureau of Budget & Planning
    url: https://data.humdata.org/dataset/pdh-palau_population_grid_2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: SPC Statistics for Development Division (SDD)
    url: https://data.humdata.org/dataset/pdh-palau_population_grid_2020
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-palau_population_grid_2020
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-palau_population_grid_2020
dataset_id: rdls_exp-plw_spc_palaupopulationgrid2020_20200424
description: 'Population Raster Palau 2020 Data Input: Household locations from 2015
  Household listing and population at Enumeration Area level extracted from 2015 Population
  and Housing Census conducted by Palau''s Bureau of Budget & Planning Year Population
  Growth Rate of 0.6 % has been applied to update population up to 2020 Household
  locations vector layer transformed into a 100m resolution raster. Access this dataset
  from the Pacific Data Hub. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-palau_population_grid_2020]'
details: null
exposure:
- asset_type:
    description: Gridded population distribution at 100m resolution derived from 2015
      census enumeration areas with 0.6% annual growth applied to 2020
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
  description: Household locations from the 2015 Palau Population and Housing Census
    were transformed into a vector layer and rasterized to 100m resolution. Population
    counts at enumeration area level were distributed across the raster grid. A 0.6%
    annual population growth rate was applied to project the 2015 census baseline
    to 2020.
  sources:
  - id: source_1
    license: null
    name: Palau Bureau of Budget & Planning
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: SPC Statistics for Development Division (SDD)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pdh-palau_population_grid_2020
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
  description: 'Data Input: Household locations from 2015 Household listing and population
    at Enumeration Area level extracted from 2015 Population and Housing Census conducted
    by Palau''s Bureau of Budget & Planning Year Population Growth Rate of 0.6 % has
    been applied to update population up to 2020'
  download_url: https://pacificdata.org/data/dataset/b3c609bf-10a7-47ce-9dfd-5eda86770bd4/resource/7de46192-6b1f-4604-95c4-92887d787234/download/plw_rastpop2020rps_100m.tif
  format: null
  id: resource_bc503b41
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PLW_PopGrid_2020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Palau_Population_Grid_2020 (Text)
  download_url: https://pacificdata.org/data/dataset/b3c609bf-10a7-47ce-9dfd-5eda86770bd4/resource/c93f3767-9aa8-4321-936e-f04dd2130895/download/plw_rastpop2020rps_100m.txt
  format: null
  id: resource_4ae1c31a
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PLW_PopGrid_2020_README
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Palau_Population_Grid_2020 (Static maps of the Palau Population Grid
    2020)
  download_url: https://pacificdata.org/data/dataset/b3c609bf-10a7-47ce-9dfd-5eda86770bd4/resource/a2c3844e-c1be-41d7-bcce-7b4ce421c3be/download/plw_pg_maps.zip
  format: zip
  id: resource_1201549a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PLW_PopGrid_2020_Atlas
- access_url: https://tiles.arcgis.com/tiles/OAxZXfmfGWlgx9kD/arcgis/rest/services/PLW_PPG_MS/MapServer
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Palau_Population_Grid_2020 (PLW_PopGrid_2020_Web Mapping Service)
  download_url: null
  format: null
  id: resource_57ef5a8e
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PLW_PopGrid_2020_Web Mapping Service
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-plw_spc_palaupopulationgrid2020_20200424
spatial:
  bbox: null
  centroid: null
  countries:
  - PLW
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-04-24'
temporal_resolution: null
title: Palau_Population_Grid_2020
version: null
vulnerability: null
---
