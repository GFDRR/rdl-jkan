---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/desplazamientosmasivos
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/desplazamientosmasivos
dataset_id: rdls_lss-col_ochacol_desplazamientosmasivos_2009
description: 'Desplazamientos en eventos masivos, corresponde a mas de 50 personas
  o 10 familias. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/desplazamientosmasivos]'
details: "Esta informaci\xF3n es de uso interno exclusivo de OCHA Colombia. No compromete\
  \ la posici\xF3n de las fuentes citadas aqu\xED. Las cifras reflejadas aqu\xED son\
  \ estimaciones con base en el contraste de diferentes fuentes. Al citar informaci\xF3\
  n extra\xEDda de esta tabla, porfavor siempre use esta leyenda: 'Desplazamientos\
  \ masivos - 2013 - Estimado OCHA a partir de fuentes oficiales y secundarias'."
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Direct observational data collected by OCHA Colombia documenting mass
    displacement events (defined as >50 persons or >10 families displaced) from 2009-2014.
    Data represents post-event impact records of population displacement, primarily
    triggered by armed conflict and violence rather than natural hazards, though flood-related
    displacement may be included.
  sources:
  - id: source_1
    license: null
    name: OCHA Colombia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/desplazamientosmasivos
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from mass displacement events (>50 people
      or >10 families)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - Desplazamientos masivos - OCHA (Desplazamientos masivos
    OCHA Colombia 2009 - 2014 (1).xlsx)
  download_url: https://data.humdata.org/dataset/b3fb194c-9d14-4f02-aadd-aaa35a2f42f5/resource/f310d715-2fe6-4bda-9131-902d62c8e19c/download/desplazamientos-masivos-ocha-colombia-2009-2014-1.xlsx
  format: null
  id: resource_f310d715
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Desplazamientos masivos OCHA Colombia 2009 - 2014 (1).xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_desplazamientosmasivos_2009
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
  end: '2015-01-01'
  start: '2009-01-01'
temporal_resolution: null
title: Colombia - Desplazamientos masivos - OCHA
version: null
vulnerability: null
---
