---
attributions:
- entity:
    affiliation: null
    email: null
    name: DesInventar
    url: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-inundaciones-1995-2015
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Instituto Nacional de Estad\xEDstica de Guatemala - INE"
    url: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-inundaciones-1995-2015
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-inundaciones-1995-2015
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-inundaciones-1995-2015
dataset_id: rdls_lss-hnd_ocharolac_poblacionmediaanualexpues_20180518
description: "El indicador representa la poblaci\xF3n anual promedio que pueda ser\
  \ afectada, desaparecida, herida, muerta, reubicada, v\xEDctima o evacuada por inundaciones,\
  \ seg\xFAn registros hist\xF3ricos en la base de datos DesInventar durante el periodo\
  \ de 1995-2015.. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-inundaciones-1995-2015]"
details: "* [INFORM Honduras.](http://www.inform-index.org/Subnational/Honduras) *\
  \ Dimensi\xF3n: Peligro y Exposici\xF3n * Categor\xEDa: Peligros Naturales * Componente:\
  \ Inundaciones"
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Annual average population exposure to flooding was calculated from
    historical disaster impact records in the DesInventar database covering 1995-2015,
    aggregating reported cases of affected, missing, injured, dead, displaced, and
    evacuated persons across Honduras to derive mean annual exposure figures.
  sources:
  - id: source_1
    license: null
    name: DesInventar
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: "Instituto Nacional de Estad\xEDstica de Guatemala - INE"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-inundaciones-1995-2015
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Annual average population exposed to flooding impacts including affected,
      missing, injured, dead, displaced, and evacuated persons
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
  description: "Honduras Poblaci\xF3n Media Anual Expuesta a Inundaciones 1995-2015\
    \ (Poblaci\xF3n promedio anual afectada por inundaciones 1995-2015)"
  download_url: https://data.humdata.org/dataset/c033299a-6a6e-4ddd-ba72-1375be682991/resource/03be6f70-ab34-48c4-8c00-86b81fffaabf/download/2-pe.nat.ind-abs-poblacion-media-anual-expuesta-a-inundaciones-absoluto.xlsx
  format: null
  id: resource_03be6f70
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "2-PE.NAT.IND-ABS - Poblaci\xF3n Media Anual Expuesta a Inundaciones (absoluto).xlsx"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hnd_ocharolac_poblacionmediaanualexpues_20180518
spatial:
  bbox: null
  centroid: null
  countries:
  - HND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-18'
temporal_resolution: null
title: "Honduras Poblaci\xF3n Media Anual Expuesta a Inundaciones 1995-2015"
version: null
vulnerability: null
---
