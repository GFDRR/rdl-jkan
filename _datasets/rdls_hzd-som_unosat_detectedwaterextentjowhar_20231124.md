---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-jowhar-city-jowhar-district-middle-shabelle-region-somalia-as-of-22-novemb
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-jowhar-city-jowhar-district-middle-shabelle-region-somalia-as-of-22-novemb
dataset_id: rdls_hzd-som_unosat_detectedwaterextentjowhar_20231124
description: 'UNOSAT code: FL20231105SOM This map illustrates satellite-detected surface
  waters in Jowhar City, Jowhar District, Middle Shabelle Region, Somalia as observed
  from a Radarsat RCM-3 image acquired on 11 and 22 November 2023 and ad Worldview-2
  image acquired on the 22 November 2023. Within the analysed area of 148 km2 about
  31 km2 of land appears to be flooded. The water seems to have increased about 11
  km2 since the 11 Nov. 2023. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to the United Nations Satellite
  Centre (UNOSAT).. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-jowhar-city-jowhar-district-middle-shabelle-region-somalia-as-of-22-novemb]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed Radarsat RCM-3 imagery acquired on 11 and\
    \ 22 November 2023 and Worldview-2 imagery from 22 November 2023 to detect surface\
    \ water extent through multi-temporal satellite image comparison. The analysis\
    \ identified 31 km\xB2 of flooded land within a 148 km\xB2 study area and quantified\
    \ water extent increase of 11 km\xB2 between the two observation dates."
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
- href: https://data.humdata.org/dataset/water-extent-in-jowhar-city-jowhar-district-middle-shabelle-region-somalia-as-of-22-novemb
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
  description: Satellite detected water extent in Jowhar City, Jowhar District, Middle
    Shabelle Region, Somalia as of 22 November 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3753/FL20231105SOM.gdb.zip
  format: Geodatabase
  id: resource_2e87c578
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
  description: Satellite detected water extent in Jowhar City, Jowhar District, Middle
    Shabelle Region, Somalia as of 22 November 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3753/FL20231105SOM_SHP.zip
  format: null
  id: resource_dc2f3a8c
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
slug: rdls_hzd-som_unosat_detectedwaterextentjowhar_20231124
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
  start: '2023-11-24'
temporal_resolution: null
title: Satellite detected water extent in Jowhar City, Jowhar District, Middle Shabelle
  Region, Somalia as of 22 November 2023
version: null
vulnerability: null
---
