---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-9-and-13-october-2021-over-south-sudan
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: VIIRS satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-9-and-13-october-2021-over-south-sudan
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-9-and-13-october-2021-over-south-sudan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-9-and-13-october-2021-over-south-sudan
dataset_id: rdls_he-ssd_unosat_detectedwaterextentsbetwe_20211018
description: 'UNOSAT code: FL20211015SSD This map illustrates cumulative satellite-detected
  water using VIRRS in South Sudan between 09 to 13 October 2021 and 26 to 30 September
  2021. Within the analyzed extent not covered by clouds, a total of about 37,000
  km2 appear to be flooded. Based on Worldpop population data and the detected surface
  water, about 1,000,000 people are exposed or living close to flooded area. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-9-and-13-october-2021-over-south-sudan]'
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
    description: Population exposed or living close to detected flooded areas derived
      from WorldPop data
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed VIIRS satellite imagery from 9-13 October
    2021 and 26-30 September 2021 to detect cumulative water extents across South
    Sudan through multi-temporal image comparison. Detected water polygons (37,000
    km2) were intersected with WorldPop gridded population data to estimate approximately
    1,000,000 people exposed to flooded areas. This is a preliminary post-event satellite-based
    assessment not yet validated in the field.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: VIIRS satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-9-and-13-october-2021-over-south-sudan
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
  description: Satellite detected water extents between 9 and 13 October 2021 over
    South Sudan (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/SS/FL20211015SSD/FL20211015SSD_gdb.zip
  format: Geodatabase
  id: resource_25906feb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20211015SSD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 9 and 13 October 2021 over
    South Sudan (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/SS/FL20211015SSD/FL20211015SSD_SHP.zip
  format: null
  id: resource_d9bd420c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20211015SSD_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-ssd_unosat_detectedwaterextentsbetwe_20211018
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
  start: '2021-10-18'
temporal_resolution: null
title: Satellite detected water extents between 9 and 13 October 2021 over South Sudan
version: null
vulnerability: null
---
