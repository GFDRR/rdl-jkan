---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/kenya-internally-displaced-people-due-to-drought
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/kenya-internally-displaced-people-due-to-drought
dataset_id: rdls_hl-ken_iom_internallydisplacedpeople_2022
description: 'IDPs due to drought in five counties in Kenya; Marsabit, Garissa, Isiolo,
  Samburu, Turkana. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/kenya-internally-displaced-people-due-to-drought]'
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
      id: hazard_1
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: drought
license: CC-BY-4.0
lineage:
  description: IOM conducted a registry-based survey to enumerate internally displaced
    persons in five drought-affected counties (Marsabit, Garissa, Isiolo, Samburu,
    Turkana) in Kenya, recording IDP estimates by county with source attribution and
    comments.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/kenya-internally-displaced-people-due-to-drought
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons due to drought in Marsabit, Garissa,
      Isiolo, Samburu, and Turkana counties
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya - Internally Displaced People due to Drought (HoA Drought Related
    Data - Kenya Drought Related IDPs.csv)
  download_url: https://data.humdata.org/dataset/549063dc-e76d-4c8d-b4bc-9b102ed20330/resource/b43ffad8-3684-4de0-bc51-9d15b111d4d2/download/hoa-drought-related-data-kenya-drought-related-idps.csv
  format: null
  id: resource_b43ffad8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HoA Drought Related Data - Kenya Drought Related IDPs.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-ken_iom_internallydisplacedpeople_2022
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
  end: '2023-04-30'
  start: '2022-10-31'
temporal_resolution: null
title: Kenya - Internally Displaced People due to Drought
version: null
vulnerability: null
---
