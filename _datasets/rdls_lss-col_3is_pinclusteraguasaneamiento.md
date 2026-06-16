---
attributions:
- entity:
    affiliation: null
    email: null
    name: "DANE (Departamento Administrativo Nacional de Estad\xEDstica)"
    url: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "UNGRD (Unidad Nacional de Gesti\xF3n del Riesgo de Desastres)"
    url: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash-2024
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: MONITOR (Conflict monitoring system)
    url: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash-2024
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash-2024
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash-2024
dataset_id: rdls_lss-col_3is_pinclusteraguasaneamiento
description: "Esta base contiene el resultado final del c\xE1lculo de las severidades,\
  \ la Poblaci\xF3n en Necesidad (PiN) y las desagregaciones poblacionales para el\
  \ Cl\xFAster de Agua, Saneamiento e Higiene (WASH), Colombia 2024.. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash-2024]"
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: "Population in need (PiN) calculated by integrating DANE census data\
    \ on water sources, sanitation infrastructure, and waste collection with health\
    \ indicators (waterborne diseases, malnutrition), natural disaster exposure from\
    \ UNGRD, armed conflict data from MONITOR, and El Ni\xF1o probability. Severity\
    \ indices were computed for each factor, weighted and aggregated to produce final\
    \ PiN estimates disaggregated by department, municipality, and population subgroups\
    \ (age, rural/urban)."
  sources:
  - id: source_1
    license: null
    name: "DANE (Departamento Administrativo Nacional de Estad\xEDstica)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: "UNGRD (Unidad Nacional de Gesti\xF3n del Riesgo de Desastres)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: MONITOR (Conflict monitoring system)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/colombia-pin-cluster-agua-saneamiento-e-higiene-wash-2024
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population in need (PiN) for WASH cluster in Colombia 2024, calculated
      from water source quality, sanitation access, and natural disaster exposure
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
  - asset_category: population
    asset_dimension: population
    description: "Population affected by El Ni\xF1o phenomenon probability and water\
      \ quality degradation"
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://reliefweb.int/report/colombia/nota-metodologica-calculo-de-personas-en-necesidad-pin-wash-2024-colombia
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Esta base contiene el resultado final del c\xE1lculo de las severidades,\
    \ la Poblaci\xF3n en Necesidad (PiN) y las desagregaciones poblacionales para\
    \ el Cl\xFAster de Agua, Saneamiento e Higiene (WASH), Colombia 2024. Para m\xE1\
    s informaci\xF3n, por favor dir\xEDjase a la nota metodol\xF3gica."
  download_url: https://data.humdata.org/dataset/17b50e0a-1100-4cac-aa32-1b70826ffe9a/resource/1cbcdeec-b216-49fd-91de-fa090e1f7129/download/matriz-resultados-pin_severidades_desagregacion-cluster-wash-2024.xlsx
  format: null
  id: resource_1cbcdeec
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Matriz resultados PiN_Severidades_Desagregaci\xF3n - Cl\xFAster WASH 2024.xlsx"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_3is_pinclusteraguasaneamiento
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: "Colombia - PiN Cl\xFAster Agua, Saneamiento e Higiene (WASH) 2024"
version: null
vulnerability: null
---
