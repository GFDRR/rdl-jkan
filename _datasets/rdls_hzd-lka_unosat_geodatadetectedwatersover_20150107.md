---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-ampara-and-batticaloa-districts-sri-january-07-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-ampara-and-batticaloa-districts-sri-january-07-2015
dataset_id: rdls_hzd-lka_unosat_geodatadetectedwatersover_20150107
description: 'This map illustrates satellite-detected areas of flood water as observed
  in Sentinel-1 imagery collected 24 November 2014 and 18 December 2014. Waters extended
  along coastal areas and shores of inland lakes, with few large bodies of flood waters
  detected. Numerous roads and railroads are likely inundated by flood waters which
  may impede transport in those areas. It is likely that flood waters have been systematically
  underestimated in highly vegetated areas along main river banks, and within built-up
  urban areas because of the characteristics of the satellite data used. This analysis
  has not yet been validated in the field. Please send ground feedback to UNITAR /UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-ampara-and-batticaloa-districts-sri-january-07-2015]'
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
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts interpreted Sentinel-1 SAR imagery acquired on 24 November
    2014 and 18 December 2014, identifying water bodies through multi-temporal image
    comparison and manual delineation. Flood water extent polygons were digitized
    with confidence levels and field validation flags recorded. The dataset represents
    observed post-event flood inundation in coastal and inland areas of Sri Lanka.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-satellite-detected-waters-over-ampara-and-batticaloa-districts-sri-january-07-2015
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
  description: Geodata of Satellite Detected Waters Over Ampara and Batticaloa Districts,
    Sri Lanka (Shapefile)
  download_url: https://cern.ch/unosat-maps/LK/FL20141230LKA/FL20141229LKA_shp.zip
  format: null
  id: resource_a8705ac1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20141229LKA_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Satellite Detected Waters Over Ampara and Batticaloa Districts,
    Sri Lanka (Shapefile)
  download_url: https://cern.ch/unosat-maps/LK/FL20141230LKA/FL20141229LKA_gdb.zip
  format: null
  id: resource_b8398b8f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20141229LKA_gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-lka_unosat_geodatadetectedwatersover_20150107
spatial:
  bbox: null
  centroid: null
  countries:
  - LKA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-01-07'
temporal_resolution: null
title: Geodata of Satellite Detected Waters Over Ampara and Batticaloa Districts,
  Sri Lanka
version: null
vulnerability: null
---
