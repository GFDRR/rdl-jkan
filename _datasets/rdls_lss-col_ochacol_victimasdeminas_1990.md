---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Direcci\xF3n para la Acci\xF3n Integral contra Minas Antipersonal (DAICMA)"
    url: https://data.humdata.org/dataset/victimas-de-minas
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/victimas-de-minas
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/victimas-de-minas
dataset_id: rdls_lss-col_ochacol_victimasdeminas_1990
description: "Seg\xFAn el Glosario Nacional de T\xE9rminos para la Acci\xF3n Integral\
  \ contra Minas Antipersonal, por 'mina antipersonal' se entiende toda mina concebida\
  \ para que explosione por la presencia, la proximidad o el contacto de una persona,\
  \ y que en caso de explosionar tenga la potencialidad de incapacitar, herir y/o\
  \ matar a una o m\xE1s personas. Las minas dise\xF1adas para detonar por la presencia,\
  \ la proximidad o el contacto de un veh\xEDculo, y no de una persona que est\xE9\
  n provistas de un dispositivo antimanipulaci\xF3n, no son consideradas minas antipersonal\
  \ por estar as\xED equipadas.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/victimas-de-minas]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Annual registry of landmine victims compiled by DAICMA from incident
    reports across Colombia. Data captures direct human casualties (deaths and injuries)
    from antipersonnel mine explosions, serving as a post-event impact record for
    disaster risk monitoring.
  sources:
  - id: source_1
    license: null
    name: "Direcci\xF3n para la Acci\xF3n Integral contra Minas Antipersonal (DAICMA)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/victimas-de-minas
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Fatalities from antipersonnel landmine incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_pest_infestation
      intensity_measure: Pest:count/area
      process: null
      trigger: null
      type: pest_infestation
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Injuries from antipersonnel landmine incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_pest_infestation
      intensity_measure: Pest:count/area
      process: null
      trigger: null
      type: pest_infestation
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: ppl_injured
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
  description: "Colombia - V\xEDctimas de minas (CSV)"
  download_url: https://data.humdata.org/dataset/94b63a7c-088b-4e11-87bc-db5a562ff3c2/resource/0f07246d-7d19-4465-9005-13cbd925f1a4/download/landmine-victims-annual.csv
  format: null
  id: resource_0f07246d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Landmine-Victims-Annual.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_victimasdeminas_1990
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2015-02-16'
  start: '1990-01-01'
temporal_resolution: null
title: "Colombia - V\xEDctimas de minas"
version: null
vulnerability: null
---
