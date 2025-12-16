---
contact_point:
  email: null
  id: attribution_contact_point_1765382033249
  name: Claudia Vitolo
  url: https://confluence.ecmwf.int/display/CEMS/User+Guide+for++Fire+danger+indices+historical+data+from+the+Copernicus+Emergency+Management+Service
creator:
  email: null
  id: attribution_creator_1765381906809
  name: ECMWF
  url: https://confluence.ecmwf.int
dataset_id: rdls_hzd-cems_fire
description: This data set provides complete historical reconstruction of meteorological
  conditions favorable to the start, spread and sustainability of fires. The fire
  danger metrics provided are part of a vast dataset produced by the Copernicus Emergency
  Management Service for the European Forest Fire Information System (EFFIS). The
  European Forest Fire Information System incorporates the fire danger indices for
  three different models developed in Canada, United States and Australia. In this
  dataset the fire danger indices are calculated using weather forecast from historical
  simulations provided by ECMWF ERA5 reanalysis, which combines model data and a vast
  set of quality controlled observations into a globally complete and consistent dataset,
  which is regarded as a good proxy for observed atmospheric conditions.
details: The selected data records in this data set are regularly extended with time
  as ERA5 forcing data become available. This dataset is produced by ECMWF in its
  role of the computational centre for fire danger forecast of the CEMS, on behalf
  of the Joint Research Centre which is the managing entity of the service.
exposure: []
extra_attributions: []
hazard:
  calculation_method: inferred
  disaster_identifiers: ''
  hazard_analysis_type: deterministic
  hazard_type: ''
  intensity: ''
  occurrence_range: ''
  processes: ''
  seasonality: ''
license: CC-BY-4.0
loss: null
project:
  name: CEMS-Fire
  url: https://confluence.ecmwf.int/display/CEMS/CEMS-Fire
publisher:
  email: null
  id: attribution_publisher_1765381868073
  name: Copernicus
  url: https://ewds.climate.copernicus.eu/
purpose: null
resources:
- coordinate_system: null
  description: "Download service from Copernicus. All variables included at the global\
    \ scale for ERA-5 reanalysis at 0.25\xC2\xB0. Requires to create an account to\
    \ access the data."
  download_url: https://ewds.climate.copernicus.eu/datasets/cems-fire-historical-v1?tab=download
  format: GRIB (grib)
  id: resource_QJtYmU44
  media_type: null
  spatial_resolution: 25000
  temporal:
    duration: null
    end: null
    start: null
    temporal_resolution: P1D
  title: CEMS Early Warning Data Store
- coordinate_system: EPSG:4326
  description: CEMS data as GEE image collection
  download_url: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:fire-monitoring-analysis/CEMS-FIRE-DAILY
  format: Cloud Optimized GeoTIFF (cog)
  id: resource_JmsMrBaL
  media_type: null
  spatial_resolution: 25000
  temporal:
    duration: null
    end: null
    start: null
    temporal_resolution: P1D
  title: CEMS Fire Danger Indices (GEE community catalog)
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-cems_fire
spatial:
  countries:
  - GLO
  scale: global
title: CEMS Global Fire Danger Indices
version: '1.0'
vulnerability: null
---
