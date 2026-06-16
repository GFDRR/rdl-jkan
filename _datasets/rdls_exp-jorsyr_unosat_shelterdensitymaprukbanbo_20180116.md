---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/shelter-density-map-at-rukban-border-crossing-syria-jordan-border-2761
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/shelter-density-map-at-rukban-border-crossing-syria-jordan-border-2761
dataset_id: rdls_exp-jorsyr_unosat_shelterdensitymaprukbanbo_20180116
description: 'This map illustrates shelters in the area of the Rukban border crossing
  on the Syrian-Jordanian border. Using a satellite image collected by the Deimos-2
  satellite on 10 January 2018, UNOSAT located 10,418 probable shelters along the
  Jordanian side of the border, 25 kilometers southwest of the Al Waleed crossing.
  This is a 6.5 percent increase in apparent shelters visible compared to the previous
  UNOSAT analysis done using an image collected 21 September 2017. Due to the small
  size and the irregularity of the shelters it is likely that some shelters may have
  been missed in this analysis, or some shelters were included erroneously. Due to
  the scale of this map and the lack of suitable border information at this scale,
  the border in this map has been excluded. This map is intended for field support
  and local authorities should be consulted for boundary information. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR-UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/shelter-density-map-at-rukban-border-crossing-syria-jordan-border-2761]'
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
    description: Shelter structures identified via satellite imagery analysis at Rukban
      border crossing
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
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts interpreted Deimos-2 satellite imagery acquired on
    10 January 2018 of the Rukban border crossing area, manually identifying 10,418
    probable shelter structures on the Jordanian side of the Syria-Jordan border.
    Change detection was performed by comparing this image to a previous acquisition
    from 21 September 2017 to quantify temporal trends in shelter density.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/shelter-density-map-at-rukban-border-crossing-syria-jordan-border-2761
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
  description: Shelter density map at Rukban border crossing, Syria-Jordan Border
    (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/CE20130604SYR_Rukban_20180110.gdb.zip
  format: Geodatabase
  id: resource_cb0d886f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130604SYR_Rukban_20180110.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Shelter density map at Rukban border crossing, Syria-Jordan Border
    (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/CE20130604SYR_Rukban_20180110_shp.zip
  format: null
  id: resource_2aabb5fa
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130604SYR_Rukban_20180110_shp.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-jorsyr_unosat_shelterdensitymaprukbanbo_20180116
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  - JOR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-01-16'
temporal_resolution: null
title: Shelter density map at Rukban border crossing, Syria-Jordan Border
version: null
vulnerability: null
---
