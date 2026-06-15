---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flood-impact-analysis-in-khemisti-bou-ismail-and-bouharoun-communes-wilaya-of-tipaza-alger
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-analysis-in-khemisti-bou-ismail-and-bouharoun-communes-wilaya-of-tipaza-alger
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-analysis-in-khemisti-bou-ismail-and-bouharoun-communes-wilaya-of-tipaza-alger
dataset_id: rdls_hel-dza_unosat_floodimpactanalysiskhemis_20230529
description: 'UNOSAT code FL20230526DZA, GDACS Id: 1102025 This map illustrates satellite-detected
  flash floods in Khemisti, Bou Ismail and Bouharoun Communes, Wilaya of Tipaza, Algeria
  as observed using Sentinel-2 satellite imagery acquired on 27 May 2023 at 11:36
  local time. Within the surface analysed of 12,000 ha, about 63 ha of potentially
  affected area observed. UNOSAT identified 2 damaged ports, 794 affected and potentially
  affected structures & 31 affected and potentially affected roads. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/flood-impact-analysis-in-khemisti-bou-ismail-and-bouharoun-communes-wilaya-of-tipaza-alger]'
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
    description: Affected and potentially affected structures identified through satellite
      imagery analysis
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
    description: Affected and potentially affected roads and ports in the flood-impacted
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
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-2 satellite imagery acquired on 27 May 2023 was analyzed by
    UNOSAT analysts through multi-temporal comparison to detect flash flood extent
    and identify surface water changes. Affected structures and infrastructure were
    identified through visual interpretation of the satellite imagery within the 12,000
    ha study area. The preliminary analysis maps flood-affected areas and counts of
    impacted assets without field validation.
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
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/flood-impact-analysis-in-khemisti-bou-ismail-and-bouharoun-communes-wilaya-of-tipaza-alger
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Affected and potentially affected structures from flash flooding
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Affected and potentially affected roads and ports from flash flooding
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood impact analysis in Khemisti, Bou Ismail and Bouharoun Communes,
    Wilaya of Tipaza, Algeria as of 27 May 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3603/FL20230526DZA_gdb.zip
  format: Geodatabase
  id: resource_30f1f174
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
  description: Flood impact analysis in Khemisti, Bou Ismail and Bouharoun Communes,
    Wilaya of Tipaza, Algeria as of 27 May 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3603/FL20230526DZA_SHP.zip
  format: null
  id: resource_3ce9c1d4
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
  description: Flood impact analysis in Khemisti, Bou Ismail and Bouharoun Communes,
    Wilaya of Tipaza, Algeria as of 27 May 2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3603/PopulationExposure_FL20230526DZA_29May2023.xlsx
  format: null
  id: resource_868b31ce
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
slug: rdls_hel-dza_unosat_floodimpactanalysiskhemis_20230529
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
  start: '2023-05-29'
temporal_resolution: null
title: Flood impact analysis in Khemisti, Bou Ismail and Bouharoun Communes, Wilaya
  of Tipaza, Algeria as of 27 May 2023
version: null
vulnerability: null
---
