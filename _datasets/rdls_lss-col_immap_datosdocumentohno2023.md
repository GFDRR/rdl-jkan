---
attributions:
- entity:
    affiliation: null
    email: null
    name: Monitor OCHA
    url: https://data.humdata.org/dataset/datos-documento-hno-colombia-2023
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Unidad para las Victimas (UARIV)
    url: https://data.humdata.org/dataset/datos-documento-hno-colombia-2023
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres (UNGRD)"
    url: https://data.humdata.org/dataset/datos-documento-hno-colombia-2023
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/datos-documento-hno-colombia-2023
creator:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/datos-documento-hno-colombia-2023
dataset_id: rdls_lss-col_immap_datosdocumentohno2023
description: "Estas bases contienen informaci\xF3n relevante, utilizada para destacar\
  \ mensajes claves dentro del documento Humanitarian Needs Overview (HNO) Colombia\
  \ 2023.. [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/datos-documento-hno-colombia-2023]"
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: 'The HNO 2023 dataset aggregates impact records from three administrative
    registries: armed conflict affectations from OCHA monitoring, individual displacement
    cases from the national victims unit (UARIV), and disaster-related impacts from
    the national disaster risk management authority (UNGRD). These sources were compiled
    to identify key humanitarian needs and affected populations for the 2023 Humanitarian
    Needs Overview.'
  sources:
  - id: source_1
    license: null
    name: Monitor OCHA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Unidad para las Victimas (UARIV)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: "Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres (UNGRD)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/datos-documento-hno-colombia-2023
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by armed conflict-related incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from armed conflict and disasters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
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
  description: "Esta base contiene el n\xFAmero de afectados seg\xFAn el tipo de afectaciones\
    \ derivadas del conflicto armado para los a\xF1os 2021 y 2022; esta base es tomada\
    \ de Monitor OCHA."
  download_url: https://data.humdata.org/dataset/c368a4f9-3b4a-4eff-8f90-062add389819/resource/de811aa7-0e12-48dd-87fa-2bf09deeff37/download/base-por-tipo-de-afectaciones-por-conflicto-armado-monitor-ocha-2021-y-2022.xlsx
  format: null
  id: resource_de811aa7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: base-por-tipo-de-afectaciones-por-conflicto-armado-monitor-ocha-2021-y-2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Esta base contiene el n\xFAmero de desplazamientos individuales por\
    \ tipo de desplazamiento desde el a\xF1o 1899 hasta octubre 2022; esta informaci\xF3\
    n es tomada de la Unidad para las Victimas (UARIV)."
  download_url: https://data.humdata.org/dataset/c368a4f9-3b4a-4eff-8f90-062add389819/resource/7eac78ed-7873-4a30-8b1e-69d535b03408/download/base-por-tipo-de-desplazamiento-individual-unidad-para-las-victimas-uariv-1899-a-octubre-2022.xlsx
  format: null
  id: resource_7eac78ed
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Base por tipo de desplazamiento individual - Unidad para las Victimas (UARIV)
    - 1899 a octubre 2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Esta base contiene el tipo de afectaciones por desastre de origen\
    \ natural de los a\xF1os 2021 y 2022; esta informaci\xF3n es tomada de la Unidad\
    \ Nacional para la Gesti\xF3n del Riesgo de Desastres (UNGRD)."
  download_url: https://data.humdata.org/dataset/c368a4f9-3b4a-4eff-8f90-062add389819/resource/fdbb91fd-bfb7-4029-bd55-67e8f3b22334/download/base-unidad-nacional-para-la-gestion-del-riesgo-de-desastres-ungrd-2021-y-2022.xlsx
  format: null
  id: resource_fdbb91fd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Base Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres (UNGRD)\
    \ - 2021 Y 2022.xlsx"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_immap_datosdocumentohno2023
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
title: Datos documento HNO Colombia 2023
version: null
vulnerability: null
---
