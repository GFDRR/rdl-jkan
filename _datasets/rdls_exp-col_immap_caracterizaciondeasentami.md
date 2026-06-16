---
attributions:
- entity:
    affiliation: null
    email: null
    name: International humanitarian organizations
    url: https://data.humdata.org/dataset/caracterizacion-de-asentamientos-nuevos-2020
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/caracterizacion-de-asentamientos-nuevos-2020
creator:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/caracterizacion-de-asentamientos-nuevos-2020
dataset_id: rdls_exp-col_immap_caracterizaciondeasentami
description: "El prop\xF3sito de esta caracterizaci\xF3n es el de validar nuevos asentamientos\
  \ identificados en Colombia a partir de im\xE1genes satelitales; lo aportado en\
  \ misiones a terreno y de organizaciones internacionales que hacen respuesta humanitaria\
  \ en asentamientos. Por lo cual es un ejercicio observacional de la estructura f\xED\
  sica de los asentamientos. En cuanto a los 'Asentamientos Nuevos' seleccionados,\
  \ el criterio geogr\xE1fico corresponde a aquellos grupos de individuos que se han\
  \ establecido en zonas donde no hab\xEDan unidades de vivienda en un corto plazo\
  \ (Se toma por ejemplo un periodo de tiempo comprendido entre 2017 y 2022), adem\xE1\
  s se tiene en cuenta que los ' Asentamientos Nuevos' que est\xE1n mayoritariamente\
  \ localizados en zonas periurbanas (espacio de delimitaci\xF3n entre lo urbano y\
  \ lo rural). Las caracter\xEDsticas que usualmente ser\xEDan relacionadas con los\
  \ 'Asentamientos Nuevos', incluyen: La ausencia de equipamiento urbano (Parques,\
  \ salones comunales, alumbrado p\xFAblico, andenes, etc). Trazado desordenado, inexistencia\
  \ de una red vial (pavimentada) e irregular divisi\xF3n de los predios. Viviendas\
  \ improvisadas (realizadas con posibles materiales perecederos como madera, lat\xF3\
  n, etc) Los Asentamientos Nuevos, no son: albergues, lugares de paso, puntos de\
  \ atenci\xF3n, campamentos, refugios, y en general todo poblado que haya sido conformado\
  \ por alguna entidad gubernamental, no gubernamental o supranacional; es decir,\
  \ que deben ser iniciativa del mismo grupo de personas que van llegando a un posible\
  \ destino para asentarse.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/caracterizacion-de-asentamientos-nuevos-2020]"
details: null
exposure:
- asset_type:
    description: Residential building stock in newly identified settlements characterized
      through satellite imagery and field validation
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Population residing in newly established informal settlements
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC0-1.0
lineage:
  description: New settlements in Colombia were identified through satellite imagery
    analysis and validated through direct field observations by iMMAP and international
    humanitarian organizations. The dataset characterizes the physical structure of
    settlements established within a short timeframe in areas previously without housing
    units, creating a spatial inventory of informal settlement locations and building
    stock.
  sources:
  - id: source_1
    license: null
    name: iMMAP Inc.
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: International humanitarian organizations
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/caracterizacion-de-asentamientos-nuevos-2020
  rel: source
loss: null
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
  description: "S\xF3lo a solicitud realizada a iMMAP, es posible entregar la base\
    \ de datos con informaci\xF3n acerca de la localizaci\xF3n de cada uno de los\
    \ asentamientos, as\xED como la inclusi\xF3n de fotograf\xEDas del mismo asentamiento."
  download_url: https://data.humdata.org/dataset/7e0d32a6-94c0-46f2-8f4b-e6edb588e671/resource/d38f80da-02f9-48b0-991c-a131d6c029f4/download/asentamientos-t3-2020-hdx-definitiva.xlsx
  format: null
  id: resource_d38f80da
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Asentamientos t3 2020 HDX definitiva.xlsx
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-col_immap_caracterizaciondeasentami
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
title: "Colombia - Caracterizaci\xF3n de asentamientos nuevos 2020"
version: null
vulnerability: null
---
