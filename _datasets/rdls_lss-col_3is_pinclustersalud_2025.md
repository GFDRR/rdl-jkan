---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/colombia-pin-cluster-salud-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/colombia-pin-cluster-salud-2025
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/colombia-pin-cluster-salud-2025
dataset_id: rdls_lss-col_3is_pinclustersalud_2025
description: "Esta base contiene el resultado final del c\xE1lculo de las severidades,\
  \ la Poblaci\xF3n en Necesidad (PiN) y las desagregaciones poblacionales para el\
  \ Cl\xFAster de Salud, Colombia 2025.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/colombia-pin-cluster-salud-2025]"
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: Population in Need (PiN) estimates were calculated by humanitarian
    partners through multi-sectoral needs assessment for the health cluster in Colombia.
    Severity classifications and population disaggregations by age, gender, and vulnerable
    groups (indigenous, Afro-Colombian, persons with disabilities) were derived from
    administrative population data (DANE 2024) and humanitarian partner assessments
    at municipal level.
  sources:
  - id: source_1
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/colombia-pin-cluster-salud-2025
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population in Need (PiN) for health cluster in Colombia 2025, disaggregated
      by severity, age, gender, and vulnerable groups
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: "Esta base contiene el resultado final del c\xE1lculo de las severidades,\
    \ la Poblaci\xF3n en Necesidad (PiN) y las desagregaciones poblacionales para\
    \ el Cl\xFAster de Salud, Colombia 2025."
  download_url: https://data.humdata.org/dataset/624c70ea-8d15-47f8-a6ed-74207e27ed51/resource/3c75b3dd-aad8-40ee-803b-00d717ebb3d3/download/pin-severidades-cluster-salud-2025-col-desagregado-hdx.xlsx
  format: null
  id: resource_3c75b3dd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pin-severidades-cluster-salud-2025-col-desagregado-hdx.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_3is_pinclustersalud_2025
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
  end: '2025-12-31'
  start: '2025-01-27'
temporal_resolution: null
title: Colombia - PiN Cluster Salud
version: null
vulnerability: null
---
