---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-bulo-burto-city-bulo-burto-district-hiraan-region-of-somalia-as-of-3-jun
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-bulo-burto-city-bulo-burto-district-hiraan-region-of-somalia-as-of-3-jun
dataset_id: rdls_hzd-som_unosat_detectedwaterextentoverbu_20230605
description: "UNOSAT code FL20230327SOM, GDACS Id: 1101908 This map illustrates satellite-detected\
  \ surface waters over Bulo Burto City, Bulo Burto District, Hiraan Region of Somalia\
  \ as observed from a Pleiades image acquired on 3 June 2023. Within the cloud free\
  \ analysed area of 14 km\xB2, about 1 km\xB2 of land appear to be flooded. Water\
  \ extent appears to have decreased by about 1 km\xB2 since 30 May 2023. This is\
  \ a preliminary analysis and has not yet been validated in the field. Please send\
  \ ground feedback to United Nations Satellite Centre (UNOSAT).. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/water-extent-over-bulo-burto-city-bulo-burto-district-hiraan-region-of-somalia-as-of-3-jun]"
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
  description: Pleiades satellite imagery acquired on 3 June 2023 was analyzed by
    UNOSAT analysts through visual interpretation and multi-temporal comparison with
    imagery from 30 May 2023 to detect changes in surface water extent. Water bodies
    were manually delineated and quantified by area, producing vector geodatabase
    and shapefile outputs of flooded areas in Bulo Burto City.
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
- href: https://data.humdata.org/dataset/water-extent-over-bulo-burto-city-bulo-burto-district-hiraan-region-of-somalia-as-of-3-jun
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
  description: Satellite detected water extent over Bulo Burto City, Bulo Burto District,
    Hiraan Region of Somalia as of 3 June 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3610/FL20230327SOM_gdb.zip
  format: Geodatabase
  id: resource_a6df24c4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230327SOM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Bulo Burto City, Bulo Burto District,
    Hiraan Region of Somalia as of 3 June 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3610/FL20230327SOM_SHP.zip
  format: null
  id: resource_f05f2e06
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230327SOM_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-som_unosat_detectedwaterextentoverbu_20230605
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
  start: '2023-06-05'
temporal_resolution: null
title: Satellite detected water extent over Bulo Burto City, Bulo Burto District,
  Hiraan Region of Somalia as of 3 June 2023
version: null
vulnerability: null
---
