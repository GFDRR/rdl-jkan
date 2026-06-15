---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-damage-in-ile-de-mozambique-as-of-18-march-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-damage-in-ile-de-mozambique-as-of-18-march-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-damage-in-ile-de-mozambique-as-of-18-march-2025
dataset_id: rdls_lss-moz_unosat_detecteddamageiledeas18ma_20250321
description: "UNOSAT code: TC20250308MOZ, GDACS ID: 1001154 This map shows the locations\
  \ where damage was detected based on a very high resolution satellite image collected\
  \ 18 March 2025 when compared to very high resolution imagery by Airbus from October\
  \ 2023 and February 2024 (south only), available through Google Earth Pro. Between\
  \ October 2023 and March 2025, multiple cyclones have passed over \xCEle de Mozambique.\
  \ Across the \xCEle de Mozambique, 78 damaged buildings were detected and accumulations\
  \ of sand indicative of prior flooding were observed on roads and in public spaces.\
  \ This is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-damage-in-ile-de-mozambique-as-of-18-march-2025]"
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
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared very high resolution satellite imagery from
    October 2023 and February 2024 baseline with March 2025 post-event imagery to
    detect damage signatures. Damaged buildings (n=78) and flood indicators (sand
    accumulation on roads/public spaces) were manually identified and vectorized as
    point and polygon features, attributed with confidence levels and damage classification.
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
- href: https://data.humdata.org/dataset/satellite-detected-damage-in-ile-de-mozambique-as-of-18-march-2025
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclones detected via satellite
      imagery comparison
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
    description: Flood impacts on roads and public spaces indicated by sand accumulation
      from prior cyclone-driven flooding
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
  description: "Satellite-detected damage in \xCEle de Mozambique as of 18 March 2025\
    \ (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/4091/TC20250308MOZ_GDB.zip
  format: Geodatabase
  id: resource_78e81916
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20250308MOZ_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Satellite-detected damage in \xCEle de Mozambique as of 18 March 2025\
    \ (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/4091/TC20250308MOZ_SHP.zip
  format: null
  id: resource_3d6b859f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20250308MOZ_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-moz_unosat_detecteddamageiledeas18ma_20250321
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
  start: '2025-03-21'
temporal_resolution: null
title: "Satellite-detected damage in \xCEle de Mozambique as of 18 March 2025"
version: null
vulnerability: null
---
