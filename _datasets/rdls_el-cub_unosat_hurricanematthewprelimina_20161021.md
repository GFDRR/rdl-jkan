---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/hurricane-matthew-preliminary-satellite-based-damage-assessment-report-guantanamo-province-cuba
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/hurricane-matthew-preliminary-satellite-based-damage-assessment-report-guantanamo-province-cuba
dataset_id: rdls_el-cub_unosat_hurricanematthewprelimina_20161021
description: 'This report describes preliminary building damage analysis carried out
  by UNITAR-UNOSAT covering the towns and its surrounding areas over Baracoa, Maisi,
  Imias, and Cajobabo. Building damage analysis was conducted with the post-disaster
  satellite images (Pleiades acquired on 7/10/2016, 10/10/2016, and 11/10/2016)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hurricane-matthew-preliminary-satellite-based-damage-assessment-report-guantanamo-province-cuba]'
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
    description: Building stock in Baracoa, Maisi, Imias, and Cajobabo towns classified
      by damage state from satellite imagery
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
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared pre- and post-event Pleiades satellite imagery
    acquired 7-11 October 2016 to identify and classify building damage in four towns
    affected by Hurricane Matthew. Damage features were digitized into vector geometries
    with confidence ratings and area measurements, delivered as geodatabase and shapefile
    formats.
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
- href: https://data.humdata.org/dataset/hurricane-matthew-preliminary-satellite-based-damage-assessment-report-guantanamo-province-cuba
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Hurricane Matthew assessed via post-event
      satellite imagery comparison
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
  description: 'Hurricane Matthew Preliminary Satellite Based Damage Assessment Report:
    Guantanamo Province, Cuba (Zipped geodatabase)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CU/TC20161005CUB/TC20161005CUB.gdb.zip
  format: Geodatabase
  id: resource_8be87c77
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
  description: 'Hurricane Matthew Preliminary Satellite Based Damage Assessment Report:
    Guantanamo Province, Cuba (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CU/TC20161005CUB/TC20161005CUB_shp.zip
  format: null
  id: resource_917599ae
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161005CUB_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-cub_unosat_hurricanematthewprelimina_20161021
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
  start: '2016-10-21'
temporal_resolution: null
title: 'Hurricane Matthew Preliminary Satellite Based Damage Assessment Report: Guantanamo
  Province, Cuba'
version: null
vulnerability: null
---
