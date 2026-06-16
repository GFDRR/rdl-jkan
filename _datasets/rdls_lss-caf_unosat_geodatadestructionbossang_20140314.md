---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNOSAT
    url: https://data.humdata.org/dataset/geodata-of-destruction-in-bossangoa-area-ouham-central-african-republic-march-14-2014
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-destruction-in-bossangoa-area-ouham-central-african-republic-march-14-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-destruction-in-bossangoa-area-ouham-central-african-republic-march-14-2014
dataset_id: rdls_lss-caf_unosat_geodatadestructionbossang_20140314
description: 'This map illustrates locations of destroyed structures in Bossangoa,
  Central African Republic. Using a satellite image acquired 28 February 2014 and
  compared to images from 22 January 2014 and 5 December 2013, UNOSAT reviewed the
  town of Bossangoa and surrounding areas to locate signs of destroyed structures.
  A total of 1,234 destroyed structures were located in the area, though structures
  marked as destroyed on 5 December are classed as ''probable'' due to the lack of
  a previous image for comparison. Some of the destruction detected in the 28 February
  2014 image was likely a result of burning given the blackened structural remains
  visible in the imagery. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-destruction-in-bossangoa-area-ouham-central-african-republic-march-14-2014]'
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
hazard: null
license: CC-BY-4.0
lineage:
  description: Multi-temporal satellite imagery analysis comparing images from December
    2013, January 2014, and February 2014 to detect and geolocate destroyed structures.
    Analysts visually identified 1,234 destroyed structures with confidence classifications
    based on image availability for comparison.
  sources:
  - id: source_1
    license: null
    name: UNOSAT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-destruction-in-bossangoa-area-ouham-central-african-republic-march-14-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Destroyed structures identified through satellite imagery analysis
      during conflict-related violence in Bossangoa area
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: Geodata of Destruction in Bossangoa Area, Ouham, Central African Republic
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/CE20131212CAF/CE20131212CAF_shp.zip
  format: null
  id: resource_93a40e62
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131212CAF_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Destruction in Bossangoa Area, Ouham, Central African Republic
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/CE20131212CAF/CE20131212CAF.gdb.zip
  format: null
  id: resource_7361ce9a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131212CAF.gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-caf_unosat_geodatadestructionbossang_20140314
spatial:
  bbox: null
  centroid: null
  countries:
  - CAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-03-14'
temporal_resolution: null
title: Geodata of Destruction in Bossangoa Area, Ouham, Central African Republic
version: null
vulnerability: null
---
