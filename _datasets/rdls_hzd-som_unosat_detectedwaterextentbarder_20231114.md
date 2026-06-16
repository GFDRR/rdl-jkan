---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-13-november-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-13-november-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-13-november-2023
dataset_id: rdls_hzd-som_unosat_detectedwaterextentbarder_20231114
description: 'UNOSAT code FL20231105SOM This map illustrates satellite-detected surface
  waters in Bardere City, Baardheere District, Gedo Region, Somalia as observed from
  a Pleiades image acquired on 12 and 13 November 2023. Within the analysed area of
  about 32 km2 about 5.3 km2 of land appears to be flooded. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-13-november-2023]'
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
  description: "Pleiades satellite imagery acquired on 12-13 November 2023 was analyzed\
    \ by UNOSAT analysts through visual interpretation and comparison with reference\
    \ imagery to detect surface water extent. The flooded area was delineated and\
    \ quantified as 5.3 km\xB2 within a 32 km\xB2 study area in Bardere City, Somalia."
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
- href: https://data.humdata.org/dataset/water-extent-in-bardere-city-baardheere-district-gedo-region-somalia-13-november-2023
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
  description: Satellite detected water extent in Bardere City, Baardheere District,
    Gedo Region, Somalia, 13 November 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3737/FL20231105SOM.gdb.zip
  format: Geodatabase
  id: resource_f6f23c13
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231105SOM.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Bardere City, Baardheere District,
    Gedo Region, Somalia, 13 November 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3737/FL20231105SOM_SHP.zip
  format: null
  id: resource_0debf67c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231105SOM_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-som_unosat_detectedwaterextentbarder_20231114
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-14'
temporal_resolution: null
title: Satellite detected water extent in Bardere City, Baardheere District, Gedo
  Region, Somalia, 13 November 2023
version: null
vulnerability: null
---
