---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/confinamiento
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/confinamiento
dataset_id: rdls_lss-col_ochacol_confinamiento_2013
description: "Desde julio de 2013 la oficina de OCHA en Colombia estableci\xF3 un\
  \ marco para el monitoreo del confinamiento. Seg\xFAn este marco, una poblaci\xF3\
  n se encuentra confinada cuando sufre limitaciones a su libre movilidad por un per\xED\
  odo igual o superior a una semana, y adem\xE1s tiene acceso limitado a tres bienes\
  \ o servicios b\xE1sicos, como: educaci\xF3n, salud, agua y saneamiento, medios\
  \ de vida, entre otros.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/confinamiento]"
details: "La informaci\xF3n disponible no refleja la totalidad del fen\xF3meno pues\
  \ depende de reportes consolidados por OCHA y los Equipos Humanitarios Locales;\
  \ de tal forma que puede haber vac\xEDos de informaci\xF3n en zonas con menos presencia\
  \ de organizaciones internacionales."
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "OCHA Colombia established a monitoring framework in July 2013 to track\
    \ population confinement through direct observational and anecdotal data collection.\
    \ Confinement is defined as restricted mobility lasting \u22651 week combined\
    \ with limited access to \u22653 basic services (education, health, water/sanitation,\
    \ livelihoods). Monthly aggregated figures are compiled into a time-series dataset\
    \ for humanitarian monitoring and response planning."
  sources:
  - id: source_1
    license: null
    name: OCHA Colombia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/confinamiento
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by conflict-related confinement with restricted
      access to basic services
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - Confinamiento (Confinamiento mensual.csv)
  download_url: https://data.humdata.org/dataset/24c09bab-af17-406f-8ec1-9bd7ddeca08d/resource/3fb3f50e-6bb7-44af-8ac9-6e50db433f67/download/confinamiento-mensual.csv
  format: null
  id: resource_3fb3f50e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Confinamiento mensual.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_confinamiento_2013
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
  end: '2015-01-01'
  start: '2013-01-01'
temporal_resolution: null
title: Colombia - Confinamiento
version: null
vulnerability: null
---
