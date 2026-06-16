---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNITAR-UNOSAT
    url: https://data.humdata.org/dataset/damage-assessment-overview-of-jeremie-area-grande-anse-department
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Copernicus
    url: https://data.humdata.org/dataset/damage-assessment-overview-of-jeremie-area-grande-anse-department
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-overview-of-jeremie-area-grande-anse-department
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-overview-of-jeremie-area-grande-anse-department
dataset_id: rdls_el-hti_unosat_damageassessmentoverviewj_20161014
description: "This map illustrates satellite-detected areas potentially damaged and\
  \ related density and the identified road obstacles in J\xE9r\xE9mie city and surrounding\
  \ areas in Grande Anse department, Haiti. The UNITAR-UNOSAT analysis used a Pleiades\
  \ satellite image acquired on the 07 October 2016 and Worldview-1 image acquired\
  \ on 01 May 2015 and 08 December 2014. The UNITAR-UNOSAT analysis in the outskirts\
  \ of Jeremie combined with Copernicus analysis in Jeremie city, identified 13,013\
  \ potentially damaged structures within this map extent. The UNITAR-UNOSAT analysis\
  \ identified 134 road obstacles and 800 population gathering sites within the map\
  \ extent.This is a preliminary analysis and has not yet been validated in the field.\
  \ Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was\
  \ automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:\
  \ https://data.humdata.org/dataset/damage-assessment-overview-of-jeremie-area-grande-anse-department]"
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
    description: "Building structures in J\xE9r\xE9mie city and surrounding areas\
      \ assessed for damage"
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
    description: Road network with identified obstacles and blockages
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
      quantity_kind: length
      unit: null
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: Post-event damage assessment derived from multi-temporal satellite
    imagery (Pleiades acquired 07 October 2016, Worldview-1 from 01 May 2015 and 08
    December 2014) analyzed by UNITAR-UNOSAT and Copernicus analysts through visual
    comparison to detect structural damage and infrastructure obstacles. Results include
    13,013 potentially damaged structures and 134 road obstacles mapped as vector
    geometries with area measurements.
  sources:
  - id: source_1
    license: null
    name: UNITAR-UNOSAT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Copernicus
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-overview-of-jeremie-area-grande-anse-department
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone assessed via satellite
      imagery comparison
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
    description: Road obstacles and disruptions caused by tropical cyclone
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displacement from tropical cyclone impact
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
  description: "Haiti - Damage Assessment Overview of J\xE9r\xE9mie area, Grande Anse\
    \ Department (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/TC20161003HTI/TC20161003THI_combined_gdb.zip
  format: Geodatabase
  id: resource_2cb06eb1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161003THI_combined_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Haiti - Damage Assessment Overview of J\xE9r\xE9mie area, Grande Anse\
    \ Department (Shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/TC20161003HTI/TC20161003THI_combined_shp.zip
  format: null
  id: resource_98d7401d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161003THI_combined_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-hti_unosat_damageassessmentoverviewj_20161014
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-14'
temporal_resolution: null
title: "Haiti - Damage Assessment Overview of J\xE9r\xE9mie area, Grande Anse Department"
version: null
vulnerability: null
---
