---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-flood-waters-extent-and-evolution-over-khersonska-oblast-in-ukraine-as-of-13-jun
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-flood-waters-extent-and-evolution-over-khersonska-oblast-in-ukraine-as-of-13-jun
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-flood-waters-extent-and-evolution-over-khersonska-oblast-in-ukraine-as-of-13-jun
dataset_id: rdls_hzd-ukr_unosat_floodwatersextentevolutio_20230614
description: "UNOSAT code FL20230606UKR This map illustrates satellite-detected flood\
  \ water extent and evolution using Sentinel-2 images acquired on the 13th of June\
  \ 2023 at 08:46 UTC and compared with pre-flood waters detected from Sentinel-2\
  \ images acquired on the 03rd and the 05th of June 2023. Within the analysed area\
  \ of 19,000 km\xB2, about 180 km\xB2 of land appear to be flooded. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/satellite-flood-waters-extent-and-evolution-over-khersonska-oblast-in-ukraine-as-of-13-jun]"
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
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-2 satellite imagery acquired on 13 June 2023 was compared\
    \ with pre-flood baseline imagery from 3-5 June 2023 to detect changes in water\
    \ extent. UNOSAT analysts manually reviewed and delineated flood water boundaries\
    \ through visual interpretation of spectral signatures, producing vector geometries\
    \ of inundated areas totaling approximately 180 km\xB2 across a 19,000 km\xB2\
    \ study area in Khersonska Oblast."
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
- href: https://data.humdata.org/dataset/satellite-flood-waters-extent-and-evolution-over-khersonska-oblast-in-ukraine-as-of-13-jun
  rel: source
loss:
  losses: []
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
  description: Satellite Flood Waters Extent and Evolution over Khersonska Oblast
    in Ukraine as of 13 June 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3623/FL20230606UKR_gdb.zip
  format: Geodatabase
  id: resource_41cf279b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230606UKR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Flood Waters Extent and Evolution over Khersonska Oblast
    in Ukraine as of 13 June 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3623/FL20230606UKR_SHP.zip
  format: null
  id: resource_7a06fb05
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230606UKR_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ukr_unosat_floodwatersextentevolutio_20230614
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-06-14'
temporal_resolution: null
title: Satellite Flood Waters Extent and Evolution over Khersonska Oblast in Ukraine
  as of 13 June 2023
version: null
vulnerability: null
---
