---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Universidad de Cantabria, Instituto de Hidraulica Ambiental de la Universidad
    de Cantabria 'IHCantabria'
  url: www.ihcantabria.com
creator:
  affiliation: null
  email: null
  name: Universidad de Cantabria, Instituto de Hidraulica Ambiental de la Universidad
    de Cantabria 'IHCantabria'
  url: www.ihcantabria.com
dataset_id: rdls_hzd-coclico_driverstwl
description: 'Drivers of Total Water Level indicate the (statistical) contributions
  of the individual components (drivers) in the Total Water Level (TWL). These are
  the mean significant wave height (Hs), the 99th percentile of storm surge level,
  the 50th percentile of Sea Level Rise and the mean tidal range. Spatial coverage:
  European coastline at coastal target points. Sources: Observational records, climate
  models, Copernicus Marine Servic, Sea Level Rise projections Common usage: Flood
  hazard mapping, storm surge modelling, coastal resilience planning. More info about
  the dataset: User Handbook. Variants in the source dataset - time: 2010.0, 2100.0
  - Time slice applied to the data. Either present-day (2010) or future state representing
  medium (2030 till 2050) and long term (2050 till 2100) outlook; scenarios: SSP245
  (SSP2-4.5), SSP585 (SSP5-8.5), none - Climate scenarios based on IPCC''s Shared
  Socioeconomic Pathways (SSPs). High-end (if applicable) refers to P83 of SSP5-8.5,
  taking into account low-confidence processes. Other scenarios use the P50; variable:
  hs (Wave height (Hs)), ssl (Storm surge level (SSL)), slr (Sea level rise (SLR)),
  tidal_range (Tidal range) - Different variables included in the dataset; lon: -18.168,
  34.5992 - longitude; lat: 27.6298, 71.1914 - latitude. [Source: This metadata record
  was automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: 'Drivers of Total Water Level indicate the (statistical) contributions
    of the individual components (drivers) in the Total Water Level (TWL). These are
    the mean significant wave height (Hs), the 99th percentile of storm surge level,
    the 50th percentile of Sea Level Rise and the mean tidal range. Spatial coverage:
    European coastline at coastal target points. Sources: Observational records, climate
    models, Copernicus Marine Servic, Sea Level Rise projections Common usage: Flood
    hazard mapping, storm surge modelling, coastal resilience planning. More info
    about the dataset: User Handbook'
  sources:
  - id: source_1
    license: null
    name: Universidad de Cantabria, Instituto de Hidraulica Ambiental de la Universidad
      de Cantabria 'IHCantabria'
    risk_data_type:
    - hazard
    type: dataset
    url: www.ihcantabria.com
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Universidad de Cantabria, Instituto de Hidraulica Ambiental de la Universidad
    de Cantabria 'IHCantabria'
  url: www.ihcantabria.com
purpose: null
referenced_by: []
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/drivers_twl/collection.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Collection metadata for this dataset, hosted as part of
    the CoCliCo catalog. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_collection
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Collection: CoCliCo - Drivers of Total Water Level [drivers_twl]'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The root of the EU Coastal Target Points - Coastal marine climatologies
    zarr dataset on public Google Cloud Storage.
  download_url: https://storage.googleapis.com/coclico-data-public/coclico/drivers_twl.zarr
  format: null
  id: resource_data
  media_type: application/vnd.zarr
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EU Coastal Target Points - Coastal marine climatologies zarr root
- access_url: https://storage.googleapis.com/download/storage/v1/b/coclico-data-public/o/coclico%2Fassets%2Fthumbnails%2Fdrivers_twl.png?alt=media
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Drivers of Total Water Level
  download_url: null
  format: null
  id: resource_thumbnail
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Thumbnail
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-coclico_driverstwl
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: CoCliCo - Drivers of Total Water Level
version: null
vulnerability: null
---
