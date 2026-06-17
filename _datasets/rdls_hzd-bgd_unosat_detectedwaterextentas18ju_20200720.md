---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-as-of-18-july-2020-over-mymensingh-rajshahi-and-rangpur-divisions-bangladesh
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-as-of-18-july-2020-over-mymensingh-rajshahi-and-rangpur-divisions-bangladesh
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-as-of-18-july-2020-over-mymensingh-rajshahi-and-rangpur-divisions-bangladesh
dataset_id: rdls_hzd-bgd_unosat_detectedwaterextentas18ju_20200720
description: 'UNOSAT code: FL20200713BGD This map illustrates satellite-detected surface
  waters over Mymensingh, Rajshahi and Rangpur Division of Bangladesh as observed
  from a TerraSAR-X image acquired on 18 July 2020. Within the analyzed area of about
  9,000 km2, a total of about 2,860 km2 of lands appear to be flooded. This is a preliminary
  analysis and has not yet been validated in the field. Please sendground feedback
  to UNITAR - UNOSAT. Important Note: Flood analysis from radar images may underestimate
  the presence of standing waters in built-up areas and densely vegetated areas due
  to backscattering properties of the radar signal.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/water-extent-as-of-18-july-2020-over-mymensingh-rajshahi-and-rangpur-divisions-bangladesh]'
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "TerraSAR-X radar satellite imagery acquired on 18 July 2020 was analyzed\
    \ by UNOSAT analysts using change detection methodology comparing pre- and post-flood\
    \ images to identify surface water extent. The analysis detected approximately\
    \ 2,860 km\xB2 of flooded land within a 9,000 km\xB2 study area covering Mymensingh,\
    \ Rajshahi, and Rangpur Divisions. This is an observed, post-event flood extent\
    \ map derived from single-date satellite observation."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-as-of-18-july-2020-over-mymensingh-rajshahi-and-rangpur-divisions-bangladesh
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
  description: Satellite detected water extent as of 18 July 2020 over Mymensingh,
    Rajshahi and Rangpur Divisions, Bangladesh (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20200713BGD/FL20200713BGD_gdb.zip
  format: Geodatabase
  id: resource_66c41261
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
  description: Satellite detected water extent as of 18 July 2020 over Mymensingh,
    Rajshahi and Rangpur Divisions, Bangladesh (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20200713BGD/FL20200713BGD_SHP.zip
  format: null
  id: resource_87ef9414
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200713BGD_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bgd_unosat_detectedwaterextentas18ju_20200720
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
  start: '2020-07-20'
temporal_resolution: null
title: Satellite detected water extent as of 18 July 2020 over Mymensingh, Rajshahi
  and Rangpur Divisions, Bangladesh
version: null
vulnerability: null
---
