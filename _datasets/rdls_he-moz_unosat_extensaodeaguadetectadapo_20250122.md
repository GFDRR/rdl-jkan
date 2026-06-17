---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/extensao-de-agua-detectada-por-satelite-nos-distritos-de-mossuril-e-ilha-de-mocambique-pro
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/extensao-de-agua-detectada-por-satelite-nos-distritos-de-mossuril-e-ilha-de-mocambique-pro
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/extensao-de-agua-detectada-por-satelite-nos-distritos-de-mossuril-e-ilha-de-mocambique-pro
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/extensao-de-agua-detectada-por-satelite-nos-distritos-de-mossuril-e-ilha-de-mocambique-pro
dataset_id: rdls_he-moz_unosat_extensaodeaguadetectadapo_20250122
description: "UNOSAT code: FL20250121MOZ Este mapa ilustra a \xE1gua detectada por\
  \ sat\xE9lite nos Distritos de Mossuril e Ilha de Mo\xE7ambique, Prov\xEDncia de\
  \ Nampula, usando imagens sat\xE9lite tirada no dia 18 de janeiro de 2025 \xE0s\
  \ 09:34, hor\xE1rio local. Dentro da \xE1rea analisada de aproximadamente 4.600\
  \ km\xB2, estima-se que 60 km\xB2 de terra tenham sido afetados pelas \xE1guas das\
  \ enchentes. Com base nos dados demogr\xE1ficos espaciais do WorldPop, aproximadamente\
  \ 9.000 pessoas est\xE3o expostas ou morando perto das \xE1reas inundadas. Essa\
  \ \xE9 uma an\xE1lise preliminar e ainda n\xE3o foi validada em campo. Envie coment\xE1\
  rios sobre o solo para o Centro de Sat\xE9lites das Na\xE7\xF5es Unidas (UNOSAT)..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/extensao-de-agua-detectada-por-satelite-nos-distritos-de-mossuril-e-ilha-de-mocambique-pro]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Approximately 9,000 people exposed to or residing near inundated
      areas based on WorldPop spatial demographic data
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
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts reviewed satellite imagery acquired on January 18,\
    \ 2025 at 09:34 local time, comparing multi-temporal images to detect notable\
    \ changes in water extent. Flood water polygons were delineated across 4,600 km\xB2\
    \ of analysis area, identifying 60 km\xB2 of inundated land. Population exposure\
    \ was estimated by intersecting detected flood extent with WorldPop gridded population\
    \ data to quantify people at risk."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/extensao-de-agua-detectada-por-satelite-nos-distritos-de-mossuril-e-ilha-de-mocambique-pro
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
  description: "Mozambique - Extens\xE3o de \xE1gua detectada por sat\xE9lite nos\
    \ Distritos de Mossuril e Ilha de Mo\xE7ambique, Prov\xEDncia de Nampula, Mo\xE7\
    ambique, no dia 18 de janeiro de 2025 (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/4070/FL20250121MOZ_gdb.zip
  format: Geodatabase
  id: resource_ecef057b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250121MOZ_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Mozambique - Extens\xE3o de \xE1gua detectada por sat\xE9lite nos\
    \ Distritos de Mossuril e Ilha de Mo\xE7ambique, Prov\xEDncia de Nampula, Mo\xE7\
    ambique, no dia 18 de janeiro de 2025 (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/4070/FL20250121MOZ_SHP.zip
  format: null
  id: resource_b8517bc6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250121MOZ_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-moz_unosat_extensaodeaguadetectadapo_20250122
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-01-22'
temporal_resolution: null
title: "Mozambique - Extens\xE3o de \xE1gua detectada por sat\xE9lite nos Distritos\
  \ de Mossuril e Ilha de Mo\xE7ambique, Prov\xEDncia de Nampula, Mo\xE7ambique, no\
  \ dia 18 de janeiro de 2025"
version: null
vulnerability: null
---
