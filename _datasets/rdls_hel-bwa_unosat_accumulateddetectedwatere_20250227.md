---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/accumulated-water-extents-in-gaborone-south-east-and-kgatleng-districts-botswana-as-of-23-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/accumulated-water-extents-in-gaborone-south-east-and-kgatleng-districts-botswana-as-of-23-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/accumulated-water-extents-in-gaborone-south-east-and-kgatleng-districts-botswana-as-of-23-
dataset_id: rdls_hel-bwa_unosat_accumulateddetectedwatere_20250227
description: "UNOSAT code: FL20250220BWA, GDACS ID: 1103128 This map illustrates the\
  \ satellite-detected accumulated flood extent in Gaborone, South East District,\
  \ Botswana, as observed from Planet imagery and very high-resolution Pleiades imagery\
  \ acquired between 23 and 25 February 2025. Within the analyzed area of approximately\
  \ 700 km\xB2, an estimated 30 km\xB2 appears to be affected by floodwaters. UNITAR-UNOSAT\
  \ has identified around 900 potentially affected structures, along with 24 affected\
  \ road segments and 10 affected bridges within the analyzed area. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/accumulated-water-extents-in-gaborone-south-east-and-kgatleng-districts-botswana-as-of-23-]"
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
    description: Building structures identified as potentially affected by floodwaters
      in the analyzed area
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
    description: Road segments and bridges within the flood-affected area
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed Planet and Pleiades satellite imagery acquired\
    \ 23-25 February 2025 over Gaborone, South East District, and Kgatleng Districts,\
    \ Botswana. Multi-temporal image comparison identified notable changes in water\
    \ extent, delineating accumulated flood areas of approximately 30 km\xB2. Spatial\
    \ analysis of the flood extent polygon identified 900 potentially affected structures\
    \ and 34 affected infrastructure elements (roads and bridges) within the 700 km\xB2\
    \ study area."
  sources:
  - id: source_1
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
- href: https://data.humdata.org/dataset/accumulated-water-extents-in-gaborone-south-east-and-kgatleng-districts-botswana-as-of-23-
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Approximately 900 potentially affected structures identified from
      satellite imagery analysis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
    description: 24 affected road segments and 10 affected bridges from fluvial flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
  description: Accumulated satellite-detected water extents in Gaborone, South East
    and Kgatleng Districts, Botswana as of 23 to 25 February 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4081/FL20250220BWA_gdb.zip
  format: Geodatabase
  id: resource_c47f1554
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250220BWA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Accumulated satellite-detected water extents in Gaborone, South East
    and Kgatleng Districts, Botswana as of 23 to 25 February 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4081/FL20250220BWA_SHP.zip
  format: null
  id: resource_152df5c6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250220BWA_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-bwa_unosat_accumulateddetectedwatere_20250227
spatial:
  bbox: null
  centroid: null
  countries:
  - BWA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-02-27'
temporal_resolution: null
title: Accumulated satellite-detected water extents in Gaborone, South East and Kgatleng
  Districts, Botswana as of 23 to 25 February 2025
version: null
vulnerability: null
---
