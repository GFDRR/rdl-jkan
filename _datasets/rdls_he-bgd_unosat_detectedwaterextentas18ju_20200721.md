---
attributions:
- entity:
    affiliation: null
    email: null
    name: TerraSAR-X satellite imagery
    url: https://data.humdata.org/dataset/water-extent-as-of-18-july-2020-over-eastern-part-of-sylhet-division-bangladesh
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-as-of-18-july-2020-over-eastern-part-of-sylhet-division-bangladesh
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-as-of-18-july-2020-over-eastern-part-of-sylhet-division-bangladesh
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-as-of-18-july-2020-over-eastern-part-of-sylhet-division-bangladesh
dataset_id: rdls_he-bgd_unosat_detectedwaterextentas18ju_20200721
description: 'UNOSAT code: FL20200713BGD This map illustrates satellite-detected surface
  waters over the Eastern part of the Sylhet division of Bangladesh as observed from
  a TerraSAR-X image acquired on 18 July 2020 due to the current monsoon rains. Within
  the analyzed area of about 8,600 km2, a total of about 2,200 km2 of lands appear
  to be flooded. This is a preliminary analysis and has not yet been validated in
  the field. Based on WorldPop population data and the detected surface waters, about
  2,000,000 people area potentially exposed or living close to flooded areas. Please
  send ground feedback to UNITAR - UNOSAT. Important Note: Flood analysis from radar
  images may underestimate the presence of standing waters in built-up areas and densely
  vegetated areas due to backscattering properties of the radar signal.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-as-of-18-july-2020-over-eastern-part-of-sylhet-division-bangladesh]'
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
    description: Population potentially exposed or living close to detected flooded
      areas, estimated at approximately 2 million people based on WorldPop data
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
  description: "Satellite imagery from TerraSAR-X acquired on 18 July 2020 was analyzed\
    \ by UNOSAT to detect surface water extent through comparison with reference imagery.\
    \ Detected flooded areas (approximately 2,200 km\xC2\xB2) were then intersected\
    \ with WorldPop gridded population data to estimate population exposure in the\
    \ Eastern Sylhet Division during the 2020 monsoon flooding event."
  sources:
  - id: source_1
    license: null
    name: TerraSAR-X satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-as-of-18-july-2020-over-eastern-part-of-sylhet-division-bangladesh
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
  description: Satellite detected water extent as of 18 July 2020 over Eastern part
    of Sylhet Division, Bangladesh (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20200713BGD/FL20200713BGD_gdb.zip
  format: Geodatabase
  id: resource_0bbb1674
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
  description: Satellite detected water extent as of 18 July 2020 over Eastern part
    of Sylhet Division, Bangladesh (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20200713BGD/FL20200713BGD_SHP.zip
  format: null
  id: resource_8354b29c
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
slug: rdls_he-bgd_unosat_detectedwaterextentas18ju_20200721
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
  start: '2020-07-21'
temporal_resolution: null
title: Satellite detected water extent as of 18 July 2020 over Eastern part of Sylhet
  Division, Bangladesh
version: null
vulnerability: null
---
