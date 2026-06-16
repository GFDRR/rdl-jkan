---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Partners
    url: https://data.humdata.org/dataset/2021-floods-and-drought-hazards
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/2021-floods-and-drought-hazards
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/2021-floods-and-drought-hazards
dataset_id: rdls_hzd-sdn_ochasdn_floodsdroughthazards_20211101
description: 'This file contains the the Sudan admin2 level localities with data of
  the climate hazards in the country (flood affected by year and overall risk/severity
  and drought risk/severity.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/2021-floods-and-drought-hazards]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: es_flood_hzd
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: es_flood
    occurrence_range: null
    seasonality: null
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: es_drought_hzd
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: es_drought
    occurrence_range: null
    seasonality: null
license: ODbL-1.0/
lineage:
  description: Hazard data compiled from direct observational records and anecdotal
    reports by humanitarian partners operating in Sudan. Flood and drought hazard
    information was aggregated at admin2 (locality) level with annual flood occurrence
    records and categorical risk/severity classifications for both hazards.
  sources:
  - id: source_1
    license: null
    name: Humanitarian Partners
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/2021-floods-and-drought-hazards
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file contains the the Sudan admin2 level localities with data
    of the climate hazards in the country (flood affected by year and overall risk/severity
    and drought risk/severity.
  download_url: https://data.humdata.org/dataset/7ba71e5d-2b95-4ba1-987a-fc99c3fc032a/resource/cf9e9077-7500-4cb3-892f-07a8d34ea20a/download/hazards_climate_2021.xlsx
  format: null
  id: resource_cf9e9077
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Hazards_Climate_2021.xlsx
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sdn_ochasdn_floodsdroughthazards_20211101
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-11-01'
temporal_resolution: null
title: Sudan - Floods and Drought Hazards
version: null
vulnerability: null
---
