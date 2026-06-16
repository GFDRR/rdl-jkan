---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Unidad de Atenci\xF3n y Reparaci\xF3n Integral a las V\xEDctimas (UARIV)"
    url: https://data.humdata.org/dataset/idps-data-by-year-and-municipality
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/idps-data-by-year-and-municipality
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/idps-data-by-year-and-municipality
dataset_id: rdls_lss-col_ochacol_datoshistoricosdedesplaza_1996
description: "N\xFAmero de desplazados por municipio seg\xFAn el Registro \xDAnico\
  \ de V\xEDctimas de la Unidad de Atenci\xF3n y Reparaci\xF3n Integral a las V\xED\
  ctimas (UARIV).. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/idps-data-by-year-and-municipality]"
details: "Los datos para 2014 tienen como fecha de corte Septiembre de este mismo\
  \ a\xF1o."
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Historical displacement data compiled from the UARIV registry, which
    systematically records internally displaced persons by municipality. The dataset
    aggregates administrative victim registration records covering the period 1999-2014,
    providing municipal-level counts of displacement events and affected populations.
  sources:
  - id: source_1
    license: null
    name: "Unidad de Atenci\xF3n y Reparaci\xF3n Integral a las V\xEDctimas (UARIV)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/idps-data-by-year-and-municipality
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons registered by municipality from armed
      conflict and violence
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia - Datos hist\xF3ricos de desplazamiento a nivel municipal\
    \ (Desplazamiento 1999-2014.xlsx)"
  download_url: https://data.humdata.org/dataset/404caaab-3746-43bf-a61e-23c81187ef03/resource/650ae95a-47aa-4da8-b161-13b54946c9e7/download/desplazamiento-1999-2014.xlsx
  format: null
  id: resource_650ae95a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Desplazamiento 1999-2014.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia - Datos hist\xF3ricos de desplazamiento a nivel municipal\
    \ (Desplazamiento 1999-2014.csv)"
  download_url: https://data.humdata.org/dataset/404caaab-3746-43bf-a61e-23c81187ef03/resource/cbf5feee-daa9-47e0-8f1e-ab706cb2173e/download/desplazamiento-1999-2014.csv
  format: null
  id: resource_cbf5feee
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Desplazamiento 1999-2014.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_datoshistoricosdedesplaza_1996
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
  end: '2014-09-30'
  start: '1996-01-01'
temporal_resolution: null
title: "Colombia - Datos hist\xF3ricos de desplazamiento a nivel municipal"
version: null
vulnerability: null
---
