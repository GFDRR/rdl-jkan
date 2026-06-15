---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/colombia-pin-cluster-salud-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/colombia-pin-cluster-salud-2024
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/colombia-pin-cluster-salud-2024
dataset_id: rdls_lss-col_3is_pinclustersalud_2024
description: "Esta base contiene el resultado final del c\xE1lculo de las severidades,\
  \ la Poblaci\xF3n en Necesidad (PiN) y las desagregaciones poblacionales para el\
  \ Cl\xFAster de Salud, Colombia 2024.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/colombia-pin-cluster-salud-2024]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Humanitarian partners conducted needs assessments across Colombia to
    identify populations requiring health assistance. Severity classifications and
    population disaggregations were calculated and aggregated to produce final PiN
    estimates by administrative divisions for Health Cluster coordination in 2024.
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
- href: https://data.humdata.org/dataset/colombia-pin-cluster-salud-2024
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population in Need (PiN) classified by health severity due to drought-related
      humanitarian crisis
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
  description: Colombia - PiN Cluster Salud (Excel)
  download_url: https://data.humdata.org/dataset/2057b741-aec0-4eec-b4ea-febfa00c3814/resource/b67d56a2-548e-495f-a828-84ced02c9540/download/pin-severidades-cluster-salud-2024-col-desagregado-hdx.xlsx
  format: null
  id: resource_b67d56a2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pin-severidades-cluster-salud-2024-col-desagregado-hdx.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_3is_pinclustersalud_2024
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
  end: '2024-12-31'
  start: '2024-01-01'
temporal_resolution: null
title: Colombia - PiN Cluster Salud
version: null
vulnerability: null
---
