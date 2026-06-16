---
attributions:
- entity:
    affiliation: null
    email: null
    name: Worldpop
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-21-july-2020-over-northwestern-region-of-bangladesh
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-1
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-21-july-2020-over-northwestern-region-of-bangladesh
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-21-july-2020-over-northwestern-region-of-bangladesh
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-21-july-2020-over-northwestern-region-of-bangladesh
dataset_id: rdls_he-bgd_unosat_detectedwaterextentas21ju_20200722
description: 'UNOSAT code: FL20200713BGD This map illustrates satellite-detected surface
  waters over Khulna, Rajshahi and Rangpur Division of Bangladesh of Bangladesh as
  observed from a Sentinel-1 image acquired on 9 July 2020 and 21 July 2020. Within
  the analyzed area of about 15,000 km2, a total of about 3,600 km2 of lands appear
  to be flooded. Based on Worldpop population data and the detected surface waters,
  about 2,507,000 people are potentially exposed or living close to flooded areas.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR - UNOSAT. Important Note: Flood analysis from Sentinel-1
  image acquired on 9 July 2020 and 21 July 2020 may underestimate the presence of
  standing. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-21-july-2020-over-northwestern-region-of-bangladesh]'
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
    description: Population potentially exposed or living close to satellite-detected
      flooded areas
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
  description: "Sentinel-1 SAR imagery from 9 July and 21 July 2020 was analyzed by\
    \ UNOSAT to detect surface water extent changes through visual comparison of satellite\
    \ images. Detected flooded areas (~3,600 km\xC2\xB2) were intersected with Worldpop\
    \ population distribution data to estimate approximately 2.5 million people potentially\
    \ exposed to flooding in Khulna, Rajshahi, and Rangpur divisions."
  sources:
  - id: source_1
    license: null
    name: Worldpop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Sentinel-1
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-21-july-2020-over-northwestern-region-of-bangladesh
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
  description: Satellite detected water extent as of 21 July 2020 over Northwestern
    region of Bangladesh (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20200713BGD/FL20200713BGD_gdb.zip
  format: Geodatabase
  id: resource_f9f87a33
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200713BGD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent as of 21 July 2020 over Northwestern
    region of Bangladesh (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20200713BGD/FL20200713BGD_SHP.zip
  format: null
  id: resource_b888d42b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200713BGD_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgd_unosat_detectedwaterextentas21ju_20200722
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
  start: '2020-07-22'
temporal_resolution: null
title: Satellite detected water extent as of 21 July 2020 over Northwestern region
  of Bangladesh
version: null
vulnerability: null
---
