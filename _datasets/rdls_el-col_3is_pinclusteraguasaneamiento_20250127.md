---
attributions:
- entity:
    affiliation: null
    email: null
    name: "DANE (Departamento Administrativo Nacional de Estad\xEDstica)"
    url: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "UNGRD (Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres)"
    url: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "SIVIGILA (Sistema de Vigilancia en Salud P\xFAblica)"
    url: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: MONITOR
    url: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "IRCA (\xCDndice de Riesgo de la Calidad del Agua)"
    url: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash
dataset_id: rdls_el-col_3is_pinclusteraguasaneamiento_20250127
description: "Esta base contiene el resultado final del c\xE1lculo de las severidades,\
  \ la Poblaci\xF3n en Necesidad (PiN) y las desagregaciones poblacionales para el\
  \ Cl\xFAster de Agua, Saneamiento e Higiene (WASH), Colombia.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash]"
details: null
exposure:
- asset_type:
    description: Population in need (PiN) disaggregated by age, gender, ethnicity,
      and disability status across Colombian municipalities
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC0-1.0
lineage:
  description: "Population in need (PiN) calculated by integrating DANE census data\
    \ on WASH infrastructure coverage (unimproved water sources, lack of sewerage,\
    \ waste collection) with health surveillance data (SIVIGILA disease rates, malnutrition,\
    \ UNGRD disaster registries) and environmental factors (IRCA water quality, El\
    \ Ni\xF1o/La Ni\xF1a phenomena). Severity scores were computed for each indicator,\
    \ weighted and aggregated to produce final PiN estimates disaggregated by municipality,\
    \ age group, gender, ethnicity, and disability status for the WASH cluster humanitarian\
    \ response."
  sources:
  - id: source_1
    license: null
    name: "DANE (Departamento Administrativo Nacional de Estad\xEDstica)"
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: "UNGRD (Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: "SIVIGILA (Sistema de Vigilancia en Salud P\xFAblica)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: MONITOR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: "IRCA (\xCDndice de Riesgo de la Calidad del Agua)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by inadequate water access and sanitation conditions,
      including water-related disease burden and malnutrition
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
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://reliefweb.int/report/colombia/nota-metodologica-calculo-de-personas-en-necesidad-pin-agua-saneamiento-e-higiene-wash-2025-colombia
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Esta base contiene el resultado final del c\xE1lculo de las severidades,\
    \ la Poblaci\xF3n en Necesidad (PiN) y las desagregaciones poblacionales para\
    \ el Cl\xFAster de Agua, Saneamiento e Higiene (WASH), Colombia 2025. Para m\xE1\
    s informaci\xF3n, por favor dir\xEDjase a la nota metodol\xF3gica en el siguiente\
    \ enlace: https://reliefweb.int/report/colombia/nota-metodologica-calculo-de-personas-en-necesidad-pin-agua-saneamiento-e-higiene-wash-2025-colombia"
  download_url: https://data.humdata.org/dataset/520dd80b-ab53-4d89-94a4-14fe5f7558a4/resource/e4c46716-693c-4dd3-9a67-52853dc316b2/download/matriz-resultados-pin_severidades_desagregacion-cluster-wash-2025.xlsx
  format: null
  id: resource_e4c46716
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: matriz-resultados-pin_severidades_desagregacion-cluster-wash-2025.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-col_3is_pinclusteraguasaneamiento_20250127
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
  end: null
  start: '2025-01-27'
temporal_resolution: null
title: "Colombia - PiN Cl\xFAster Agua, Saneamiento e Higiene (WASH)"
version: null
vulnerability: null
---
