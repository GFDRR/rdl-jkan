---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-gaza-damage-assessment-2014-unosat-satellite-derived-geospatial-an-october-02-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-gaza-damage-assessment-2014-unosat-satellite-derived-geospatial-an-october-02-2014
dataset_id: rdls_el-pse_unosat_geodatadamageassessment20_20141002
description: 'This report documents damage over the Gaza Strip following the July-August
  2014 conflict. It is based on analysis of commercial satellite imagery and quantifies
  damage to overall building structures, health facilities, education facilities,
  agricultural fields and greenhouses. The study also compares damage from the 2014
  conflict to that of the 2009 conflict. The analysis is supplemented by ground photos
  following UNOSAT deployment to Gaza in September 2014.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-gaza-damage-assessment-2014-unosat-satellite-derived-geospatial-an-october-02-2014]'
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
    description: Building structures across Gaza Strip classified by damage state
      from satellite imagery
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Health facilities and education facilities (schools) inventoried
      and assessed for damage
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Agricultural fields and greenhouses mapped and assessed for damage
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_3
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared multi-temporal commercial satellite imagery
    acquired before and after the July-August 2014 conflict to identify and quantify
    damage to buildings, health facilities, education facilities, and agricultural
    areas. Ground photos from September 2014 deployment validated satellite-derived
    damage classifications. Damage polygons were digitized with confidence levels
    and linked to settlement administrative units.
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
- href: https://data.humdata.org/dataset/geodata-of-gaza-damage-assessment-2014-unosat-satellite-derived-geospatial-an-october-02-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from July-August 2014 conflict
      derived from satellite imagery comparison
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to health facilities and education facilities from
      July-August 2014 conflict
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_2
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
  - asset_category: agriculture
    asset_dimension: product
    description: Direct damage to agricultural fields and greenhouses from July-August
      2014 conflict
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: 'Palestine - Geodata of Gaza Damage Assessment 2014: UNOSAT Satellite
    Derived Geospatial Analysis (Shapefile)'
  download_url: https://cern.ch/unosat-maps/PS/CE20140715PSE/CE20140715PSE.shp.zip
  format: null
  id: resource_bce8ed09
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140715PSE.shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Palestine - Geodata of Gaza Damage Assessment 2014: UNOSAT Satellite
    Derived Geospatial Analysis (Shapefile)'
  download_url: https://cern.ch/unosat-maps/PS/CE20140715PSE/CE20140715PSE.gdb.zip
  format: null
  id: resource_b5ade36e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140715PSE.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_geodatadamageassessment20_20141002
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-10-02'
temporal_resolution: null
title: 'Palestine - Geodata of Gaza Damage Assessment 2014: UNOSAT Satellite Derived
  Geospatial Analysis'
version: null
vulnerability: null
---
