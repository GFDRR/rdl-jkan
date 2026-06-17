---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/impact-des-inondations-du-25-26-mai-2023-dans-les-communes-de-khemisti-bousmail-et-bouharo
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/impact-des-inondations-du-25-26-mai-2023-dans-les-communes-de-khemisti-bousmail-et-bouharo
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/impact-des-inondations-du-25-26-mai-2023-dans-les-communes-de-khemisti-bousmail-et-bouharo
dataset_id: rdls_hel-dza_unosat_impactdesinondationsdu252_20230530
description: "UNOSAT code FL20230526DZA, GDACS Id: 1102025 Cette carte illustre l'\xE9\
  tendue ainsi que l'impact des crues subite tels qu'observ\xE9s \xE0 partir de l'image\
  \ satellite Sentinel-2 acquise le 27 mai 2023 \xE0 11:36 heure locale dans les communes\
  \ de Khemisti, Bousmail et Bouharoun dans la wilaya de Tipaza en Alg\xE9rie. Dans\
  \ la zone analys\xE9e d'environs 12,000 ha, une zone d'une soixantaine d'hectares\
  \ semble avoir subi des d\xE9g\xE2ts importants. Dans cette zone, UNOSAT a identifi\xE9\
  \ 2 ports endommag\xE9s, 794 structures affect\xE9es et potentiellement affect\xE9\
  es ainsi que 31 sections de routes ayant subi des d\xE9g\xE2ts. Ceci est une analyse\
  \ pr\xE9liminaire et n'a pas encore \xE9t\xE9 valid\xE9e sur le terrain. Merci de\
  \ bien vouloir adresser vos commentaires au Centre Satellitaire des Nations Unies\
  \ (UNOSAT).. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/impact-des-inondations-du-25-26-mai-2023-dans-les-communes-de-khemisti-bousmail-et-bouharo]"
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
    description: Building structures affected and potentially affected by flooding
      in Khemisti, Bousmail, and Bouharoun communes
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
    description: Port facilities and road sections exposed to flooding in the study
      area
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre- and post-event Sentinel-2 satellite imagery
    acquired on 27 May 2023 to delineate flood extent and identify damage to buildings,
    ports, and road infrastructure in three communes of Tipaza Wilaya, Algeria following
    sudden flooding on 25-26 May 2023. The analysis covered approximately 12,000 hectares
    with detailed damage assessment in a 60-hectare impact zone.
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
- href: https://data.humdata.org/dataset/impact-des-inondations-du-25-26-mai-2023-dans-les-communes-de-khemisti-bousmail-et-bouharo
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct damage to 794 building structures from fluvial flooding
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to 2 ports and 31 road sections from fluvial flooding
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
  description: "Algeria - Impact des inondations du 25/26 mai 2023 dans les communes\
    \ de Khemisti, Bousmail et Bouharoun, Wilaya de Tipaza, Alg\xE9rie (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/3604/FL20230526DZA_gdb.zip
  format: Geodatabase
  id: resource_41c86577
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230526DZA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Algeria - Impact des inondations du 25/26 mai 2023 dans les communes\
    \ de Khemisti, Bousmail et Bouharoun, Wilaya de Tipaza, Alg\xE9rie (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/3604/FL20230526DZA_SHP.zip
  format: null
  id: resource_6ca62956
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230526DZA_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Algeria - Impact des inondations du 25/26 mai 2023 dans les communes\
    \ de Khemisti, Bousmail et Bouharoun, Wilaya de Tipaza, Alg\xE9rie (Excel file)"
  download_url: https://unosat.org/static/unosat_filesystem/3604/PopulationExposure_FL20230526DZA_29May2023.xlsx
  format: null
  id: resource_5efcee8b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PopulationExposure_FL20230526DZA_29May2023.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-dza_unosat_impactdesinondationsdu252_20230530
spatial:
  bbox: null
  centroid: null
  countries:
  - DZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-30'
temporal_resolution: null
title: "Algeria - Impact des inondations du 25/26 mai 2023 dans les communes de Khemisti,\
  \ Bousmail et Bouharoun, Wilaya de Tipaza, Alg\xE9rie"
version: null
vulnerability: null
---
