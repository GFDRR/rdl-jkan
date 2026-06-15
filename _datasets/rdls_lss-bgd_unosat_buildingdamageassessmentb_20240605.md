---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assessment-in-bagerhat-district-khulna-division-bangladesh-as-of-4-june-20
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assessment-in-bagerhat-district-khulna-division-bangladesh-as-of-4-june-20
dataset_id: rdls_lss-bgd_unosat_buildingdamageassessmentb_20240605
description: "UNOSAT code: FL20240502BGD, GDACS ID: 1001064 This map illustrates potentially\
  \ damaged structures as observed by using a Pl\xE9iades satellite image acquired\
  \ on 4 June 2024 at 10:31 Local Time. Within the analysis extent, UNOSAT identified\
  \ 1,100 potentially damaged structures. This is a preliminary analysis and has not\
  \ yet been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/building-damage-assessment-in-bagerhat-district-khulna-division-bangladesh-as-of-4-june-20]"
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
  description: "UNOSAT analysts compared Pl\xE9iades satellite imagery acquired on\
    \ 4 June 2024 with reference imagery to identify structural damage in Bagerhat\
    \ District, Bangladesh following a tropical cyclone event. The analysis identified\
    \ 1,100 potentially damaged structures through visual interpretation of satellite\
    \ data; this is a preliminary assessment not yet validated in the field."
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
- href: https://data.humdata.org/dataset/building-damage-assessment-in-bagerhat-district-khulna-division-bangladesh-as-of-4-june-20
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone assessed via satellite
      imagery
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
  description: Building Damage Assessment in Bagerhat District, Khulna Division, Bangladesh
    as of 4 June 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3870/TC20240502BGD_GDB.zip
  format: Geodatabase
  id: resource_dbc10148
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240502BGD_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Building Damage Assessment in Bagerhat District, Khulna Division, Bangladesh
    as of 4 June 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3870/TC20240502BGD_SHP.zip
  format: null
  id: resource_87b015b5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240502BGD_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bgd_unosat_buildingdamageassessmentb_20240605
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-06-05'
temporal_resolution: null
title: Building Damage Assessment in Bagerhat District, Khulna Division, Bangladesh
  as of 4 June 2024
version: null
vulnerability: null
---
