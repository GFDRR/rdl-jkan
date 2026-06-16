---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-puli-khumri-area-baghlan-province-afghanistan-november-13-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-puli-khumri-area-baghlan-province-afghanistan-november-13-2015
dataset_id: rdls_lss-afg_unosat_geodatadamageassessmentpu_20151113
description: 'This map illustrates satellite-detected potentially damaged structures
  in the area of Puli Khumri, Baghlan Province, Afghanistan. The Puli Khumri area
  is located approximately 190 kilometers southwest of the 26 October 2015 earthquake
  epicenter. Using Pleiades satellite imagery acquired 03 November 2015 and WorldView-2
  imagery from 01 September 2014, UNITAR - UNOSAT identified 133 potentially damaged
  structures. Note that some areas heavily damaged in the south of Qahwakhana appear
  to have also been affected by a limited landslide. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  - UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-puli-khumri-area-baghlan-province-afghanistan-november-13-2015]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts compared Pleiades satellite imagery acquired 03 November
    2015 (post-event) with WorldView-2 imagery from 01 September 2014 (pre-event)
    to identify 133 potentially damaged structures in the Puli Khumri area through
    visual change detection analysis. This is a preliminary post-earthquake damage
    assessment derived from satellite remote sensing without field validation.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-puli-khumri-area-baghlan-province-afghanistan-november-13-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected potentially damaged structures from the 26 October
      2015 earthquake in Puli Khumri area
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: Geodata of Damage Assessment of Puli Khumri Area, Baghlan Province,
    Afghanistan (Shapefile)
  download_url: https://cern.ch/unosat-maps/AF/EQ20151026AFG/EQ20151026AFG_shp.zip
  format: null
  id: resource_00bf7325
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20151026AFG_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Puli Khumri Area, Baghlan Province,
    Afghanistan (Shapefile)
  download_url: https://cern.ch/unosat-maps/AF/EQ20151026AFG/EQ20151026AFG.gdb.zip
  format: null
  id: resource_559b65c5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20151026AFG.gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_unosat_geodatadamageassessmentpu_20151113
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-11-13'
temporal_resolution: null
title: Geodata of Damage Assessment of Puli Khumri Area, Baghlan Province, Afghanistan
version: null
vulnerability: null
---
