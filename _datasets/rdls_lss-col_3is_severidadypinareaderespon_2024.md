---
attributions:
- entity:
    affiliation: null
    email: null
    name: 3iSolution
    url: https://data.humdata.org/dataset/severidad-y-pin-area-de-responsabilidad-de-proteccion-de-la-ninez-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/severidad-y-pin-area-de-responsabilidad-de-proteccion-de-la-ninez-2025
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/severidad-y-pin-area-de-responsabilidad-de-proteccion-de-la-ninez-2025
dataset_id: rdls_lss-col_3is_severidadypinareaderespon_2024
description: "Resultados del c\xE1lculo del PiN para el \xE1rea de responsabilidad\
  \ de protecci\xF3n de la ni\xF1ez. Contiene los indicadores de reclutamiento, conflicto,\
  \ salud mental, desastres naturales y PiN final. [Source: This metadata record was\
  \ automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:\
  \ https://data.humdata.org/dataset/severidad-y-pin-area-de-responsabilidad-de-proteccion-de-la-ninez-2025]"
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: PiN 2025 severity and needs assessment calculated for Colombia's child
    protection area of responsibility by aggregating indicators across recruitment,
    conflict, mental health, and natural disaster exposure domains to produce final
    PiN estimates at administrative levels.
  sources:
  - id: source_1
    license: null
    name: 3iSolution
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/severidad-y-pin-area-de-responsabilidad-de-proteccion-de-la-ninez-2025
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by natural disasters (desastres naturales) in
      child protection area of responsibility
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  description: "Colombia - Severidad y PiN Area de Responsabilidad de Protecci\xF3\
    n de la Ni\xF1ez (PiN 2025 Adrn.xlsx)"
  download_url: https://data.humdata.org/dataset/88f2b93a-7b0b-4e7e-a54c-8b5ed3d7ad25/resource/cc88a17c-7ebb-4509-a1bf-afad41504198/download/pin-2025-adrn.xlsx
  format: null
  id: resource_cc88a17c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PiN 2025 Adrn.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_3is_severidadypinareaderespon_2024
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
  end: '2025-10-01'
  start: '2024-10-01'
temporal_resolution: null
title: "Colombia - Severidad y PiN Area de Responsabilidad de Protecci\xF3n de la\
  \ Ni\xF1ez"
version: null
vulnerability: null
---
