---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Instituto Hondure\xF1o de Ciencias de la Tierra (IHCIT)"
    url: https://data.humdata.org/dataset/poblacion-expuesta-a-ciclone-2010
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "El Instituto Nacional de Estad\xEDstica (INE)"
    url: https://data.humdata.org/dataset/poblacion-expuesta-a-ciclone-2010
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/poblacion-expuesta-a-ciclone-2010
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/poblacion-expuesta-a-ciclone-2010
dataset_id: rdls_he-hnd_ocharolac_poblacionexpuestaciclones_20180518
description: "El indicador estima la poblaci\xF3n expuesta que habita en \xE1reas\
  \ con amenaza alta en base al Mapa de Amenaza por Ciclones resultado de la integraci\xF3\
  n de 29 mapas de los ciclones que han afectado en territorio desde 1970 al 2010,\
  \ incluyendo los huracanes Fifi y el Mitch. El resultado es la composici\xF3n de\
  \ capas de las zonas con una amenaza alta y el total de la poblaci\xF3n que habita\
  \ sobre dicha \xE1rea.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/poblacion-expuesta-a-ciclone-2010]"
details: "* [INFORM Honduras.](http://www.inform-index.org/Subnational/Honduras) *\
  \ Dimensi\xF3n: Peligro y Exposici\xF3n * Categor\xEDa: Peligros Naturales * Componente/Subcomponente:\
  \ Cicl\xF3n Tropical y Marejada / Cicl\xF3n Tropical"
exposure:
- asset_type:
    description: Population residing in high cyclone hazard zones across Honduras
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
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: Historical cyclone track data from 1970-2010 (including Hurricanes
    Fifi and Mitch) were integrated into 29 individual hazard maps by IHCIT. These
    maps were composited to identify high-threat cyclone zones. Population data from
    INE were spatially overlaid with high-hazard areas to estimate exposed population
    counts at the national level.
  sources:
  - id: source_1
    license: null
    name: "Instituto Hondure\xF1o de Ciencias de la Tierra (IHCIT)"
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: "El Instituto Nacional de Estad\xEDstica (INE)"
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/poblacion-expuesta-a-ciclone-2010
  rel: source
loss: null
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
  description: "Honduras Poblaci\xF3n Expuesta a Ciclones 2012 (Poblaci\xF3n que habita\
    \ en zonas expuestas a ciclones.)"
  download_url: https://data.humdata.org/dataset/2076c24b-371e-4320-8dda-ffe42a50c619/resource/3f73691a-500c-40bb-b460-287af4eb9595/download/3-pe.nat.cm.cln-abs-poblacion-expuesta-a-ciclones-absoluto.xlsx
  format: null
  id: resource_3f73691a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "3-PE.NAT.CM.CLN-ABS - Poblaci\xF3n Expuesta a Ciclones (absoluto).xlsx"
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-hnd_ocharolac_poblacionexpuestaciclones_20180518
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
title: "Honduras Poblaci\xF3n Expuesta a Ciclones 2012"
version: null
vulnerability: null
---
