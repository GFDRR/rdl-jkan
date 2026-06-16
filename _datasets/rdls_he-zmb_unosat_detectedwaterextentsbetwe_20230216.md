---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-07-and-11-february-2023-in-zambia
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-07-and-11-february-2023-in-zambia
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-07-and-11-february-2023-in-zambia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-07-and-11-february-2023-in-zambia
dataset_id: rdls_he-zmb_unosat_detectedwaterextentsbetwe_20230216
description: "UNOSAT code FL20230131ZMB This map illustrates cumulative satellite-detected\
  \ water using VIIRS in Zambia between 07 to 11 February 2023. Within the cloud free\
  \ analysed areas of about 653,000 km\xB2 and based on Worldpop spatial demographic\
  \ data and the maximum flood water extent, about 400,000 people out of 19 million\
  \ are potentially exposed or living close to maximum floodwaters areas. This is\
  \ a preliminary analysis and has not yet been validated in the field. Please send\
  \ ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-07-and-11-february-2023-in-zambia]"
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
    description: Population potentially exposed or living close to maximum floodwater
      areas based on WorldPop spatial demographic data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
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
  description: "UNOSAT analysts reviewed and compared VIIRS satellite imagery from\
    \ 7-11 February 2023 to detect cumulative water extents across cloud-free areas\
    \ of approximately 653,000 km\xB2 in Zambia. Population exposure estimates were\
    \ derived by intersecting the maximum flood water extent with WorldPop spatial\
    \ demographic data to identify approximately 400,000 people at risk out of 19\
    \ million total population."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-07-and-11-february-2023-in-zambia
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
  description: Satellite detected water extents between 07 and 11 February 2023 in
    Zambia (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3499/FL20220131ZMB_gdb.zip
  format: Geodatabase
  id: resource_99b27477
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220131ZMB_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 07 and 11 February 2023 in
    Zambia (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3499/FL20230131ZMB_SHP.zip
  format: null
  id: resource_2b3d7b56
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230131ZMB_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 07 and 11 February 2023 in
    Zambia (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3499/Satellite%20detected%20water%20extents%20between%2007%20and%2011%20February%202023%20in%20Zambia%20(1).xlsx
  format: null
  id: resource_52d2ae71
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Satellite detected water extents between 07 and 11 February 2023 in Zambia
    (1).xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-zmb_unosat_detectedwaterextentsbetwe_20230216
spatial:
  bbox: null
  centroid: null
  countries:
  - ZMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-02-16'
temporal_resolution: null
title: Satellite detected water extents between 07 and 11 February 2023 in Zambia
version: null
vulnerability: null
---
