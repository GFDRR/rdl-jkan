---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNOSAT
    url: https://data.humdata.org/dataset/flood-extent-for-kilifi-garissa-and-tana-river
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Kenya Red Cross Society
  url: https://data.humdata.org/dataset/flood-extent-for-kilifi-garissa-and-tana-river
creator:
  affiliation: null
  email: null
  name: Kenya Red Cross Society
  url: https://data.humdata.org/dataset/flood-extent-for-kilifi-garissa-and-tana-river
dataset_id: rdls_hzd-ken_krcs_floodextentkilifigarissat_2018
description: 'This file contains flood hazard extent for Garissa, Kilifi and Tana
  River counties for the period 2018, 2019 and 2023. This data was obtained by merging
  flood extent from different sources among them UNOSAT. This data is in vector format..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/flood-extent-for-kilifi-garissa-and-tana-river]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Flood extent polygons were derived from satellite imagery (including
    UNOSAT products) for three Kenyan counties across multiple years (2018, 2019,
    2023). Multiple flood hazard layers from different sources were merged and integrated
    into a single vector dataset with confidence and validation fields to create a
    composite observed flood extent map.
  sources:
  - id: source_1
    license: null
    name: UNOSAT
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/flood-extent-for-kilifi-garissa-and-tana-river
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
  description: This file contains flood hazard extent for Garissa, Kilifi and Tana
    River counties for the period 2018, 2019 and 2023. This data was obtained by merging
    flood extent from different sources among them UNOSAT. This data is in vector
    format.
  download_url: https://data.humdata.org/dataset/43a7c291-1df5-43c9-afe0-ef99b5beac33/resource/c7181e17-c866-4f72-bd43-5ac9f1ef240b/download/floodextent01.zip
  format: null
  id: resource_c7181e17
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FloodExtent01.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ken_krcs_floodextentkilifigarissat_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2018-01-01'
temporal_resolution: null
title: Kenya - Flood extent for Kilifi, Garissa and Tana river
version: null
vulnerability: null
---
