---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Instituto Hondure\xF1o de Ciencias de la Tierra (IHCIT)"
    url: https://data.humdata.org/dataset/honduras-poblacion-expuesta-que-habita-en-zonas-expuestas-a-marejadas-2010
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "El Instituto Nacional de Estad\xEDstica (INE)"
    url: https://data.humdata.org/dataset/honduras-poblacion-expuesta-que-habita-en-zonas-expuestas-a-marejadas-2010
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-poblacion-expuesta-que-habita-en-zonas-expuestas-a-marejadas-2010
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-poblacion-expuesta-que-habita-en-zonas-expuestas-a-marejadas-2010
dataset_id: rdls_he-hnd_ocharolac_poblacionexpuestamarejada_20180518
description: "El indicador estima la poblaci\xF3n expuesta que habita en \xE1reas\
  \ con amenaza alta en base al Mapa de Amenaza por Mareas y Marejadas. El resultado\
  \ es la composici\xF3n de capas de las zonas con una amenaza alta y el total de\
  \ la poblaci\xF3n que habita sobre dicha \xE1rea, resalta el hecho de ser una amenaza\
  \ recurrente de forma anual en las costas de pacifico. El indicador se basa en la\
  \ calidad de informaci\xF3n del Mapa de Mareas Marejadas, se requiere una reflexi\xF3\
  n adicional entre la poblaci\xF3n bajo amenaza alta y el recuento hist\xF3rico que\
  \ registra 7,844 afectados o damnificados desde el 1965 al 2010.. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/honduras-poblacion-expuesta-que-habita-en-zonas-expuestas-a-marejadas-2010]"
details: "* [INFORM Honduras.](http://www.inform-index.org/Subnational/Honduras) *\
  \ Dimensi\xF3n: Peligro y Exposici\xF3n * Categor\xEDa: Peligros Naturales * Componente/Subcomponente:\
  \ Cicl\xF3n Tropical y Marejada / Marejada"
exposure:
- asset_type:
    description: Population residing in high-hazard coastal flood zones
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
  event_sets_by_hazard_type:
    flood:
    - analysis_type: deterministic
      calculation_method: inferred
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Population exposure indicator derived by overlaying high-threat coastal
    flood hazard zones (from IHCIT tidal surge/storm surge mapping) with gridded population
    data (INE census). The composite layer quantifies absolute population residing
    in annually recurrent coastal hazard areas, validated against historical impact
    records (7,844 affected/displaced 1965-2010).
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
- href: https://data.humdata.org/dataset/honduras-poblacion-expuesta-que-habita-en-zonas-expuestas-a-marejadas-2010
  rel: source
loss:
  losses: []
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
  description: "Honduras Poblaci\xF3n expuesta a marejadas 2012 (Honduras Poblaci\xF3\
    n que habita en zonas expuestas a marejadas.)"
  download_url: https://data.humdata.org/dataset/ee80351e-52bc-45c6-822d-79ff95c5c30f/resource/ddbe7c92-4d0b-4519-b69e-044a0cb7f652/download/4-pe.nat.cm.mrj-abs-poblacion-expuesta-a-marejadas-absoluto.xlsx
  format: null
  id: resource_ddbe7c92
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "4-PE.NAT.CM.MRJ-ABS - Poblaci\xF3n Expuesta a Marejadas (absoluto).xlsx"
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-hnd_ocharolac_poblacionexpuestamarejada_20180518
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
title: "Honduras Poblaci\xF3n expuesta a marejadas 2012"
version: null
vulnerability: null
---
