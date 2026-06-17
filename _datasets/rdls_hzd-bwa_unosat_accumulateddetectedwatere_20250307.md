---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/accumulated-water-extents-in-gaborone-south-east-and-kgatleng-districts-botswana-as-of-4-m
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/accumulated-water-extents-in-gaborone-south-east-and-kgatleng-districts-botswana-as-of-4-m
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/accumulated-water-extents-in-gaborone-south-east-and-kgatleng-districts-botswana-as-of-4-m
dataset_id: rdls_hzd-bwa_unosat_accumulateddetectedwatere_20250307
description: "UNOSAT code: FL20250220BWA, GDACS ID: 1103128 Satellite detected water\
  \ extents in Gaborone, South East and Kgatleng Districts, Botswana as of 4 March\
  \ 2025 This map illustrates the satellite-detected accumulated flood extent in Gaborone,\
  \ South East District, Botswana, as observed from multisatellite imagery, including\
  \ Sentinel-2, PlanetScope, and Kanopus-V, acquired on 4 March 2025. Within the analyzed\
  \ area of approximately 700 km\xB2, an estimated 7 km\xB2 remains affected by floodwaters.\
  \ Floodwaters have receded by about 23 km\xB2 since 23 and 25 February 2025. This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/accumulated-water-extents-in-gaborone-south-east-and-kgatleng-districts-botswana-as-of-4-m]"
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
  description: "UNOSAT analysts processed multisatellite imagery (Sentinel-2, PlanetScope,\
    \ Kanopus-V) acquired on 4 March 2025, comparing images from 23-25 February 2025\
    \ to detect and map accumulated flood water extents across approximately 700 km\xB2\
    \ in Gaborone, South East, and Kgatleng Districts. Water classification and area\
    \ calculations (in m\xB2 and hectares) were performed on the detected features\
    \ to quantify flood coverage and recession."
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
- href: https://data.humdata.org/dataset/accumulated-water-extents-in-gaborone-south-east-and-kgatleng-districts-botswana-as-of-4-m
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
  description: Accumulated satellite-detected water extents in Gaborone, South East
    and Kgatleng Districts, Botswana as of 4 March 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4083/FL20250220BWA_gdb.zip
  format: Geodatabase
  id: resource_3e854869
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
    and Kgatleng Districts, Botswana as of 4 March 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4083/FL20250220BWA_SHP.zip
  format: null
  id: resource_663ef9db
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250220BWA_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bwa_unosat_accumulateddetectedwatere_20250307
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
  start: '2025-03-07'
temporal_resolution: null
title: Accumulated satellite-detected water extents in Gaborone, South East and Kgatleng
  Districts, Botswana as of 4 March 2025
version: null
vulnerability: null
---
