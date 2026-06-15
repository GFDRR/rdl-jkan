---
attributions:
- entity:
    affiliation: null
    email: null
    name: NOAA20-VIIRS
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-between-2-6-june-2021-in-guyana
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Worldpop
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-between-2-6-june-2021-in-guyana
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-between-2-6-june-2021-in-guyana
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-between-2-6-june-2021-in-guyana
dataset_id: rdls_he-guy_unosat_detectedwaterextentbetwee_20210607
description: 'UNOSAT code: FL20210520GUY This map illustrates cumulative floods using
  NOAA20-VIIRS data in Guyana between the 2nd and the 6th of June 2021. Within the
  analyzed cloud free zones of about 200,000 km2, a total of about 5,000 km2 of lands
  appear to be flooded. Based on Worldpop population data and the detected surface
  waters, about 80,000 people are potentially exposed or living close to flooded areas.
  The potentially exposed population is mainly located in the Region 6 with ~22,000
  people, Region 3 with ~19,000 and Region 5 with ~15,000 people. This is a preliminary
  analysis that has not yet been validated in the field. Please send ground feedback
  to UNITAR-UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-between-2-6-june-2021-in-guyana]'
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
    description: Population potentially exposed to or living close to detected flooded
      areas, approximately 80,000 people distributed across Regions 3, 5, and 6
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
  description: UNOSAT analysts processed NOAA20-VIIRS satellite imagery acquired between
    June 2-6, 2021, comparing multiple images to detect notable changes in surface
    water extent. Detected flood polygons were intersected with Worldpop gridded population
    data to estimate potentially exposed populations by administrative region.
  sources:
  - id: source_1
    license: null
    name: NOAA20-VIIRS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Worldpop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-between-2-6-june-2021-in-guyana
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
  description: Satellite detected water extent between 2 & 6 June 2021 in Guyana (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/GY/FL20210520GUY/FL20210520GUY_gdb.zip
  format: Geodatabase
  id: resource_a8190b27
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210520GUY_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent between 2 & 6 June 2021 in Guyana (Zipped
    shapefile)
  download_url: https://unosat-maps.web.cern.ch/GY/FL20210520GUY/FL20210520GUY_SHP.zip
  format: null
  id: resource_05b46836
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210520GUY_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-guy_unosat_detectedwaterextentbetwee_20210607
spatial:
  bbox: null
  centroid: null
  countries:
  - GUY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-06-07'
temporal_resolution: null
title: Satellite detected water extent between 2 & 6 June 2021 in Guyana
version: null
vulnerability: null
---
