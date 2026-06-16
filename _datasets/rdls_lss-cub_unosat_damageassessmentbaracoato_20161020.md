---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-baracoa-town-guantanamo-province-cuba
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-baracoa-town-guantanamo-province-cuba
dataset_id: rdls_lss-cub_unosat_damageassessmentbaracoato_20161020
description: 'This map illustrates potential satellite-detected damaged structures
  in Baracoa town, in Guantanamo Province, Cuba. The UNITAR-UNOSAT analysis used a
  Pleiades satellite image, acquired on the 11 October 2016, and identified 3,147
  damaged structures inside the town of Baracoa.This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-baracoa-town-guantanamo-province-cuba]'
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre- and post-event Pleiades satellite imagery
    acquired on 11 October 2016 to detect structural damage in Baracoa town following
    a tropical cyclone event. Damaged structures were identified through visual interpretation
    of notable changes between images and mapped as vector features with confidence
    ratings and area measurements.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-baracoa-town-guantanamo-province-cuba
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone detected via satellite
      imagery
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
  description: Cuba - Damage Assessment in Baracoa town, Guantanamo province (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CU/TC20161005CUB/TC20161005CUB.gdb.zip
  format: Geodatabase
  id: resource_00efc0c9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161005CUB.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cuba - Damage Assessment in Baracoa town, Guantanamo province (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CU/TC20161005CUB/TC20161005CUB_shp.zip
  format: null
  id: resource_00a3d4f9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161005CUB_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cub_unosat_damageassessmentbaracoato_20161020
spatial:
  bbox: null
  centroid: null
  countries:
  - CUB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-20'
temporal_resolution: null
title: Cuba - Damage Assessment in Baracoa town, Guantanamo province
version: null
vulnerability: null
---
