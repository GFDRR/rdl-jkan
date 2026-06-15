---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA-Monitor
    url: https://data.humdata.org/dataset/datos-boletin-humanitario-ocha-colombia-noviembre-2014
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: SIGPAD
    url: https://data.humdata.org/dataset/datos-boletin-humanitario-ocha-colombia-noviembre-2014
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: DAICMA
    url: https://data.humdata.org/dataset/datos-boletin-humanitario-ocha-colombia-noviembre-2014
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UARIV
    url: https://data.humdata.org/dataset/datos-boletin-humanitario-ocha-colombia-noviembre-2014
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/datos-boletin-humanitario-ocha-colombia-noviembre-2014
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/datos-boletin-humanitario-ocha-colombia-noviembre-2014
dataset_id: rdls_lss-col_ochacol_datosboletinhumanitariono_201411
description: "Contiene los datos utilizados y citados en el [Bolet\xEDn Humanitario\
  \ OCHA Colombia Noviembre 2014] (http://www.salahumanitaria.co/es/search/document-type/42).\
  \ Contiene: PDI en eventos de desplazamiento masivo. Nov. 2014 (OCHA-Monitor) /\
  \ No. Personas afectadas por desastres. Nov. 2014 (SIGPAD) / No. PDI en eventos\
  \ de desplazamiento masivo. Nov. 19/2012 - Nov. 18/2014 (Periodo di\xE1logos de\
  \ paz con las FARC-EP) (OCHA-Monitor) / No. v\xEDctimas MAP/MUSE Nov. 19/2012 -\
  \ Nov. 18/2014 (Periodo di\xE1logos de paz con las FARC-EP) (DAICMA) / No. Personas\
  \ afectadas por limitaciones de movilidad, acceso y confinamiento. Nov. 19/2012\
  \ - Nov. 18/2014 (Periodo di\xE1logos de paz con las FARC-EP) (OCHA-Monitor) / No.\
  \ Personas afectadas por confinamiento Nov. 19/2012 - Nov. 18/2014 (Periodo di\xE1\
  logos de paz con las FARC-EP) (OCHA-Monitor) / No. total de PDI. Nov. 2012 - Sept.\
  \ 2014 (UARIV). [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/datos-boletin-humanitario-ocha-colombia-noviembre-2014]"
details: "Estos datos son recopilados de diversas fuentes, procesados por OCHA Colombia.\
  \ Los datos de OCHA-Monitor se actualizan diariamente, la informaci\xF3n puede variar\
  \ seg\xFAn la fecha de consulta."
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: This dataset aggregates impact data from multiple Colombian government
    and humanitarian sources (OCHA-Monitor, SIGPAD, DAICMA, UARIV) covering displacement,
    affected populations, and casualties recorded during November 2014 and the preceding
    peace dialogue period. Data were compiled and processed by OCHA Colombia for inclusion
    in the November 2014 Humanitarian Bulletin.
  sources:
  - id: source_1
    license: null
    name: OCHA-Monitor
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: SIGPAD
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: DAICMA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: UARIV
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/datos-boletin-humanitario-ocha-colombia-noviembre-2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Number of people affected by disasters in November 2014
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
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from mass displacement events in November
      2014
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Datos Bolet\xEDn Humanitario OCHA Colombia Noviembre 2014 (Datos HDX.xlsx)"
  download_url: https://data.humdata.org/dataset/eb9032a4-bf6b-4c16-8eee-758c4678550e/resource/1dddf7e0-1e06-439d-a1a3-b3eab0b54f0c/download/datos-hdx.xlsx
  format: null
  id: resource_1dddf7e0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Datos HDX.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_datosboletinhumanitariono_201411
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
  end: '2014-11-30'
  start: '2014-11-01'
temporal_resolution: null
title: "Datos Bolet\xEDn Humanitario OCHA Colombia Noviembre 2014"
version: null
vulnerability: null
---
