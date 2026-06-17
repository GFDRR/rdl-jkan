---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-23-and-27-february-2022-over-south-sudan
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-23-and-27-february-2022-over-south-sudan
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-23-and-27-february-2022-over-south-sudan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-23-and-27-february-2022-over-south-sudan
dataset_id: rdls_he-ssd_unosat_detectedwaterextentsbetwe_20220302
description: 'UNOSAT code: FL20220119SSD This map illustrates cumulative satellite-detected
  water using VIIRS in South Sudan between 23 to 27 Feb. 2022 compared with the period
  from 11 to 15 Feb. 2022. Within the cloud free analyzed areas of about 629,000 km2,
  a total of about 21,200 km2 of lands appear to be affected with flood waters. Water
  extent appears to have decreased about 8,000 km2 since the period between 11 to
  15 Feb. 2022. Based on Worldpop population data and the maximal flood water coverage,
  ~522,000 people are potentially exposed or living close to flooded areas. This is
  a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-23-and-27-february-2022-over-south-sudan]'
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
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed VIIRS satellite imagery from 23-27 February\
    \ 2022 and compared it with baseline imagery from 11-15 February 2022 to detect\
    \ cumulative water extent changes. Detected flood water polygons (21,200 km\xC2\
    \xB2 total) were intersected with WorldPop population grids to estimate ~522,000\
    \ people potentially exposed to flooded areas."
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-23-and-27-february-2022-over-south-sudan
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
  description: Satellite detected water extents between 23 and 27 February 2022 over
    South Sudan (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/SS/FL20220119SSD/FL20220119SSD_gdb.zip
  format: Geodatabase
  id: resource_024143f9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220119SSD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 23 and 27 February 2022 over
    South Sudan (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/SS/FL20220119SSD/FL20220119SSD_SHP.zip
  format: null
  id: resource_ea820ed9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220119SSD_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-ssd_unosat_detectedwaterextentsbetwe_20220302
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-03-02'
temporal_resolution: null
title: Satellite detected water extents between 23 and 27 February 2022 over South
  Sudan
version: null
vulnerability: null
---
