---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Bank
    url: https://data.humdata.org/dataset/cap-haitien-haiti-flood-event-extents
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Sustainable Organic Integrated Livelihoods
  url: https://data.humdata.org/dataset/cap-haitien-haiti-flood-event-extents
creator:
  affiliation: null
  email: null
  name: Sustainable Organic Integrated Livelihoods
  url: https://data.humdata.org/dataset/cap-haitien-haiti-flood-event-extents
dataset_id: rdls_hzd-hti_soil_capfloodeventextents_20220201
description: "This file contains shapefiles depicting the extent of 5-, 25-, and 100-\
  \ year flood recurrence events. This data was created by the World Bank and should\
  \ be credited as follows: Plan d'\xC9laboration propre bas\xE9e sur les donn\xE9\
  es de la Banque Mondiale: Inondation de R\xE9currence (5 ans / 25 ans / 100 ans).\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cap-haitien-haiti-flood-event-extents]"
details: "This data was created by the World Bank and should be credited as follows:\
  \ Plan d'\xC9laboration propre bas\xE9e sur les donn\xE9es de la Banque Mondiale:\
  \ Inondation de R\xE9currence (5 ans / 25 ans / 100 ans)"
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 3
    events:
    - calculation_method: simulated
      description: Probabilistic fluvial flood hazard model depicting inundation extents
        at 5-, 25-, and 100-year return periods for Cap Haitien
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_5yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.2
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: Probabilistic fluvial flood hazard model depicting inundation extents
        at 5-, 25-, and 100-year return periods for Cap Haitien
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_25yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.04
          probability: null
          return_period: 25
    - calculation_method: simulated
      description: Probabilistic fluvial flood hazard model depicting inundation extents
        at 5-, 25-, and 100-year return periods for Cap Haitien
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_100yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.01
          probability: null
          return_period: 100
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: The World Bank developed probabilistic flood hazard models for Cap
    Haitien, generating inundation extent shapefiles at 5-, 25-, and 100-year return
    periods. The dataset represents simulated flood extents derived from hydrological
    and hydraulic modeling, with elevation data included to characterize flood depths
    across the urban area.
  sources:
  - id: source_1
    license: null
    name: World Bank
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cap-haitien-haiti-flood-event-extents
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
  description: Flood extent data in Cap Haitien, Haiti for 5 year/ 25 year/ and 100
    year flood recurrence events.
  download_url: https://data.humdata.org/dataset/5deac5b5-f135-45e2-9994-bf555c38ed22/resource/0cb67376-e085-4862-b3c8-86f0dded3cd3/download/world_bank_flood_extents_caphaitien.zip
  format: null
  id: resource_0cb67376
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: World_Bank_Flood_Extents_CapHaitien.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-hti_soil_capfloodeventextents_20220201
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-02-01'
temporal_resolution: null
title: Haiti - Cap Haitien Flood Event Extents
version: null
vulnerability: null
---
