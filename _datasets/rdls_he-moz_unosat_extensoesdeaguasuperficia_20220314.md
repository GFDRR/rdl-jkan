---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/extensoes-de-agua-superficias-detectadas-por-satelite-na-provincia-de-nampula-mocambique-n
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/extensoes-de-agua-superficias-detectadas-por-satelite-na-provincia-de-nampula-mocambique-n
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/extensoes-de-agua-superficias-detectadas-por-satelite-na-provincia-de-nampula-mocambique-n
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/extensoes-de-agua-superficias-detectadas-por-satelite-na-provincia-de-nampula-mocambique-n
dataset_id: rdls_he-moz_unosat_extensoesdeaguasuperficia_20220314
description: "UNOSAT code: TC20220311MOZ Este mapa ilustra \xE1gua superficias detectadas\
  \ por sat\xE9lite nos distritos de Mossuril, Mogincual e Li\xFApo, Prov\xEDncia\
  \ de Nampula em Mo\xE7ambique, no dia 13 de mar\xE7o, 2022, as 17:44 hora local.\
  \ Dentro da \xE1rea analisada de cerca de 14,000 km2, um total de 110 km2 aparece\
  \ inundada. Baseado nos dados de popula\xE7\xE3o do Worldpop e na \xE1guas superficiais,\
  \ cerca de 12,000 pessoas est\xE3o potencialmente expostos ou vivem perto das \xE1\
  reas inundadas. Esto sao an\xE1lises preliminar e ainda n\xE3o foram verificados\
  \ no terreno. Por favor, envie coment\xE1rios United Nations Satellite Centre (UNOSAT).\
  \ Nota importante: An\xE1lises de inunda\xE7\xE3oes a partir de imagens radar podem\
  \ subestimar a presen\xE7a de \xE1guas acumuladas em \xE1reas constru\xEDdas e \xE1\
  reas de vegeta\xE7\xE3o densa devido \xE0s propriedades de retrodifus\xE3o do sinal\
  \ radar.. [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/extensoes-de-agua-superficias-detectadas-por-satelite-na-provincia-de-nampula-mocambique-n]"
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
    description: Residential population potentially exposed to or living near inundated
      areas, derived from WorldPop data
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts compared satellite imagery acquired on 13 March 2022\
    \ to detect surface water extent changes in Nampula Province. Inundated areas\
    \ (110 km\xB2) were mapped across three districts. Population exposure was estimated\
    \ by intersecting detected water extent with WorldPop gridded population data,\
    \ yielding approximately 12,000 potentially affected persons. This is a preliminary\
    \ post-event damage assessment based on satellite observation without field verification."
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/extensoes-de-agua-superficias-detectadas-por-satelite-na-provincia-de-nampula-mocambique-n
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
  description: "Mozambique - Extens\xF5es de \xE1gua superficias detectadas por sat\xE9\
    lite na Prov\xEDncia de Nampula, Mo\xE7ambique, no dia 13 de mar\xE7o de 2022\
    \ (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/MZ/TC20220311MOZ/TC20220311MOZ_gdb.zip
  format: Geodatabase
  id: resource_e6785af2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220311MOZ_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Mozambique - Extens\xF5es de \xE1gua superficias detectadas por sat\xE9\
    lite na Prov\xEDncia de Nampula, Mo\xE7ambique, no dia 13 de mar\xE7o de 2022\
    \ (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/MZ/TC20220311MOZ/TC20220311MOZ_SHP.zip
  format: null
  id: resource_8eb81be4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220311MOZ_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-moz_unosat_extensoesdeaguasuperficia_20220314
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
  start: '2022-03-14'
temporal_resolution: null
title: "Mozambique - Extens\xF5es de \xE1gua superficias detectadas por sat\xE9lite\
  \ na Prov\xEDncia de Nampula, Mo\xE7ambique, no dia 13 de mar\xE7o de 2022"
version: null
vulnerability: null
---
