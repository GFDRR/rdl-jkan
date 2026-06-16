---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Unidad para la Atenci\xF3n y Reparaci\xF3n Integral a las V\xEDctimas (UARIV)"
    url: https://data.humdata.org/dataset/subsidiariedad-uariv15
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/subsidiariedad-uariv15
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/subsidiariedad-uariv15
dataset_id: rdls_lss-col_ochacol_subsidiariedaddelaunidadp_20161231
description: "Corresponde a los municipios focalizados por la Unidad para la Atenci\xF3\
  n a V\xEDctimas (UARIV) entre 2013 al 2015; y para el 2016, representa los municipios\
  \ focalizados, los montos asignados y pagados (ejecutados) y la cantidad de hogares\
  \ apoyados en la etapa de inmediatez, lo cual corresponde a la etapa en la cual\
  \ las v\xEDctimas se encuentran entre la declaraci\xF3n de los hechos y se emita\
  \ el concepto de valoraci\xF3n.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/subsidiariedad-uariv15]"
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: This dataset compiles administrative records from the Colombian Victims
    Unit (UARIV) documenting municipalities prioritized for victim assistance between
    2013-2015, and for 2016 includes allocated and executed monetary amounts alongside
    household counts supported during the immediate assistance phase following armed
    conflict events.
  sources:
  - id: source_1
    license: null
    name: "Unidad para la Atenci\xF3n y Reparaci\xF3n Integral a las V\xEDctimas (UARIV)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/subsidiariedad-uariv15
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Count of households supported by the Victims Unit during immediate
      assistance phase following armed conflict events
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
  - asset_category: economic_indicator
    asset_dimension: index
    description: Monetary amounts assigned and executed by the Victims Unit for victim
      assistance and reparation
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
          quantity_kind: currency
          unit: null
        metric: loss
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
  description: "Subsidiariedad de la Unidad para las V\xEDctimas en Colombia, 2013\
    \ - 2015 (Excel)"
  download_url: https://data.humdata.org/dataset/9f833509-a29a-4798-a3a1-1d2f1fd54ba1/resource/d3f6ccdd-284b-459c-abe9-42666d6f8a03/download/reporte-ejecucion-mun-2013-2016.xlsx
  format: null
  id: resource_d3f6ccdd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Subsidiariedad-UARIV-2013-2015.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_subsidiariedaddelaunidadp_20161231
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
  start: '2016-12-31'
temporal_resolution: null
title: "Subsidiariedad de la Unidad para las V\xEDctimas en Colombia, 2013 - 2015"
version: null
vulnerability: null
---
