---
attributions:
- entity:
    affiliation: null
    email: null
    name: SPC Statistics for Development Division (SDD)
    url: https://data.humdata.org/dataset/pdh-nauru_population_grid_2020
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-nauru_population_grid_2020
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-nauru_population_grid_2020
dataset_id: rdls_exp-nru_spc_naurupopulationgrid2020_20200421
description: 'Population Raster Nauru 2020 Data Input: Household locations from 2019
  Population and Housing Census conducted using Survey Solutions CAPI (Computer Assisted
  Personal Interview). Year Population Growth Rate of 0.8% has been applied to update
  population up to 2020 Household locations vector layer has been transformed into
  a 100m resolution raster. Access this dataset from the Pacific Data Hub. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/pdh-nauru_population_grid_2020]'
details: null
exposure:
- asset_type:
    description: Gridded population distribution at 100m resolution derived from 2019
      census household locations with 0.8% growth rate applied to 2020
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
  description: Household locations from the 2019 Population and Housing Census (collected
    via CAPI survey) were transformed into a 100m resolution raster grid. A 0.8% population
    growth rate was applied to project the 2019 census data to 2020. The resulting
    gridded population dataset provides spatially explicit exposure information for
    Nauru at national scale.
  sources:
  - id: source_1
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
- href: https://data.humdata.org/dataset/pdh-nauru_population_grid_2020
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
  description: Population Raster Nauru 2020 Household locations vector layer transformed
    into a 100m resolution raster. This is a demo version, SDD is still evaluating
    the methodology but given the COVID outbreak the dataset has been early released.
  download_url: https://pacificdata.org/data/dataset/4d516c3f-e19c-40c0-9b00-5c434e578cc0/resource/4ae0314a-a5f4-46e0-ac06-718054bf69f6/download/nru_rastpop2020rps_100m.tif
  format: null
  id: resource_0e40ab45
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_PopGrid_2020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nauru_Population_Grid_2020 (Text)
  download_url: https://pacificdata.org/data/dataset/4d516c3f-e19c-40c0-9b00-5c434e578cc0/resource/d840c712-3bc7-4ee2-9573-38924b6cf429/download/nru_rastpop2020rps_100m.txt
  format: null
  id: resource_93ed3152
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_PopGrid_2020_README
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nauru_Population_Grid_2020 (Static map of the Nauru Population Grid
    2020)
  download_url: https://pacificdata.org/data/dataset/4d516c3f-e19c-40c0-9b00-5c434e578cc0/resource/da56c333-28ee-4ed0-b332-853a6f9e1e2f/download/nru_popgrid_2020_map.jpg
  format: JPEG
  id: resource_d1306737
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_PopGrid_2020_Map
- access_url: https://tiles.arcgis.com/tiles/OAxZXfmfGWlgx9kD/arcgis/rest/services/NRU_PPG_MS/MapServer
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nauru_Population_Grid_2020 (NRU_PopGrid_2020_Web Mapping Service)
  download_url: null
  format: null
  id: resource_4c4e8e76
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU_PopGrid_2020_Web Mapping Service
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nru_spc_naurupopulationgrid2020_20200421
spatial:
  bbox: null
  centroid: null
  countries:
  - NRU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-04-21'
temporal_resolution: null
title: Nauru_Population_Grid_2020
version: null
vulnerability: null
---
