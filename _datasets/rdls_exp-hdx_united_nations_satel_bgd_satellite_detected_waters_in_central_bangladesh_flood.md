---
contact_point:
  email: null
  id: attribution_contact
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/32e725a8-9f29-4ab3-8903-ba7f10ae581f
creator:
  email: null
  id: attribution_creator
  name: UNOSAT
  url: https://data.humdata.org/dataset/32e725a8-9f29-4ab3-8903-ba7f10ae581f
dataset_id: rdls_exp-hdx_united_nations_satel_bgd_satellite_detected_waters_in_central_bangladesh_flood
description: 'This map illustrates satellite-detected surface water extent in the
  central part of Bangladesh using a Sentinel-1 satellite image acquired on the 12
  August 2017 with a total surface of 4,280,650 ha. In this analyzed area; 1,644,983
  ha (38%) of lands are likely affected. These lands are are mainly cropland irrigated
  and rainfed areas and estimated to 1,576,351 ha. The population exposure analysis
  using WorldPop data shows that ~17,000,000 people are potentially affected by floods
  in the analysed zone: ~8,400,000 are located in Dhaka Division and ~5,750,000 in
  Rajshahi Division. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR-UNOSAT. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX) at
  https://data.humdata.org] [Original dataset: https://data.humdata.org/dataset/32e725a8-9f29-4ab3-8903-ba7f10ae581f]'
details: 'Caveats: This is a preliminary assessment and has not yet been validated
  in the field. It is important to consider the characteristics of the source imagery
  used in the analyses when interpreting results. For damage assessments it should
  be noted that only significant damage to the structural integrity of the buildings
  analyzed can be seen in imagery, while minor damage such as cracks or holes may
  not be visible at all. For flood extractions using radar data it is important to
  note that urban areas and highly vegetated areas may mask the flood signature and
  result in underestimation of flood waters. Users with specific questions or concerns
  should contact unosat@unitar.org to seek clarification. | Methodology: UNOSAT datasets
  and maps are produced using a variety of methods. In general, analysts closely review
  satellite imagery, often comparing two or more images together, and determine notable
  changes between the images. For damage assessments, refugee or IDP assessments,
  and similar analyses, these changes are then manually documented in the vector data
  by the analyst. For flood extractions, landcover mapping and similar analyses, a
  variety of automated remote sensing techniques are used to extract the relevant
  information which is then reviewed and revised as necessary by the analyst. In all
  cases, resulting data is then loaded into a standardized UNOSAT geodatabase and
  exported asshapefiles for dissemination. | Temporal coverage: [2017-08-15T00:00:00
  TO 2017-08-15T23:59:59] | Update frequency: Never | Last modified: 2025-11-21'
exposure:
- category: population
  dimension: population
  quantity_kind: count
  taxonomy: null
- category: agriculture
  dimension: structure
  quantity_kind: area
  taxonomy: null
- category: natural_environment
  dimension: structure
  quantity_kind: area
  taxonomy: null
extra_attributions: []
hazard:
  calculation_method: inferred
  disaster_identifiers: ''
  hazard_analysis_type: empirical
  hazard_type: flood
  intensity: wd:m
  occurrence_range: ''
  processes: pluvial_flood
  seasonality: ''
license: CC-BY-SA-4.0
loss: null
project: null
publisher:
  email: null
  id: attribution_publisher
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/32e725a8-9f29-4ab3-8903-ba7f10ae581f
purpose: null
resources:
- coordinate_system: null
  description: Dataset-level metadata exported from HDX.
  download_url: https://data.humdata.org/dataset/32e725a8-9f29-4ab3-8903-ba7f10ae581f/download_metadata?format=json
  format: JSON (json)
  id: hdx_dataset_metadata_json
  media_type: null
  spatial_resolution: null
  temporal: null
  title: HDX dataset metadata (JSON)
- coordinate_system: null
  description: Zipped geodatabase
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20170815BGD/FL20170815BGD_gdb.zip
  format: File Geodatabase (gdb)
  id: hdx_res_ed5b0d50
  media_type: null
  spatial_resolution: null
  temporal: null
  title: FL20170815BGD_gdb.zip
- coordinate_system: null
  description: Zipped shapefile
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20170815BGD/FL20170815BGD_shp.zip
  format: Shapefile (shp)
  id: hdx_res_ce506301
  media_type: null
  spatial_resolution: null
  temporal: null
  title: FL20170815BGD_shp.zip
risk_data_type:
- hazard
- exposure
schema: rdl-03
slug: rdls_exp-hdx_united_nations_satel_bgd_satellite_detected_waters_in_central_bangladesh_flood
spatial:
  countries:
  - BGD
  scale: national
title: Satellite Detected Waters in Central Bangladesh
version: null
vulnerability: null
---
