---
attributions:
- entity:
    affiliation: null
    email: null
    name: DANE
    url: https://data.humdata.org/dataset/pin-y-severidades-del-cluster-de-alojamientos-y-asentamientos-aya-colombia-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/pin-y-severidades-del-cluster-de-alojamientos-y-asentamientos-aya-colombia-2025
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/pin-y-severidades-del-cluster-de-alojamientos-y-asentamientos-aya-colombia-2025
dataset_id: rdls_lss-col_3is_calculodelaspersonasennec_2025
description: "El archivo tiene los resultados del c\xE1lculo de las Personas en Necesidad\
  \ (PiN) y las Severidades del cl\xFAster de Alojamientos y Asentamientos (AyA) para\
  \ el a\xF1o 2025 en Colombia.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pin-y-severidades-del-cluster-de-alojamientos-y-asentamientos-aya-colombia-2025]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: PiN and severity data compiled from multiple administrative and survey
    sources including DANE statistics, aggregated through registry methodology to
    assess shelter and settlement needs across Colombia for 2025. The dataset represents
    post-event or ongoing humanitarian impact assessments classified by severity levels
    for the shelter cluster.
  sources:
  - id: source_1
    license: null
    name: DANE
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: 3iS
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pin-y-severidades-del-cluster-de-alojamientos-y-asentamientos-aya-colombia-2025
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in Need (PiN) and severity classifications for shelter and
      settlements sector in Colombia
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia: C\xE1lculo de las Personas en Necesidad (PiN) y las Severidades\
    \ del cl\xFAster de Alojamientos y Asentamientos (AyA) (PiN_Severidad_A&A_Colombia_2025.xlsx)"
  download_url: https://data.humdata.org/dataset/0a94491e-c4e4-498f-8249-02804facf4e0/resource/da069b38-fc1d-42aa-9e82-00b82a9ddaa1/download/pin_severidad_aa_colombia_2025.xlsx
  format: null
  id: resource_da069b38
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PiN_Severidad_A&A_Colombia_2025.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_3is_calculodelaspersonasennec_2025
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
  start: '2025-01-01'
temporal_resolution: null
title: "Colombia: C\xE1lculo de las Personas en Necesidad (PiN) y las Severidades\
  \ del cl\xFAster de Alojamientos y Asentamientos (AyA)"
version: null
vulnerability: null
---
