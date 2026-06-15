---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-bu-aale-city-bu-aale-district-middle-juba-region-somalia-13-november-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-bu-aale-city-bu-aale-district-middle-juba-region-somalia-13-november-2023
dataset_id: rdls_hzd-som_unosat_detectedwaterextentbuaale_20231113
description: 'UNOSAT code FL20231105SOM This map illustrates satellite-detected surface
  waters in Bu''aale City, Bu''aale District, Middle Juba Region, Somalia as observed
  from a Pleiades image acquired on 13 November 2023 at 07:24 UTC. Within the analysed
  area of about 1,000 hectares about 700 hectares of land appear to be flooded. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to United Nations Satellite Centre (UNOSAT).. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/water-extent-in-bu-aale-city-bu-aale-district-middle-juba-region-somalia-13-november-2023]'
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
  description: Pleiades satellite imagery acquired on 13 November 2023 was analyzed
    by UNOSAT analysts through visual interpretation and comparison with reference
    imagery to detect surface water extent. Flooded area was delineated within a 1,000
    hectare study area in Bu'aale City, resulting in a preliminary geodatabase product
    of observed water extent.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-in-bu-aale-city-bu-aale-district-middle-juba-region-somalia-13-november-2023
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
  description: Satellite detected water extent in Bu'aale City, Bu'aale District,
    Middle Juba Region, Somalia, 13 November 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3735/FL20231105SOM.gdb.zip
  format: Geodatabase
  id: resource_9f611648
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231105SOM.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-som_unosat_detectedwaterextentbuaale_20231113
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
  start: '2023-11-13'
temporal_resolution: null
title: Satellite detected water extent in Bu'aale City, Bu'aale District, Middle Juba
  Region, Somalia, 13 November 2023
version: null
vulnerability: null
---
