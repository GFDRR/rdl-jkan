---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aliabad-area-hunza-nagar-district-pakistan-november-05-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aliabad-area-hunza-nagar-district-pakistan-november-05-2015
dataset_id: rdls_lss-pak_unosat_geodatadamageassessmental_20151105
description: "This map illustrates satellite-detected damage and destruction in the\
  \ Aliabad area of Hunza Nagar District, Pakistan and located roughly 350 km east\
  \ of the 26 October 2015 earthquake epicenter. Using a Pl\xE9iades satellite image\
  \ acquired 31 October 2015 and a WorldView-2 image acquired 12 August 2015, UNITAR-UNOSAT\
  \ identified 55 potentially damaged structures. This is a preliminary analysis and\
  \ has not yet been validated in the field. Please send ground feedback to UNITAR\
  \ - UNOSAT.. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aliabad-area-hunza-nagar-district-pakistan-november-05-2015]"
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
  description: "UNOSAT analysts compared Pl\xE9iades satellite imagery acquired 31\
    \ October 2015 (post-event) with WorldView-2 imagery from 12 August 2015 (pre-event)\
    \ to detect structural damage in the Aliabad area through visual interpretation\
    \ of notable changes between the two images, identifying 55 potentially damaged\
    \ structures as a preliminary unvalidated assessment."
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aliabad-area-hunza-nagar-district-pakistan-november-05-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected building damage from the 26 October 2015 earthquake
      in Hunza Nagar District
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
  description: Geodata of Damage Assessment of Aliabad Area, Hunza Nagar District,
    Pakistan (Shapefile)
  download_url: https://cern.ch/unosat-maps/AF/EQ20151026AFG/EQ20151026AFG_shp.zip
  format: null
  id: resource_6bd6a4cb
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
  description: Geodata of Damage Assessment of Aliabad Area, Hunza Nagar District,
    Pakistan (Shapefile)
  download_url: https://cern.ch/unosat-maps/AF/EQ20151026AFG/EQ20151026AFG.gdb.zip
  format: null
  id: resource_a06845f6
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
slug: rdls_lss-pak_unosat_geodatadamageassessmental_20151105
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-11-05'
temporal_resolution: null
title: Geodata of Damage Assessment of Aliabad Area, Hunza Nagar District, Pakistan
version: null
vulnerability: null
---
