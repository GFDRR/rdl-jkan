---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/detecao-de-danos-no-patrimonio-cultural-atraves-da-analise-de-imagem-de-satelite-de-16-de-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/detecao-de-danos-no-patrimonio-cultural-atraves-da-analise-de-imagem-de-satelite-de-16-de-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/detecao-de-danos-no-patrimonio-cultural-atraves-da-analise-de-imagem-de-satelite-de-16-de-
dataset_id: rdls_hl-cpv_unosat_detecaodedanosnopatrimoni_20250902
description: "UNOSAT code: FL20250812CPV Este mapa mostra poss\xEDveis danos no patrim\xF3\
  nio cultural, detetados a 1,3 km a oeste do parque, com base numa imagem de sat\xE9\
  lite de alta resolu\xE7\xE3o obtida em 16 de Agosto de 2025, quando comparada com\
  \ uma imagem de sat\xE9lite de alta resolu\xE7\xE3o de 9 de fevereiro de 2025. Mais\
  \ especificamente, foram detetados poss\xEDveis danos numa sec\xE7\xE3o de campos\
  \ agr\xEDcolas tradicionais em socalcos (Figura 1). Esta forma tradicional de agricultura\
  \ \xE9 referida no Crit\xE9rio (v) como uma das justifica\xE7\xF5es para o Valor\
  \ Universal Excecional da \xE1rea e a sua inclus\xE3o na Lista Provis\xF3ria da\
  \ UNESCO. Tamb\xE9m foram detetados fluxos de \xE1gua e lama tanto dentro como em\
  \ torno do parque. Esta \xE9 uma an\xE1lise preliminar e ainda n\xE3o foi validada\
  \ no terreno. Qualquer informa\xE7\xE3o, por favor, envie para o Centro de Sat\xE9\
  lites das Na\xE7\xF5es Unidas (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/detecao-de-danos-no-patrimonio-cultural-atraves-da-analise-de-imagem-de-satelite-de-16-de-]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared high-resolution satellite imagery from 16
    August 2025 (post-flood) with baseline imagery from 9 February 2025 to detect
    notable changes and damage to cultural heritage sites and traditional terraced
    agricultural fields. Damage polygons were delineated and attributed with area
    measurements and event metadata.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/detecao-de-danos-no-patrimonio-cultural-atraves-da-analise-de-imagem-de-satelite-de-16-de-
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct damage to traditional terraced agricultural fields and cultural
      heritage from flooding
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
          quantity_kind: area
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cabo Verde - Dete\xE7\xE3o de danos no patrim\xF3nio cultural atrav\xE9\
    s da an\xE1lise de imagem de sat\xE9lite de 16 de Agosto de 2025 (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/4191/FL20250812CPV_gdb.zip
  format: Geodatabase
  id: resource_70f50d11
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250812CPV_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cabo Verde - Dete\xE7\xE3o de danos no patrim\xF3nio cultural atrav\xE9\
    s da an\xE1lise de imagem de sat\xE9lite de 16 de Agosto de 2025 (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/4191/FL20250812CPV_SHP.zip
  format: null
  id: resource_ab4055be
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250812CPV_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-cpv_unosat_detecaodedanosnopatrimoni_20250902
spatial:
  bbox: null
  centroid: null
  countries:
  - CPV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-09-02'
temporal_resolution: null
title: "Cabo Verde - Dete\xE7\xE3o de danos no patrim\xF3nio cultural atrav\xE9s da\
  \ an\xE1lise de imagem de sat\xE9lite de 16 de Agosto de 2025"
version: null
vulnerability: null
---
