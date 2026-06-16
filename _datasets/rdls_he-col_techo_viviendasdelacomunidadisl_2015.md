---
attributions:
- entity:
    affiliation: null
    email: null
    name: TECHO Colombia
    url: https://data.humdata.org/dataset/viviendas-de-la-comunidad-isla-de-leon-en-cartagena
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian OpenStreetMap Team (HOT)
    url: https://data.humdata.org/dataset/viviendas-de-la-comunidad-isla-de-leon-en-cartagena
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: TECHO Colombia (inactive)
  url: https://data.humdata.org/dataset/viviendas-de-la-comunidad-isla-de-leon-en-cartagena
creator:
  affiliation: null
  email: null
  name: TECHO Colombia (inactive)
  url: https://data.humdata.org/dataset/viviendas-de-la-comunidad-isla-de-leon-en-cartagena
dataset_id: rdls_he-col_techo_viviendasdelacomunidadisl_2015
description: "Muestra las viviendas, iglesias y tiendas presentes en la Comunidad\
  \ 'Isla de Le\xF3n' en Cartagena. Resalta las viviendas de emergencia de TECHO COL\
  \ en pilotis (elevadas a 1 metro y 50 cent\xEDmetros) ya que se presentan inundaciones\
  \ frecuentes. Capas vectoriales de poligonos.. [Source: This metadata record was\
  \ automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:\
  \ https://data.humdata.org/dataset/viviendas-de-la-comunidad-isla-de-leon-en-cartagena]"
details: "La cartograf\xEDa corresponde al estado de las viviendas de la Comunidad\
  \ hasta la fecha del 12 de Abril de 2015, ya que despu\xE9s de ello se presento\
  \ una invasi\xF3n en el territorio que modific\xF3 lo inicialmente mapeado."
exposure:
- asset_type:
    description: "Residential buildings, churches, and shops in Isla de Le\xF3n community,\
      \ including emergency housing structures elevated on stilts"
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
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Community-level building inventory created through HOT mapping methodology\
    \ combining JOSM digitization with Field Papers ground validation. The dataset\
    \ documents residential structures, religious facilities, and commercial establishments\
    \ in Isla de Le\xF3n, with explicit notation of TECHO Colombia emergency housing\
    \ elevated at 1.5 meters to mitigate frequent flooding, providing both exposure\
    \ and implicit hazard evidence."
  sources:
  - id: source_1
    license: null
    name: TECHO Colombia
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Humanitarian OpenStreetMap Team (HOT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/viviendas-de-la-comunidad-isla-de-leon-en-cartagena
  rel: source
loss: null
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
  description: "Colombia - Viviendas de la Comunidad 'Isla de Le\xF3n' en Cartagena\
    \ (Shapefile)"
  download_url: https://data.humdata.org/dataset/b4f7dbb1-5e98-4e6e-a3d5-a7e91a313b0b/resource/a913e649-4dc7-44b6-a7db-f56be0705e25/download/isla-viviendas.zip
  format: null
  id: resource_a913e649
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Isla_Viviendas.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-col_techo_viviendasdelacomunidadisl_2015
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
  end: '2015-05-31'
  start: '2015-01-12'
temporal_resolution: null
title: "Colombia - Viviendas de la Comunidad 'Isla de Le\xF3n' en Cartagena"
version: null
vulnerability: null
---
