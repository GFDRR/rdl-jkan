---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus
    url: https://ewds.climate.copernicus.eu/
  id: attribution_publisher_1765381868073
  role: publisher
- entity:
    affiliation: null
    email: null
    name: ECMWF
    url: https://confluence.ecmwf.int
  id: attribution_creator_1765381906809
  role: creator
- entity:
    affiliation: null
    email: null
    name: Claudia Vitolo
    url: https://confluence.ecmwf.int/display/CEMS/User+Guide+for++Fire+danger+indices+historical+data+from+the+Copernicus+Emergency+Management+Service
  id: attribution_contact_point_1765382033249
  role: contact_point
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://ewds.climate.copernicus.eu/
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://ewds.climate.copernicus.eu/
dataset_id: rdls_hzd-cems_globalfiredangerindices
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
hazard:
  event_sets_by_hazard_type:
    wildfire:
    - analysis_type: deterministic
      calculation_method: inferred
      event_count: 1
      events:
      - calculation_method: inferred
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_kE9ObP1U
          intensity_measure: FWI:-
          process: wildfire
          trigger: null
          type: wildfire
        id: event_F7g3L26J
        occurrence:
          deterministic: null
          empirical:
            return_period: null
            temporal:
              central_year: null
              duration: null
              end: '2019-12-31'
              start: '1940-01-01'
          probabilistic: null
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_kE9ObP1U
        intensity_measure: FWI:-
        process: wildfire
        trigger: null
        type: wildfire
      id: event_set_GO2O8zSU
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project:
  name: CEMS-Fire
  url: https://confluence.ecmwf.int/display/CEMS/CEMS-Fire
publisher:
  affiliation: null
  email: null
  name: Copernicus
  url: https://ewds.climate.copernicus.eu/
purpose: null
referenced_by:
- author_names: null
  date_published: '2020-07-07'
  doi: https://doi.org/10.1038/s41597-020-0554-z
  id: reference_atEfDsRW
  name: ERA5-based global meteorological wildfire danger maps
  url: https://www.nature.com/articles/s41597-020-0554-z
resources:
- access_url: https://ewds.climate.copernicus.eu/datasets/cems-fire-historical-v1?tab=download
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Download service from Copernicus. All variables included at the global\
    \ scale for ERA-5 reanalysis at 0.25\xC2\xB0. Requires to create an account to\
    \ access the data."
  download_url: null
  format: GRIB
  id: resource_QJtYmU44
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 25000
  temporal: null
  temporal_resolution: P1D
  title: CEMS Early Warning Data Store
- access_url: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:fire-monitoring-analysis/CEMS-FIRE-DAILY
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: CEMS data as GEE image collection
  download_url: null
  format: Cloud Optimized GeoTIFF
  id: resource_JmsMrBaL
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 25000
  temporal: null
  temporal_resolution: P1D
  title: CEMS Fire Danger Indices (GEE community catalog)
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-cems_globalfiredangerindices
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: CEMS Global Fire Danger Indices
version: '1.0'
vulnerability: null
---
