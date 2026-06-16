---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/west-java-earthquake-21-november-2022-m-5-6-unosat-live-web-map
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/west-java-earthquake-21-november-2022-m-5-6-unosat-live-web-map
dataset_id: rdls_lss-idn_unosat_westjavaearthquake21novem_20221123
description: 'UNOSAT code EQ20221121IDN, GDACS Id: 1347183 Live web map providing
  geospatial information about damaged caused by the earthquake that stroke Indonesia
  on 21 November 2022. This web map gives an updated overview over potentially damaged
  and damaged buildings based on very high-resolution satellite images.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/west-java-earthquake-21-november-2022-m-5-6-unosat-live-web-map]'
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
  description: UNOSAT analysts conducted post-event damage assessment by comparing
    pre- and post-earthquake very high-resolution satellite imagery of the West Java
    region, identifying and mapping buildings with notable structural damage or destruction
    caused by the M5.6 earthquake on 21 November 2022.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/west-java-earthquake-21-november-2022-m-5-6-unosat-live-web-map
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from the 21 November 2022 M5.6
      West Java earthquake based on satellite imagery analysis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: Indonesia - West Java Earthquake (21 November 2022, M 5.6) - UNOSAT
    Live Web Map (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3451/EQ20221121IDN_gdb.zip
  format: Geodatabase
  id: resource_76904373
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20221121IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Indonesia - West Java Earthquake (21 November 2022, M 5.6) - UNOSAT
    Live Web Map (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3451/EQ20221121IDN_SHP.zip
  format: null
  id: resource_c8f7814a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20221121IDN_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-idn_unosat_westjavaearthquake21novem_20221123
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-11-23'
temporal_resolution: null
title: Indonesia - West Java Earthquake (21 November 2022, M 5.6) - UNOSAT Live Web
  Map
version: null
vulnerability: null
---
